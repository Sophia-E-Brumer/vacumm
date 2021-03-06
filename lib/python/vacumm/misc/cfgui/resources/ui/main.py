# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Dec  4 17:31:58 2017
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tab_config = QtGui.QWidget()
        self.tab_config.setObjectName(_fromUtf8("tab_config"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_config)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeview_config = QtGui.QTreeView(self.tab_config)
        self.treeview_config.setAcceptDrops(False)
        self.treeview_config.setDragEnabled(False)
        self.treeview_config.setObjectName(_fromUtf8("treeview_config"))
        self.verticalLayout.addWidget(self.treeview_config)
        self.tabs.addTab(self.tab_config, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabs, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.frame_left = QtGui.QFrame(self.centralwidget)
        self.frame_left.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_left.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_left.setObjectName(_fromUtf8("frame_left"))
        self.gridLayout.addWidget(self.frame_left, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_edit = QtGui.QMenu(self.menubar)
        self.menu_edit.setObjectName(_fromUtf8("menu_edit"))
        self.menu_help = QtGui.QMenu(self.menubar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolbar = QtGui.QToolBar(MainWindow)
        self.toolbar.setObjectName(_fromUtf8("toolbar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.menu_file_new = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-new"))
        self.menu_file_new.setIcon(icon)
        self.menu_file_new.setObjectName(_fromUtf8("menu_file_new"))
        self.menu_file_open = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-open"))
        self.menu_file_open.setIcon(icon)
        self.menu_file_open.setObjectName(_fromUtf8("menu_file_open"))
        self.menu_file_save = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save"))
        self.menu_file_save.setIcon(icon)
        self.menu_file_save.setObjectName(_fromUtf8("menu_file_save"))
        self.menu_file_save_as = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save-as"))
        self.menu_file_save_as.setIcon(icon)
        self.menu_file_save_as.setObjectName(_fromUtf8("menu_file_save_as"))
        self.menu_file_quit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("window-close"))
        self.menu_file_quit.setIcon(icon)
        self.menu_file_quit.setObjectName(_fromUtf8("menu_file_quit"))
        self.menu_edit_reload = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("view-refresh"))
        self.menu_edit_reload.setIcon(icon)
        self.menu_edit_reload.setObjectName(_fromUtf8("menu_edit_reload"))
        self.menu_edit_load_default = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("edit-clear"))
        self.menu_edit_load_default.setIcon(icon)
        self.menu_edit_load_default.setObjectName(_fromUtf8("menu_edit_load_default"))
        self.menu_edit_save_default = QtGui.QAction(MainWindow)
        self.menu_edit_save_default.setObjectName(_fromUtf8("menu_edit_save_default"))
        self.menu_edit_load_specification_default = QtGui.QAction(MainWindow)
        self.menu_edit_load_specification_default.setObjectName(_fromUtf8("menu_edit_load_specification_default"))
        self.menu_edit_sessions = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-properties"))
        self.menu_edit_sessions.setIcon(icon)
        self.menu_edit_sessions.setObjectName(_fromUtf8("menu_edit_sessions"))
        self.menu_edit_preferences = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("preferences-other"))
        self.menu_edit_preferences.setIcon(icon)
        self.menu_edit_preferences.setObjectName(_fromUtf8("menu_edit_preferences"))
        self.actionBar = QtGui.QAction(MainWindow)
        self.actionBar.setObjectName(_fromUtf8("actionBar"))
        self.menu_edit_collapse_all = QtGui.QAction(MainWindow)
        self.menu_edit_collapse_all.setObjectName(_fromUtf8("menu_edit_collapse_all"))
        self.menu_edit_expand_all = QtGui.QAction(MainWindow)
        self.menu_edit_expand_all.setObjectName(_fromUtf8("menu_edit_expand_all"))
        self.menu_file.addAction(self.menu_file_new)
        self.menu_file.addAction(self.menu_file_open)
        self.menu_file.addAction(self.menu_file_save)
        self.menu_file.addAction(self.menu_file_save_as)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_file_quit)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.menu_edit_expand_all)
        self.menu_edit.addAction(self.menu_edit_collapse_all)
        self.menu_edit.addAction(self.menu_edit_reload)
        self.menu_edit.addAction(self.menu_edit_load_default)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.menu_edit_sessions)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.menu_edit_preferences)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.toolbar.addAction(self.menu_file_new)
        self.toolbar.addAction(self.menu_file_open)
        self.toolbar.addAction(self.menu_file_save)
        self.toolbar.addAction(self.menu_file_save_as)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.menu_edit_reload)
        self.toolbar.addAction(self.menu_edit_load_default)
        self.toolbar.addAction(self.menu_edit_sessions)
        self.toolbar.addAction(self.menu_edit_preferences)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.menu_file_new, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.on_menu_file_new)
        QtCore.QObject.connect(self.menu_file_open, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.on_menu_file_open)
        QtCore.QObject.connect(self.menu_file_save, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.on_menu_file_save)
        QtCore.QObject.connect(self.menu_file_save_as, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.on_menu_file_save_as)
        QtCore.QObject.connect(self.menu_edit_preferences, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.on_menu_file_preferences)
        QtCore.QObject.connect(self.menu_edit_sessions, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.on_menu_file_sessions)
        QtCore.QObject.connect(self.menu_file_quit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.on_menu_file_quit)
        QtCore.QObject.connect(self.menu_edit_reload, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.on_menu_edit_reload)
        QtCore.QObject.connect(self.menu_edit_load_default, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.on_menu_edit_load_default)
        QtCore.QObject.connect(self.menu_edit_collapse_all, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.on_menu_edit_collapse_all)
        QtCore.QObject.connect(self.menu_edit_expand_all, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.on_menu_edit_expand_all)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CfgUI", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_config), _translate("MainWindow", "Configuration", None))
        self.menu_file.setTitle(_translate("MainWindow", "File", None))
        self.menu_edit.setTitle(_translate("MainWindow", "Edit", None))
        self.menu_help.setTitle(_translate("MainWindow", "Help", None))
        self.toolbar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.menu_file_new.setText(_translate("MainWindow", "New", None))
        self.menu_file_new.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.menu_file_open.setText(_translate("MainWindow", "Open", None))
        self.menu_file_open.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.menu_file_save.setText(_translate("MainWindow", "Save", None))
        self.menu_file_save.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.menu_file_save_as.setText(_translate("MainWindow", "Save as", None))
        self.menu_file_save_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S", None))
        self.menu_file_quit.setText(_translate("MainWindow", "Quit", None))
        self.menu_file_quit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.menu_edit_reload.setText(_translate("MainWindow", "Reload", None))
        self.menu_edit_reload.setShortcut(_translate("MainWindow", "F5", None))
        self.menu_edit_load_default.setText(_translate("MainWindow", "Load default values", None))
        self.menu_edit_load_default.setShortcut(_translate("MainWindow", "Ctrl+F5", None))
        self.menu_edit_save_default.setText(_translate("MainWindow", "Save as default values", None))
        self.menu_edit_load_specification_default.setText(_translate("MainWindow", "Load default values from specification", None))
        self.menu_edit_sessions.setText(_translate("MainWindow", "Sessions", None))
        self.menu_edit_sessions.setShortcut(_translate("MainWindow", "Ctrl+Shift+O", None))
        self.menu_edit_preferences.setText(_translate("MainWindow", "Preferences", None))
        self.menu_edit_preferences.setShortcut(_translate("MainWindow", "Ctrl+Shift+P", None))
        self.actionBar.setText(_translate("MainWindow", "bar", None))
        self.menu_edit_collapse_all.setText(_translate("MainWindow", "Collapse all", None))
        self.menu_edit_expand_all.setText(_translate("MainWindow", "Expand all", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

