# coding: utf-8
import os
import sys
import tempfile
import shutil
import subprocess as sp
import multiprocessing

from PyQt5.Qt import QTemporaryDir
from PyQt5.QtCore import (Qt, QCoreApplication, pyqtSlot, QEvent, QSize,
                          QSettings)
from PyQt5.QtWidgets import (QApplication, QPushButton, QComboBox, QWidget,
                             QLineEdit, QTabWidget, QLabel, QFrame, QGroupBox,
                             QCheckBox, QSpinBox, QDoubleSpinBox, QScrollArea,
                             QMenuBar, QAction, QSizePolicy, QTextEdit)
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox, QColorDialog
from PyQt5.QtWidgets import QFormLayout, QHBoxLayout, QVBoxLayout, QBoxLayout
from PyQt5.QtWidgets import QSplashScreen, QProgressBar
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtGui import QPixmap, QColor

from sequana import snaketools, sequana_data
from sequana.snaketools import Module


class SequanaGUI(QWidget):
    """ Sequana GUI !
    """

    _not_a_rule = {"requirements", "gatk_bin", "input_directory", "pattern",
                   "samples"}
    _browser_keyword = {"reference"}

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # snakemake cluster/local option dialog windows
        self.snakemake_dialog = SnakemakeOptionDialog(self)

        # create menu bar
        self.create_menu_bar()

        # box to choose the pipeline
        self.pipeline_is_chosen = False
        choice_layout = QHBoxLayout()
        self.create_choice_button()
        choice_layout.addWidget(self.choice_button)

        # create browser tab to choice directory or files
        self.create_tabs_browser()
        self.tabs_browser.currentChanged.connect(self.switch_run)

        # select the working directory
        groupbox_layout = QHBoxLayout()
        self.working_dir = FileBrowser(directory=True)
        groupbox_layout.addWidget(self.working_dir)
        groupbox = QGroupBox("Working directory")
        groupbox.setContentsMargins(0, 5, 0, 0)
        groupbox.setLayout(groupbox_layout)

        # "until" and "starting" combobox
        control_widget = QGroupBox("Pipeline control")
        control_widget.setContentsMargins(0, 3, 0, -3)
        control_layout = QVBoxLayout(control_widget)
        control_layout.setSpacing(0)
        until_box = ComboBoxOption("Until")
        starting_box = ComboBoxOption("Starting")
        control_layout.addWidget(starting_box)
        control_layout.addWidget(until_box)

        # connect fuction on working_dir browser
        self.working_dir.clicked_connect(self.check_existing_config)
        self.working_dir.clicked_connect(self.switch_run)

        # formular which contains all options the pipeline chosen
        widget_formular = QWidget()
        self.formular = QVBoxLayout(widget_formular)
        self.formular.setSpacing(10)
        scroll_area = QScrollArea()
        scroll_area.setWidget(widget_formular)
        scroll_area.setWidgetResizable(True)
        scroll_area.setMinimumHeight(300)

        # main layout
        vlayout = QVBoxLayout(self)
        vlayout.insertSpacing(0, 10)

        # add widgets in layout
        vlayout.addLayout(choice_layout)
        vlayout.addWidget(self.tabs_browser)
        vlayout.addWidget(groupbox)
        vlayout.addWidget(control_widget)
        vlayout.addWidget(scroll_area)
        vlayout.addWidget(self.create_footer_button())

        # main window options
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Sequana")
        self.show()

        self._tempdir = QTemporaryDir()

    def quit(self):
        quit_msg = WarningMessage("Do you really want to quit ?")
        quit_msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        quit_msg.setDefaultButton(QMessageBox.No)
        quit_answer = quit_msg.exec_()
        if quit_answer == QMessageBox.Yes:
            self.close()

    def about(self):
        from sequana import version
        url = 'gdsctools.readthedocs.io'
        msg = About()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Sequana version %s " % version)
        msg.setInformativeText("""
            Online documentation on <a href="http://%(url)s">%(url)s</a>
            """ % {"url": url})
        msg.setWindowTitle("Sequana")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        # msg.buttonClicked.connect(self.msgbtn)
        retval = msg.exec_()

    def import_config(self):
        pass

    def clear_layout(self, layout):
        """ Clean all widget contained in a layout.
        """
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                self.clear_layout(child.layout())

    def create_menu_bar(self):
        """ Create menu bar.
        """
        # action quit
        quitAction = QAction("Quit", self)
        quitAction.setShortcut('Ctrl+Q')
        quitAction.setStatusTip('Quit Sequana')
        quitAction.triggered.connect(self.quit)

        # action About
        aboutAction = QAction("About", self)
        aboutAction.setShortcut('Ctrl+A')
        aboutAction.triggered.connect(self.about)

        # action Options
        optionAction = QAction("Option", self)
        optionAction.setShortcut('Ctrl+O')
        optionAction.triggered.connect(self.snakemake_dialog.exec_)

        # action import config file
        importAction = QAction("Import", self)
        importAction.setShortcut('Ctrl+I')
        importAction.triggered.connect(self.import_config)

        # set menu bar
        menu_bar = QMenuBar(self)
        menu_bar.setMinimumWidth(500)
        options_menu = menu_bar.addMenu("&File")
        options_menu.addAction(importAction)
        options_menu.addAction(quitAction)
        options_menu = menu_bar.addMenu("&Option")
        options_menu.addAction(optionAction)
        options_menu = menu_bar.addMenu("&About")
        options_menu.addAction(aboutAction)

    def create_choice_button(self):
        """ Create button to select the wished pipeline.
        """
        self.choice_button = QComboBox()
        snaketools.pipeline_names.sort()
        self.choice_button.addItems(["select pipeline"] +
                                    snaketools.pipeline_names)
        self.choice_button.currentIndexChanged[str].connect(
            self.on_pipeline_choice)
        self.choice_button.installEventFilter(self)

    @pyqtSlot(str)
    def on_pipeline_choice(self, index):
        """ Change options formular when user change the pipeline.
        """
        config_file = snaketools.Module(index)._get_config()
        self.choice_button.removeItem(
            self.choice_button.findText("select pipeline"))
        try:
            cfg = snaketools.SequanaConfig(config_file)
            cfg.cleanup()
            self.config_dict = cfg.config
        except AssertionError:
            print("Could not parse the config file")
            return

        self.create_base_formular(self.config_dict)
        self.pipeline_is_chosen = True
        self.switch_run()

    def create_base_formular(self, config_dict):
        """ Create formular with all options necessary for a pipeline.
        """
        self.clear_layout(self.formular)
        rules_list = list(config_dict.keys())
        rules_list.sort()
        self.necessary_dict = {}
        for count, rule in enumerate(rules_list):
            # Check if dictionnary or not
            contains = config_dict[rule]
            if isinstance(contains, dict) and (
                    rule not in SequanaGUI._not_a_rule):
                rule_box = RuleFormular(rule, contains, count)
                self.formular.addWidget(rule_box)
            else:

                if isinstance(contains, list):
                    self.necessary_dict = dict(self.necessary_dict,
                                           **{rule: contains})
                else:
                    self.necessary_dict = dict(self.necessary_dict,
                                           **{rule: '{0}'.format(contains)})

    def create_tabs_browser(self):
        """ Generate file browser widget.
        """
        # create browser file
        fastq_filter = "Fastq file (*.fastq *.fastq.gz *.fq *.fq.gz)"
        paired_tab = FileBrowser(paired=True, file_filter=fastq_filter)
        directory_tab = FileBrowser(directory=True, file_filter=fastq_filter)
        paired_tab.clicked_connect(self.switch_run)
        directory_tab.clicked_connect(self.switch_run)
        # create tab box
        self.tabs_browser = QTabWidget()
        self.tabs_browser.addTab(directory_tab, "Directory")
        self.tabs_browser.addTab(paired_tab, "Sample")

    def create_footer_button(self):
        """ Create Run/Save/Quit buttons
        """
        self.run_btn = QPushButton("Run")
        self.run_btn.setEnabled(False)
        self.run_btn.clicked.connect(self.run_sequana)

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save_config_file)

        self.dag_btn = QPushButton("Show DAG")
        # self.dag_btn.setEnabled(False)
        self.dag_btn.setToolTip("""<p>Pressing this button, a DAG is created
                                 and shown. This is a good way to check your
                                 config file </p>""" )
        self.dag_btn.clicked.connect(self.show_dag)

        footer_widget = QWidget()
        footer_layout = QHBoxLayout(footer_widget)
        footer_layout.addWidget(self.run_btn)
        footer_layout.addWidget(save_btn)
        footer_layout.addWidget(self.dag_btn)
        return footer_widget

    def show_dag(self):

        print("Creating the DAG (takes a few seconds)")
        if self.pipeline_is_chosen:
            snakefile = Module(self.choice_button.currentText()).snakefile
        else:
            print("Select a pipeline first")
            return

        if self.check_existing_config():
            working_dir = self.working_dir.get_filenames()
            cfgpath = working_dir + "/config.yaml"
        else:
            print("No config file found, save it")
            return

        # Although the config and pipeline are in the working directory, we do
        # not want to interfer with it. So, we use a temporary directory
        # shutil.copy(snakefile, self._tempdir.path())
        # shutil.copy(cfgpath, self._tempdir.path() + os.sep + "config.yaml")
        # cwd = self._tempdir.path()
        # snakemake_line = ["snakemake", "-s", os.path.basename(snakefile)]
        # snakemake_line += ["--rulegraph", "--configfile", "config.yaml"]
        
        try:
            snakemake_line = ["snakemake", "-s", snakefile]
            snakemake_line += ["--rulegraph", "--configfile", cfgpath]
            cwd = working_dir

            snakemake_proc = sp.Popen(snakemake_line,
                                  cwd=cwd,
                                  stdout=sp.PIPE)
    
            filename = self._tempdir.path() + os.sep + "test.svg"
            cmd = ["dot", "-Tsvg", "-o", filename]
            dot_proc = sp.Popen(cmd, cwd=cwd,
                            stdin=snakemake_proc.stdout)
            dot_proc.communicate()
            if os.path.exists(filename):
                diag = SVGDialog(filename)
                diag.exec_()
        except Exception as err:
            print(err)


