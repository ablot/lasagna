# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designerFiles/lasagna_mainWindow.ui'
#
# Created: Fri Jan 15 15:38:29 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_lasagna_mainWindow(object):
    def setupUi(self, lasagna_mainWindow):
        lasagna_mainWindow.setObjectName(_fromUtf8("lasagna_mainWindow"))
        lasagna_mainWindow.resize(1002, 795)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lasagna_mainWindow.sizePolicy().hasHeightForWidth())
        lasagna_mainWindow.setSizePolicy(sizePolicy)
        lasagna_mainWindow.setMinimumSize(QtCore.QSize(540, 540))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/lasagna_32.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        lasagna_mainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(lasagna_mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.graphicsView_1 = LasagnaPlotWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_1.sizePolicy().hasHeightForWidth())
        self.graphicsView_1.setSizePolicy(sizePolicy)
        self.graphicsView_1.setObjectName(_fromUtf8("graphicsView_1"))
        self.graphicsView_2 = LasagnaPlotWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.graphicsView_3 = LasagnaPlotWidget(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.frame_2 = QtGui.QFrame(self.splitter_2)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
        lasagna_mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(lasagna_mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1002, 27))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOpen_recent = QtGui.QMenu(self.menuFile)
        self.menuOpen_recent.setObjectName(_fromUtf8("menuOpen_recent"))
        self.menuLoad_ingredient = QtGui.QMenu(self.menuFile)
        self.menuLoad_ingredient.setObjectName(_fromUtf8("menuLoad_ingredient"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuPlugins = QtGui.QMenu(self.menuBar)
        self.menuPlugins.setObjectName(_fromUtf8("menuPlugins"))
        lasagna_mainWindow.setMenuBar(self.menuBar)
        self.mainDockWidget = QtGui.QDockWidget(lasagna_mainWindow)
        self.mainDockWidget.setMinimumSize(QtCore.QSize(331, 587))
        self.mainDockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.mainDockWidget.setObjectName(_fromUtf8("mainDockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.imageSettingsTab = QtGui.QWidget()
        self.imageSettingsTab.setObjectName(_fromUtf8("imageSettingsTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.imageSettingsTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.intensityHistogram = PlotWidget(self.imageSettingsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intensityHistogram.sizePolicy().hasHeightForWidth())
        self.intensityHistogram.setSizePolicy(sizePolicy)
        self.intensityHistogram.setMinimumSize(QtCore.QSize(0, 180))
        self.intensityHistogram.setMaximumSize(QtCore.QSize(16777215, 180))
        self.intensityHistogram.setObjectName(_fromUtf8("intensityHistogram"))
        self.verticalLayout_3.addWidget(self.intensityHistogram)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.logYcheckBox = QtGui.QCheckBox(self.imageSettingsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logYcheckBox.sizePolicy().hasHeightForWidth())
        self.logYcheckBox.setSizePolicy(sizePolicy)
        self.logYcheckBox.setMaximumSize(QtCore.QSize(16777215, 21))
        self.logYcheckBox.setChecked(True)
        self.logYcheckBox.setObjectName(_fromUtf8("logYcheckBox"))
        self.horizontalLayout_13.addWidget(self.logYcheckBox)
        self.imageAlpha_horizontalSlider = QtGui.QSlider(self.imageSettingsTab)
        self.imageAlpha_horizontalSlider.setMinimumSize(QtCore.QSize(221, 0))
        self.imageAlpha_horizontalSlider.setMaximum(100)
        self.imageAlpha_horizontalSlider.setProperty("value", 100)
        self.imageAlpha_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.imageAlpha_horizontalSlider.setInvertedAppearance(False)
        self.imageAlpha_horizontalSlider.setInvertedControls(False)
        self.imageAlpha_horizontalSlider.setObjectName(_fromUtf8("imageAlpha_horizontalSlider"))
        self.horizontalLayout_13.addWidget(self.imageAlpha_horizontalSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.imageStackLayers_TreeView = QtGui.QTreeView(self.imageSettingsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageStackLayers_TreeView.sizePolicy().hasHeightForWidth())
        self.imageStackLayers_TreeView.setSizePolicy(sizePolicy)
        self.imageStackLayers_TreeView.setMinimumSize(QtCore.QSize(0, 271))
        self.imageStackLayers_TreeView.setRootIsDecorated(False)
        self.imageStackLayers_TreeView.setObjectName(_fromUtf8("imageStackLayers_TreeView"))
        self.verticalLayout_3.addWidget(self.imageStackLayers_TreeView)
        spacerItem = QtGui.QSpacerItem(20, 162, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.imageSettingsTab, _fromUtf8(""))
        self.pointsSettingsTab = QtGui.QWidget()
        self.pointsSettingsTab.setObjectName(_fromUtf8("pointsSettingsTab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.pointsSettingsTab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.points_TreeView = QtGui.QTreeView(self.pointsSettingsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points_TreeView.sizePolicy().hasHeightForWidth())
        self.points_TreeView.setSizePolicy(sizePolicy)
        self.points_TreeView.setMinimumSize(QtCore.QSize(0, 281))
        self.points_TreeView.setMaximumSize(QtCore.QSize(16777215, 330))
        self.points_TreeView.setObjectName(_fromUtf8("points_TreeView"))
        self.verticalLayout_5.addWidget(self.points_TreeView)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.groupBoxAxisRatio_2 = QtGui.QGroupBox(self.pointsSettingsTab)
        self.groupBoxAxisRatio_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxAxisRatio_2.sizePolicy().hasHeightForWidth())
        self.groupBoxAxisRatio_2.setSizePolicy(sizePolicy)
        self.groupBoxAxisRatio_2.setMinimumSize(QtCore.QSize(131, 131))
        self.groupBoxAxisRatio_2.setMaximumSize(QtCore.QSize(131, 16777215))
        self.groupBoxAxisRatio_2.setObjectName(_fromUtf8("groupBoxAxisRatio_2"))
        self.layoutWidget = QtGui.QWidget(self.groupBoxAxisRatio_2)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 30, 106, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.axisRatioLabel_4 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_4.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_4.setSizePolicy(sizePolicy)
        self.axisRatioLabel_4.setMinimumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_4.setMaximumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.axisRatioLabel_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_4.setObjectName(_fromUtf8("axisRatioLabel_4"))
        self.horizontalLayout_5.addWidget(self.axisRatioLabel_4)
        self.view1Z_spinBox = QtGui.QSpinBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view1Z_spinBox.sizePolicy().hasHeightForWidth())
        self.view1Z_spinBox.setSizePolicy(sizePolicy)
        self.view1Z_spinBox.setMinimum(1)
        self.view1Z_spinBox.setMaximum(99)
        self.view1Z_spinBox.setObjectName(_fromUtf8("view1Z_spinBox"))
        self.horizontalLayout_5.addWidget(self.view1Z_spinBox)
        self.layoutWidget1 = QtGui.QWidget(self.groupBoxAxisRatio_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 60, 106, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.axisRatioLabel_5 = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_5.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_5.setSizePolicy(sizePolicy)
        self.axisRatioLabel_5.setMinimumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_5.setMaximumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_5.setObjectName(_fromUtf8("axisRatioLabel_5"))
        self.horizontalLayout_6.addWidget(self.axisRatioLabel_5)
        self.view2Z_spinBox = QtGui.QSpinBox(self.layoutWidget1)
        self.view2Z_spinBox.setMinimum(1)
        self.view2Z_spinBox.setObjectName(_fromUtf8("view2Z_spinBox"))
        self.horizontalLayout_6.addWidget(self.view2Z_spinBox)
        self.layoutWidget2 = QtGui.QWidget(self.groupBoxAxisRatio_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(11, 90, 106, 29))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.axisRatioLabel_6 = QtGui.QLabel(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_6.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_6.setSizePolicy(sizePolicy)
        self.axisRatioLabel_6.setMinimumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_6.setMaximumSize(QtCore.QSize(45, 16))
        self.axisRatioLabel_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_6.setObjectName(_fromUtf8("axisRatioLabel_6"))
        self.horizontalLayout_7.addWidget(self.axisRatioLabel_6)
        self.view3Z_spinBox = QtGui.QSpinBox(self.layoutWidget2)
        self.view3Z_spinBox.setMinimum(1)
        self.view3Z_spinBox.setObjectName(_fromUtf8("view3Z_spinBox"))
        self.horizontalLayout_7.addWidget(self.view3Z_spinBox)
        self.horizontalLayout_10.addWidget(self.groupBoxAxisRatio_2)
        self.frame = QtGui.QFrame(self.pointsSettingsTab)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelMarker = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMarker.sizePolicy().hasHeightForWidth())
        self.labelMarker.setSizePolicy(sizePolicy)
        self.labelMarker.setMaximumSize(QtCore.QSize(42, 24))
        self.labelMarker.setObjectName(_fromUtf8("labelMarker"))
        self.horizontalLayout_4.addWidget(self.labelMarker)
        self.markerSymbol_comboBox = QtGui.QComboBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.markerSymbol_comboBox.sizePolicy().hasHeightForWidth())
        self.markerSymbol_comboBox.setSizePolicy(sizePolicy)
        self.markerSymbol_comboBox.setMaximumSize(QtCore.QSize(85, 24))
        self.markerSymbol_comboBox.setObjectName(_fromUtf8("markerSymbol_comboBox"))
        self.horizontalLayout_4.addWidget(self.markerSymbol_comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.labelMarker_2 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMarker_2.sizePolicy().hasHeightForWidth())
        self.labelMarker_2.setSizePolicy(sizePolicy)
        self.labelMarker_2.setMaximumSize(QtCore.QSize(42, 24))
        self.labelMarker_2.setObjectName(_fromUtf8("labelMarker_2"))
        self.horizontalLayout_8.addWidget(self.labelMarker_2)
        self.markerSize_spinBox = QtGui.QSpinBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.markerSize_spinBox.sizePolicy().hasHeightForWidth())
        self.markerSize_spinBox.setSizePolicy(sizePolicy)
        self.markerSize_spinBox.setMinimum(1)
        self.markerSize_spinBox.setMaximum(99)
        self.markerSize_spinBox.setProperty("value", 1)
        self.markerSize_spinBox.setObjectName(_fromUtf8("markerSize_spinBox"))
        self.horizontalLayout_8.addWidget(self.markerSize_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.labelMarker_3 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMarker_3.sizePolicy().hasHeightForWidth())
        self.labelMarker_3.setSizePolicy(sizePolicy)
        self.labelMarker_3.setMaximumSize(QtCore.QSize(42, 24))
        self.labelMarker_3.setObjectName(_fromUtf8("labelMarker_3"))
        self.horizontalLayout_9.addWidget(self.labelMarker_3)
        self.markerAlpha_spinBox = QtGui.QSpinBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.markerAlpha_spinBox.sizePolicy().hasHeightForWidth())
        self.markerAlpha_spinBox.setSizePolicy(sizePolicy)
        self.markerAlpha_spinBox.setMinimum(0)
        self.markerAlpha_spinBox.setMaximum(255)
        self.markerAlpha_spinBox.setProperty("value", 255)
        self.markerAlpha_spinBox.setObjectName(_fromUtf8("markerAlpha_spinBox"))
        self.horizontalLayout_9.addWidget(self.markerAlpha_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.labelMarker_5 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMarker_5.sizePolicy().hasHeightForWidth())
        self.labelMarker_5.setSizePolicy(sizePolicy)
        self.labelMarker_5.setMaximumSize(QtCore.QSize(42, 24))
        self.labelMarker_5.setObjectName(_fromUtf8("labelMarker_5"))
        self.horizontalLayout_12.addWidget(self.labelMarker_5)
        self.lineWidth_spinBox = QtGui.QSpinBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineWidth_spinBox.sizePolicy().hasHeightForWidth())
        self.lineWidth_spinBox.setSizePolicy(sizePolicy)
        self.lineWidth_spinBox.setMinimum(1)
        self.lineWidth_spinBox.setMaximum(25)
        self.lineWidth_spinBox.setProperty("value", 2)
        self.lineWidth_spinBox.setObjectName(_fromUtf8("lineWidth_spinBox"))
        self.horizontalLayout_12.addWidget(self.lineWidth_spinBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.markerColor_pushButton = QtGui.QPushButton(self.frame)
        self.markerColor_pushButton.setObjectName(_fromUtf8("markerColor_pushButton"))
        self.verticalLayout_4.addWidget(self.markerColor_pushButton)
        self.horizontalLayout_10.addWidget(self.frame)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        spacerItem1 = QtGui.QSpacerItem(20, 204, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.tabWidget.addTab(self.pointsSettingsTab, _fromUtf8(""))
        self.axisSetingsTab = QtGui.QWidget()
        self.axisSetingsTab.setObjectName(_fromUtf8("axisSetingsTab"))
        self.groupBoxAxisRatio = QtGui.QGroupBox(self.axisSetingsTab)
        self.groupBoxAxisRatio.setGeometry(QtCore.QRect(10, 10, 131, 121))
        self.groupBoxAxisRatio.setObjectName(_fromUtf8("groupBoxAxisRatio"))
        self.layoutWidget3 = QtGui.QWidget(self.groupBoxAxisRatio)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 30, 110, 22))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.axisRatioLabel_1 = QtGui.QLabel(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_1.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_1.setSizePolicy(sizePolicy)
        self.axisRatioLabel_1.setMinimumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_1.setMaximumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.axisRatioLabel_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_1.setObjectName(_fromUtf8("axisRatioLabel_1"))
        self.horizontalLayout.addWidget(self.axisRatioLabel_1)
        self.axisRatioLineEdit_1 = QtGui.QLineEdit(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLineEdit_1.sizePolicy().hasHeightForWidth())
        self.axisRatioLineEdit_1.setSizePolicy(sizePolicy)
        self.axisRatioLineEdit_1.setMaximumSize(QtCore.QSize(31, 20))
        self.axisRatioLineEdit_1.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.axisRatioLineEdit_1.setObjectName(_fromUtf8("axisRatioLineEdit_1"))
        self.horizontalLayout.addWidget(self.axisRatioLineEdit_1)
        self.layoutWidget4 = QtGui.QWidget(self.groupBoxAxisRatio)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 50, 110, 22))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.axisRatioLabel_2 = QtGui.QLabel(self.layoutWidget4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_2.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_2.setSizePolicy(sizePolicy)
        self.axisRatioLabel_2.setMinimumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_2.setMaximumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_2.setObjectName(_fromUtf8("axisRatioLabel_2"))
        self.horizontalLayout_2.addWidget(self.axisRatioLabel_2)
        self.axisRatioLineEdit_2 = QtGui.QLineEdit(self.layoutWidget4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLineEdit_2.sizePolicy().hasHeightForWidth())
        self.axisRatioLineEdit_2.setSizePolicy(sizePolicy)
        self.axisRatioLineEdit_2.setMaximumSize(QtCore.QSize(31, 20))
        self.axisRatioLineEdit_2.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.axisRatioLineEdit_2.setObjectName(_fromUtf8("axisRatioLineEdit_2"))
        self.horizontalLayout_2.addWidget(self.axisRatioLineEdit_2)
        self.layoutWidget5 = QtGui.QWidget(self.groupBoxAxisRatio)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 70, 110, 22))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.axisRatioLabel_3 = QtGui.QLabel(self.layoutWidget5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLabel_3.sizePolicy().hasHeightForWidth())
        self.axisRatioLabel_3.setSizePolicy(sizePolicy)
        self.axisRatioLabel_3.setMinimumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_3.setMaximumSize(QtCore.QSize(71, 16))
        self.axisRatioLabel_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.axisRatioLabel_3.setObjectName(_fromUtf8("axisRatioLabel_3"))
        self.horizontalLayout_3.addWidget(self.axisRatioLabel_3)
        self.axisRatioLineEdit_3 = QtGui.QLineEdit(self.layoutWidget5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axisRatioLineEdit_3.sizePolicy().hasHeightForWidth())
        self.axisRatioLineEdit_3.setSizePolicy(sizePolicy)
        self.axisRatioLineEdit_3.setMaximumSize(QtCore.QSize(31, 20))
        self.axisRatioLineEdit_3.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.axisRatioLineEdit_3.setObjectName(_fromUtf8("axisRatioLineEdit_3"))
        self.horizontalLayout_3.addWidget(self.axisRatioLineEdit_3)
        self.groupBoxFlip = QtGui.QGroupBox(self.axisSetingsTab)
        self.groupBoxFlip.setEnabled(True)
        self.groupBoxFlip.setGeometry(QtCore.QRect(150, 10, 81, 121))
        self.groupBoxFlip.setToolTip(_fromUtf8(""))
        self.groupBoxFlip.setObjectName(_fromUtf8("groupBoxFlip"))
        self.layoutWidget6 = QtGui.QWidget(self.groupBoxFlip)
        self.layoutWidget6.setGeometry(QtCore.QRect(20, 20, 43, 92))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_FlipView1 = QtGui.QPushButton(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_FlipView1.sizePolicy().hasHeightForWidth())
        self.pushButton_FlipView1.setSizePolicy(sizePolicy)
        self.pushButton_FlipView1.setMaximumSize(QtCore.QSize(41, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_FlipView1.setFont(font)
        self.pushButton_FlipView1.setCheckable(True)
        self.pushButton_FlipView1.setObjectName(_fromUtf8("pushButton_FlipView1"))
        self.verticalLayout.addWidget(self.pushButton_FlipView1)
        self.pushButton_FlipView2 = QtGui.QPushButton(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_FlipView2.sizePolicy().hasHeightForWidth())
        self.pushButton_FlipView2.setSizePolicy(sizePolicy)
        self.pushButton_FlipView2.setMaximumSize(QtCore.QSize(41, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_FlipView2.setFont(font)
        self.pushButton_FlipView2.setCheckable(True)
        self.pushButton_FlipView2.setObjectName(_fromUtf8("pushButton_FlipView2"))
        self.verticalLayout.addWidget(self.pushButton_FlipView2)
        self.pushButton_FlipView3 = QtGui.QPushButton(self.layoutWidget6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_FlipView3.sizePolicy().hasHeightForWidth())
        self.pushButton_FlipView3.setSizePolicy(sizePolicy)
        self.pushButton_FlipView3.setMaximumSize(QtCore.QSize(41, 16777215))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_FlipView3.setFont(font)
        self.pushButton_FlipView3.setCheckable(True)
        self.pushButton_FlipView3.setObjectName(_fromUtf8("pushButton_FlipView3"))
        self.verticalLayout.addWidget(self.pushButton_FlipView3)
        self.tabWidget.addTab(self.axisSetingsTab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.mainDockWidget.setWidget(self.dockWidgetContents)
        lasagna_mainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.mainDockWidget)
        self.toolBar = QtGui.QToolBar(lasagna_mainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        lasagna_mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(lasagna_mainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        lasagna_mainWindow.setStatusBar(self.statusBar)
        self.actionOpen = QtGui.QAction(lasagna_mainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/icons/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionAbout = QtGui.QAction(lasagna_mainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(lasagna_mainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/icons/window-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.action_ARA_Explorer = QtGui.QAction(lasagna_mainWindow)
        self.action_ARA_Explorer.setCheckable(True)
        self.action_ARA_Explorer.setObjectName(_fromUtf8("action_ARA_Explorer"))
        self.actionResetAxes = QtGui.QAction(lasagna_mainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/icons/edit-redo.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionResetAxes.setIcon(icon3)
        self.actionResetAxes.setObjectName(_fromUtf8("actionResetAxes"))
        self.actionLoadOverlay = QtGui.QAction(lasagna_mainWindow)
        self.actionLoadOverlay.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/icons/overlay.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoadOverlay.setIcon(icon4)
        self.actionLoadOverlay.setShortcut(_fromUtf8(""))
        self.actionLoadOverlay.setObjectName(_fromUtf8("actionLoadOverlay"))
        self.actionRemoveOverlay = QtGui.QAction(lasagna_mainWindow)
        self.actionRemoveOverlay.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/actions/icons/removeoverlay.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveOverlay.setIcon(icon5)
        self.actionRemoveOverlay.setObjectName(_fromUtf8("actionRemoveOverlay"))
        self.actionNone = QtGui.QAction(lasagna_mainWindow)
        self.actionNone.setObjectName(_fromUtf8("actionNone"))
        self.actionOpen_2 = QtGui.QAction(lasagna_mainWindow)
        self.actionOpen_2.setObjectName(_fromUtf8("actionOpen_2"))
        self.menuLoad_ingredient.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuLoad_ingredient.menuAction())
        self.menuFile.addAction(self.menuOpen_recent.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPlugins.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionResetAxes)
        self.toolBar.addSeparator()

        self.retranslateUi(lasagna_mainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(lasagna_mainWindow)

    def retranslateUi(self, lasagna_mainWindow):
        lasagna_mainWindow.setWindowTitle(_translate("lasagna_mainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("lasagna_mainWindow", "&File", None))
        self.menuOpen_recent.setTitle(_translate("lasagna_mainWindow", "&Open recent", None))
        self.menuLoad_ingredient.setTitle(_translate("lasagna_mainWindow", "&Load ingredient", None))
        self.menuHelp.setTitle(_translate("lasagna_mainWindow", "Help", None))
        self.menuPlugins.setTitle(_translate("lasagna_mainWindow", "&Plugins", None))
        self.logYcheckBox.setText(_translate("lasagna_mainWindow", "Log Y", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.imageSettingsTab), _translate("lasagna_mainWindow", "Image", None))
        self.groupBoxAxisRatio_2.setTitle(_translate("lasagna_mainWindow", "z-spread", None))
        self.axisRatioLabel_4.setText(_translate("lasagna_mainWindow", "View 1", None))
        self.axisRatioLabel_5.setText(_translate("lasagna_mainWindow", "View 2", None))
        self.axisRatioLabel_6.setText(_translate("lasagna_mainWindow", "View 3", None))
        self.labelMarker.setText(_translate("lasagna_mainWindow", "Marker", None))
        self.labelMarker_2.setText(_translate("lasagna_mainWindow", "Size", None))
        self.labelMarker_3.setText(_translate("lasagna_mainWindow", "Alpha", None))
        self.labelMarker_5.setText(_translate("lasagna_mainWindow", "Width", None))
        self.markerColor_pushButton.setText(_translate("lasagna_mainWindow", "Color", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pointsSettingsTab), _translate("lasagna_mainWindow", "Points", None))
        self.groupBoxAxisRatio.setTitle(_translate("lasagna_mainWindow", "Axis ratios", None))
        self.axisRatioLabel_1.setText(_translate("lasagna_mainWindow", "View 1", None))
        self.axisRatioLineEdit_1.setText(_translate("lasagna_mainWindow", "1", None))
        self.axisRatioLabel_2.setText(_translate("lasagna_mainWindow", "View 2", None))
        self.axisRatioLineEdit_2.setText(_translate("lasagna_mainWindow", "2", None))
        self.axisRatioLabel_3.setText(_translate("lasagna_mainWindow", "View 3", None))
        self.axisRatioLineEdit_3.setText(_translate("lasagna_mainWindow", "0.5", None))
        self.groupBoxFlip.setTitle(_translate("lasagna_mainWindow", "Flip Stacks", None))
        self.pushButton_FlipView1.setText(_translate("lasagna_mainWindow", "View 1", None))
        self.pushButton_FlipView2.setText(_translate("lasagna_mainWindow", "View 2", None))
        self.pushButton_FlipView3.setText(_translate("lasagna_mainWindow", "View 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.axisSetingsTab), _translate("lasagna_mainWindow", "Axis", None))
        self.toolBar.setWindowTitle(_translate("lasagna_mainWindow", "toolBar", None))
        self.actionOpen.setText(_translate("lasagna_mainWindow", "&New base stack", None))
        self.actionAbout.setText(_translate("lasagna_mainWindow", "About", None))
        self.actionQuit.setText(_translate("lasagna_mainWindow", "&Quit", None))
        self.action_ARA_Explorer.setText(_translate("lasagna_mainWindow", "&ARA Explorer", None))
        self.actionResetAxes.setText(_translate("lasagna_mainWindow", "resetAxes", None))
        self.actionResetAxes.setToolTip(_translate("lasagna_mainWindow", "reset axes", None))
        self.actionResetAxes.setShortcut(_translate("lasagna_mainWindow", "Ctrl+R", None))
        self.actionLoadOverlay.setText(_translate("lasagna_mainWindow", "&Load overlay", None))
        self.actionRemoveOverlay.setText(_translate("lasagna_mainWindow", "removeOverlay", None))
        self.actionRemoveOverlay.setToolTip(_translate("lasagna_mainWindow", "removeOverlay", None))
        self.actionNone.setText(_translate("lasagna_mainWindow", "none", None))
        self.actionOpen_2.setText(_translate("lasagna_mainWindow", "Open", None))

from pyqtgraph import PlotWidget
from lasagnaplotwidget import LasagnaPlotWidget
import mainWindow_rc
