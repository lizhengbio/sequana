# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(734, 815)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.vlayout.setContentsMargins(5, 0, 5, 0)
        self.vlayout.setSpacing(0)
        self.vlayout.setObjectName("vlayout")
        self.tabWidget_framework = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_framework.sizePolicy().hasHeightForWidth())
        self.tabWidget_framework.setSizePolicy(sizePolicy)
        self.tabWidget_framework.setMinimumSize(QtCore.QSize(0, 118))
        self.tabWidget_framework.setObjectName("tabWidget_framework")
        self.tab_6 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_6.sizePolicy().hasHeightForWidth())
        self.tab_6.setSizePolicy(sizePolicy)
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_6)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 501, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.choice_button = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.choice_button.setObjectName("choice_button")
        self.choice_button.addItem("")
        self.verticalLayout.addWidget(self.choice_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.tabs_browser = QtWidgets.QTabWidget(self.horizontalLayoutWidget_2)
        self.tabs_browser.setObjectName("tabs_browser")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabs_browser.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabs_browser.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabs_browser)
        self.tabWidget_framework.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget_framework.addTab(self.tab_7, "")
        self.vlayout.addWidget(self.tabWidget_framework)
        self.working_directory = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.working_directory.sizePolicy().hasHeightForWidth())
        self.working_directory.setSizePolicy(sizePolicy)
        self.working_directory.setMinimumSize(QtCore.QSize(0, 86))
        self.working_directory.setObjectName("working_directory")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.working_directory)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 211, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.layout_wk = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_wk.setContentsMargins(0, 0, 0, 0)
        self.layout_wk.setObjectName("layout_wk")
        self.vlayout.addWidget(self.working_directory)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 89))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 141, 58))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.until_box = QtWidgets.QComboBox(self.formLayoutWidget)
        self.until_box.setEditable(False)
        self.until_box.setCurrentText("")
        self.until_box.setObjectName("until_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.until_box)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.starting_box = QtWidgets.QComboBox(self.formLayoutWidget)
        self.starting_box.setObjectName("starting_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.starting_box)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(180, 20, 211, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comboBox_local = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox_local.setObjectName("comboBox_local")
        self.comboBox_local.addItem("")
        self.comboBox_local.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_local)
        self.vlayout.addWidget(self.groupBox)
        self.qtab_widget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qtab_widget.sizePolicy().hasHeightForWidth())
        self.qtab_widget.setSizePolicy(sizePolicy)
        self.qtab_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.qtab_widget.setMaximumSize(QtCore.QSize(16777215, 2000))
        self.qtab_widget.setBaseSize(QtCore.QSize(0, 0))
        self.qtab_widget.setObjectName("qtab_widget")
        self.snakemake = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.snakemake.sizePolicy().hasHeightForWidth())
        self.snakemake.setSizePolicy(sizePolicy)
        self.snakemake.setObjectName("snakemake")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.snakemake)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 631, 321))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 629, 319))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 611, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layout_snakemake = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_snakemake.setContentsMargins(0, 0, 0, 0)
        self.layout_snakemake.setObjectName("layout_snakemake")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.qtab_widget.addTab(self.snakemake, "")
        self.ipython = QtWidgets.QWidget()
        self.ipython.setObjectName("ipython")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.ipython)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 641, 331))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.layout_ipython = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.layout_ipython.setContentsMargins(0, 0, 0, 0)
        self.layout_ipython.setObjectName("layout_ipython")
        self.qtab_widget.addTab(self.ipython, "")
        self.logger = QtWidgets.QWidget()
        self.logger.setObjectName("logger")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.logger)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 661, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_logger = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_logger.setContentsMargins(0, 0, 0, 0)
        self.layout_logger.setObjectName("layout_logger")
        self.qtab_widget.addTab(self.logger, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 641, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 639, 329))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.qtab_widget.addTab(self.tab_3, "")
        self.vlayout.addWidget(self.qtab_widget)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.run_btn = QtWidgets.QPushButton(self.widget_5)
        self.run_btn.setObjectName("run_btn")
        self.horizontalLayout.addWidget(self.run_btn)
        self.stop_btn = QtWidgets.QPushButton(self.widget_5)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout.addWidget(self.stop_btn)
        self.unlock_btn = QtWidgets.QPushButton(self.widget_5)
        self.unlock_btn.setObjectName("unlock_btn")
        self.horizontalLayout.addWidget(self.unlock_btn)
        self.report_btn = QtWidgets.QPushButton(self.widget_5)
        self.report_btn.setObjectName("report_btn")
        self.horizontalLayout.addWidget(self.report_btn)
        self.save_report = QtWidgets.QPushButton(self.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_report.sizePolicy().hasHeightForWidth())
        self.save_report.setSizePolicy(sizePolicy)
        self.save_report.setObjectName("save_report")
        self.horizontalLayout.addWidget(self.save_report)
        self.dag_btn = QtWidgets.QPushButton(self.widget_5)
        self.dag_btn.setObjectName("dag_btn")
        self.horizontalLayout.addWidget(self.dag_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.vlayout.addWidget(self.widget_5)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 1)
        self.progressBar.setObjectName("progressBar")
        self.vlayout.addWidget(self.progressBar)
        self.vlayout.setStretch(1, 1)
        self.vlayout.setStretch(2, 1)
        self.vlayout.setStretch(5, 1)
        self.horizontalLayout_3.addLayout(self.vlayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImportConfig = QtWidgets.QAction(MainWindow)
        self.actionImportConfig.setObjectName("actionImportConfig")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionSnakemake = QtWidgets.QAction(MainWindow)
        self.actionSnakemake.setCheckable(False)
        self.actionSnakemake.setObjectName("actionSnakemake")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionIPython = QtWidgets.QAction(MainWindow)
        self.actionIPython.setCheckable(True)
        self.actionIPython.setObjectName("actionIPython")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setEnabled(True)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImportConfig)
        self.menuFile.addAction(self.actionQuit)
        self.menuOption.addAction(self.actionSnakemake)
        self.menuOption.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_framework.setCurrentIndex(0)
        self.tabs_browser.setCurrentIndex(0)
        self.qtab_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.choice_button.setToolTip(_translate("MainWindow", "<html><head/><body><p>Sequana pipelines are automatically fetched from sequana library.</p><p>Each pipeline is defined by a pipeline name. Its config file is fetched automatically.</p><p>Each pipeline require the user to define the input. It may be one of:</p><p><ul><li> a directory</li><li> a set of FastQ input file</li></ul></body></html>"))
        self.choice_button.setCurrentText(_translate("MainWindow", "Select a Sequana pipeline"))
        self.choice_button.setItemText(0, _translate("MainWindow", "Select a Sequana pipeline"))
        self.tabs_browser.setTabText(self.tabs_browser.indexOf(self.tab), _translate("MainWindow", "Directory (input)"))
        self.tabs_browser.setTabText(self.tabs_browser.indexOf(self.tab_2), _translate("MainWindow", "Sample"))
        self.tabWidget_framework.setTabText(self.tabWidget_framework.indexOf(self.tab_6), _translate("MainWindow", "Sequana pipelines"))
        self.tabWidget_framework.setTabText(self.tabWidget_framework.indexOf(self.tab_7), _translate("MainWindow", "Generic pipelines"))
        self.working_directory.setToolTip(_translate("MainWindow", "<html><head/><body><p>Set the working directory where the pipeline and its config are copied. </p><p>Files created in the pipeline will use this working directory as the root directory except if the pipeline specifies paths itself.</p><p><br/></p></body></html>"))
        self.working_directory.setTitle(_translate("MainWindow", "Working Directory"))
        self.groupBox.setTitle(_translate("MainWindow", "Pipeline control"))
        self.label.setText(_translate("MainWindow", "Until"))
        self.label_2.setText(_translate("MainWindow", "Starting"))
        self.label_3.setText(_translate("MainWindow", "Local or cluster run ?"))
        self.comboBox_local.setItemText(0, _translate("MainWindow", "local"))
        self.comboBox_local.setItemText(1, _translate("MainWindow", "cluster"))
        self.qtab_widget.setToolTip(_translate("MainWindow", "<p>This is an IPython shell included in the GUI. The entire Sequana GUI is accessible as the variable <span style=\" font-weight:600;\">gui.</span></p><p>For instance, you can access to layout or values set in the graphical interface with:</p><p>    gui.ui</p><p>More generally, this is a pure IPython code, so you use e.g. matplotlib/pylab:</p><p>  import pylab<br>pylab.plot([1,2,3])</p>"))
        self.qtab_widget.setTabText(self.qtab_widget.indexOf(self.snakemake), _translate("MainWindow", "Snakemake output"))
        self.qtab_widget.setTabText(self.qtab_widget.indexOf(self.ipython), _translate("MainWindow", "IPython shell"))
        self.qtab_widget.setTabText(self.qtab_widget.indexOf(self.logger), _translate("MainWindow", "Logger"))
        self.qtab_widget.setTabText(self.qtab_widget.indexOf(self.tab_3), _translate("MainWindow", "Config parameters"))
        self.run_btn.setToolTip(_translate("MainWindow", "Run the pipeline (shortcut: Ctrl+R)"))
        self.run_btn.setText(_translate("MainWindow", "Run"))
        self.run_btn.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.stop_btn.setToolTip(_translate("MainWindow", "Stop the running pipeline"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.unlock_btn.setToolTip(_translate("MainWindow", "Unlock the directory where the pipeline is run"))
        self.unlock_btn.setText(_translate("MainWindow", "Unlock"))
        self.report_btn.setText(_translate("MainWindow", "Open Report"))
        self.save_report.setText(_translate("MainWindow", "Save Config"))
        self.dag_btn.setToolTip(_translate("MainWindow", "Pressing this button, a DAG is created and shown. \n"
"This is a good way to check your config file ."))
        self.dag_btn.setText(_translate("MainWindow", "Show Dag"))
        self.progressBar.setToolTip(_translate("MainWindow", "<p>Progress of the pipeline. color codes:\n"
"            <ul>\n"
"                <li style=\"color:red\">Red: an error occured</li>\n"
"                <li style=\"color:green\">Green: completed with success</li>\n"
"                <li style=\"color:blue\">Blue: in progress</li>\n"
"            </ul>\n"
"            </p>\""))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionImportConfig.setText(_translate("MainWindow", "&Import Config File"))
        self.actionImportConfig.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionQuit.setText(_translate("MainWindow", "&Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSnakemake.setText(_translate("MainWindow", "Snakemake &Options"))
        self.actionSnakemake.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionPreferences.setText(_translate("MainWindow", "&Preferences"))
        self.actionPreferences.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionIPython.setText(_translate("MainWindow", "Show/Hide IPython &Debug dialog"))
        self.actionIPython.setToolTip(_translate("MainWindow", "Show or Hide an IPython dialog for debugging"))
        self.actionIPython.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionHelp.setText(_translate("MainWindow", "Quick Start"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))

