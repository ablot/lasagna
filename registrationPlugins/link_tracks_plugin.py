"""
Plugin to take a few lines and rotate images to align them
"""

from lasagna_plugin import lasagna_plugin
import link_track_UI
import selectstack_UI
from PyQt4 import QtGui, QtCore
import sys
import numpy as np
from scipy import ndimage

SCALE = 5.1803  # scale for my images


class plugin(lasagna_plugin, QtGui.QWidget, link_track_UI.Ui_linkTrack):  # must inherit lasagna_plugin first

    def __init__(self, lasagna, parent=None):
        super(plugin, self).__init__(
            lasagna)  # This calls the lasagna_plugin constructor which in turn calls subsequent constructors

        # re-define some default properties that were originally defined in lasagna_plugin
        self.pluginShortName = 'Link track'  # Appears on the menu
        self.pluginLongName = 'link selected lines by moving stacks'  # Can be used for other purposes (e.g. tool-tip)
        self.pluginAuthor = 'Antonin Blot'

        # Create widgets defined in the designer file
        self.setupUi(self)
        self.show()

        # Set up the close button by linking it to the same slot as the normal window close button
        self.closeButton.released.connect(self.closePlugin)

        self.initialise()
        self.original_data = dict() # empty dict to store copy of modified stack

        # Connections:
        self.refresh_pushButton.clicked.connect(self.initialise)
        self.translate_pushButton.clicked.connect(self.do_translate)
        self.rotate_pushButton.clicked.connect(self.do_rotate)
        self.cancel_pushButton.clicked.connect(self.cancel)
        self.tableWidget.cellChanged.connect(self.changeLine)
        self.cancel_pushButton.clicked.connect(self.cancel)
        # self.fit_pushButton.clicked.connect(self.fit_line)
        # self.deg_spinBox.valueChanged.connect(self.fit_line)
        # self.clear_pushButton.clicked.connect(self.clear_line)
        # self.add_pushButton.clicked.connect(self.add_line)
        # self.interactive_checkBox.clicked.connect(self.fit_line)

    def initialise(self):
        tb = self.tableWidget
        tb.clear()
        tb.setHorizontalHeaderLabels(['name', 'slice', 'use it', 'anchor', 'translate'])
        colWidth = [170, 50,  60, 50, 70]
        for i_col, w in enumerate(colWidth):
            tb.setColumnWidth(i_col, w)
        lines = self.lasagna.returnIngredientByType('lines')
        if lines is False:
            return
        self.tableWidget.setRowCount(len(lines))
        firstSlice = True
        for ind, line in enumerate(lines):
            it = QtGui.QTableWidgetItem(line.objectName)
            tb.setItem(ind, 0, it)
            line_data = line.raw_data()
            if len(line_data) == 0:
                sls = 'no data'
            else:
                sls = ', '.join([str(s) for s in np.unique(line_data[:, 0])])
            it = QtGui.QTableWidgetItem(sls)
            tb.setItem(ind, 1, it)
            it = QtGui.QTableWidgetItem()
            it.setCheckState(True)
            tb.setItem(ind, 2, it)
            it = QtGui.QTableWidgetItem()
            it.setCheckState(firstSlice)
            tb.setItem(ind, 3, it)
            firstSlice = False
            it = QtGui.QTableWidgetItem()
            it.setCheckState(True)
            tb.setItem(ind, 4, it)

        self.stackListWidget.clear()
        stk_list = [st.objectName for st in self.lasagna.returnIngredientByType('imagestack')]
        self.stackListWidget.addItems(stk_list)

    def cancel(self):
        """Cancel transformation by reloading copied data

        """
        for stackName, data in self.original_data.items():
            print('Reset %s' % stackName)
            stack = self.lasagna.returnIngredientByName(stackName)
            stack._data = data

    def changeLine(self, row, column):
        """Slot for changes in TableWidget with lines
        """
        if column == 3:
            # it's a change in anchor, check the state
            item = self.tableWidget.item(row, column)
            if item.checkState():
                # it's true, assert that it is the sole anchor
                # check that it's a line that I use
                if not self.tableWidget.item(row, 2).checkState():
                    print('Cannot set an unused slice as anchor')
                    item.setCheckState(False)
                    return
                for i_row in range(self.tableWidget.rowCount()):
                    if i_row == row: # skip the changed item
                        continue
                    other_item = self.tableWidget.item(i_row, column)
                    if other_item is None: # there no item yet there
                        continue
                    other_item.setCheckState(False)
            else:
                # check if there is an anchor and recheck it if there isn't
                oneCheck = False
                for i_row in range(self.tableWidget.rowCount()):
                    if i_row == row: # skip the changed item
                        continue
                    other_item = self.tableWidget.item(i_row, column)
                    if other_item is None: # there no item yet there
                        continue
                    if other_item.checkState():
                        oneCheck = True
                if not oneCheck:
                    item.setCheckState(True)
        if column ==2:
            # it's a change of use it, check that I don't de-use the anchor
            item = self.tableWidget.item(row, column)
            if item.checkState():
                # adding a new slice, no pb
                pass
            else:
                # removing a slice
                item_anch_col = self.tableWidget.item(row, 3)
                if item_anch_col.checkState():
                    print('Cannot remove anchor from slice to use')
                    item.setCheckState(True)
                    return
        self.updateMvt()

    def updateMvt(self):
        """Update values in the mvtTableWidget
        """
        self.mvtTableWidget

    def do_rotate(self):
        raise NotImplementedError

    def do_translate(self):
        print('Doing translation')

        stacks_list = self.stackListWidget.selectedItems()
        stacks_list = [it.text() for it in stacks_list]
        if not len(stacks_list):
            print('    No stack selected')
        else:
            # get the mvt
            start_axis = str(self.axisOrderingComboBox.currentText())[0]
            top = str(self.topOrderingComboBox.currentText()).split(' ')[-1]
            # topOrderingComboBox can be either '0 at top/right' or '0 at bottom/left'
            top = 'max' if top.endswith('left') else 'min'
            mvt = self.get_translation(start_axis=start_axis, top=top)

            for stack_name in stacks_list:
                print('    Translating %s'%stack_name)
                stk = self.lasagna.returnIngredientByName(str(stack_name))
                self.translate_stack(stk, mvt, extend_canvas=bool(self.extendCheckBox.checkState()))

    def get_translation(self, top='max', start_axis='Y'):
        """Translate slices to match points of lines with id

        slice_order is True for  ascending, False for descending number
        """
        if start_axis.lower() == 'y':
            ax = 2
        elif start_axis.lower() == 'x':
            ax = 1
        else:
            raise IOError('%s is not a valid axis [X and Y are accepted]')
        if top.lower() == 'max':
            beg = np.argmax
            end = np.argmin
        elif top.lower() == 'min':
            beg = np.argmin
            end = np.argmax
        else:
            raise IOError('%s is not a valid order [min and max are accepted]')

        # find rows with selected line
        data = [[], [], [], []] # data will contain the row index, the line name, the slices and if it is the anchor
        for i_row in range(self.tableWidget.rowCount()):
            useit = self.tableWidget.item(i_row,2)
            if useit.checkState():
                # add the row data to the list of point
                data[0].append(i_row)
                for i in range(2):
                    data[i + 1].append(str(self.tableWidget.item(i_row, i).text()))
                data[3].append(bool(self.tableWidget.item(i_row, 3).checkState()))

        for i in data[2]:
            try:
                float(i)
            except ValueError:
                print('WARNING: link_track can only use non-empty lines that are on a single slice')
                print('I cannot use %s and will return'%data[1][i])
                return

        sls = np.array([float(i) for i in data[2]])
        if len(sls) != len(np.unique(sls)):
            print('WARNING: I expect only one line per slice.')
            print('I will try to do with what you gave me, but don\'t blame me if it fails')

        anchor_id = np.where(data[3])[0][0]
        anchor_sls = float(data[2][anchor_id])

        # zOrderingComboBox text can be either 'high Z is above' or 'low Z is above'
        if str(self.zOrderingComboBox.currentText()).startswith('high'):
            sls_above = sls[sls >= anchor_sls]
            sls_below = sls[sls <= anchor_sls]
            invert_order = False
        else:
            sls_below = sls[sls >= anchor_sls]
            sls_above = sls[sls <= anchor_sls]
            invert_order = True

        #Move stuff above the anchor:
        origin = None
        mvt = [np.zeros(3)]
        mvt_above = None
        if len(sls_above) > 1:
            slice_indices = sls_above.argsort()
            if invert_order: # the slice above have a lower Z value, count the other way
                slice_indices = slice_indices[::-1]
            for ind in slice_indices:
                sl_ind = np.where(sls==sls_above[ind])[0][0]
                line = self.lasagna.returnIngredientByName(str(data[1][sl_ind]))
                d = line.raw_data()
                startpts = d[beg(d[:, ax])]
                endpts = d[end(d[:, ax])]
                if origin is None:
                    origin = startpts
                    continue
                mvt.append(np.array(origin - endpts) + mvt[-1])
                origin = startpts
            mvt_above = np.vstack(mvt)
            mvt_above[:, 0] = sls_above[slice_indices]

        #Move stuff below the anchor:
        origin = None
        mvt = [np.zeros(3)]
        mvt_below = None
        if len(sls_below) > 1:
            slice_indices = sls_below.argsort()[::-1]
            if invert_order:
                slice_indices = slice_indices[::-1]
            for ind in slice_indices:
                sl_ind = np.where(sls==sls_below[ind])[0][0]
                line = self.lasagna.returnIngredientByName(str(data[1][sl_ind]))
                d = line.raw_data()
                startpts = d[beg(d[:, ax])]
                endpts = d[end(d[:, ax])]
                if origin is None:
                    origin = endpts
                    continue
                mvt.append(np.array(origin - startpts) + mvt[-1])
                origin = endpts
            mvt_below = np.vstack(mvt)
            mvt_below[:, 0] = sls_below[slice_indices]
        mvt = np.array([anchor_sls, 0, 0])
        if mvt_above is not None:
            mvt = np.vstack((mvt, mvt_above[1:,:]))
        if mvt_below is not None:
            mvt = np.vstack((mvt, mvt_below[1:, :]))
        return mvt

    def changingStack(self, stack):
        """ Called when a stack is changed, used to cancel

        Ideal I should store the transformation and undo them but for now
        I'll just make a copy of the original data
        """
        self.original_data[stack.objectName] = stack.raw_data()

    def translate_stack(self, stack, mvt, extend_canvas=False):
        """Apply the transform to a stack ingredient

        :param mvt:
        :param extend_canvas:
        :return:
        """

        new_data = np.array(stack.raw_data(), copy=True)
        self.changingStack(stack)
        if extend_canvas:
            pad_pos = np.array(np.round(np.max(mvt[:, 1:], axis=0)), dtype=int)
            pad_pos[pad_pos < 0] = 0
            pad_neg = np.array(np.round(np.min(mvt[:, 1:], axis=0)), dtype=int)
            pad_neg[pad_neg > 0] = 0
            pad_z = np.zeros_like(pad_pos) # I won't pad in z axis
            new_data = np.pad(new_data, (pad_z, -pad_neg, pad_pos), 'edge')

        for sl, x_shift, y_shift in mvt:
            sl = int(sl)
            x_shift = int(np.round(x_shift))
            y_shift = int(np.round(y_shift))
            if x_shift > 0:
                new_data[sl, :x_shift, :] = 0
                new_data[sl, x_shift:, :] = new_data[sl, :-x_shift, :]
            elif x_shift < 0:
                new_data[sl, x_shift:, :] = 0
                new_data[sl, :x_shift, :] = new_data[sl, -x_shift:, :]

            if y_shift > 0:
                new_data[sl, :, y_shift] = 0
                new_data[sl, :, y_shift:] = new_data[sl, :, :-y_shift]
            elif y_shift < 0:
                new_data[sl, :, y_shift:] = 0
                new_data[sl, :, :y_shift] = new_data[sl, :, -y_shift:]
        stack._data = new_data

    def translate_pts(self, line, mvt):
        """Apply the movement to a line ingredient
        """
        out = np.array(line.raw_data(), copy=True)

        sls = list(mvt[:, 0])
        for i, l in enumerate(out):
            if l[0] in sls:
                out[i, 1:] -= mvt[sls.index(l[0]), 1:]
        line._data = out

    def distance_along(self, id, distance_array, start='max', start_axis='Y'):
        """Find coordinates of pts along track id
        """
        if start_axis.lower() == 'y':
            ax = 2
        elif start_axis.lower() == 'z':
            ax = 1
        else:
            raise IOError()
        if start.lower() == 'max':
            beg = np.argmax
            end = np.argmin
            def sorting(x):
                return np.argsort(x)[::-1]
        elif start.lower() == 'min':
            beg = np.argmin
            end = np.argmax
            sorting = np.argsort
        else:
            raise IOError()

        # find rows with good id
        data = [[], [], [], []]
        for row in range(self.tableWidget.rowCount()):
            row_id = self.tableWidget.item(row, 2).text()
            if int(row_id) == id:
                data[0].append(row)
                for i in range(3):
                    data[i + 1].append(self.tableWidget.item(row, i).text())

        sls = np.array([float(str(i)) for i in data[2]])
        begs = []
        ends = []
        distances = []
        lengths = []
        datas = []
        for ind in sls.argsort():
            line = self.lasagna.returnIngredientByName(str(data[1][ind]))
            d = line.raw_data()
            ind_d = sorting(d[:, ax])
            d = d[ind_d]
            datas.append(d)
            # measure distance along line
            distances.append(np.sqrt(np.sum(np.diff(d[:, 1:] * SCALE, axis=0) ** 2, axis=1)))
            lengths.append(np.sum(distances[-1]))
            begs.append(d[beg(d[:, ax])])
            ends.append(d[end(d[:, ax])])
        lengths = np.hstack(lengths)
        begs = np.vstack(begs)

        slice_order = sorting(begs[:, ax])
        dist = np.hstack([[0], lengths[slice_order]]).cumsum()

        closest_coords = []
        for d in distance_array:
            indice = dist.searchsorted(d) - 1
            rest = d - dist[indice]
            if indice < len(slice_order):
                d_slice = np.hstack([[0], distances[slice_order[indice]]]).cumsum()
                closest = d_slice.searchsorted(rest) - 1
                closest_coords.append(datas[slice_order[indice]][closest, :])
            else:
                # the point is above the last part, do a linear interpolation from the last 2 pts
                e = ends[slice_order[-1]]
                n_steps = rest / distances[slice_order[-1]][-1]
                step = np.diff(datas[slice_order[-1]][-2:, :], axis=0)
                closest_coords.append(e + n_steps * step)
        return np.vstack(closest_coords)

    def rotateImage(self, img, angle, pivot):
        padX = [img.shape[1] - pivot[0], pivot[0]]
        padY = [img.shape[0] - pivot[1], pivot[1]]
        imgP = np.pad(img, [padY, padX], 'edge')
        imgR = ndimage.rotate(imgP, angle, reshape=False)
        return imgR[padY[0]: -padY[1], padX[0]: -padX[1]]

    def rotate_pts(self, XY, center, angle):
        """Rotate a point around center by angle degrees

        XY is a tuple with (x,y) coordinante
        """

        XY = np.array(XY, ndmin=2)
        center = np.asarray(center)
        XY -= center

        angle = 360 - angle  # because the axis has y at top, so invert rotation
        theta = np.deg2rad(angle)
        rot_mat = np.matrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

        newcoords = np.array(rot_mat * XY.T).T
        newcoords += center
        return newcoords.squeeze()

    def find_rotation(self, fix_id, moving_id):
        """Try to rotate every slice around the fix_id point to get the moving_id close
        to next slice

        """

        return

    # The following methods are involved in shutting down the plugin window
    def closePlugin(self):
        """
        This method is called by lasagna when the user unchecks the plugin in the menu.
        """
        self.detachHooks()
        self.close()


    # We define this here because we can't assume all plugins will have QWidget::closeEvent
    def closeEvent(self, event):
        """
        This event is executed when the user presses the close window (cross) button in the title bar
        """
        self.lasagna.stopPlugin(self.__module__)  # This will call self.closePlugin
        self.lasagna.pluginActions[self.__module__].setChecked(
            False)  # Uncheck the menu item associated with this plugin's name
        self.deleteLater()
        event.accept()