################

    def run_sequana(self):
        working_dir = self.working_dir.get_filenames()
        self.save_config_file()
        rules = self.get_rules(self.formular)
        snakefile = Module(self.choice_button.currentText()).snakefile
        shutil.copy(snakefile, working_dir)
        snakemake_line = ["snakemake", "-s", snakefile]
        options = self.snakemake_dialog.get_snakemake_options()
        snakemake_line += options
        snakemake_proc = sp.Popen(snakemake_line, cwd=working_dir)
        snakemake_proc.communicate()

###############

    def switch_run(self):
        if self.working_dir.path_is_setup():
            if self.tabs_browser.currentWidget().path_is_setup():
                if self.working_dir.path_is_setup():
                    if self.pipeline_is_chosen:
                        return self.run_btn.setEnabled(True)
        return self.run_btn.setEnabled(False)

    def save_config_file(self):
        try:
            formular_dict = dict(self.create_formular_dict(self.formular),
                                 **self.necessary_dict)
        except AttributeError:
            msg = WarningMessage("You must choose a pipeline before saving.")
            msg.exec_()
            return

        # get samples names or input_directory
        if self.tabs_browser.currentIndex() == 1:
            formular_dict["samples"] = (
                self.tabs_browser.currentWidget().get_filenames())
        else:
            formular_dict["input_directory"] = (
                self.tabs_browser.currentWidget().get_filenames())
        yaml = snaketools.SequanaConfig(data=formular_dict,
                                        test_requirements=False)
        if self.working_dir.path_is_setup():
            yaml_path = self.working_dir.get_filenames() + "/config.yaml"
            yaml.copy_requirements(target=self.working_dir.get_filenames())
            if os.path.isfile(yaml_path):
                save_msg = WarningMessage(
                    "The file {0} already exist".format(yaml_path))
                save_msg.setInformativeText(
                    "Do you want to overwrite the file?")
                save_msg.setStandardButtons(
                    QMessageBox.Save | QMessageBox.Discard |
                    QMessageBox.Cancel)
                save_msg.setDefaultButton(QMessageBox.Save)
                if save_msg.exec_() == 2048:
                    yaml.save(yaml_path)
            else:
                yaml.save(yaml_path)
        else:
            msg = WarningMessage("You must indicate your working directory")
            msg.exec_()

    def create_formular_dict(self, layout):
        widgets = (layout.itemAt(i).widget() for i in range(layout.count()))
        formular_dict = {w.get_name(): w.get_value() if w.is_option()
                         else self.create_formular_dict(w.get_layout())
                         for w in widgets}
        return formular_dict

    def check_existing_config(self):
        path_directory = self.working_dir.get_filenames()
        config_file = path_directory + "/config.yaml"
        if not os.path.isfile(config_file):
            return False
        if not self.pipeline_is_chosen:
            msg = WarningMessage("A config.yaml file already exist in this "
                                 "directory. Please, choose a pipeline to "
                                 "know if the existing config file correspond "
                                 "to your pipeline.", self)
            self.working_dir.set_empty_path()
            msg.exec_()
            return False
        try:
            config_dict = snaketools.SequanaConfig(config_file).config
        except AssertionError:
            msg = WarningMessage("Could not parse the config file.")
            msg.exec_()
            return False
        except Exception as err:
            msg = WarningMessage(
                "Unexpected error while checking the config file %s."
                % config_file + str(err))
            msg.exec_()
            return False
    
        if set(self.config_dict.keys()) == set(config_dict.keys()):
            msg = QMessageBox(
                QMessageBox.Question, "Question",
                "A config file already exist in the working directory.\n"
                "Do you want to merge this file ?",
                QMessageBox.Yes | QMessageBox.No,
                self, Qt.Dialog | Qt.CustomizeWindowHint)
            if msg.exec_() == 16384:
                self.config_dict.update(config_dict)
                self.create_base_formular(self.config_dict)
        return True

    def get_rules(self, layout):
        widgets = (layout.itemAt(i).widget() for i in range(layout.count()))
        rules = [w.get_name() for w in widgets]
        return rules

    def eventFilter(self, source, event):
        """ Inactivate wheel event of combobox
        """
        if event.type() == QEvent.Wheel and source is self.choice_button:
            return True
        return False


