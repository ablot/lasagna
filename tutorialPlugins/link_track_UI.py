# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'link_track.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_linkTrack(object):
    def setupUi(self, linkTrack):
        linkTrack.setObjectName(_fromUtf8("linkTrack"))
        linkTrack.resize(514, 522)
        self.verticalLayout = QtGui.QVBoxLayout(linkTrack)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(linkTrack)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.graphicsView = PlotWidget(self.splitter)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.tableWidget = QtGui.QTableWidget(self.splitter)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.doit_pushButton = QtGui.QPushButton(linkTrack)
        self.doit_pushButton.setObjectName(_fromUtf8("doit_pushButton"))
        self.horizontalLayout.addWidget(self.doit_pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.refresh_pushButton = QtGui.QPushButton(linkTrack)
        self.refresh_pushButton.setObjectName(_fromUtf8("refresh_pushButton"))
        self.horizontalLayout.addWidget(self.refresh_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.closeButton = QtGui.QPushButton(linkTrack)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout_2.addWidget(self.closeButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.apply_pushButton = QtGui.QPushButton(linkTrack)
        self.apply_pushButton.setObjectName(_fromUtf8("apply_pushButton"))
        self.horizontalLayout_2.addWidget(self.apply_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(linkTrack)
        QtCore.QMetaObject.connectSlotsByName(linkTrack)

    def retranslateUi(self, linkTrack):
        linkTrack.setWindowTitle(_translate("linkTrack", "link_track", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("linkTrack", "name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("linkTrack", "slice", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("linkTrack", "order", None))
        self.doit_pushButton.setText(_translate("linkTrack", "do it!", None))
        self.refresh_pushButton.setText(_translate("linkTrack", "refresh list", None))
        self.closeButton.setText(_translate("linkTrack", "&Close", None))
        self.apply_pushButton.setText(_translate("linkTrack", "apply", None))

from pyqtgraph import PlotWidget