if False:
    import os


    def load_all_pts(mnames=['75', '74', '73', '66', '63'],
                     root='/mnt/microscopy/Data/Antonin/LP_project/awake_exp/histo/overview/'):
        all_pts_dict = {}
        for mouse_number in mnames:
            home = os.path.join(root, mouse_number)
            ids = {}
            fnames = [[], []]
            for fname in os.listdir(home):
                for ind, shk in enumerate(['medial', 'lateral']):
                    if fname.endswith('%s_shk_fit.txt' % shk):
                        tasty.loadActions['lines_reader'].showLoadDialog([os.path.join(home, fname)])
                        fnames[ind].append(fname)
                        ids[fname] = ind
            data = [[], []]
            for i, fs in enumerate(fnames):
                for f in fs:
                    data[i].append(tasty.returnIngredientByName(f).raw_data())
            all_pts_dict[mouse_number] = data
        return all_pts_dict


    def dist_all(all_pts_dict, factor=1.15):
        f = lambda x: np.sqrt((x ** 2 + 150 ** 2))
        sorting = lambda x: np.argsort(x)[::-1]
        ax = 2
        out = {}
        out_real = {}
        for mouse_number, data_list in all_pts_dict.items():
            distances = [[], []]
            lengths = [[], []]
            real_lengths = [[], []]
            for shk, data_shk in enumerate(data_list):
                for d in data_shk:
                    ind_d = sorting(d[:, ax])
                    d = d[ind_d]
                    # measure distance along line
                    distances[shk].append(np.sqrt(np.sum(np.diff(d[:, 1:] * SCALE, axis=0) ** 2, axis=1)))
                    lengths[shk].append(np.sum(distances[shk][-1]))
                    real_lengths[shk] = [f(l) for l in lengths[shk]]
            lengths[shk] = np.hstack(lengths[shk])
            real_lengths[shk] = np.hstack(real_lengths[shk])
            out[mouse_number] = [np.sum(l) * factor for l in lengths]
            out_real[mouse_number] = [np.sum(l) * factor for l in real_lengths]
        return out


    dep_max = {'63': 1284.0, '66': np.nan, '73': 1163.0, '74': 1132.0, '75': 1316.0}


    # script to generate some analysis data
    def savelines(home):
        [line.save(os.path.join(home, line.objectName + '.txt')) for line in tasty.returnIngredientByType('lines')]


    tetrode = np.arange(8) * 130 * 90 / 100. + 1
    root = '/mnt/microscopy/Data/Antonin/LP_project/awake_exp/histo/overview/'
    what = ['DyI', 'GFP', 'DAPI']
    mouse_number = '63'

    slice_order = {'75': 1, '74': 1, '73': 0, '66': 0, '63': 0}
    pos_dict = {'73': {1: np.array([196.]), 2: np.array([0.])},
                '74': {1: np.array([199.]), 2: np.array([0.])},
                '75': {1: np.array([235.]), 2: np.array([53.]), 3: np.array([0.])},
                '63': {1: np.array([469.]), 2: np.array([315.]), 3: np.array([196.]), 4: np.array([0.])},
                '66': {1: np.array([0.])}}
    home = os.path.join(root, mouse_number)

    for w in what:
        tasty.loadImageStack(os.path.join(home, 'AF%s_reorder_%s.tif' % (mouse_number, w)))

    start = 'min'
    # slice_order = dict([(k, 1-v) for k,v in slice_order.items()])
    ids = {}
    for fname in os.listdir(home):
        for ind, shk in enumerate(['medial', 'lateral']):
            if fname.endswith('%s_shk_fit.txt' % shk):
                tasty.loadActions['lines_reader'].showLoadDialog([os.path.join(home, fname)])
                ids[fname] = ind

    self = tasty.plugins['link_tracks_plugin']
    self.initialise()

    # find rows with good id
    for row in range(self.tableWidget.rowCount()):
        fname = self.tableWidget.item(row, 0).text()
        self.tableWidget.item(row, 2).setText(str(ids[str(fname)]))

    tasty.initialiseAxes()

    which = 'medial'
    id = 1 if which == 'lateral' else 0

    mvt = self.get_translation(id, slice_order=slice_order[mouse_number], start=start, start_axis='y')
    stacks = self.lasagna.returnIngredientByType('imagestack')
    for stack in stacks:
        self.translate_stack(stack, mvt)
    [self.translate_pts(pt, mvt) for pt in self.lasagna.returnIngredientByType('lines')]

    for p, shift in pos_dict[mouse_number].items():
        pts = self.distance_along(id, tetrode + shift, start='max', start_axis='Y')
        ptsName = 'AF%s_pos%i_%s.txt' % (mouse_number, p, which)
        self.lasagna.addIngredient(objectName=ptsName,
                                   kind='sparsepoints',
                                   data=pts)
        self.lasagna.returnIngredientByName(ptsName).addToPlots()

    tasty.initialiseAxes()

    manual_array_medial = dict(
        AF75=dict(pos1={0: 'out', 1: 'out', 2: '1', 3: '2/3', 4: '2/3', 5: '4', 6: '5a', 7: '6a'},
                  pos2={0: '1', 1: '1', 2: '2/3', 3: '2/3', 4: '5a', 5: '5b', 6: '6a', 7: '6b'},
                  pos3={0: '1', 1: '2/3', 2: '2/3', 3: '4', 4: '5a', 5: '6a', 6: '6b', 7: '6b'}),
        AF74=dict(pos1={0: '1', 1: '2/3', 2: '2/3', 3: '4', 4: '4', 5: '5a', 6: '5b', 7: '6a'},
                  pos2={0: '2/3', 1: '2/3', 2: '4', 3: '5a', 4: '5b', 5: '6a', 6: '6b', 7: '6b'}),
        AF73=dict(pos1={0: 'out', 1: 'out', 2: '1', 3: '1', 4: '2/3', 5: '4', 6: '5a', 7: '5b'},
                  pos2={0: 'out', 1: '1', 2: '2/3', 3: '2/3', 4: '4', 5: '5b', 6: '6a', 7: '6b'}),
        AF66=dict(pos1={0: '2/3', 1: '2/3', 2: '4', 3: '5a', 4: '5b', 5: '6a', 6: '6a', 7: '6b'}),
        AF63=dict(pos1={0: '1', 1: '1', 2: '2/3', 3: '2/3', 4: '2/3', 5: '4', 6: '4', 7: '5a'},
                  pos2={0: '2/3', 1: '2/3', 2: '2/3', 3: '2/3', 4: '4', 5: '5a', 6: '5a', 7: '6a'},
                  pos3={0: '2/3', 1: '2/3', 2: '2/3', 3: '4', 4: '5a', 5: '5b', 6: '6a', 7: '6b'},
                  pos4={0: '2/3', 1: '4', 2: '5a', 3: '5a', 4: '5b', 5: '6b', 6: '6b', 7: 'WM'}))

    manual_array_lateral = dict(
        AF75=dict(pos1={0: 'out', 1: '1', 2: '2/3', 3: '2/3', 4: '2/3', 5: '5a', 6: '5b', 7: '6a'},
                  pos2={0: '2/3', 1: '2/3', 2: '2/3', 3: '4', 4: '5a', 5: '6a', 6: '6b', 7: '6b'},
                  pos3={0: '2/3', 1: '2/3', 2: '2/3', 3: '4', 4: '5b', 5: '6a', 6: '6b', 7: 'WM'}),
        AF74=dict(pos1={0: 'out', 1: '1', 2: '2/3', 3: '2/3', 4: '4', 5: '5a', 6: '6a', 7: '6b'},
                  pos2={0: '2/3', 1: '2/3', 2: '4', 3: '4', 4: '5a', 5: '6a', 6: '6b', 7: '6b'}),

        AF73=dict(pos1={0: '1', 1: '2/3', 2: '2/3', 3: '4', 4: '5a', 5: '5a', 6: '6a', 7: '6b'},
                  pos2={0: 'out', 1: 'out', 2: '1', 3: '2/3', 4: '2/3', 5: '4', 6: '5b', 7: '6a'}),
        AF66=dict(pos1={0: '2/3', 1: '4', 2: '5a', 3: '5b', 4: '6a', 5: '6a', 6: '6b', 7: 'WM'}),
        AF63=dict(pos1={0: 'out', 1: '1', 2: '2/3', 3: '2/3', 4: '2/3', 5: '4', 6: '4', 7: '5a'},
                  pos2={0: '1', 1: '2/3', 2: '2/3', 3: '2/3', 4: '4', 5: '5a', 6: '5b', 7: '6a'},
                  pos3={0: '2/3', 1: '2/3', 2: '2/3', 3: '4', 4: '5a', 5: '5a', 6: '6a', 7: '6a'},
                  pos4={0: '2/3', 1: '4', 2: '4', 3: '5a', 4: '5b', 5: '6a', 6: '6b', 7: 'WM'}))