class About(QMessageBox):
    """A resizable QMessageBox for the About dialog"""
    def __init__(self, *args, **kwargs):
        super(About, self).__init__(*args, **kwargs)
        self.setSizeGripEnabled(True)

    def event(self, e):
        result = super(About, self).event(e)

        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setMinimumWidth(0)
        self.setMaximumWidth(16777215)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        textEdit = self.findChild(QTextEdit)
        if textEdit is not None:
            textEdit.setMinimumHeight(0)
            textEdit.setMaximumHeight(16777215)
            textEdit.setMinimumWidth(0)
            textEdit.setMaximumWidth(16777215)
            textEdit.setSizePolicy(QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)

        return result

#    # We only need to extend resizeEvent, not every event.
#    def resizeEvent(self, event):
#        result = super(About, self).resizeEvent(event)
#        details_box = self.findChild(QTextEdit)
#        if details_box is not None:
#            details_box.setFixedSize(details_box.sizeHint())
#        return result



class FileBrowser(QWidget):
    """ Class to create a file browser in PyQT5.
    """
    def __init__(self, paired=False, directory=False, file_filter=None):
        super().__init__()
        # Set filter for file dialog
        self.filter = "Any file (*)"
        if file_filter is not None:
            self.filter = file_filter + ";;" + self.filter
        self.empty_msg = "No file selected"
        self.btn = QPushButton("Browse")    
        self.btn.setFixedSize(100,20)

        # Add default color
        self.btn.setStyleSheet("QPushButton {background-color: #AA0000; "
                               "color: #EEEEEE}")

        if directory:
            self.empty_msg = "No directory selected"
            self.btn.clicked.connect(self.browse_directory)
        elif paired:
            self.btn.clicked.connect(self.browse_paired_file)
        else:
            self.btn.clicked.connect(self.browse_file)
        self.btn_filename = QLabel(self.empty_msg)
        self.set_empty_path()
        widget_layout = QHBoxLayout(self)
        widget_layout.setContentsMargins(0, 3, 0, 3)
        widget_layout.addWidget(self.btn)
        widget_layout.addWidget(self.btn_filename)
    
    def _setup_true(self):
        self.setup = True
        
    def setup_color(self):
        if self.path_is_setup():
            self.btn.setStyleSheet("QPushButton {background-color: #00AA00; "
                                   "color: #EEEEEE}")
        else:
            self.btn.setStyleSheet("QPushButton {background-color: #AA0000; "
                                   "color: #EEEEEE}")

    def browse_paired_file(self):
        file_path = QFileDialog.getOpenFileNames(self, "Select a sample", ".",
                                                 self.filter)[0]
        if not file_path:
            self.set_empty_path()
        elif len(file_path) > 2:
            msg = WarningMessage("You must pick only one sample", self)
            self.set_empty_path()
            msg.exec_()
        else:
            self.paths = {"file{0}".format(i+1): file_path[i]
                          for i in range(0, len(file_path))}
            self.btn_filename.setText("\n".join([key + ": " + value
                                      for key, value in self.paths.items()]))
            self._setup_true()
            self.setup_color()

    def browse_directory(self):
        dialog = DirectoryDialog(self, "Select a directory", ".", self.filter)
        directory_path = dialog.get_directory_path()
        if directory_path:
            self.set_filenames(directory_path)
        else:
            self.set_empty_path()

    def browse_file(self):
        try:
            file_path = QFileDialog.getOpenFileNames(self, "Single File", ".",
                                                     self.filter)[0][0]
            self.set_filenames(file_path)
        except IndexError:
            self.set_empty_path()

    def get_filenames(self):
        return self.paths

    def set_filenames(self, filename):
        self.paths = filename
        self.btn_filename.setText("....../" + filename.split("/")[-1])
        self._setup_true()
        self.setup_color()

    def set_empty_path(self):
        self.btn_filename.setText(self.empty_msg)
        self.paths = ""
        self.setup = False
        self.setup_color()

    def set_enable(self, switch_bool):
        if switch_bool:
            self.setup_color()
        else:
            self.btn.setStyleSheet("QPushButton {background-color: #AAAAAA; "
                                   "color: #222222}")
        self.btn.setEnabled(switch_bool)

    def path_is_setup(self):
        return self.setup

    def clicked_connect(self, function):
        """ Connect additionnal function on browser button. It is used to
        activate run button in Sequana GUI.
        """
        self.btn.clicked.connect(function)


