#!/usr/bin/env bash
pyuic4 ./designerFiles/lasagna_mainWindow.ui > ./lasagna_mainWindow.py
pyrcc4 ./designerFiles/mainWindow.qrc >  ./mainWindow_rc.py
pyuic4 ./designerFiles/alert.ui > ./alert_UI.py
# compile the tutorial plugins
cd tutorialPlugins
./updatePluginUIs.sh
# compile the registration plugins
cd ../registrationPlugins
./updatePluginUIs.sh