class RuleFormular(QGroupBox):
    do_option = "do"
    def __init__(self, rule_name, rule_dict, count=0):
        super().__init__(rule_name)

        # to handle recursive case
        self.do_widget = None

        self.rule_name = rule_name
        self.rule_dict = rule_dict
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(2)
        self.setAutoFillBackground(True)

        for option, value in self.rule_dict.items():
            if option.endswith("_directory"):
                option_widget = FileBrowserOption(option, value,
                                                  directory=True)
            elif option in SequanaGUI._browser_keyword:
                option_widget = FileBrowserOption(option, value,
                                                  directory=False)
            elif isinstance(value, bool):
                option_widget = BooleanOption(option, value)
                if option == RuleFormular.do_option:
                    self.do_widget = option_widget
                    option_widget.connect(self._widget_lock)
            else:
                try:
                    option_widget = NumberOption(option, value)
                except TypeError:
                    try:
                        option_widget = TextOption(option, value)
                    except TypeError:
                        option_widget = RuleFormular(option, value)
            self.layout.addWidget(option_widget)
        try:
            self._widget_lock(self.do_widget.get_value())
        except AttributeError:
            pass

    def get_name(self):
        return self.rule_name

    def get_layout(self):
        return self.layout

    def is_option(self):
        return False

    def _widget_lock(self, switch_bool):
        widget_list = (self.layout.itemAt(i).widget() for i in
                       range(self.layout.count()))
        for w in widget_list:
            if w is self.do_widget:
                continue
            w.set_enable(switch_bool)

    def set_enable(self, switch_bool):
        self._widget_lock(switch_bool)
        

class GeneralOption(QWidget):
    """ Parent class for Options. It define design of options
    """
    def __init__(self, option):
        super().__init__()
        self.option = option
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 3, 0, 3)
        self.layout.addWidget(QLabel(option))

    def get_name(self):
        return self.option

    def is_option(self):
        return True

    def get_value(self):
        pass

    def get_tuple(self):
        return (self.get_name(), self.get_value())

    def set_enable(self):
        pass


class BooleanOption(GeneralOption):
    """ Wrapp QCheckBox class
    """
    def __init__(self, option, value):
        super().__init__(option)

        self.check_box = QCheckBox()
        self.check_box.setChecked(value)

        self.answer = QLabel()
        self.switch_answer()

        self.check_box.clicked.connect(self.switch_answer)

        self.layout.addWidget(self.check_box)
        self.layout.addWidget(self.answer)

    def get_value(self):
        return self.check_box.isChecked()

    def set_enable(self, switch_bool):
        self.check_box.setEnabled(switch_bool)

    def switch_answer(self):
        value = self.get_value()
        if value:
            self.answer.setText("<b> yes <\b>")
        else:
            self.answer.setText("<b> no <\b>")

    def connect(self, task):
        self.check_box.clicked.connect(task)


class TextOption(GeneralOption):
    def __init__(self, option, value):
        super().__init__(option)
        self.text = QLineEdit(value)

        self.layout.addWidget(self.text)

    def get_value(self):
        if not self.text.text():
            return "''"
        return self.text.text()

    def set_value(self, text):
        self.text.setText(text)

    def set_enable(self, switch_bool):
        self.text.setEnabled(switch_bool)


class NumberOption(GeneralOption):
    def __init__(self, option, value):
        super().__init__(option)

        if isinstance(value, float):
            self.number = QDoubleSpinBox()
        else:
            self.number = QSpinBox()
        self.number.setRange(-1000000, 1000000)
        self.number.setValue(value)
        self.number.installEventFilter(self)

        self.layout.addWidget(self.number)

    def get_value(self):
        return self.number.value()

    def set_value(self, value):
        self.number.setValue(value)

    def set_range(self, min_value, max_value):
        self.number.setRange(min_value, max_value)

    def set_enable(self, switch_bool):
        self.number.setEnabled(switch_bool)

    def eventFilter(self, source, event):
        if event.type() == QEvent.Wheel and source is self.number:
            return True
        return False


class FileBrowserOption(GeneralOption):
    def __init__(self, option, value=None, directory=False):
        super().__init__(option)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.browser = FileBrowser(directory=directory)
        self.layout.addWidget(self.browser)
        if value:
            self.browser.set_filenames(value)

    def get_value(self):
        if not self.browser.get_filenames():
            return "''"
        return self.browser.get_filenames()

    def set_enable(self, switch_bool):
        self.browser.set_enable(switch_bool)


class ComboBoxOption(GeneralOption):
    def __init__(self, option):
        super().__init__(option)
        self.combobox = QComboBox()
        self.layout.addWidget(self.combobox)

    def add_items(self, items_list):
        self.combobox.clear()
        self.combobox.addItems([None] + items_list)

    def get_value(self):
        return self.combobox.currentText()


class SVGDialog(QDialog):
    def __init__(self, filename):
        super().__init__()
        self.main_layout = QVBoxLayout(self)
        self.setWindowTitle("DAG")

        import os
        if os.path.exists(filename):
            widget = QSvgWidget(filename)
            self.main_layout.addWidget(widget)


class SnakemakeOptionDialog(QDialog):
    """ Widget to set up options of snakemake and launch pipeline. It provides
    a progress bar to know how your jobs work.
    """
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.main_layout = QVBoxLayout(self)
        self.setWindowTitle("Snakemake options")

        # Settings option
        settings = QSettings("Sequana", "Snakemake_option")
        self._cores = settings.value("cores", 2, type=int)
        self._jobs = settings.value("jobs", 2, type=int)
        self._cluster = settings.value("cluster", "", type=str)
        self._tab_pos = settings.value("tab_pos", 0, type=int)

        self.set_launch_options()

        footer = self.footer_button()
        self.main_layout.addWidget(self.tabs)
        self.main_layout.addWidget(footer)

    def ok_event(self):
        settings = QSettings("Sequana", "Snakemake_option")
        settings.setValue("cores", self.cores_option.get_value())
        settings.setValue("jobs", self.jobs_option.get_value())
        settings.setValue("cluster", self.cluster_options.get_value())
        settings.setValue("tab_pos", self.tabs.currentIndex())
        self.close()

    def cancel_event(self):
        self.cores_option.set_value(self._cores)
        self.jobs_option.set_value(self._jobs)
        self.cluster_options.set_value(self._cluster)
        self.tabs.setCurrentIndex(self._tab_pos)
        self.close()

    def footer_button(self):
        ok_btn = QPushButton("Ok")
        ok_btn.clicked.connect(self.ok_event)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.cancel_event)

        footer_widget = QWidget()
        footer_layout = QHBoxLayout(footer_widget)
        footer_layout.addWidget(ok_btn)
        footer_layout.addWidget(cancel_btn)

        return footer_widget

    def set_launch_options(self):
        self.cores_option = NumberOption("--cores", self._cores)
        self.jobs_option = NumberOption("--jobs", self._jobs)
        self.cluster_options = TextOption("--cluster", self._cluster)

        launch_cluster_widget = QWidget()
        launch_cluster_layout = QVBoxLayout(launch_cluster_widget)
        launch_cluster_layout.addWidget(self.cluster_options)
        launch_cluster_layout.addWidget(self.jobs_option)

        self.jobs_option.set_range(1, 10000)
        self.cores_option.set_range(1, multiprocessing.cpu_count())

        # create tab
        self.tabs = QTabWidget()
        self.tabs.addTab(self.cores_option, "Local")
        self.tabs.addTab(launch_cluster_widget, "Cluster")
        self.tabs.setCurrentIndex(self._tab_pos)

    def get_snakemake_options(self):
        # cluster/local option
        current_tab = self.tabs.currentWidget()
        try:
            option_list = [current_tab.get_name(),
                           str(current_tab.get_value())]
        except AttributeError:
            current_layout = current_tab.layout()
            widgets = (current_layout.itemAt(i).widget() for i in
                       range(current_layout.count()))
            option_list = [str(x) for w in widgets for x in w.get_tuple()]
        return option_list


class WarningMessage(QMessageBox):
    def __init__(self, msg, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Warning message")
        self.setIcon(QMessageBox.Warning)
        self.setText(msg)


class DirectoryDialog(QFileDialog):
    def __init__(self, parent, title, directory, file_filter):
        super().__init__(parent)
        self.setAcceptMode(QFileDialog.AcceptOpen)
        self.setFileMode(QFileDialog.Directory)
        self.setViewMode(QFileDialog.Detail)
        self.setWindowTitle(title)
        self.setDirectory(directory)
        self.setNameFilter(file_filter)

    def get_directory_path(self):
        if self.exec_():
            return self.selectedFiles()[0]
        return None


def main():
    app = QApplication(sys.argv)

    import time

    filename = sequana_data("splash_loading.png", "../gui")

    splash_pix = QPixmap(filename)
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)

    progressBar = QProgressBar(splash)
    splash.setMask(splash_pix.mask())

    # Show the splash screen for 5 seconds
    splash.show()
    for i in range(0, 100):
        progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 1./100.:
            app.processEvents()

    app.processEvents()
    sequana = SequanaGUI()
    sequana.show()
    splash.finish(sequana)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()