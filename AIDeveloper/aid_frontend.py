import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtWidgets, QtGui
import sys,os,json

#dir_root = os.getcwd()
#dir_settings = os.path.join(dir_root,"AIDeveloper_Settings.json")#dir to settings
#if os.path.isfile(dir_settings):
#    pass
#else:
#    dir_root = os.path.dirname(sys.argv[0]) #Get directory of this script
#    dir_settings = os.path.join(dir_root,"AIDeveloper_Settings.json")#dir to settings

#The above does not work:
#When using the search-function in windows to look for AIDeveloper.exe, and starting
#it from there (double-click on the search result), the app crashed because it
#set the dir_root to C:/Windows/System32
#The only way I found to get the directory where AID sits, is to import a module
#and call "__file__"

import aid_start #import a module that sits in the AIDeveloper folder
dir_root = os.path.dirname(aid_start.__file__)#ask the module for its origin
dir_settings = os.path.join(dir_root,"AIDeveloper_Settings.json")#dir to settings
with open(dir_settings) as f:
    Default_dict = json.load(f)
    #Older versions of AIDeveloper might not have the Icon theme option->add it!
    if "Icon theme" not in Default_dict.keys():
        Default_dict["Icon theme"] = "Icon theme 1"
    if "Path of last model" not in Default_dict.keys():
        Default_dict["Path of last model"] = 'c:\\'

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class MyTable(QtWidgets.QTableWidget):
    dropped = QtCore.pyqtSignal(list)

    def __init__(self,  rows, columns, parent):
        super(MyTable, self).__init__(rows, columns, parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        #self.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.drag_item = None
        self.drag_row = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.drag_item = None
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.dropped.emit(links)
        else:
            event.ignore()       
        
    def startDrag(self, supportedActions):
        super(MyTable, self).startDrag(supportedActions)
        self.drag_item = self.currentItem()
        self.drag_row = self.row(self.drag_item)


class Fitting_Ui(QtWidgets.QWidget):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(797, 786)

        self.gridLayout_slider_pop = QtWidgets.QGridLayout(Form)
        self.gridLayout_slider_pop.setObjectName("gridLayout_slider_pop")
        self.verticalLayout_4_pop = QtWidgets.QVBoxLayout()
        self.verticalLayout_4_pop.setObjectName("verticalLayout_4_pop")
        self.horizontalLayout_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_pop.setObjectName("horizontalLayout_pop")
        self.tableWidget_HistoryInfo_pop = QtWidgets.QTableWidget(Form)
        self.tableWidget_HistoryInfo_pop.setObjectName("tableWidget_HistoryInfo_pop")
        self.tableWidget_HistoryInfo_pop.setColumnCount(0)
        self.tableWidget_HistoryInfo_pop.setRowCount(0)
        self.horizontalLayout_pop.addWidget(self.tableWidget_HistoryInfo_pop)
        self.verticalLayout_2_pop = QtWidgets.QVBoxLayout()
        self.verticalLayout_2_pop.setObjectName("verticalLayout_2_pop")
        self.pushButton_UpdatePlot_pop = QtWidgets.QPushButton(Form)
        self.pushButton_UpdatePlot_pop.setObjectName("pushButton_UpdatePlot_pop")
        self.verticalLayout_2_pop.addWidget(self.pushButton_UpdatePlot_pop)

        self.checkBox_realTimePlotting_pop = QtWidgets.QCheckBox(Form)
        self.checkBox_realTimePlotting_pop.setObjectName("checkBox_realTimePlotting_pop")
        self.verticalLayout_2_pop.addWidget(self.checkBox_realTimePlotting_pop)
        self.horizontalLayout_rtepochs_pop = QtWidgets.QHBoxLayout()
        self.label_realTimeEpochs_pop = QtWidgets.QLabel(Form)
        self.label_realTimeEpochs_pop.setObjectName("label_realTimeEpochs_pop")
        self.horizontalLayout_rtepochs_pop.addWidget(self.label_realTimeEpochs_pop)
        self.spinBox_realTimeEpochs = QtWidgets.QSpinBox(Form)
        self.spinBox_realTimeEpochs.setObjectName("spinBox_realTimeEpochs")
        self.horizontalLayout_rtepochs_pop.addWidget(self.spinBox_realTimeEpochs)        
        self.verticalLayout_2_pop.addLayout(self.horizontalLayout_rtepochs_pop)
        
        self.horizontalLayout_pop.addLayout(self.verticalLayout_2_pop)
        self.verticalLayout_4_pop.addLayout(self.horizontalLayout_pop)
        self.verticalLayout_3_pop = QtWidgets.QVBoxLayout()
        self.verticalLayout_3_pop.setObjectName("verticalLayout_3_pop")
        self.widget_pop = pg.GraphicsLayoutWidget(Form)#QtWidgets.QWidget(Form)
        self.widget_pop.setMinimumSize(QtCore.QSize(771, 331))
        self.widget_pop.setObjectName("widget_pop")
        self.verticalLayout_3_pop.addWidget(self.widget_pop)
        self.splitter_pop = QtWidgets.QSplitter(Form)
        self.splitter_pop.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_pop.setObjectName("splitter_pop")
        self.groupBox_FittingInfo_pop = QtWidgets.QGroupBox(self.splitter_pop)
        self.groupBox_FittingInfo_pop.setObjectName("groupBox_FittingInfo_pop")
        self.gridLayout_2_pop = QtWidgets.QGridLayout(self.groupBox_FittingInfo_pop)
        self.gridLayout_2_pop.setObjectName("gridLayout_2_pop")
        self.progressBar_Fitting_pop = QtWidgets.QProgressBar(self.groupBox_FittingInfo_pop)
        self.progressBar_Fitting_pop.setProperty("value", 24)
        self.progressBar_Fitting_pop.setObjectName("progressBar_Fitting_pop")
        self.gridLayout_2_pop.addWidget(self.progressBar_Fitting_pop, 0, 0, 1, 1)
        self.textBrowser_FittingInfo_pop = QtWidgets.QTextBrowser(self.groupBox_FittingInfo_pop)
        self.textBrowser_FittingInfo_pop.setObjectName("textBrowser_FittingInfo_pop")
        self.gridLayout_2_pop.addWidget(self.textBrowser_FittingInfo_pop, 1, 0, 1, 1)
        self.horizontalLayout_saveClearText_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_saveClearText_pop.setObjectName("horizontalLayout_saveClearText_pop")
        self.pushButton_saveTextWindow_pop = QtWidgets.QPushButton(self.groupBox_FittingInfo_pop)
        self.pushButton_saveTextWindow_pop.setObjectName("pushButton_saveTextWindow_pop")
        self.horizontalLayout_saveClearText_pop.addWidget(self.pushButton_saveTextWindow_pop)
        self.pushButton_clearTextWindow_pop = QtWidgets.QPushButton(self.groupBox_FittingInfo_pop)
        self.pushButton_clearTextWindow_pop.setObjectName("pushButton_clearTextWindow_pop")
        self.horizontalLayout_saveClearText_pop.addWidget(self.pushButton_clearTextWindow_pop)
        self.gridLayout_2_pop.addLayout(self.horizontalLayout_saveClearText_pop, 2, 0, 1, 1)
        self.groupBox_ChangeModel_pop = QtWidgets.QGroupBox(self.splitter_pop)
        self.groupBox_ChangeModel_pop.setEnabled(True)
        self.groupBox_ChangeModel_pop.setCheckable(False)
        self.groupBox_ChangeModel_pop.setObjectName("groupBox_ChangeModel_pop")
        self.gridLayout_3_pop = QtWidgets.QGridLayout(self.groupBox_ChangeModel_pop)
        self.gridLayout_3_pop.setObjectName("gridLayout_3_pop")
        self.tabWidget_DefineModel_pop = QtWidgets.QTabWidget(self.groupBox_ChangeModel_pop)
        self.tabWidget_DefineModel_pop.setEnabled(True)
        self.tabWidget_DefineModel_pop.setToolTip("")
        self.tabWidget_DefineModel_pop.setUsesScrollButtons(True)
        self.tabWidget_DefineModel_pop.setObjectName("tabWidget_DefineModel_pop")
        self.tab_DefineModel_pop = QtWidgets.QWidget()
        self.tab_DefineModel_pop.setObjectName("tab_DefineModel_pop")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_DefineModel_pop)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_defineModel_pop = QtWidgets.QVBoxLayout()
        self.verticalLayout_defineModel_pop.setObjectName("verticalLayout_defineModel_pop")
        
        
        
        
        
        
        
        
#        self.horizontalLayout_2_pop = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_2_pop.setObjectName("horizontalLayout_2_pop")
#        self.label_ModelGeom_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
#        self.label_ModelGeom_pop.setObjectName("label_ModelGeom_pop")
#        self.horizontalLayout_2_pop.addWidget(self.label_ModelGeom_pop)
#        self.horizontalLayout_2_pop.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
#        self.comboBox_ModelSelection_pop = QtWidgets.QComboBox(self.tab_DefineModel_pop)
#        self.comboBox_ModelSelection_pop.setEnabled(False)
#        self.comboBox_ModelSelection_pop.setMinimumSize(QtCore.QSize(200, 20))
#        self.comboBox_ModelSelection_pop.setMaximumSize(QtCore.QSize(16777215, 20))
#        self.comboBox_ModelSelection_pop.setEditable(True)
#        self.comboBox_ModelSelection_pop.setObjectName("comboBox_ModelSelection_pop")
#        self.horizontalLayout_2_pop.addWidget(self.comboBox_ModelSelection_pop)
#        self.verticalLayout_defineModel_pop.addLayout(self.horizontalLayout_2_pop)
#        self.horizontalLayout_colorNorm_pop = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_colorNorm_pop.setObjectName("horizontalLayout_colorNorm_pop")
#        self.horizontalLayout_8_pop = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_8_pop.setObjectName("horizontalLayout_8_pop")
#        self.label_colorModeIcon_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
#        self.label_colorModeIcon_pop.setObjectName("label_colorModeIcon_pop")
#        self.horizontalLayout_8_pop.addWidget(self.label_colorModeIcon_pop)
#        self.label_colorMode_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
#        self.label_colorMode_pop.setObjectName("label_colorMode_pop")
#        self.horizontalLayout_8_pop.addWidget(self.label_colorMode_pop)
#        self.comboBox_colorMode_pop = QtWidgets.QComboBox(self.tab_DefineModel_pop)
#        self.comboBox_colorMode_pop.setEnabled(False)
#        self.comboBox_colorMode_pop.setObjectName("comboBox_colorMode_pop")
#        self.horizontalLayout_8_pop.addWidget(self.comboBox_colorMode_pop)
#        self.horizontalLayout_colorNorm_pop.addLayout(self.horizontalLayout_8_pop)
#        self.horizontalLayout_5_pop = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_5_pop.setObjectName("horizontalLayout_5_pop")
#        self.label_NormalizationIcon_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
#        self.label_NormalizationIcon_pop.setLayoutDirection(QtCore.Qt.RightToLeft)
#        self.label_NormalizationIcon_pop.setObjectName("label_NormalizationIcon_pop")
#        self.horizontalLayout_5_pop.addWidget(self.label_NormalizationIcon_pop)
#        self.label_Normalization_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
#        self.label_Normalization_pop.setLayoutDirection(QtCore.Qt.RightToLeft)
#        self.label_Normalization_pop.setObjectName("label_Normalization_pop")
#        self.label_Normalization_pop.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
#        self.horizontalLayout_5_pop.addWidget(self.label_Normalization_pop)
#        self.comboBox_Normalization_pop = QtWidgets.QComboBox(self.tab_DefineModel_pop)
#        self.comboBox_Normalization_pop.setEnabled(False)
#        self.comboBox_Normalization_pop.setMinimumSize(QtCore.QSize(100, 0))
#        self.comboBox_Normalization_pop.setObjectName("comboBox_Normalization_pop")
#        self.horizontalLayout_5_pop.addWidget(self.comboBox_Normalization_pop)
#        self.horizontalLayout_colorNorm_pop.addLayout(self.horizontalLayout_5_pop)
#        self.verticalLayout_defineModel_pop.addLayout(self.horizontalLayout_colorNorm_pop)
#        self.horizontalLayout_6_pop = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_6_pop.setObjectName("horizontalLayout_6_pop")
#        self.horizontalLayout_4_pop = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_4_pop.setObjectName("horizontalLayout_4_pop")
#        self.label_CropIcon_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
#        self.label_CropIcon_pop.setObjectName("label_CropIcon_pop")
#        self.horizontalLayout_4_pop.addWidget(self.label_CropIcon_pop)
#        self.label_Crop_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
#        self.label_Crop_pop.setObjectName("label_Crop_pop")
#        self.horizontalLayout_4_pop.addWidget(self.label_Crop_pop)
#        self.spinBox_imagecrop_pop = QtWidgets.QSpinBox(self.tab_DefineModel_pop)
#        self.spinBox_imagecrop_pop.setEnabled(False)
#        self.spinBox_imagecrop_pop.setMaximum(9999)
#        self.spinBox_imagecrop_pop.setObjectName("spinBox_imagecrop_pop")
#        self.horizontalLayout_4_pop.addWidget(self.spinBox_imagecrop_pop)
#        self.horizontalLayout_6_pop.addLayout(self.horizontalLayout_4_pop)
#        self.horizontalLayout_3_pop_2 = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_3_pop_2.setObjectName("horizontalLayout_3_pop_2")
#        self.label_Crop_NrEpochs_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
#        self.label_Crop_NrEpochs_pop.setObjectName("label_Crop_NrEpochs_pop")
#        self.horizontalLayout_3_pop_2.addWidget(self.label_Crop_NrEpochs_pop)
#        self.spinBox_NrEpochs_pop = QtWidgets.QSpinBox(self.tab_DefineModel_pop)
#        self.spinBox_NrEpochs_pop.setObjectName("spinBox_NrEpochs_pop")
#        self.horizontalLayout_3_pop_2.addWidget(self.spinBox_NrEpochs_pop)
#        self.horizontalLayout_6_pop.addLayout(self.horizontalLayout_3_pop_2)
#        self.verticalLayout_defineModel_pop.addLayout(self.horizontalLayout_6_pop)
        
        
        
        
        self.horizontalLayout_2_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2_pop.setObjectName("horizontalLayout_2_pop")
        self.label_ModelGeomIcon_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
        self.label_ModelGeomIcon_pop.setText("")
        self.label_ModelGeomIcon_pop.setObjectName("label_ModelGeomIcon_pop")
        self.label_ModelGeomIcon_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2_pop.addWidget(self.label_ModelGeomIcon_pop)
        self.label_ModelGeom_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
        self.label_ModelGeom_pop.setObjectName("label_ModelGeom_pop")
        self.label_ModelGeom_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2_pop.addWidget(self.label_ModelGeom_pop)
        self.comboBox_ModelSelection_pop = QtWidgets.QComboBox(self.tab_DefineModel_pop)
        self.comboBox_ModelSelection_pop.setEnabled(False)
        self.comboBox_ModelSelection_pop.setMinimumSize(QtCore.QSize(200, 20))
        self.comboBox_ModelSelection_pop.setMaximumSize(QtCore.QSize(16777215, 20))
        self.comboBox_ModelSelection_pop.setEditable(True)
        self.comboBox_ModelSelection_pop.setObjectName("comboBox_ModelSelection_pop")
        self.horizontalLayout_2_pop.addWidget(self.comboBox_ModelSelection_pop)
        self.verticalLayout_defineModel_pop.addLayout(self.horizontalLayout_2_pop)
        self.horizontalLayout_colorNorm_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_colorNorm_pop.setObjectName("horizontalLayout_colorNorm_pop")
        self.horizontalLayout_8_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8_pop.setObjectName("horizontalLayout_8_pop")
        self.label_CropIcon_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
        self.label_CropIcon_pop.setText("")
        self.label_CropIcon_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_CropIcon_pop.setObjectName("label_CropIcon_pop")
        self.horizontalLayout_8_pop.addWidget(self.label_CropIcon_pop)
        self.label_Crop_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
        self.label_Crop_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Crop_pop.setObjectName("label_Crop_pop")
        self.horizontalLayout_8_pop.addWidget(self.label_Crop_pop)
        self.spinBox_imagecrop_pop = QtWidgets.QSpinBox(self.tab_DefineModel_pop)
        self.spinBox_imagecrop_pop.setEnabled(False)
        self.spinBox_imagecrop_pop.setMaximum(9999)
        self.spinBox_imagecrop_pop.setObjectName("spinBox_imagecrop_pop")
        self.horizontalLayout_8_pop.addWidget(self.spinBox_imagecrop_pop)
        self.horizontalLayout_colorNorm_pop.addLayout(self.horizontalLayout_8_pop)
        self.horizontalLayout_5_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5_pop.setObjectName("horizontalLayout_5_pop")
        self.label_NormalizationIcon_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
        self.label_NormalizationIcon_pop.setText("")
        self.label_NormalizationIcon_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_NormalizationIcon_pop.setObjectName("label_NormalizationIcon_pop")
        self.horizontalLayout_5_pop.addWidget(self.label_NormalizationIcon_pop)
        self.label_Normalization_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
        self.label_Normalization_pop.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_Normalization_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Normalization_pop.setObjectName("label_Normalization_pop")
        self.horizontalLayout_5_pop.addWidget(self.label_Normalization_pop)
        self.comboBox_Normalization_pop = QtWidgets.QComboBox(self.tab_DefineModel_pop)
        self.comboBox_Normalization_pop.setEnabled(False)
        self.comboBox_Normalization_pop.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_Normalization_pop.setObjectName("comboBox_Normalization_pop")
        self.horizontalLayout_5_pop.addWidget(self.comboBox_Normalization_pop)
        self.horizontalLayout_colorNorm_pop.addLayout(self.horizontalLayout_5_pop)
        self.verticalLayout_defineModel_pop.addLayout(self.horizontalLayout_colorNorm_pop)
        self.horizontalLayout_6_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6_pop.setObjectName("horizontalLayout_6_pop")
        self.horizontalLayout_4_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4_pop.setObjectName("horizontalLayout_4_pop")
        self.label_Crop_NrEpochsIcon_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
        self.label_Crop_NrEpochsIcon_pop.setText("")
        self.label_Crop_NrEpochsIcon_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Crop_NrEpochsIcon_pop.setObjectName("label_Crop_NrEpochsIcon_pop")
        self.horizontalLayout_4_pop.addWidget(self.label_Crop_NrEpochsIcon_pop)
        self.label_Crop_NrEpochs_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
        self.label_Crop_NrEpochs_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Crop_NrEpochs_pop.setObjectName("label_Crop_NrEpochs_pop")
        self.horizontalLayout_4_pop.addWidget(self.label_Crop_NrEpochs_pop)
        self.spinBox_NrEpochs_pop = QtWidgets.QSpinBox(self.tab_DefineModel_pop)
        self.spinBox_NrEpochs_pop.setMaximum(999999999)
        self.spinBox_NrEpochs_pop.setObjectName("spinBox_NrEpochs_pop")
        self.horizontalLayout_4_pop.addWidget(self.spinBox_NrEpochs_pop)
        self.horizontalLayout_6_pop.addLayout(self.horizontalLayout_4_pop)
        self.horizontalLayout_3_pop_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3_pop_2.setObjectName("horizontalLayout_3_pop_2")
        self.label_colorModeIcon_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
        self.label_colorModeIcon_pop.setText("")
        self.label_colorModeIcon_pop.setScaledContents(False)
        self.label_colorModeIcon_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_colorModeIcon_pop.setObjectName("label_colorModeIcon_pop")
        self.horizontalLayout_3_pop_2.addWidget(self.label_colorModeIcon_pop)
        self.label_colorMode_pop = QtWidgets.QLabel(self.tab_DefineModel_pop)
        self.label_colorMode_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_colorMode_pop.setObjectName("label_colorMode_pop")
        self.horizontalLayout_3_pop_2.addWidget(self.label_colorMode_pop)
        self.comboBox_colorMode_pop = QtWidgets.QComboBox(self.tab_DefineModel_pop)
        self.comboBox_colorMode_pop.setEnabled(False)
        self.comboBox_colorMode_pop.setObjectName("comboBox_colorMode_pop")
        self.horizontalLayout_3_pop_2.addWidget(self.comboBox_colorMode_pop)
        self.horizontalLayout_6_pop.addLayout(self.horizontalLayout_3_pop_2)
        self.verticalLayout_defineModel_pop.addLayout(self.horizontalLayout_6_pop)
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.horizontalLayout_modelname_2_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_modelname_2_pop.setObjectName("horizontalLayout_modelname_2_pop")
        self.pushButton_modelname_pop = QtWidgets.QPushButton(self.tab_DefineModel_pop)
        self.pushButton_modelname_pop.setEnabled(False)
        self.pushButton_modelname_pop.setObjectName("pushButton_modelname_pop")
        self.horizontalLayout_modelname_2_pop.addWidget(self.pushButton_modelname_pop)
        self.lineEdit_modelname_pop = QtWidgets.QLineEdit(self.tab_DefineModel_pop)
        self.lineEdit_modelname_pop.setEnabled(False)
        self.lineEdit_modelname_pop.setMinimumSize(QtCore.QSize(0, 22))
        self.lineEdit_modelname_pop.setMaximumSize(QtCore.QSize(16777215, 22))
        self.lineEdit_modelname_pop.setObjectName("lineEdit_modelname_pop")
        self.horizontalLayout_modelname_2_pop.addWidget(self.lineEdit_modelname_pop)
        self.verticalLayout_defineModel_pop.addLayout(self.horizontalLayout_modelname_2_pop)
        self.line2_pop = QtWidgets.QFrame(self.tab_DefineModel_pop)
        self.line2_pop.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2_pop.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2_pop.setObjectName("line2_pop")
        self.verticalLayout_defineModel_pop.addWidget(self.line2_pop)
        self.horizontalLayout_9_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9_pop.setObjectName("horizontalLayout_9_pop")
        self.pushButton_showModelSumm_pop = QtWidgets.QPushButton(self.tab_DefineModel_pop)
        self.pushButton_showModelSumm_pop.setObjectName("pushButton_showModelSumm_pop")
        self.horizontalLayout_9_pop.addWidget(self.pushButton_showModelSumm_pop)
        self.pushButton_saveModelSumm_pop = QtWidgets.QPushButton(self.tab_DefineModel_pop)
        self.pushButton_saveModelSumm_pop.setObjectName("pushButton_saveModelSumm_pop")
        self.horizontalLayout_9_pop.addWidget(self.pushButton_saveModelSumm_pop)
        self.verticalLayout_defineModel_pop.addLayout(self.horizontalLayout_9_pop)
        self.line_pop = QtWidgets.QFrame(self.tab_DefineModel_pop)
        self.line_pop.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_pop.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_pop.setObjectName("line_pop")
        self.verticalLayout_defineModel_pop.addWidget(self.line_pop)
        self.horizontalLayout_7_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7_pop.setObjectName("horizontalLayout_7_pop")
        self.checkBox_ApplyNextEpoch = QtWidgets.QCheckBox(self.tab_DefineModel_pop)
        self.checkBox_ApplyNextEpoch.setAutoFillBackground(False)
        self.checkBox_ApplyNextEpoch.setTristate(False)
        self.checkBox_ApplyNextEpoch.setObjectName("checkBox_ApplyNextEpoch")
        self.horizontalLayout_7_pop.addWidget(self.checkBox_ApplyNextEpoch)
        self.checkBox_saveEpoch_pop = QtWidgets.QCheckBox(self.tab_DefineModel_pop)
        self.checkBox_saveEpoch_pop.setObjectName("checkBox_saveEpoch_pop")
        self.horizontalLayout_7_pop.addWidget(self.checkBox_saveEpoch_pop)
        self.pushButton_Pause_pop = QtWidgets.QPushButton(self.tab_DefineModel_pop)
        self.pushButton_Pause_pop.setObjectName("pushButton_Pause_pop")
        self.horizontalLayout_7_pop.addWidget(self.pushButton_Pause_pop)
        self.pushButton_Stop_pop = QtWidgets.QPushButton(self.tab_DefineModel_pop)
        self.pushButton_Stop_pop.setObjectName("pushButton_Stop_pop")
        self.horizontalLayout_7_pop.addWidget(self.pushButton_Stop_pop)
        self.verticalLayout_defineModel_pop.addLayout(self.horizontalLayout_7_pop)
        self.gridLayout.addLayout(self.verticalLayout_defineModel_pop, 0, 0, 1, 1)
        self.tabWidget_DefineModel_pop.addTab(self.tab_DefineModel_pop, "")
        self.tab_KerasImgAug_pop = QtWidgets.QWidget()
        self.tab_KerasImgAug_pop.setObjectName("tab_KerasImgAug_pop")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_KerasImgAug_pop)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_9_pop = QtWidgets.QVBoxLayout()
        self.verticalLayout_9_pop.setObjectName("verticalLayout_9_pop")
        self.horizontalLayout_10_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10_pop.setObjectName("horizontalLayout_10_pop")
        self.label_RefreshAfterEpochs_pop = QtWidgets.QLabel(self.tab_KerasImgAug_pop)
        self.label_RefreshAfterEpochs_pop.setObjectName("label_RefreshAfterEpochs_pop")
        self.horizontalLayout_10_pop.addWidget(self.label_RefreshAfterEpochs_pop)
        self.spinBox_RefreshAfterEpochs_pop = QtWidgets.QSpinBox(self.tab_KerasImgAug_pop)
        self.spinBox_RefreshAfterEpochs_pop.setObjectName("spinBox_RefreshAfterEpochs_pop")
        self.horizontalLayout_10_pop.addWidget(self.spinBox_RefreshAfterEpochs_pop)
        self.verticalLayout_9_pop.addLayout(self.horizontalLayout_10_pop)
        self.verticalLayout_10_pop = QtWidgets.QVBoxLayout()
        self.verticalLayout_10_pop.setObjectName("verticalLayout_10_pop")
        self.horizontalLayout_11_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11_pop.setObjectName("horizontalLayout_11_pop")
        self.checkBox_HorizFlip_pop = QtWidgets.QCheckBox(self.tab_KerasImgAug_pop)
        self.checkBox_HorizFlip_pop.setObjectName("checkBox_HorizFlip_pop")
        self.horizontalLayout_11_pop.addWidget(self.checkBox_HorizFlip_pop)
        self.checkBox_VertFlip_pop = QtWidgets.QCheckBox(self.tab_KerasImgAug_pop)
        self.checkBox_VertFlip_pop.setObjectName("checkBox_VertFlip_pop")
        self.horizontalLayout_11_pop.addWidget(self.checkBox_VertFlip_pop)
        self.verticalLayout_10_pop.addLayout(self.horizontalLayout_11_pop)
        self.splitter_2_pop = QtWidgets.QSplitter(self.tab_KerasImgAug_pop)
        self.splitter_2_pop.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2_pop.setObjectName("splitter_2_pop")
        self.layoutWidget_4 = QtWidgets.QWidget(self.splitter_2_pop)
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_11_pop = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_11_pop.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11_pop.setObjectName("verticalLayout_11_pop")
        self.label_Rotation_pop = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.label_Rotation_pop.setObjectName("label_Rotation_pop")
        self.verticalLayout_11_pop.addWidget(self.label_Rotation_pop)
        self.label_width_shift_pop = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.label_width_shift_pop.setObjectName("label_width_shift_pop")
        self.verticalLayout_11_pop.addWidget(self.label_width_shift_pop)
        self.label_height_shift_pop = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.label_height_shift_pop.setObjectName("label_height_shift_pop")
        self.verticalLayout_11_pop.addWidget(self.label_height_shift_pop)
        self.label_zoom_pop = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.label_zoom_pop.setObjectName("label_zoom_pop")
        self.verticalLayout_11_pop.addWidget(self.label_zoom_pop)
        self.label_shear_pop = QtWidgets.QCheckBox(self.layoutWidget_4)
        self.label_shear_pop.setObjectName("label_shear_pop")
        self.verticalLayout_11_pop.addWidget(self.label_shear_pop)
        self.layoutWidget_5 = QtWidgets.QWidget(self.splitter_2_pop)
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_12_pop = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_12_pop.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12_pop.setObjectName("verticalLayout_12_pop")
        
        self.onlyFloat = QtGui.QDoubleValidator()        
        
        self.lineEdit_Rotation_pop = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_Rotation_pop.setObjectName("lineEdit_Rotation_pop")
        self.lineEdit_Rotation_pop.setValidator(self.onlyFloat)
        self.verticalLayout_12_pop.addWidget(self.lineEdit_Rotation_pop)
        self.lineEdit_Rotation_pop_2 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_Rotation_pop_2.setObjectName("lineEdit_Rotation_pop_2")
        self.lineEdit_Rotation_pop_2.setValidator(self.onlyFloat)

        self.verticalLayout_12_pop.addWidget(self.lineEdit_Rotation_pop_2)
        self.lineEdit_Rotation_pop_3 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_Rotation_pop_3.setObjectName("lineEdit_Rotation_pop_3")
        self.lineEdit_Rotation_pop_3.setValidator(self.onlyFloat)

        self.verticalLayout_12_pop.addWidget(self.lineEdit_Rotation_pop_3)
        self.lineEdit_Rotation_pop_4 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_Rotation_pop_4.setObjectName("lineEdit_Rotation_pop_4")
        self.lineEdit_Rotation_pop_4.setValidator(self.onlyFloat)

        self.verticalLayout_12_pop.addWidget(self.lineEdit_Rotation_pop_4)
        self.lineEdit_Rotation_pop_5 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_Rotation_pop_5.setObjectName("lineEdit_Rotation_pop_5")
        self.lineEdit_Rotation_pop_5.setValidator(self.onlyFloat)

        self.verticalLayout_12_pop.addWidget(self.lineEdit_Rotation_pop_5)
        self.verticalLayout_10_pop.addWidget(self.splitter_2_pop)
        self.verticalLayout_9_pop.addLayout(self.verticalLayout_10_pop)
        self.gridLayout_8.addLayout(self.verticalLayout_9_pop, 0, 0, 1, 1)
        self.tabWidget_DefineModel_pop.addTab(self.tab_KerasImgAug_pop, "")



        self.tab_BrightnessAug_pop = QtWidgets.QWidget()
        self.tab_BrightnessAug_pop.setObjectName("tab_BrightnessAug_pop")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_BrightnessAug_pop)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollArea_BrightnessAug_pop = QtWidgets.QScrollArea(self.tab_BrightnessAug_pop)
        self.scrollArea_BrightnessAug_pop.setWidgetResizable(True)
        self.scrollArea_BrightnessAug_pop.setObjectName("scrollArea_BrightnessAug_pop")
        self.scrollAreaWidgetContents_pop_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_pop_2.setGeometry(QtCore.QRect(0, 0, 423, 269))
        self.scrollAreaWidgetContents_pop_2.setObjectName("scrollAreaWidgetContents_pop_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_pop_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_RefreshAfterNrEpochs_pop = QtWidgets.QLabel(self.scrollAreaWidgetContents_pop_2)
        self.label_RefreshAfterNrEpochs_pop.setObjectName("label_RefreshAfterNrEpochs_pop")
        self.gridLayout_9.addWidget(self.label_RefreshAfterNrEpochs_pop, 0, 0, 1, 1)
        self.spinBox_RefreshAfterNrEpochs_pop = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_pop_2)
        self.spinBox_RefreshAfterNrEpochs_pop.setObjectName("spinBox_RefreshAfterNrEpochs_pop")
        self.gridLayout_9.addWidget(self.spinBox_RefreshAfterNrEpochs_pop, 0, 1, 1, 1)
        self.groupBox_BrightnessAugmentation_pop = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_pop_2)
        self.groupBox_BrightnessAugmentation_pop.setObjectName("groupBox_BrightnessAugmentation_pop")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_BrightnessAugmentation_pop)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_Plus_pop = QtWidgets.QCheckBox(self.groupBox_BrightnessAugmentation_pop)
        self.label_Plus_pop.setObjectName("label_Plus_pop")
        self.gridLayout_5.addWidget(self.label_Plus_pop, 0, 0, 1, 1)
        self.spinBox_PlusLower_pop = QtWidgets.QSpinBox(self.groupBox_BrightnessAugmentation_pop)
        self.spinBox_PlusLower_pop.setObjectName("spinBox_PlusLower_pop")
        self.gridLayout_5.addWidget(self.spinBox_PlusLower_pop, 0, 1, 1, 1)
        self.spinBox_PlusUpper_pop = QtWidgets.QSpinBox(self.groupBox_BrightnessAugmentation_pop)
        self.spinBox_PlusUpper_pop.setObjectName("spinBox_PlusUpper_pop")
        self.gridLayout_5.addWidget(self.spinBox_PlusUpper_pop, 0, 2, 1, 1)
        self.label_Mult_pop = QtWidgets.QCheckBox(self.groupBox_BrightnessAugmentation_pop)
        self.label_Mult_pop.setObjectName("label_Mult_pop")
        self.gridLayout_5.addWidget(self.label_Mult_pop, 1, 0, 1, 1)
        self.doubleSpinBox_MultLower_pop = QtWidgets.QDoubleSpinBox(self.groupBox_BrightnessAugmentation_pop)
        self.doubleSpinBox_MultLower_pop.setObjectName("doubleSpinBox_MultLower_pop")
        self.gridLayout_5.addWidget(self.doubleSpinBox_MultLower_pop, 1, 1, 1, 1)
        self.doubleSpinBox_MultUpper_pop = QtWidgets.QDoubleSpinBox(self.groupBox_BrightnessAugmentation_pop)
        self.doubleSpinBox_MultUpper_pop.setObjectName("doubleSpinBox_MultUpper_pop")
        self.gridLayout_5.addWidget(self.doubleSpinBox_MultUpper_pop, 1, 2, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_BrightnessAugmentation_pop, 1, 0, 1, 1)
        self.groupBox_GaussianNoise_pop = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_pop_2)
        self.groupBox_GaussianNoise_pop.setObjectName("groupBox_GaussianNoise_pop")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_GaussianNoise_pop)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_GaussianNoiseMean_pop = QtWidgets.QCheckBox(self.groupBox_GaussianNoise_pop)
        self.label_GaussianNoiseMean_pop.setObjectName("label_GaussianNoiseMean_pop")
        self.gridLayout_6.addWidget(self.label_GaussianNoiseMean_pop, 0, 0, 1, 1)
        self.doubleSpinBox_GaussianNoiseMean_pop = QtWidgets.QDoubleSpinBox(self.groupBox_GaussianNoise_pop)
        self.doubleSpinBox_GaussianNoiseMean_pop.setObjectName("doubleSpinBox_GaussianNoiseMean_pop")
        self.gridLayout_6.addWidget(self.doubleSpinBox_GaussianNoiseMean_pop, 0, 1, 1, 1)
        self.label_GaussianNoiseScale_pop = QtWidgets.QCheckBox(self.groupBox_GaussianNoise_pop)
        self.label_GaussianNoiseScale_pop.setObjectName("label_GaussianNoiseScale_pop")
        self.gridLayout_6.addWidget(self.label_GaussianNoiseScale_pop, 1, 0, 1, 1)
        self.doubleSpinBox_GaussianNoiseScale_pop = QtWidgets.QDoubleSpinBox(self.groupBox_GaussianNoise_pop)
        self.doubleSpinBox_GaussianNoiseScale_pop.setObjectName("doubleSpinBox_GaussianNoiseScale_pop")
        self.gridLayout_6.addWidget(self.doubleSpinBox_GaussianNoiseScale_pop, 1, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_GaussianNoise_pop, 1, 1, 1, 1)
        self.groupBox_colorAugmentation_pop = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_pop_2)
        self.groupBox_colorAugmentation_pop.setCheckable(False)
        self.groupBox_colorAugmentation_pop.setObjectName("groupBox_colorAugmentation_pop")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_colorAugmentation_pop)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.doubleSpinBox_contrastLower_pop = QtWidgets.QDoubleSpinBox(self.groupBox_colorAugmentation_pop)
        self.doubleSpinBox_contrastLower_pop.setMaximum(100.0)
        self.doubleSpinBox_contrastLower_pop.setSingleStep(0.1)
        #self.doubleSpinBox_contrastLower_pop.setProperty("value", 0.7)
        self.doubleSpinBox_contrastLower_pop.setObjectName("doubleSpinBox_contrastLower_pop")
        self.gridLayout_15.addWidget(self.doubleSpinBox_contrastLower_pop, 0, 1, 1, 1)
        self.doubleSpinBox_saturationHigher_pop = QtWidgets.QDoubleSpinBox(self.groupBox_colorAugmentation_pop)
        self.doubleSpinBox_saturationHigher_pop.setMaximum(100.0)
        self.doubleSpinBox_saturationHigher_pop.setSingleStep(0.1)
        #self.doubleSpinBox_saturationHigher_pop.setProperty("value", 1.3)
        self.doubleSpinBox_saturationHigher_pop.setObjectName("doubleSpinBox_saturationHigher_pop")
        self.gridLayout_15.addWidget(self.doubleSpinBox_saturationHigher_pop, 1, 2, 1, 1)
        self.doubleSpinBox_contrastHigher_pop = QtWidgets.QDoubleSpinBox(self.groupBox_colorAugmentation_pop)
        self.doubleSpinBox_contrastHigher_pop.setMaximum(100.0)
        self.doubleSpinBox_contrastHigher_pop.setSingleStep(0.1)
        #self.doubleSpinBox_contrastHigher_pop.setProperty("value", 1.3)
        self.doubleSpinBox_contrastHigher_pop.setObjectName("doubleSpinBox_contrastHigher_pop")
        self.gridLayout_15.addWidget(self.doubleSpinBox_contrastHigher_pop, 0, 2, 1, 1)
        self.checkBox_contrast_pop = QtWidgets.QCheckBox(self.groupBox_colorAugmentation_pop)
        self.checkBox_contrast_pop.setCheckable(True)
        self.checkBox_contrast_pop.setChecked(True)
        self.checkBox_contrast_pop.setObjectName("checkBox_contrast_pop")
        self.gridLayout_15.addWidget(self.checkBox_contrast_pop, 0, 0, 1, 1)
        self.doubleSpinBox_saturationLower_pop = QtWidgets.QDoubleSpinBox(self.groupBox_colorAugmentation_pop)
        self.doubleSpinBox_saturationLower_pop.setMaximum(100.0)
        self.doubleSpinBox_saturationLower_pop.setSingleStep(0.1)
        #self.doubleSpinBox_saturationLower_pop.setProperty("value", 0.7)
        self.doubleSpinBox_saturationLower_pop.setObjectName("doubleSpinBox_saturationLower_pop")
        self.gridLayout_15.addWidget(self.doubleSpinBox_saturationLower_pop, 1, 1, 1, 1)
        self.doubleSpinBox_hueDelta_pop = QtWidgets.QDoubleSpinBox(self.groupBox_colorAugmentation_pop)
        self.doubleSpinBox_hueDelta_pop.setMaximum(0.5)
        self.doubleSpinBox_hueDelta_pop.setSingleStep(0.01)
        #self.doubleSpinBox_hueDelta_pop.setProperty("value", 0.08)
        self.doubleSpinBox_hueDelta_pop.setObjectName("doubleSpinBox_hueDelta_pop")
        self.gridLayout_15.addWidget(self.doubleSpinBox_hueDelta_pop, 2, 1, 1, 1)
        self.checkBox_saturation_pop = QtWidgets.QCheckBox(self.groupBox_colorAugmentation_pop)
        self.checkBox_saturation_pop.setObjectName("checkBox_saturation_pop")
        self.gridLayout_15.addWidget(self.checkBox_saturation_pop, 1, 0, 1, 1)
        self.checkBox_hue_pop = QtWidgets.QCheckBox(self.groupBox_colorAugmentation_pop)
        self.checkBox_hue_pop.setObjectName("checkBox_hue_pop")
        self.gridLayout_15.addWidget(self.checkBox_hue_pop, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_colorAugmentation_pop, 2, 0, 1, 1)
        
        
        self.groupBox_blurringAug_pop = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_pop_2)
        self.groupBox_blurringAug_pop.setObjectName("groupBox_blurringAug_pop")
        self.gridLayout_45 = QtWidgets.QGridLayout(self.groupBox_blurringAug_pop)
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.gridLayout_blur_pop = QtWidgets.QGridLayout()
        self.gridLayout_blur_pop.setObjectName("gridLayout_blur_pop")
        self.label_motionBlurKernel_pop = QtWidgets.QLabel(self.groupBox_blurringAug_pop)
        self.label_motionBlurKernel_pop.setMaximumSize(QtCore.QSize(31, 16777215))
        self.label_motionBlurKernel_pop.setObjectName("label_motionBlurKernel_pop")
        self.gridLayout_blur_pop.addWidget(self.label_motionBlurKernel_pop, 2, 1, 1, 1)
        self.lineEdit_motionBlurAngle_pop = QtWidgets.QLineEdit(self.groupBox_blurringAug_pop)
        self.lineEdit_motionBlurAngle_pop.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_motionBlurAngle_pop.setInputMask("")
        self.lineEdit_motionBlurAngle_pop.setObjectName("lineEdit_motionBlurAngle_pop")
        validator = QtGui.QRegExpValidator(QtCore.QRegExp("^[-+]?[0-9]\\d{0,3},(\\d{3})$"))
        self.lineEdit_motionBlurAngle_pop.setValidator(validator)
        self.gridLayout_blur_pop.addWidget(self.lineEdit_motionBlurAngle_pop, 2, 4, 1, 1)
        self.label_avgBlurMin_pop = QtWidgets.QLabel(self.groupBox_blurringAug_pop)
        self.label_avgBlurMin_pop.setMaximumSize(QtCore.QSize(31, 16777215))
        self.label_avgBlurMin_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_avgBlurMin_pop.setObjectName("label_avgBlurMin_pop")
        self.gridLayout_blur_pop.addWidget(self.label_avgBlurMin_pop, 0, 1, 1, 1)
        self.spinBox_gaussBlurMax_pop = QtWidgets.QSpinBox(self.groupBox_blurringAug_pop)
        self.spinBox_gaussBlurMax_pop.setObjectName("spinBox_gaussBlurMax_pop")
        self.gridLayout_blur_pop.addWidget(self.spinBox_gaussBlurMax_pop, 1, 4, 1, 1)
        self.checkBox_motionBlur_pop = QtWidgets.QCheckBox(self.groupBox_blurringAug_pop)
        self.checkBox_motionBlur_pop.setMaximumSize(QtCore.QSize(100, 16777215))
        self.checkBox_motionBlur_pop.setObjectName("checkBox_motionBlur_pop")
        self.gridLayout_blur_pop.addWidget(self.checkBox_motionBlur_pop, 2, 0, 1, 1)
        self.spinBox_avgBlurMin_pop = QtWidgets.QSpinBox(self.groupBox_blurringAug_pop)
        self.spinBox_avgBlurMin_pop.setObjectName("spinBox_avgBlurMin_pop")
        self.gridLayout_blur_pop.addWidget(self.spinBox_avgBlurMin_pop, 0, 2, 1, 1)
        self.spinBox_gaussBlurMin_pop = QtWidgets.QSpinBox(self.groupBox_blurringAug_pop)
        self.spinBox_gaussBlurMin_pop.setObjectName("spinBox_gaussBlurMin_pop")
        self.gridLayout_blur_pop.addWidget(self.spinBox_gaussBlurMin_pop, 1, 2, 1, 1)
        self.label_motionBlurAngle_pop = QtWidgets.QLabel(self.groupBox_blurringAug_pop)
        self.label_motionBlurAngle_pop.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_motionBlurAngle_pop.setObjectName("label_motionBlurAngle_pop")
        self.gridLayout_blur_pop.addWidget(self.label_motionBlurAngle_pop, 2, 3, 1, 1)
        self.label_gaussBlurMin_pop = QtWidgets.QLabel(self.groupBox_blurringAug_pop)
        self.label_gaussBlurMin_pop.setMaximumSize(QtCore.QSize(31, 16777215))
        self.label_gaussBlurMin_pop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_gaussBlurMin_pop.setObjectName("label_gaussBlurMin_pop")
        self.gridLayout_blur_pop.addWidget(self.label_gaussBlurMin_pop, 1, 1, 1, 1)
        self.checkBox_gaussBlur_pop = QtWidgets.QCheckBox(self.groupBox_blurringAug_pop)
        self.checkBox_gaussBlur_pop.setObjectName("checkBox_gaussBlur_pop")
        self.gridLayout_blur_pop.addWidget(self.checkBox_gaussBlur_pop, 1, 0, 1, 1)
        self.spinBox_avgBlurMax_pop = QtWidgets.QSpinBox(self.groupBox_blurringAug_pop)
        self.spinBox_avgBlurMax_pop.setObjectName("spinBox_avgBlurMax_pop")
        self.gridLayout_blur_pop.addWidget(self.spinBox_avgBlurMax_pop, 0, 4, 1, 1)
        self.label_gaussBlurMax_pop = QtWidgets.QLabel(self.groupBox_blurringAug_pop)
        self.label_gaussBlurMax_pop.setMaximumSize(QtCore.QSize(31, 16777215))
        self.label_gaussBlurMax_pop.setObjectName("label_gaussBlurMax_pop")
        self.gridLayout_blur_pop.addWidget(self.label_gaussBlurMax_pop, 1, 3, 1, 1)
        self.checkBox_avgBlur_pop = QtWidgets.QCheckBox(self.groupBox_blurringAug_pop)
        self.checkBox_avgBlur_pop.setObjectName("checkBox_avgBlur_pop")
        self.gridLayout_blur_pop.addWidget(self.checkBox_avgBlur_pop, 0, 0, 1, 1)
        self.label_avgBlurMax_pop = QtWidgets.QLabel(self.groupBox_blurringAug_pop)
        self.label_avgBlurMax_pop.setMaximumSize(QtCore.QSize(31, 16777215))
        self.label_avgBlurMax_pop.setObjectName("label_avgBlurMax_pop")
        self.gridLayout_blur_pop.addWidget(self.label_avgBlurMax_pop, 0, 3, 1, 1)
        self.lineEdit_motionBlurKernel_pop = QtWidgets.QLineEdit(self.groupBox_blurringAug_pop)
        self.lineEdit_motionBlurKernel_pop.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_motionBlurKernel_pop.setInputMask("")
        self.lineEdit_motionBlurKernel_pop.setMaxLength(32767)
        self.lineEdit_motionBlurKernel_pop.setClearButtonEnabled(False)
        validator = QtGui.QRegExpValidator(QtCore.QRegExp("^\\d{1,3},(\\d{3})$"))
        self.lineEdit_motionBlurKernel_pop.setValidator(validator)
        self.lineEdit_motionBlurKernel_pop.setObjectName("lineEdit_motionBlurKernel_pop")
        self.gridLayout_blur_pop.addWidget(self.lineEdit_motionBlurKernel_pop, 2, 2, 1, 1)
        self.gridLayout_45.addLayout(self.gridLayout_blur_pop, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_blurringAug_pop, 2, 1, 1, 1)
        
        
        self.scrollArea_BrightnessAug_pop.setWidget(self.scrollAreaWidgetContents_pop_2)
        self.gridLayout_7.addWidget(self.scrollArea_BrightnessAug_pop, 0, 0, 1, 1)
        self.tabWidget_DefineModel_pop.addTab(self.tab_BrightnessAug_pop, "")
        self.tabWidget_DefineModel_pop.addTab(self.tab_BrightnessAug_pop, "")
        
        self.tab_ExampleImgs_pop = QtWidgets.QWidget()
        self.tab_ExampleImgs_pop.setObjectName("tab_ExampleImgs_pop")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tab_ExampleImgs_pop)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.splitter_5_pop = QtWidgets.QSplitter(self.tab_ExampleImgs_pop)
        self.splitter_5_pop.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5_pop.setObjectName("splitter_5_pop")
        self.layoutWidget_6 = QtWidgets.QWidget(self.splitter_5_pop)
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_ExampleImgs_pop = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_ExampleImgs_pop.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_ExampleImgs_pop.setObjectName("horizontalLayout_ExampleImgs_pop")
        self.comboBox_ShowTrainOrValid_pop = QtWidgets.QComboBox(self.layoutWidget_6)
        self.comboBox_ShowTrainOrValid_pop.setObjectName("comboBox_ShowTrainOrValid_pop")
        self.horizontalLayout_ExampleImgs_pop.addWidget(self.comboBox_ShowTrainOrValid_pop)
        self.comboBox_ShowWOrWoAug_pop = QtWidgets.QComboBox(self.layoutWidget_6)
        self.comboBox_ShowWOrWoAug_pop.setObjectName("comboBox_ShowWOrWoAug_pop")
        self.horizontalLayout_ExampleImgs_pop.addWidget(self.comboBox_ShowWOrWoAug_pop)
        self.label_ShowIndex_pop = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_ShowIndex_pop.setObjectName("label_ShowIndex_pop")
        self.label_ShowIndex_pop.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.horizontalLayout_ExampleImgs_pop.addWidget(self.label_ShowIndex_pop)
        self.spinBox_ShowIndex_pop = QtWidgets.QSpinBox(self.layoutWidget_6)
        self.spinBox_ShowIndex_pop.setObjectName("spinBox_ShowIndex_pop")
        self.horizontalLayout_ExampleImgs_pop.addWidget(self.spinBox_ShowIndex_pop)
        self.pushButton_ShowExamleImgs_pop = QtWidgets.QPushButton(self.layoutWidget_6)
        self.pushButton_ShowExamleImgs_pop.setObjectName("pushButton_ShowExamleImgs_pop")
        self.horizontalLayout_ExampleImgs_pop.addWidget(self.pushButton_ShowExamleImgs_pop)
        self.widget_ViewImages_pop = QtWidgets.QWidget(self.splitter_5_pop)
        self.widget_ViewImages_pop.setObjectName("widget_ViewImages_pop")
        self.gridLayout_18.addWidget(self.splitter_5_pop, 0, 0, 1, 1)
        self.tabWidget_DefineModel_pop.addTab(self.tab_ExampleImgs_pop, "")
        self.tab_expertMode_pop = QtWidgets.QWidget()
        #self.tab_expertMode_pop.setEnabled(True)
        self.tab_expertMode_pop.setObjectName("tab_expertMode_pop")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_expertMode_pop)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_expertMode_pop = QtWidgets.QGroupBox(self.tab_expertMode_pop)
        self.groupBox_expertMode_pop.setEnabled(True)
        self.groupBox_expertMode_pop.setCheckable(True)
        self.groupBox_expertMode_pop.setChecked(False)
        self.groupBox_expertMode_pop.setObjectName("groupBox_expertMode_pop")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_expertMode_pop)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_expertMode_pop = QtWidgets.QScrollArea(self.groupBox_expertMode_pop)
        #self.scrollArea_expertMode_pop.setEnabled(True)
        self.scrollArea_expertMode_pop.setWidgetResizable(True)
        self.scrollArea_expertMode_pop.setObjectName("scrollArea_expertMode_pop")
        self.scrollAreaWidgetContents_pop = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_pop.setGeometry(QtCore.QRect(0, 0, 399, 220))
        self.scrollAreaWidgetContents_pop.setObjectName("scrollAreaWidgetContents_pop")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_pop)
        
        
        
        
        
        self.groupBox_modelKerasFit_pop = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_pop)
        self.groupBox_modelKerasFit_pop.setObjectName("groupBox_modelKerasFit_pop")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_modelKerasFit_pop)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.verticalLayout_22_pop = QtWidgets.QVBoxLayout()
        self.verticalLayout_22_pop.setObjectName("verticalLayout_22_pop")
        self.horizontalLayout_40_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40_pop.setObjectName("horizontalLayout_40_pop")
        
        self.label_batchSize_pop = QtWidgets.QLabel(self.groupBox_modelKerasFit_pop)
        self.label_batchSize_pop.setObjectName("label_batchSize_pop")
        self.horizontalLayout_40_pop.addWidget(self.label_batchSize_pop)
        self.spinBox_batchSize_pop = QtWidgets.QSpinBox(self.groupBox_modelKerasFit_pop)
#        self.spinBox_batchSize_pop.setMinimum(1)
#        self.spinBox_batchSize_pop.setMaximum(999999999)
#        self.spinBox_batchSize_pop.setProperty("value", 128)
        self.spinBox_batchSize_pop.setObjectName("spinBox_batchSize_pop")
        self.horizontalLayout_40_pop.addWidget(self.spinBox_batchSize_pop)
        self.verticalLayout_22_pop.addLayout(self.horizontalLayout_40_pop)
        self.horizontalLayout_41_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41_pop.setObjectName("horizontalLayout_41_pop")
        self.label_epochs_pop = QtWidgets.QLabel(self.groupBox_modelKerasFit_pop)
        self.label_epochs_pop.setObjectName("label_epochs_pop")
        self.horizontalLayout_41_pop.addWidget(self.label_epochs_pop)
        self.spinBox_epochs_pop = QtWidgets.QSpinBox(self.groupBox_modelKerasFit_pop)
#        self.spinBox_epochs_pop.setMinimum(1)
#        self.spinBox_epochs_pop.setMaximum(999999999)
        self.spinBox_epochs_pop.setObjectName("spinBox_epochs_pop")
        self.horizontalLayout_41_pop.addWidget(self.spinBox_epochs_pop)
        self.verticalLayout_22_pop.addLayout(self.horizontalLayout_41_pop)
        self.gridLayout_11.addLayout(self.verticalLayout_22_pop, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_modelKerasFit_pop, 0, 0, 1, 1)
        
        
        self.groupBox_expt_imgProc_pop = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_pop)
        self.groupBox_expt_imgProc_pop.setObjectName("groupBox_expt_imgProc_pop")
        self.gridLayout_48 = QtWidgets.QGridLayout(self.groupBox_expt_imgProc_pop)
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.checkBox_expt_paddingMode_pop = QtWidgets.QCheckBox(self.groupBox_expt_imgProc_pop)
        self.checkBox_expt_paddingMode_pop.setObjectName("checkBox_expt_paddingMode_pop")
        self.gridLayout_48.addWidget(self.checkBox_expt_paddingMode_pop, 0, 0, 1, 1)
        self.comboBox_expt_paddingMode_pop = QtWidgets.QComboBox(self.groupBox_expt_imgProc_pop)
        self.comboBox_expt_paddingMode_pop.setEnabled(False)
        self.comboBox_expt_paddingMode_pop.setObjectName("comboBox_expt_paddingMode_pop")
        self.comboBox_expt_paddingMode_pop.addItem("")
        self.comboBox_expt_paddingMode_pop.addItem("")
        self.comboBox_expt_paddingMode_pop.addItem("")
        self.comboBox_expt_paddingMode_pop.addItem("")
        self.comboBox_expt_paddingMode_pop.addItem("")
        self.comboBox_expt_paddingMode_pop.addItem("")
        self.comboBox_expt_paddingMode_pop.addItem("")
        self.comboBox_expt_paddingMode_pop.addItem("")
        self.comboBox_expt_paddingMode_pop.addItem("")
        self.comboBox_expt_paddingMode_pop.addItem("")
        self.gridLayout_48.addWidget(self.comboBox_expt_paddingMode_pop, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_expt_imgProc_pop, 2, 0, 1, 1)
        
              
        
        self.groupBox_regularization_pop = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_pop)
        self.groupBox_regularization_pop.setObjectName("groupBox_regularization_pop")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_regularization_pop)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalLayout_loss_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_loss_pop.setObjectName("horizontalLayout_loss_pop")
        self.checkBox_expt_loss_pop = QtWidgets.QCheckBox(self.groupBox_regularization_pop)
        self.checkBox_expt_loss_pop.setObjectName("checkBox_expt_loss_pop")
        self.horizontalLayout_loss_pop.addWidget(self.checkBox_expt_loss_pop)
        self.comboBox_expt_loss_pop = QtWidgets.QComboBox(self.groupBox_regularization_pop)
        self.comboBox_expt_loss_pop.setEnabled(False)
        self.comboBox_expt_loss_pop.setObjectName("comboBox_expt_loss_pop")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.comboBox_expt_loss_pop.addItem("")
        self.horizontalLayout_loss_pop.addWidget(self.comboBox_expt_loss_pop)
        self.gridLayout_12.addLayout(self.horizontalLayout_loss_pop, 0, 0, 1, 1)
        self.horizontalLayout_lropti = QtWidgets.QHBoxLayout()
        self.horizontalLayout_lropti.setObjectName("horizontalLayout_lropti")
        
        
        self.checkBox_learningRate_pop = QtWidgets.QCheckBox(self.groupBox_regularization_pop)
        self.checkBox_learningRate_pop.setObjectName("checkBox_learningRate_pop")
        self.horizontalLayout_lropti.addWidget(self.checkBox_learningRate_pop)
        self.doubleSpinBox_learningRate_pop = QtWidgets.QDoubleSpinBox(self.groupBox_regularization_pop)
        self.doubleSpinBox_learningRate_pop.setEnabled(False)
#        self.doubleSpinBox_learningRate_pop.setDecimals(6)
#        self.doubleSpinBox_learningRate_pop.setMinimum(0.0)
#        self.doubleSpinBox_learningRate_pop.setMaximum(999.0)
#        self.doubleSpinBox_learningRate_pop.setSingleStep(0.0001)
#        self.doubleSpinBox_learningRate_pop.setProperty("value", 0.001)
        self.doubleSpinBox_learningRate_pop.setObjectName("doubleSpinBox_learningRate_pop")
        self.horizontalLayout_lropti.addWidget(self.doubleSpinBox_learningRate_pop)
        self.checkBox_optimizer_pop = QtWidgets.QCheckBox(self.groupBox_regularization_pop)
        self.checkBox_optimizer_pop.setObjectName("checkBox_optimizer_pop")
        self.horizontalLayout_lropti.addWidget(self.checkBox_optimizer_pop)
        self.comboBox_optimizer_pop = QtWidgets.QComboBox(self.groupBox_regularization_pop)
        self.comboBox_optimizer_pop.setEnabled(False)
        self.comboBox_optimizer_pop.setObjectName("comboBox_optimizer_pop")
        self.comboBox_optimizer_pop.addItem("")
        self.comboBox_optimizer_pop.addItem("")
        self.comboBox_optimizer_pop.addItem("")
        self.comboBox_optimizer_pop.addItem("")
        self.comboBox_optimizer_pop.addItem("")
        self.comboBox_optimizer_pop.addItem("")
        self.comboBox_optimizer_pop.addItem("")
        self.horizontalLayout_lropti.addWidget(self.comboBox_optimizer_pop)
        self.gridLayout_12.addLayout(self.horizontalLayout_lropti, 1, 0, 1, 1)
        self.horizontalLayout_43_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_43_pop.setObjectName("horizontalLayout_43_pop")
        self.checkBox_trainLastNOnly_pop = QtWidgets.QCheckBox(self.groupBox_regularization_pop)
        self.checkBox_trainLastNOnly_pop.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_trainLastNOnly_pop.setCheckable(True)
        self.checkBox_trainLastNOnly_pop.setObjectName("checkBox_trainLastNOnly_pop")
        self.horizontalLayout_43_pop.addWidget(self.checkBox_trainLastNOnly_pop)
        self.spinBox_trainLastNOnly_pop = QtWidgets.QSpinBox(self.groupBox_regularization_pop)
        self.spinBox_trainLastNOnly_pop.setEnabled(False)
        self.spinBox_trainLastNOnly_pop.setMaximum(9999)
        self.spinBox_trainLastNOnly_pop.setObjectName("spinBox_trainLastNOnly_pop")
        self.horizontalLayout_43_pop.addWidget(self.spinBox_trainLastNOnly_pop)
        self.checkBox_trainDenseOnly_pop = QtWidgets.QCheckBox(self.groupBox_regularization_pop)
        self.checkBox_trainDenseOnly_pop.setObjectName("checkBox_trainDenseOnly_pop")
        self.horizontalLayout_43_pop.addWidget(self.checkBox_trainDenseOnly_pop)
        self.gridLayout_12.addLayout(self.horizontalLayout_43_pop, 2, 0, 1, 1)
        self.horizontalLayout_3_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3_pop.setObjectName("horizontalLayout_3_pop")
        self.checkBox_dropout_pop = QtWidgets.QCheckBox(self.groupBox_regularization_pop)
        self.checkBox_dropout_pop.setObjectName("checkBox_dropout_pop")
        self.horizontalLayout_3_pop.addWidget(self.checkBox_dropout_pop)
        self.lineEdit_dropout_pop = QtWidgets.QLineEdit(self.groupBox_regularization_pop)
        self.lineEdit_dropout_pop.setEnabled(False)
        validator = QtGui.QRegExpValidator(QtCore.QRegExp("^[0-9 . ,]+$")) #validator allows numbers, dots and commas
        #aternatively, I could use "^[0-9 . , \[ \] ]+$" - this would also allow the user to put the brackets. But why? I just do it in the program
        self.lineEdit_dropout_pop.setValidator(validator)        

        self.lineEdit_dropout_pop.setObjectName("lineEdit_dropout_pop")
        self.horizontalLayout_3_pop.addWidget(self.lineEdit_dropout_pop)
        self.gridLayout_12.addLayout(self.horizontalLayout_3_pop, 3, 0, 1, 1)
        
#        self.horizontalLayout_pTr_pop = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_pTr_pop.setObjectName("horizontalLayout_pTr_pop")
#        self.checkBox_pTr_pop = QtWidgets.QCheckBox(self.groupBox_regularization_pop)
#        self.checkBox_pTr_pop.setObjectName("checkBox_pTr_pop")
#        self.horizontalLayout_pTr_pop.addWidget(self.checkBox_pTr_pop)
#        self.checkBox_pTr_pop.setEnabled(False) #For now this option is just a placeholder!
#        self.lineEdit_pTr_pop = QtWidgets.QLineEdit(self.groupBox_regularization_pop)
#        self.lineEdit_pTr_pop.setEnabled(False)
#        self.lineEdit_pTr_pop.setObjectName("lineEdit_pTr_pop")
#        self.horizontalLayout_pTr_pop.addWidget(self.lineEdit_pTr_pop)
#        self.pushButton_pTr_pop = QtWidgets.QPushButton(self.groupBox_regularization_pop)
#        self.pushButton_pTr_pop.setEnabled(False)
#        self.pushButton_pTr_pop.setMaximumSize(QtCore.QSize(40, 16777215))
#        self.pushButton_pTr_pop.setObjectName("pushButton_pTr_pop")
#        self.horizontalLayout_pTr_pop.addWidget(self.pushButton_pTr_pop)
#        self.gridLayout_12.addLayout(self.horizontalLayout_pTr_pop, 4, 0, 1, 1)
        
        self.horizontalLayout_lossW_pop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_lossW_pop.setObjectName("horizontalLayout_lossW_pop")
        self.checkBox_lossW = QtWidgets.QCheckBox(self.groupBox_regularization_pop)
        self.checkBox_lossW.setObjectName("checkBox_lossW")
        self.horizontalLayout_lossW_pop.addWidget(self.checkBox_lossW)
        self.lineEdit_lossW = QtWidgets.QLineEdit(self.groupBox_regularization_pop)
        self.lineEdit_lossW.setEnabled(False)
        self.lineEdit_lossW.setObjectName("lineEdit_lossW")
        self.horizontalLayout_lossW_pop.addWidget(self.lineEdit_lossW)
        self.pushButton_lossW = QtWidgets.QPushButton(self.groupBox_regularization_pop)
        self.pushButton_lossW.setEnabled(False)
        self.pushButton_lossW.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_lossW.setObjectName("pushButton_lossW")
        self.horizontalLayout_lossW_pop.addWidget(self.pushButton_lossW)
        self.gridLayout_12.addLayout(self.horizontalLayout_lossW_pop, 5, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_regularization_pop, 1, 0, 1, 1)
           
        
        
        
        
        
        
        
        
        
        self.scrollArea_expertMode_pop.setWidget(self.scrollAreaWidgetContents_pop)
        self.gridLayout_3.addWidget(self.scrollArea_expertMode_pop, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_expertMode_pop, 0, 0, 1, 1)
        self.tabWidget_DefineModel_pop.addTab(self.tab_expertMode_pop, "")
        self.gridLayout_3_pop.addWidget(self.tabWidget_DefineModel_pop, 1, 0, 1, 1)
        self.verticalLayout_3_pop.addWidget(self.splitter_pop)
        self.verticalLayout_4_pop.addLayout(self.verticalLayout_3_pop)
        self.gridLayout_slider_pop.addLayout(self.verticalLayout_4_pop, 0, 0, 1, 1)



        ######################ICONS############################################        
        os.path.join(dir_root,"art",Default_dict["Icon theme"],"color_mode.png")

        self.label_colorModeIcon_pop.setPixmap(QtGui.QPixmap(os.path.join(dir_root,"art",Default_dict["Icon theme"],"color_mode.png")))
        self.label_NormalizationIcon_pop.setPixmap(QtGui.QPixmap(os.path.join(dir_root,"art",Default_dict["Icon theme"],"normalization.png")))
        self.label_Crop_NrEpochsIcon_pop.setPixmap(QtGui.QPixmap(os.path.join(dir_root,"art",Default_dict["Icon theme"],"nr_epochs.png")))
        self.label_ModelGeomIcon_pop.setPixmap(QtGui.QPixmap(os.path.join(dir_root,"art",Default_dict["Icon theme"],"model_architecture.png")))
        
        self.label_CropIcon_pop.setPixmap(QtGui.QPixmap(os.path.join(dir_root,"art",Default_dict["Icon theme"],"cropping.png")))
        self.label_Crop_pop.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.checkBox_ApplyNextEpoch.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"thumb.png")))

        self.checkBox_saveEpoch_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"save_epoch.png")))
        self.pushButton_Pause_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"pause.png")))
        self.pushButton_Stop_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"stop.png")))

        self.checkBox_HorizFlip_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"horizontal_flip.png")))
        self.checkBox_VertFlip_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"vertical_flip.png")))
        self.label_Rotation_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"rotation.png")))
        self.label_Rotation_pop.setChecked(True)
        self.label_Rotation_pop.stateChanged.connect(self.keras_changed_rotation_pop)
        self.label_width_shift_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"width_shift.png")))
        self.label_width_shift_pop.setChecked(True)
        self.label_width_shift_pop.stateChanged.connect(self.keras_changed_width_shift_pop)
        self.label_height_shift_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"height_shift.png")))
        self.label_height_shift_pop.setChecked(True)
        self.label_height_shift_pop.stateChanged.connect(self.keras_changed_height_shift_pop)
        self.label_zoom_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"zoom.png")))
        self.label_zoom_pop.setChecked(True)
        self.label_zoom_pop.stateChanged.connect(self.keras_changed_zoom_pop)
        self.label_shear_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"shear.png")))
        self.label_shear_pop.setChecked(True)
        self.label_shear_pop.stateChanged.connect(self.keras_changed_shear_pop)
        self.label_Plus_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"brightness_plus.png")))
        self.label_Plus_pop.setChecked(True)
        self.label_Plus_pop.stateChanged.connect(self.keras_changed_brightplus_pop)
        self.label_Mult_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"brightness_mult.png")))
        self.label_Mult_pop.setChecked(True)
        self.label_Mult_pop.stateChanged.connect(self.keras_changed_brightmult_pop)
        self.label_GaussianNoiseMean_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"gaussian_noise_mean.png")))
        self.label_GaussianNoiseMean_pop.setChecked(True)
        self.label_GaussianNoiseMean_pop.stateChanged.connect(self.keras_changed_noiseMean_pop)
        self.label_GaussianNoiseScale_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"gaussian_noise_scale.png")))
        self.label_GaussianNoiseScale_pop.setChecked(True)
        self.label_GaussianNoiseScale_pop.stateChanged.connect(self.keras_changed_noiseScale_pop)
        self.checkBox_contrast_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"contrast.png")))
        self.checkBox_contrast_pop.stateChanged.connect(self.keras_changed_contrast_pop)
        self.checkBox_saturation_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"saturation.png")))
        self.checkBox_saturation_pop.stateChanged.connect(self.keras_changed_saturation_pop)
        self.checkBox_hue_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"hue.png")))
        self.checkBox_hue_pop.stateChanged.connect(self.keras_changed_hue_pop)

        self.checkBox_avgBlur_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"average_blur.png")))
        #self.checkBox_avgBlur_pop.stateChanged.connect(self.changed_averageBlur_pop)
        self.checkBox_gaussBlur_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"gaussian_blur.png")))
        #self.checkBox_gaussBlur_pop.stateChanged.connect(self.changed_gaussBlur_pop)
        self.checkBox_motionBlur_pop.setIcon(QtGui.QIcon(os.path.join(dir_root,"art",Default_dict["Icon theme"],"motion_blur.png")))
        #self.checkBox_motionBlur_pop.stateChanged.connect(self.changed_motionBlur_pop)






        self.spinBox_realTimeEpochs.setSingleStep(1)
        self.spinBox_realTimeEpochs.setMinimum(1)
        self.spinBox_realTimeEpochs.setMaximum(9999999)
        self.spinBox_realTimeEpochs.setValue(250)
        self.spinBox_NrEpochs_pop.setMaximum(999999999)
        self.pushButton_Pause_pop.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_Pause_pop.setMaximumSize(QtCore.QSize(60, 30))
        self.pushButton_Stop_pop.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton_Stop_pop.setMaximumSize(QtCore.QSize(60, 30))
        self.doubleSpinBox_learningRate_pop.setDecimals(9)
        self.doubleSpinBox_learningRate_pop.setMinimum(1e-06)
        self.doubleSpinBox_learningRate_pop.setMaximum(9999999.0)
        self.doubleSpinBox_learningRate_pop.setSingleStep(0.0001)
        self.doubleSpinBox_learningRate_pop.setValue(0.001)
        self.spinBox_trainLastNOnly_pop.setMaximum(9999)
        self.spinBox_batchSize_pop.setMinimum(1)
        self.spinBox_batchSize_pop.setMaximum(999999999)
        self.spinBox_batchSize_pop.setValue(128)
        self.spinBox_epochs_pop.setMinimum(1)
        self.spinBox_epochs_pop.setMaximum(999999999)



        #####################Some manual settings##############################
        self.Histories = [] #List container for the fitting histories, that are produced by the keras.fit function that is controlled by this popup
        self.RealTime_Acc,self.RealTime_ValAcc,self.RealTime_Loss,self.RealTime_ValLoss = [],[],[],[]
        self.RealTime_OtherMetrics = {} #provide dictionary where AID can save all other metrics in case there are some (like precision...)
        self.X_batch_aug = []#list for storing augmented image, created by some parallel processes
        self.threadpool_quad = QtCore.QThreadPool()#Threadpool for image augmentation
        self.threadpool_quad.setMaxThreadCount(4)#Maximum 4 threads
        self.threadpool_quad_count = 0 #count nr. of threads in queue; 
        
        self.epoch_counter = 0 #Counts the nr. of epochs
        self.tableWidget_HistoryInfo_pop.setMinimumSize(QtCore.QSize(0, 100))
        self.tableWidget_HistoryInfo_pop.setMaximumSize(QtCore.QSize(16777215, 140))
        self.tableWidget_HistoryInfo_pop.setColumnCount(7)
        self.tableWidget_HistoryInfo_pop.setRowCount(0)
        self.spinBox_imagecrop_pop.setMinimum(1)
        self.spinBox_imagecrop_pop.setMaximum(9E8)

        #self.comboBox_colorMode_pop.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_Normalization_pop.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_Crop_NrEpochs_pop.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.spinBox_NrEpochs_pop.setMinimum(1)
        self.spinBox_NrEpochs_pop.setMaximum(9E8)
        self.spinBox_RefreshAfterEpochs_pop.setMinimum(1)
        self.spinBox_RefreshAfterEpochs_pop.setMaximum(9E8)
        self.spinBox_RefreshAfterNrEpochs_pop.setMinimum(1)
        self.spinBox_RefreshAfterNrEpochs_pop.setMaximum(9E8)
        self.spinBox_PlusLower_pop.setMinimum(-255)
        self.spinBox_PlusLower_pop.setMaximum(255)
        self.spinBox_PlusLower_pop.setSingleStep(1)
        self.spinBox_PlusUpper_pop.setMinimum(-255)
        self.spinBox_PlusUpper_pop.setMaximum(255)
        self.spinBox_PlusUpper_pop.setSingleStep(1)
        self.doubleSpinBox_MultLower_pop.setMinimum(0)
        self.doubleSpinBox_MultLower_pop.setMaximum(10)
        self.doubleSpinBox_MultLower_pop.setSingleStep(0.1)
        self.doubleSpinBox_MultUpper_pop.setMinimum(0)
        self.doubleSpinBox_MultUpper_pop.setMaximum(10)
        self.doubleSpinBox_MultUpper_pop.setSingleStep(0.1)
        self.doubleSpinBox_GaussianNoiseMean_pop.setMinimum(-255)
        self.doubleSpinBox_GaussianNoiseMean_pop.setMaximum(255) 
        self.doubleSpinBox_GaussianNoiseMean_pop.setSingleStep(0.1)
        self.doubleSpinBox_GaussianNoiseScale_pop.setMinimum(0)
        self.doubleSpinBox_GaussianNoiseScale_pop.setMaximum(100)
        self.doubleSpinBox_GaussianNoiseScale_pop.setSingleStep(0.1)

        self.spinBox_avgBlurMin_pop.setMinimum(0)
        self.spinBox_avgBlurMin_pop.setMaximum(255)
        self.spinBox_avgBlurMax_pop.setMinimum(0)
        self.spinBox_avgBlurMax_pop.setMaximum(255)
        self.spinBox_gaussBlurMin_pop.setMinimum(0)
        self.spinBox_gaussBlurMin_pop.setMaximum(255)
        self.spinBox_gaussBlurMax_pop.setMinimum(0)
        self.spinBox_gaussBlurMax_pop.setMaximum(255)


        self.comboBox_ShowTrainOrValid_pop.addItems(["Training","Validation"])       
        self.comboBox_ShowWOrWoAug_pop.addItems(["With Augmentation","Original image"])    


#        self.groupBox_expertMode_pop.setEnabled(True)
#        self.groupBox_expertMode_pop.setCheckable(True)
#        self.groupBox_expertMode_pop.setChecked(False)
#        self.scrollArea_expertMode_pop.setWidgetResizable(True)
  
        #Adjust some QObjects manually
        self.spinBox_batchSize_pop.setMinimum(1)       
        self.spinBox_batchSize_pop.setMaximum(1E6)       
        self.spinBox_batchSize_pop.setValue(128)       
        self.spinBox_epochs_pop.setMinimum(1)       
        self.spinBox_epochs_pop.setMaximum(1E6)       
        self.spinBox_epochs_pop.setValue(1)       
        self.doubleSpinBox_learningRate_pop.setDecimals(9)
        self.doubleSpinBox_learningRate_pop.setMinimum(0.0)       
        self.doubleSpinBox_learningRate_pop.setMaximum(1E6)       
        self.doubleSpinBox_learningRate_pop.setValue(0.001)       
        self.doubleSpinBox_learningRate_pop.setSingleStep(0.0001)
        self.spinBox_trainLastNOnly_pop.setMinimum(0)       
        self.spinBox_trainLastNOnly_pop.setMaximum(1E6)       
        self.spinBox_trainLastNOnly_pop.setValue(0)    
        self.checkBox_trainDenseOnly_pop.setChecked(False)


        ######################Connections######################################
        self.doubleSpinBox_learningRate_pop.setEnabled(False)
        self.spinBox_trainLastNOnly_pop.setEnabled(False)
        self.lineEdit_dropout_pop.setEnabled(False)
                        
        self.checkBox_learningRate_pop.toggled['bool'].connect(self.doubleSpinBox_learningRate_pop.setEnabled) 
        self.checkBox_expt_loss_pop.toggled['bool'].connect(self.comboBox_expt_loss_pop.setEnabled)
        self.checkBox_optimizer_pop.toggled['bool'].connect(self.comboBox_optimizer_pop.setEnabled)
        self.checkBox_expt_paddingMode_pop.toggled['bool'].connect(self.comboBox_expt_paddingMode_pop.setEnabled)

        self.checkBox_trainLastNOnly_pop.toggled['bool'].connect(self.spinBox_trainLastNOnly_pop.setEnabled)
        self.checkBox_dropout_pop.toggled['bool'].connect(self.lineEdit_dropout_pop.setEnabled)

        self.checkBox_avgBlur_pop.clicked['bool'].connect(self.spinBox_avgBlurMin_pop.setEnabled)
        self.checkBox_avgBlur_pop.clicked['bool'].connect(self.spinBox_avgBlurMax_pop.setEnabled)
        self.checkBox_gaussBlur_pop.clicked['bool'].connect(self.spinBox_gaussBlurMin_pop.setEnabled)
        self.checkBox_gaussBlur_pop.clicked['bool'].connect(self.spinBox_gaussBlurMax_pop.setEnabled)
        self.checkBox_motionBlur_pop.clicked['bool'].connect(self.label_motionBlurKernel_pop.setEnabled)
        self.checkBox_motionBlur_pop.clicked['bool'].connect(self.lineEdit_motionBlurKernel_pop.setEnabled)
        self.checkBox_motionBlur_pop.clicked['bool'].connect(self.label_motionBlurAngle_pop.setEnabled)
        self.checkBox_motionBlur_pop.clicked['bool'].connect(self.lineEdit_motionBlurAngle_pop.setEnabled)
        self.checkBox_gaussBlur_pop.clicked['bool'].connect(self.label_gaussBlurMin_pop.setEnabled)
        self.checkBox_gaussBlur_pop.clicked['bool'].connect(self.label_gaussBlurMax_pop.setEnabled)
        self.checkBox_avgBlur_pop.clicked['bool'].connect(self.label_avgBlurMin_pop.setEnabled)
        self.checkBox_avgBlur_pop.clicked['bool'].connect(self.label_avgBlurMax_pop.setEnabled)

        self.checkBox_optimizer_pop.toggled['bool'].connect(self.comboBox_optimizer_pop.setEnabled)
        self.checkBox_expt_loss_pop.toggled['bool'].connect(self.comboBox_expt_loss_pop.setEnabled)
        self.comboBox_optimizer_pop.currentTextChanged.connect(self.expert_optimizer_changed_pop)
        self.checkBox_optimizer_pop.stateChanged.connect(self.expert_optimizer_off_pop)
        self.checkBox_learningRate_pop.stateChanged.connect(self.expert_learningrate_off_pop)
        self.checkBox_expt_loss_pop.stateChanged.connect(self.expert_loss_off_pop)
        self.groupBox_expertMode_pop.toggled.connect(self.expert_mode_off_pop)
        self.checkBox_expt_paddingMode_pop.stateChanged.connect(self.expert_paddingMode_off_pop)


        self.retranslateUi(Form)
        self.tabWidget_DefineModel_pop.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_UpdatePlot_pop.setText(_translate("Form", "Update Plot", None))
        self.checkBox_realTimePlotting_pop.setToolTip(_translate("Form", "<html><head/><body><p>Plot model metrics like accuracy, val. accuracy... in real time. Please first hit 'Update plot' to initiate the plotting region.</p></body></html>", None))
        self.checkBox_realTimePlotting_pop.setText(_translate("Form", "Real-time plotting", None))
        self.label_realTimeEpochs_pop.setText(_translate("Form", "Nr. of epochs for RT", None))
        self.label_realTimeEpochs_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define how many of the last epochs should be plotted in real time. 250 means the last 250 epochs are plotted</p></body></html>", None))
        self.spinBox_realTimeEpochs.setToolTip(_translate("Form", "<html><head/><body><p>Define how many of the last epochs should be plotted in real time. 250 means the last 250 epochs are plotted</p></body></html>", None))


        self.groupBox_FittingInfo_pop.setTitle(_translate("Form", "Fitting Info", None))
        self.pushButton_saveTextWindow_pop.setText(_translate("Form", "Save text ", None))
        self.pushButton_clearTextWindow_pop.setToolTip(_translate("Form", "Clear the text window (fitting info)", None))
        self.pushButton_clearTextWindow_pop.setText(_translate("Form", "Clear text", None))
        self.groupBox_ChangeModel_pop.setTitle(_translate("Form", "Change fitting parameters", None))
        self.label_ModelGeom_pop.setText(_translate("Form", "Model Architecture", None))
        self.label_colorMode_pop.setToolTip(_translate("Form", "Color mode used for this model", None))
        self.label_colorMode_pop.setText(_translate("Form", "Color Mode", None))
        self.comboBox_colorMode_pop.setToolTip(_translate("Form", "Color mode used for this model", None))
        self.label_Normalization_pop.setToolTip(_translate("Form", "<html><head/><body><p>Image normalization method. Default is \'Div. by 255\'. Other normalization methods may not be supported by the Sorting Software</p></body></html>", None))
        self.label_Normalization_pop.setText(_translate("Form", "Normalization", None))
        self.comboBox_Normalization_pop.setToolTip(_translate("Form", "<html><head/><body><p>Image normalization method. Default is \'Div. by 255\'. Other normalization methods may not be supported by the Sorting Software</p></body></html>", None))
        self.label_Crop_pop.setToolTip(_translate("Form", "<html><head/><body><p>Models need a defined input image size. Choose wisely since cutting off from large objects might result in information loss.</p></body></html>", None))
        self.label_Crop_pop.setText(_translate("Form", "Input image size", None))
        self.spinBox_imagecrop_pop.setToolTip(_translate("Form", "<html><head/><body><p>Models need a defined input image size. Choose wisely since cutting off from large objects might result in information loss.</p></body></html>", None))
        self.label_Crop_NrEpochs_pop.setToolTip(_translate("Form", "Total number of training iterations", None))
        self.label_Crop_NrEpochs_pop.setText(_translate("Form", "Nr. epochs", None))
        self.spinBox_NrEpochs_pop.setToolTip(_translate("Form", "Total number of training iterations", None))
        self.pushButton_modelname_pop.setToolTip(_translate("Form", "Define path and filename for the model you want to fit", None))
        self.pushButton_modelname_pop.setText(_translate("Form", "Model path:", None))
        self.lineEdit_modelname_pop.setToolTip(_translate("Form", "Define path and filename for the model you want to fit", None))
        self.pushButton_showModelSumm_pop.setText(_translate("Form", "Show model summary", None))
        self.pushButton_saveModelSumm_pop.setText(_translate("Form", "Save model summary", None))
        self.checkBox_ApplyNextEpoch.setToolTip(_translate("Form", "Changes made in this window will be applied at the next epoch", None))
        self.checkBox_ApplyNextEpoch.setText(_translate("Form", "Apply at next epoch", None))
        self.checkBox_saveEpoch_pop.setToolTip(_translate("Form", "Save the model, when the current epoch is done", None))
        self.checkBox_saveEpoch_pop.setText(_translate("Form", "Save Model", None))
        self.pushButton_Pause_pop.setToolTip(_translate("Form", "Pause fitting, push this button again to continue", None))
        self.pushButton_Pause_pop.setText(_translate("Form", " ", None))
        self.pushButton_Stop_pop.setToolTip(_translate("Form", "Stop fitting entirely, Close this window manually, after the progressbar shows 100%", None))
        self.pushButton_Stop_pop.setText(_translate("Form", "", None))
        self.tabWidget_DefineModel_pop.setTabText(self.tabWidget_DefineModel_pop.indexOf(self.tab_DefineModel_pop), _translate("Form", "Define Model", None))
        self.tab_KerasImgAug_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define settings for  affine image augmentations</p></body></html>", None))
        self.label_RefreshAfterEpochs_pop.setToolTip(_translate("Form", "<html><head/><body><p>Affine image augmentation takes quite long; so maybe use the same images for this nr. of epochs</p></body></html>", None))
        self.label_RefreshAfterEpochs_pop.setText(_translate("Form", "Refresh after nr. epochs:", None))
        self.spinBox_RefreshAfterEpochs_pop.setToolTip(_translate("Form", "<html><head/><body><p>Affine image augmentation using takes quite long; so maybe use the same images for this nr. of epochs</p></body></html>", None))
        self.checkBox_HorizFlip_pop.setToolTip(_translate("Form", "<html><head/><body><p>Flip some training images randomly along horiz. axis (left becomes right; right becomes left)</p></body></html>", None))
        self.checkBox_HorizFlip_pop.setText(_translate("Form", "Horizontal flip", None))
        self.checkBox_VertFlip_pop.setToolTip(_translate("Form", "<html><head/><body><p>Flip some training images randomly along vert. axis (bottom up; top down)</p></body></html>", None))
        self.checkBox_VertFlip_pop.setText(_translate("Form", "Vertical flip", None))
        self.label_Rotation_pop.setToolTip(_translate("Form", "<html><head/><body><p>Degree range for random rotations</p></body></html>", None))
        self.label_Rotation_pop.setText(_translate("Form", "Rotation", None))
        self.label_width_shift_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define random shift of width<br>Fraction of total width, if &lt; 1. Otherwise pixels if>=1.<br>Value defines an interval (-width_shift_range, +width_shift_range) from which random numbers are created</p></body></html>", None))
        self.label_width_shift_pop.setText(_translate("Form", "Width shift", None))
        self.label_height_shift_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define random shift of height<br>Fraction of total height if &lt; 1. Otherwise pixels if>=1.<br>Value defines an interval (-height_shift_range, +height_shift_range) from which random numbers are created</p></body></html>", None))
        self.label_height_shift_pop.setText(_translate("Form", "Height shift", None))
        self.label_zoom_pop.setToolTip(_translate("Form", "<html><head/><body><p>Range for random zoom</p></body></html>", None))
        self.label_zoom_pop.setText(_translate("Form", "Zoom", None))
        self.label_shear_pop.setToolTip(_translate("Form", "<html><head/><body><p>Shear Intensity (Shear angle in counter-clockwise direction in degrees)</p></body></html>", None))
        self.label_shear_pop.setText(_translate("Form", "Shear", None))
        self.lineEdit_Rotation_pop.setToolTip(_translate("Form", "<html><head/><body><p>Degree range for random rotations</p></body></html>", None))
        self.lineEdit_Rotation_pop_2.setToolTip(_translate("Form", "<html><head/><body><p>Define random shift of width<br>Fraction of total width, if &lt; 1. Otherwise pixels if>=1.<br>Value defines an interval (-width_shift_range, +width_shift_range) from which random numbers are created</p></body></html>", None))
        self.lineEdit_Rotation_pop_3.setToolTip(_translate("Form", "<html><head/><body><p>Define random shift of height<br>Fraction of total height if &lt; 1. Otherwise pixels if>=1.<br>Value defines an interval (-height_shift_range, +height_shift_range) from which random numbers are created   </p></body></html>", None))
        self.lineEdit_Rotation_pop_4.setToolTip(_translate("Form", "<html><head/><body><p>Range for random zoom</p></body></html>", None))
        self.lineEdit_Rotation_pop_5.setToolTip(_translate("Form", "<html><head/><body><p>Shear Intensity (Shear angle in counter-clockwise direction in degrees)</p></body></html>", None))
        self.tabWidget_DefineModel_pop.setTabText(self.tabWidget_DefineModel_pop.indexOf(self.tab_KerasImgAug_pop), _translate("Form", "Affine img. augm.", None))
        self.label_RefreshAfterNrEpochs_pop.setToolTip(_translate("Form", "<html><head/><body><p>Brightness augmentation is really fast, so best you refresh images for each epoch (set to 1)</p></body></html>", None))
        self.label_RefreshAfterNrEpochs_pop.setText(_translate("Form", "Refresh after nr. epochs:", None))
        self.spinBox_RefreshAfterNrEpochs_pop.setToolTip(_translate("Form", "<html><head/><body><p>Brightness augmentation is really fast, so best you refresh images for each epoch (set to 1)</p></body></html>", None))
        self.groupBox_BrightnessAugmentation_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define add/multiply offset to make image randomly slightly brighter or darker. Additive offset (A) is one number that is added to all pixels values; Multipl. offset (M) is a value to multiply each pixel value with: NewImage = A + M*Image</p></body></html>", None))
        self.groupBox_BrightnessAugmentation_pop.setTitle(_translate("Form", "Brightness augmentation", None))
        self.label_Plus_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define lower threshold for additive offset</p></body></html>", None))
        self.label_Plus_pop.setText(_translate("Form", "Add.", None))
        self.spinBox_PlusLower_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define lower threshold for additive offset</p></body></html>", None))
        #self.label_PlusTo_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define upper threshold for additive offset</p></body></html>", None))
        #self.label_PlusTo_pop.setText(_translate("Form", "...", None))
        self.spinBox_PlusUpper_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define upper threshold for additive offset</p></body></html>", None))
        self.label_Mult_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define lower threshold for multiplicative offset</p></body></html>", None))
        self.label_Mult_pop.setText(_translate("Form", "Mult.", None))
        self.doubleSpinBox_MultLower_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define lower threshold for multiplicative offset</p></body></html>", None))
        #self.label_Rotation_MultTo_pop.setText(_translate("Form", "...", None))
        self.groupBox_GaussianNoise_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define Gaussian Noise, which is added to the image</p></body></html>", None))
        self.groupBox_GaussianNoise_pop.setTitle(_translate("Form", "Gaussian noise", None))
        self.label_GaussianNoiseMean_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define the mean of the Gaussian noise. Typically this should be zero. If you use a positive number it would mean that your noise tends to be positive, i.e. bright.</p></body></html>", None))
        self.label_GaussianNoiseMean_pop.setText(_translate("Form", "Mean", None))
        self.doubleSpinBox_GaussianNoiseMean_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define the mean of the Gaussian noise. Typically this should be zero. If you use a positive number it would mean that your noise tends to be positive, i.e. bright.</p></body></html>", None))
        self.label_GaussianNoiseScale_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define the standard deviation of the Gaussian noise. A larger number means a wider distribution of the noise, which results in an image that looks more noisy. Prefer to change this parameter over chainging the mean.</p></body></html>", None))
        self.label_GaussianNoiseScale_pop.setText(_translate("Form", "Scale", None))
        self.doubleSpinBox_GaussianNoiseScale_pop.setToolTip(_translate("Form", "<html><head/><body><p>Define the standard deviation of the Gaussian noise. A larger number means a wider distribution of the noise, which results in an image that looks more noisy. Prefer to change this parameter over chainging the mean.</p></body></html>", None))

        self.groupBox_colorAugmentation_pop.setTitle(_translate("Form", "Color augm.", None))
        self.checkBox_contrast_pop.setText(_translate("Form", "Contrast", None))
        self.checkBox_contrast_pop.setToolTip(_translate("Form", "<html><head/><body><p>Augment contrast using a random factor. Applicable for Grayscale and RGB. Left spinbox (lower factor) has to be >0. '0.70' to '1.3' means plus/minus 30% contrast (at random)</p></body></html>", None))
        self.checkBox_saturation_pop.setText(_translate("Form", "Saturation", None))
        self.checkBox_saturation_pop.setToolTip(_translate("Form", "<html><head/><body><p>Augment saturation using a random factor. Applicable for RGB only. Left spinbox (lower factor) has to be >0. '0.70' to '1.3' means plus/minus 30% saturation (at random)</p></body></html>", None))
        self.checkBox_hue_pop.setText(_translate("Form", "Hue", None))
        self.checkBox_hue_pop.setToolTip(_translate("Form", "<html><head/><body><p>Augment hue using a random factor. Applicable for RGB only. Left spinbox (lower factor) has to be >0. '0.70' to '1.3' means plus/minus 30% hue (at random)</p></body></html>", None))




        self.groupBox_blurringAug_pop.setTitle(_translate("MainWindow", "Blurring", None))
        tooltip_blurringAug = "Define methods to randomly blur images."
        self.groupBox_blurringAug_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>"+tooltip_blurringAug+"</p></body></html>", None))
        self.label_motionBlurKernel_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define kernels by giving a range [min,max]. Values in this range are then randomly picked for each image</p></body></html>", None))
        self.label_motionBlurKernel_pop.setText(_translate("MainWindow", "Kernel", None))
        self.lineEdit_motionBlurAngle_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define angle for the motion blur by defining a range \"min degree,max degree\". Values in this range are then randomly picked for each image</p></body></html>", None))
        #self.lineEdit_motionBlurAngle_pop.setText(_translate("MainWindow", "-10,10", None))
        self.label_avgBlurMin_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the minimum kernel size for average blur</p></body></html>", None))
        self.label_avgBlurMin_pop.setText(_translate("MainWindow", "Min", None))
        self.spinBox_gaussBlurMax_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the maximum kernel size for gaussian blur</p></body></html>", None))
        tooltip_motionBlur = "Apply random motion blurring. Motion blur is defined by an intensity ('kernel') and a direction ('angle'). Please define a range for 'kernel' and 'angle'. AID will pick a random value (within each range) for each image."
        self.checkBox_motionBlur_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>"+tooltip_motionBlur+"</p></body></html>", None))
        self.checkBox_motionBlur_pop.setText(_translate("MainWindow", "Motion", None))
        self.spinBox_avgBlurMin_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the minimum kernel size for average blur</p></body></html>", None))
        self.spinBox_gaussBlurMin_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the minimum kernel size for gaussian blur</p></body></html>", None))
        self.label_motionBlurAngle_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define a range of angles for the motion blur: 'min degree,max degree'. Values from this range are then randomly picked for each image</p></body></html>", None))
        self.label_motionBlurAngle_pop.setText(_translate("MainWindow", "Angle", None))
        self.label_gaussBlurMin_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the minimum kernel size for gaussian blur</p></body></html>", None))
        self.label_gaussBlurMin_pop.setText(_translate("MainWindow", "Min", None))
        self.label_gaussBlurMin_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the minimum kernel size for gaussian blur</p></body></html>", None))
        tooltip_gaussianBlur = "Apply random gaussian blurring. For gaussian blurring, a gaussian kernel of defined size is used. Please define a min. and max. kernel size. For each image a random value is picked from this range to generate a gaussian kernel."
        self.checkBox_gaussBlur_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>"+tooltip_gaussianBlur+"</p></body></html>", None))
        self.checkBox_gaussBlur_pop.setText(_translate("MainWindow", "Gauss", None))
        self.spinBox_avgBlurMax_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the maximum kernel size for average blur</p></body></html>", None))
        self.label_gaussBlurMax_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the maximum kernel size for gaussian blur</p></body></html>", None))
        self.label_gaussBlurMax_pop.setText(_translate("MainWindow", "Max", None))
        self.label_gaussBlurMax_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the maximum kernel size for gaussian blur</p></body></html>", None))
        tooltip_avgBlur = "Apply random average blurring. Define a range of kernel sizes for the average blur (min. and max. kernel size). Values from this range are then randomly picked for each image. To blur an image, all pixels within the kernel area used to compute an average pixel value. The central element of the kernel area in the image is then set to this value. This operation is carried out over the entire image"
        self.checkBox_avgBlur_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>"+tooltip_avgBlur+"</p></body></html>", None))        
        self.checkBox_avgBlur_pop.setText(_translate("MainWindow", "Average", None))
        
        self.label_avgBlurMax_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the maximum kernel size for average blur</p></body></html>", None))
        self.label_avgBlurMax_pop.setText(_translate("MainWindow", "Max", None))
        self.spinBox_avgBlurMin_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the minimum kernel size for average blur</p></body></html>", None))
        self.spinBox_avgBlurMax_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define the maximum kernel size for average blur</p></body></html>", None))
        self.lineEdit_motionBlurKernel_pop.setToolTip(_translate("MainWindow", "<html><head/><body><p>Define kernels by giving a range \"min,max\". Values from this range are then randomly picked for each image</p></body></html>", None))
        #self.lineEdit_motionBlurKernel_pop.setText(_translate("MainWindow", "0,5", None))















        
        self.tabWidget_DefineModel_pop.setTabText(self.tabWidget_DefineModel_pop.indexOf(self.tab_BrightnessAug_pop), _translate("Form", "Brightn/Color augm.", None))
        self.label_ShowIndex_pop.setText(_translate("Form", "Class", None))
        self.pushButton_ShowExamleImgs_pop.setText(_translate("Form", "Show", None))
        self.tabWidget_DefineModel_pop.setTabText(self.tabWidget_DefineModel_pop.indexOf(self.tab_ExampleImgs_pop), _translate("Form", "Example imgs.", None))
        self.tabWidget_DefineModel_pop.setTabToolTip(self.tabWidget_DefineModel_pop.indexOf(self.tab_ExampleImgs_pop), _translate("Form", "<html><head/><body><p>Show random example images of the training data</p></body></html>", None))

        self.groupBox_expertMode_pop.setToolTip(_translate("Form", "<html><head/><body><p>Expert mode allows changing the learning rate and you can even set parts of the neural net to \'not trainable\' in order to perform transfer learning and fine tune models. Also dropout rates can be adjusted. When expert mode is turned off again, the initial values are applied again.</p></body></html>", None))
        self.groupBox_expertMode_pop.setTitle(_translate("Form", "Expert mode", None))
        self.groupBox_modelKerasFit_pop.setTitle(_translate("Form", "In model_keras.fit()", None))       
        self.checkBox_learningRate_pop.setToolTip(_translate("Form", "<html><head/><body><p>Change the learning rate. The default optimizer is \'adam\' with a learning rate of 0.001</p></body></html>", None))
        self.checkBox_learningRate_pop.setText(_translate("Form", "Learning Rate", None))
        self.doubleSpinBox_learningRate_pop.setToolTip(_translate("Form", "<html><head/><body><p>Change the learning rate. Optimizer is always \'adam\' and default value is 0.001</p></body></html>", None))
        self.checkBox_trainLastNOnly_pop.setToolTip(_translate("Form", "<html><head/><body><p>When checked, only the last n layers of the model, which have >0 parameters will stay trainable. Layers before are set to trainable=False. Please specify n using the spinbox. After this change, the model has to be recompiled, which means the optimizer values are deleted.</p></body></html>", None))
        self.checkBox_trainLastNOnly_pop.setText(_translate("Form", "Train last N layers only. N=", None))
        self.spinBox_trainLastNOnly_pop.setToolTip(_translate("Form", "<html><head/><body><p>Specify the number of last layer in your model that should be kept trainable. Only layers with >0 parameters are counted. Use the checkbox to apply this option. After this change, the model has to be recompiled, which means the optimizer values are deleted. </p></body></html>", None))
        self.checkBox_trainDenseOnly_pop.setToolTip(_translate("Form", "<html><head/><body><p>When checked, only the dense layers are kept trainable (if they have >0 parameters).Other layers are set to trainable=False. After this change, the model has to be recompiled, which means the optimizer values are deleted.</p></body></html>", None))
        self.checkBox_trainDenseOnly_pop.setText(_translate("Form", "Train Dense only", None))

        self.label_batchSize_pop.setToolTip(_translate("Form", "<html><head/><body><p>Number of samples per gradient update. If unspecified, batch_size will default to 128. (Source: Keras documentation)</p></body></html>", None))
        self.label_batchSize_pop.setText(_translate("Form", "Batch size", None))
        self.spinBox_batchSize_pop.setToolTip(_translate("Form", "<html><head/><body><p>Number of samples per gradient update. If unspecified, batch_size will default to 128. (Source: Keras documentation)</p></body></html>", None))
        self.label_epochs_pop.setToolTip(_translate("Form", "<html><head/><body><p>Number of epochs to train the model on identical batch.</p></body></html>", None))
        self.label_epochs_pop.setText(_translate("Form", "Epochs", None))
        self.spinBox_epochs_pop.setToolTip(_translate("Form", "<html><head/><body><p>Number of epochs to train the model on identical batch.</p></body></html>", None))

        self.groupBox_expt_imgProc_pop.setTitle(_translate("Form", "Image processing", None))
        self.checkBox_expt_paddingMode_pop.setText(_translate("Form", "Padding mode", None))
        self.comboBox_expt_paddingMode_pop.setToolTip(_translate("Form", "<html><head/><body><p>By default, the padding mode is \"constant\", which means that zeros are padded.\n"
"\"edge\": Pads with the edge values of array.\n"
"\"linear_ramp\": Pads with the linear ramp between end_value and the array edge value.\n"
"\"maximum\": Pads with the maximum value of all or part of the vector along each axis.\n"
"\"mean\": Pads with the mean value of all or part of the vector along each axis.\n"
"\"median\": Pads with the median value of all or part of the vector along each axis.\n"
"\"minimum\": Pads with the minimum value of all or part of the vector along each axis.\n"
"\"reflect\": Pads with the reflection of the vector mirrored on the first and last values of the vector along each axis.\n"
"\"symmetric\": Pads with the reflection of the vector mirrored along the edge of the array.\n"
"\"wrap\": Pads with the wrap of the vector along the axis. The first values are used to pad the end and the end values are used to pad the beginning.\n"
"Text copied from https://docs.scipy.org/doc/numpy/reference/generated/numpy.pad.html</p></body></html>", None))
        self.comboBox_expt_paddingMode_pop.setItemText(0, _translate("Form", "constant", None))
        self.comboBox_expt_paddingMode_pop.setItemText(1, _translate("Form", "edge", None))
        self.comboBox_expt_paddingMode_pop.setItemText(2, _translate("Form", "linear_ramp", None))
        self.comboBox_expt_paddingMode_pop.setItemText(3, _translate("Form", "maximum", None))
        self.comboBox_expt_paddingMode_pop.setItemText(4, _translate("Form", "mean", None))
        self.comboBox_expt_paddingMode_pop.setItemText(5, _translate("Form", "median", None))
        self.comboBox_expt_paddingMode_pop.setItemText(6, _translate("Form", "minimum", None))
        self.comboBox_expt_paddingMode_pop.setItemText(7, _translate("Form", "reflect", None))
        self.comboBox_expt_paddingMode_pop.setItemText(8, _translate("Form", "symmetric", None))
        self.comboBox_expt_paddingMode_pop.setItemText(9, _translate("Form", "wrap", None))


        self.groupBox_regularization_pop.setTitle(_translate("Form", "Loss / Regularization", None))
        self.checkBox_expt_loss_pop.setText(_translate("Form", "Loss", None))
        self.comboBox_expt_loss_pop.setItemText(0, _translate("Form", "categorical_crossentropy", None))
        #self.comboBox_expt_loss_pop.setItemText(1, _translate("Form", "sparse_categorical_crossentropy", None))
        self.comboBox_expt_loss_pop.setItemText(1, _translate("Form", "mean_squared_error", None))
        self.comboBox_expt_loss_pop.setItemText(2, _translate("Form", "mean_absolute_error", None))
        self.comboBox_expt_loss_pop.setItemText(3, _translate("Form", "mean_absolute_percentage_error", None))
        self.comboBox_expt_loss_pop.setItemText(4, _translate("Form", "mean_squared_logarithmic_error", None))
        self.comboBox_expt_loss_pop.setItemText(5, _translate("Form", "squared_hinge", None))
        self.comboBox_expt_loss_pop.setItemText(6, _translate("Form", "hinge", None))
        self.comboBox_expt_loss_pop.setItemText(7, _translate("Form", "categorical_hinge", None))
        self.comboBox_expt_loss_pop.setItemText(8, _translate("Form", "logcosh", None))
        #self.comboBox_expt_loss_pop.setItemText(10, _translate("Form", "huber_loss", None))
        self.comboBox_expt_loss_pop.setItemText(9, _translate("Form", "binary_crossentropy", None))
        self.comboBox_expt_loss_pop.setItemText(10, _translate("Form", "kullback_leibler_divergence", None))
        self.comboBox_expt_loss_pop.setItemText(11, _translate("Form", "poisson", None))
        self.comboBox_expt_loss_pop.setItemText(12, _translate("Form", "cosine_proximity", None))
        #self.comboBox_expt_loss_pop.setItemText(15, _translate("Form", "is_categorical_crossentropy", None))


        self.checkBox_optimizer_pop.setText(_translate("Form", "Optimizer", None))
        self.comboBox_optimizer_pop.setItemText(0, _translate("Form", "Adam", None))
        self.comboBox_optimizer_pop.setItemText(1, _translate("Form", "SGD", None))
        self.comboBox_optimizer_pop.setItemText(2, _translate("Form", "RMSprop", None))
        self.comboBox_optimizer_pop.setItemText(3, _translate("Form", "Adagrad", None))
        self.comboBox_optimizer_pop.setItemText(4, _translate("Form", "Adadelta", None))
        self.comboBox_optimizer_pop.setItemText(5, _translate("Form", "Adamax", None))
        self.comboBox_optimizer_pop.setItemText(6, _translate("Form", "Nadam", None))


        self.checkBox_dropout_pop.setToolTip(_translate("Form", "<html><head/><body><p>If your model has one or more dropout layers, you can change the dropout rates here. Insert into the lineEdit one value (e.g. 0.5) to apply this one value to all dropout layers, or insert a list of values to specify the dropout rates for each dropout layer individually (e.g. for three dropout layers: [ 0.2 , 0.5 , 0.25 ]. The model will be recompiled, but the optimizer weights are not deleted.</p></body></html>", None))
        self.checkBox_dropout_pop.setText(_translate("Form", "Change Dropout to", None))
        self.lineEdit_dropout_pop.setToolTip(_translate("Form", "<html><head/><body><p>If your model has one or more dropout layers, you can change the dropout rates here. Insert into the lineEdit one value (e.g. 0.5) to apply this one value to all dropout layers, or insert a list of values to specify the dropout rates for each dropout layer individually (e.g. for three dropout layers: [ 0.2 , 0.5 , 0.25 ]. The model will be recompiled, but the optimizer weights are not deleted.</p></body></html>", None))

#        self.checkBox_pTr_pop.setText(_translate("Form", "Partial trainability", None))
#        self.checkBox_pTr_pop.setToolTip(_translate("Form", "<html><head/><body><p>Partial trainability allows you to make parts of a layer non-trainable. Hence, this option makes most sense in combination with 'Load and continue' training a model. After checking this box, the model you chose on 'Define model'-tab is initialized. The line on the right shows the trainability of each layer in the model. Use the button on the right ('...') to open a popup menu, which allows you to specify individual trainabilities for each layer.</p></body></html>", None))
#        self.lineEdit_pTr_pop.setToolTip(_translate("Form", "<html><head/><body><p>Partial trainability allows you to make parts of a layer non-trainable. Hence, this option makes most sense in combination with 'Load and continue' training a model. After checking this box, the model you chose on 'Define model'-tab is initialized. The line on the right shows the trainability of each layer in the model. Use the button on the right ('...') to open a popup menu, which allows you to specify individual trainabilities for each layer.</p></body></html>", None))
#        self.pushButton_pTr_pop.setText(_translate("Form", "...", None))
#        self.pushButton_pTr_pop.setToolTip(_translate("Form", "<html><head/><body><p>Partial trainability allows you to make parts of a layer non-trainable. Hence, this option makes most sense in combination with 'Load and continue' training a model. After checking this box, the model you chose on 'Define model'-tab is initialized. The line on the right shows the trainability of each layer in the model. Use the button on the right ('...') to open a popup menu, which allows you to specify individual trainabilities for each layer.</p></body></html>", None))

        self.checkBox_lossW.setText(_translate("Form", "Loss Weights", None))
        self.checkBox_lossW.setToolTip(_translate("Form", "<html><head/><body><p>Specify scalar coefficients to weight the loss contributions of different classes.</p></body></html>", None))
        self.lineEdit_lossW.setToolTip(_translate("Form", "<html><head/><body><p>Specify scalar coefficients to weight the loss contributions of different classes.</p></body></html>", None))
        self.pushButton_lossW.setToolTip(_translate("Form", "<html><head/><body><p>Specify scalar coefficients to weight the loss contributions of different classes.</p></body></html>", None))
        self.pushButton_lossW.setText(_translate("Form", "...", None))

        self.tabWidget_DefineModel_pop.setTabText(self.tabWidget_DefineModel_pop.indexOf(self.tab_expertMode_pop), _translate("Form", "Expert", None))
        
    #Functions for Keras augmentation checkboxes
    def keras_changed_rotation_pop(self,on_or_off):
        if on_or_off==0:
            self.lineEdit_Rotation_pop.setText(str(0))
            self.lineEdit_Rotation_pop.setEnabled(False)
        elif on_or_off==2:
            self.lineEdit_Rotation_pop.setText(str(Default_dict ["rotation"]))
            self.lineEdit_Rotation_pop.setEnabled(True)
        else:
            return
    def keras_changed_width_shift_pop(self,on_or_off):
        if on_or_off==0:
            self.lineEdit_Rotation_pop_2.setText(str(0))
            self.lineEdit_Rotation_pop_2.setEnabled(False)
        elif on_or_off==2:
            self.lineEdit_Rotation_pop_2.setText(str(Default_dict ["width_shift"]))
            self.lineEdit_Rotation_pop_2.setEnabled(True)
        else:
            return
    def keras_changed_height_shift_pop(self,on_or_off):
        if on_or_off==0:
            self.lineEdit_Rotation_pop_3.setText(str(0))
            self.lineEdit_Rotation_pop_3.setEnabled(False)
        elif on_or_off==2:
            self.lineEdit_Rotation_pop_3.setText(str(Default_dict ["height_shift"]))
            self.lineEdit_Rotation_pop_3.setEnabled(True)
        else:
            return
    def keras_changed_zoom_pop(self,on_or_off):
        if on_or_off==0:
            self.lineEdit_Rotation_pop_4.setText(str(0))
            self.lineEdit_Rotation_pop_4.setEnabled(False)
        elif on_or_off==2:
            self.lineEdit_Rotation_pop_4.setText(str(Default_dict ["zoom"]))
            self.lineEdit_Rotation_pop_4.setEnabled(True)
        else:
            return
    def keras_changed_shear_pop(self,on_or_off):
        if on_or_off==0:
            self.lineEdit_Rotation_pop_5.setText(str(0))
            self.lineEdit_Rotation_pop_5.setEnabled(False)
        elif on_or_off==2:
            self.lineEdit_Rotation_pop_5.setText(str(Default_dict ["shear"]))
            self.lineEdit_Rotation_pop_5.setEnabled(True)
        else:
            return
    def keras_changed_brightplus_pop(self,on_or_off):
        if on_or_off==0:
            self.spinBox_PlusLower_pop.setValue(0)
            self.spinBox_PlusLower_pop.setEnabled(False)
            self.spinBox_PlusUpper_pop.setValue(0)
            self.spinBox_PlusUpper_pop.setEnabled(False)
        elif on_or_off==2:
            self.spinBox_PlusLower_pop.setValue(Default_dict ["Brightness add. lower"])
            self.spinBox_PlusLower_pop.setEnabled(True)
            self.spinBox_PlusUpper_pop.setValue(Default_dict ["Brightness add. upper"])
            self.spinBox_PlusUpper_pop.setEnabled(True)
        else:
            return
    def keras_changed_brightmult_pop(self,on_or_off):
        if on_or_off==0:
            self.doubleSpinBox_MultLower_pop.setValue(1.0)
            self.doubleSpinBox_MultLower_pop.setEnabled(False)
            self.doubleSpinBox_MultUpper_pop.setValue(1.0)
            self.doubleSpinBox_MultUpper_pop.setEnabled(False)
        elif on_or_off==2:
            self.doubleSpinBox_MultLower_pop.setValue(Default_dict ["Brightness mult. lower"])
            self.doubleSpinBox_MultLower_pop.setEnabled(True)
            self.doubleSpinBox_MultUpper_pop.setValue(Default_dict ["Brightness mult. upper"])
            self.doubleSpinBox_MultUpper_pop.setEnabled(True)
        else:
            return
    def keras_changed_noiseMean_pop(self,on_or_off):
        if on_or_off==0:
            self.doubleSpinBox_GaussianNoiseMean_pop.setValue(0.0)
            self.doubleSpinBox_GaussianNoiseMean_pop.setEnabled(False)
        elif on_or_off==2:
            self.doubleSpinBox_GaussianNoiseMean_pop.setValue(Default_dict ["Gaussnoise Mean"])
            self.doubleSpinBox_GaussianNoiseMean_pop.setEnabled(True)
        else:
            return
    def keras_changed_noiseScale_pop(self,on_or_off):
        if on_or_off==0:
            self.doubleSpinBox_GaussianNoiseScale_pop.setValue(0.0)
            self.doubleSpinBox_GaussianNoiseScale_pop.setEnabled(False)
        elif on_or_off==2:
            self.doubleSpinBox_GaussianNoiseScale_pop.setValue(Default_dict ["Gaussnoise Scale"])
            self.doubleSpinBox_GaussianNoiseScale_pop.setEnabled(True)
        else:
            return
    def keras_changed_contrast_pop(self,on_or_off):
        if on_or_off==0:
            self.doubleSpinBox_contrastLower_pop.setEnabled(False)
            self.doubleSpinBox_contrastHigher_pop.setEnabled(False)
        elif on_or_off==2:
            self.doubleSpinBox_contrastLower_pop.setEnabled(True)
            self.doubleSpinBox_contrastHigher_pop.setEnabled(True)
        else:
            return
    def keras_changed_saturation_pop(self,on_or_off):
        if on_or_off==0:
            self.doubleSpinBox_saturationLower_pop.setEnabled(False)
            self.doubleSpinBox_saturationHigher_pop.setEnabled(False)
        elif on_or_off==2:
            self.doubleSpinBox_saturationLower_pop.setEnabled(True)
            self.doubleSpinBox_saturationHigher_pop.setEnabled(True)
        else:
            return
    def keras_changed_hue_pop(self,on_or_off):
        if on_or_off==0:
            self.doubleSpinBox_hueDelta_pop.setEnabled(False)
        elif on_or_off==2:
            self.doubleSpinBox_hueDelta_pop.setEnabled(True)
        else:
            return


    def expert_mode_off_pop(self,on_or_off):
        """
        Reset all values on the expert tab to the default values, excluding the metrics
        metrics are defined only once when starting fitting and should not be changed
        """
        if on_or_off==0: #switch off
            self.spinBox_batchSize_pop.setValue(Default_dict["spinBox_batchSize"])
            self.spinBox_epochs_pop.setValue(1)
            self.checkBox_expt_loss_pop.setChecked(False)
            self.expert_loss_off_pop(0)
            self.checkBox_learningRate_pop.setChecked(False)        
            self.expert_learningrate_off_pop(0)
            self.checkBox_optimizer_pop.setChecked(False)
            self.expert_optimizer_off_pop(0)
            self.checkBox_expt_paddingMode_pop.setChecked(False)            
            self.expert_paddingMode_off_pop(0)


    def expert_loss_off_pop(self,on_or_off):
        if on_or_off==0: #switch off
            #switch back to categorical_crossentropy 
            index = self.comboBox_expt_loss_pop.findText("categorical_crossentropy", QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.comboBox_expt_loss_pop.setCurrentIndex(index)
        
    def expert_learningrate_off_pop(self,on_or_off):
        if on_or_off==0: #switch off
            #which optimizer is used? (there are different default learning-rates
            #for each optimizer!)
            optimizer = str(self.comboBox_optimizer_pop.currentText())
            self.doubleSpinBox_learningRate_pop.setValue(Default_dict["doubleSpinBox_learningRate_"+optimizer])

    def expert_optimizer_off_pop(self,on_or_off):
        if on_or_off==0: #switch off, set back to categorical_crossentropy
            optimizer = "Adam"
            index = self.comboBox_optimizer_pop.findText(optimizer, QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.comboBox_optimizer_pop.setCurrentIndex(index)
                #also reset the learning rate to the default
                self.doubleSpinBox_learningRate_pop.setValue(Default_dict["doubleSpinBox_learningRate_"+optimizer])

    def expert_optimizer_changed_pop(self,value):
        #set the learning rate to the default for this optimizer
        optimizer = value
        value_current = float(self.doubleSpinBox_learningRate_pop.value())
        value_wanted = Default_dict["doubleSpinBox_learningRate_"+optimizer]
        text = str(self.textBrowser_FittingInfo_pop.toPlainText())
        if value_current!=value_wanted and len(text)>120:#avoid that the message pops up when window is created
            self.doubleSpinBox_learningRate_pop.setValue(value_wanted)
            #Inform user
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)       
            msg.setWindowTitle("Learning rate to default")
            msg.setText("Learning rate was set to the default for "+optimizer)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return


    def expert_paddingMode_off_pop(self,value):
        if value==0: #switch off
            #switch back to "constant" padding 
            index = self.comboBox_expt_paddingMode_pop.findText("constant", QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.comboBox_expt_paddingMode_pop.setCurrentIndex(index)



















class popup_trainability(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 789)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
#        self.pushButton_pop_pTr_reset = QtWidgets.QPushButton(Form)
#        self.pushButton_pop_pTr_reset.setObjectName("pushButton_pop_pTr_reset")
#        self.horizontalLayout_8.addWidget(self.pushButton_pop_pTr_reset)
        spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.pushButton_pop_pTr_update = QtWidgets.QPushButton(Form)
        self.pushButton_pop_pTr_update.setObjectName("pushButton_pop_pTr_update")
        self.horizontalLayout_8.addWidget(self.pushButton_pop_pTr_update)
        self.pushButton_pop_pTr_ok = QtWidgets.QPushButton(Form)
        self.pushButton_pop_pTr_ok.setObjectName("pushButton_pop_pTr_ok")
        self.horizontalLayout_8.addWidget(self.pushButton_pop_pTr_ok)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_pop_pTr_modelPath = QtWidgets.QLabel(self.groupBox)
        self.label_pop_pTr_modelPath.setObjectName("label_pop_pTr_modelPath")
        self.horizontalLayout_4.addWidget(self.label_pop_pTr_modelPath)
        self.lineEdit_pop_pTr_modelPath = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_pop_pTr_modelPath.setEnabled(False)
        self.lineEdit_pop_pTr_modelPath.setObjectName("lineEdit_pop_pTr_modelPath")
        self.horizontalLayout_4.addWidget(self.lineEdit_pop_pTr_modelPath)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 3)
#        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
#        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
#        self.label_pop_pTr_arch = QtWidgets.QLabel(self.groupBox)
#        self.label_pop_pTr_arch.setObjectName("label_pop_pTr_arch")
#        self.horizontalLayout_5.addWidget(self.label_pop_pTr_arch)
#        self.lineEdit_pop_pTr_arch = QtWidgets.QLineEdit(self.groupBox)
#        self.lineEdit_pop_pTr_arch.setEnabled(False)
#        self.lineEdit_pop_pTr_arch.setObjectName("lineEdit_pop_pTr_arch")
#        self.horizontalLayout_5.addWidget(self.lineEdit_pop_pTr_arch)
#        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
#        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#        self.label_pop_pTr_norm = QtWidgets.QLabel(self.groupBox)
#        self.label_pop_pTr_norm.setObjectName("label_pop_pTr_norm")
#        self.horizontalLayout_3.addWidget(self.label_pop_pTr_norm)
#        self.comboBox_pop_pTr_norm = QtWidgets.QComboBox(self.groupBox)
#        self.comboBox_pop_pTr_norm.setEnabled(False)
#        self.comboBox_pop_pTr_norm.setObjectName("comboBox_pop_pTr_norm")
#        self.horizontalLayout_3.addWidget(self.comboBox_pop_pTr_norm)
#        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
#        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_pop_pTr_inpSize = QtWidgets.QLabel(self.groupBox)
        self.label_pop_pTr_inpSize.setObjectName("label_pop_pTr_inpSize")
        self.horizontalLayout.addWidget(self.label_pop_pTr_inpSize)
        self.spinBox_pop_pTr_inpSize = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_pop_pTr_inpSize.setEnabled(False)
        self.spinBox_pop_pTr_inpSize.setAccessibleName("")
        self.spinBox_pop_pTr_inpSize.setObjectName("spinBox_pop_pTr_inpSize")
        self.horizontalLayout.addWidget(self.spinBox_pop_pTr_inpSize)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_pop_pTr_outpSize = QtWidgets.QLabel(self.groupBox)
        self.label_pop_pTr_outpSize.setObjectName("label_pop_pTr_outpSize")
        self.horizontalLayout_2.addWidget(self.label_pop_pTr_outpSize)
        self.spinBox_pop_pTr_outpSize = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_pop_pTr_outpSize.setEnabled(False)
        self.spinBox_pop_pTr_outpSize.setObjectName("spinBox_pop_pTr_outpSize")
        self.horizontalLayout_2.addWidget(self.spinBox_pop_pTr_outpSize)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_pop_pTr_colorMode = QtWidgets.QLabel(self.groupBox)
        self.label_pop_pTr_colorMode.setObjectName("label_pop_pTr_colorMode")
        self.horizontalLayout_6.addWidget(self.label_pop_pTr_colorMode)
        self.comboBox_pop_pTr_colorMode = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_pop_pTr_colorMode.setEnabled(False)
        self.comboBox_pop_pTr_colorMode.setObjectName("comboBox_pop_pTr_colorMode")
        self.horizontalLayout_6.addWidget(self.comboBox_pop_pTr_colorMode)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 2, 1, 1)
        self.groupBox_pop_pTr_layersTable = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_pop_pTr_layersTable.setObjectName("groupBox_pop_pTr_layersTable")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_pop_pTr_layersTable)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget_pop_pTr_layersTable = MyTable(0,5,self.groupBox_pop_pTr_layersTable)
        self.tableWidget_pop_pTr_layersTable.setObjectName("tableWidget_pop_pTr_layersTable")

        header_labels = ["Name", "Type" ,"No.Params", "No.Units", "Trainability"]
        self.tableWidget_pop_pTr_layersTable.setHorizontalHeaderLabels(header_labels) 
        header = self.tableWidget_pop_pTr_layersTable.horizontalHeader()
        for i in range(len(header_labels)):
            header.setResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)        
        self.tableWidget_pop_pTr_layersTable.setAcceptDrops(True)
        self.tableWidget_pop_pTr_layersTable.setDragEnabled(True)
        self.tableWidget_pop_pTr_layersTable.resizeRowsToContents()

        self.gridLayout_3.addWidget(self.tableWidget_pop_pTr_layersTable, 0, 0, 1, 1)
        self.groupBox_pop_pTr_modelSummary = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_pop_pTr_modelSummary.sizePolicy().hasHeightForWidth())
        self.groupBox_pop_pTr_modelSummary.setSizePolicy(sizePolicy)
        self.groupBox_pop_pTr_modelSummary.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox_pop_pTr_modelSummary.setFlat(False)
        self.groupBox_pop_pTr_modelSummary.setCheckable(False)
        self.groupBox_pop_pTr_modelSummary.setObjectName("groupBox_pop_pTr_modelSummary")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_pop_pTr_modelSummary)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.gridLayout_4.setHorizontalSpacing(7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser_pop_pTr_modelSummary = QtWidgets.QTextBrowser(self.groupBox_pop_pTr_modelSummary)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_pop_pTr_modelSummary.sizePolicy().hasHeightForWidth())
        self.textBrowser_pop_pTr_modelSummary.setSizePolicy(sizePolicy)
        self.textBrowser_pop_pTr_modelSummary.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser_pop_pTr_modelSummary.setBaseSize(QtCore.QSize(0, 0))
        self.textBrowser_pop_pTr_modelSummary.setAutoFillBackground(False)
        self.textBrowser_pop_pTr_modelSummary.setObjectName("textBrowser_pop_pTr_modelSummary")
        self.gridLayout_4.addWidget(self.textBrowser_pop_pTr_modelSummary, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Form)
                
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Partial trainability", None))
        self.tableWidget_pop_pTr_layersTable.setToolTip(_translate("Form", "<html><head/><body><p>The table shows all Dense and Conv2D layers and their trainablilities. To decrease the trainability, use the spinbox and a value between 0 and 1 and hit 'Update'. Then, the layers where you chose decrease the trainabliity are split into a layer that stays trainable and another layer that is set to not-trainable. Next, a Concatenation-layer is inserted, which combines both aforementioned layers again. Of course the weights are copied from the initial model, to the customized model, but you cannot specify, which particular nodes/filters of a layer are trainable or non-trainable. If you set for example a trainabliity of 0.25, the first 75% of the nodes are set to not-trainable and the rest 25% are left trainable.</p></body></html>", None))
        #self.pushButton_pop_pTr_reset.setText(_translate("Form", "Reset", None))
        #self.pushButton_pop_pTr_reset.setToolTip(_translate("Form", "<html><head/><body><p>Not implemented yet.</p></body></html>", None))
        self.pushButton_pop_pTr_update.setText(_translate("Form", "Update", None))
        self.pushButton_pop_pTr_update.setToolTip(_translate("Form", "<html><head/><body><p>Apply the requested changes in trainability.</p></body></html>", None))
        self.pushButton_pop_pTr_ok.setText(_translate("Form", "OK", None))
        self.pushButton_pop_pTr_ok.setToolTip(_translate("Form", "<html><head/><body><p>Save the customized model to a user-defined location. This model will automaticlly be selected for 'Load and continue' in the 'Define model'-tab. Just determine a 'Model path' before training. Training will then start using your customized model.</p></body></html>", None))
        self.groupBox.setTitle(_translate("Form", "Model information", None))
        self.label_pop_pTr_modelPath.setText(_translate("Form", "Model path", None))
#        self.label_pop_pTr_arch.setText(_translate("Form", "Architecture", None))
#        self.label_pop_pTr_norm.setText(_translate("Form", "Normalization", None))
        self.label_pop_pTr_inpSize.setText(_translate("Form", "Input size", None))
        self.label_pop_pTr_outpSize.setText(_translate("Form", "Output classes", None))
        self.label_pop_pTr_colorMode.setText(_translate("Form", "Color Mode", None))
        self.groupBox_pop_pTr_layersTable.setTitle(_translate("Form", "Layers", None))
        self.groupBox_pop_pTr_modelSummary.setTitle(_translate("Form", "Model summary", None))


class popup_lossweights(QtWidgets.QWidget):
    def setupUi(self, Form_lossW):
        Form_lossW.setObjectName("Form_lossW")
        Form_lossW.resize(470, 310)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form_lossW)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_lossW = QtWidgets.QGroupBox(Form_lossW)
        self.groupBox_lossW.setObjectName("groupBox_lossW")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_lossW)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_lossW = MyTable(0,5,self.groupBox_lossW)
        self.tableWidget_lossW.setObjectName("tableWidget_lossW")

        header_labels = ["Class", "Events tot." ,"Events/Epoch", "Events/Epoch[%]", "Loss weight"]
        self.tableWidget_lossW.setHorizontalHeaderLabels(header_labels) 
        header = self.tableWidget_lossW.horizontalHeader()
        for i in range(len(header_labels)):
            header.setResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)        
        self.tableWidget_lossW.setAcceptDrops(True)
        self.tableWidget_lossW.setDragEnabled(True)
        self.tableWidget_lossW.resizeRowsToContents()

        self.gridLayout.addWidget(self.tableWidget_lossW, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_lossW, 0, 0, 1, 1)
        self.horizontalLayout_lossW_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_lossW_buttons.setObjectName("horizontalLayout_lossW_buttons")
#        self.pushButton_pop_lossW_reset = QtWidgets.QPushButton(Form_lossW)
#        self.pushButton_pop_lossW_reset.setObjectName("pushButton_pop_lossW_reset")
#        self.horizontalLayout_lossW_buttons.addWidget(self.pushButton_pop_lossW_reset)
        spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_lossW_buttons.addItem(spacerItem)
        self.pushButton_pop_lossW_cancel = QtWidgets.QPushButton(Form_lossW)
        self.pushButton_pop_lossW_cancel.setObjectName("pushButton_pop_lossW_cancel")
        self.horizontalLayout_lossW_buttons.addWidget(self.pushButton_pop_lossW_cancel)
        self.comboBox_lossW = QtWidgets.QComboBox(Form_lossW)
        self.comboBox_lossW.setObjectName("comboBox_lossW")
        self.comboBox_lossW.addItems(["None","Balanced","Custom"])
        self.horizontalLayout_lossW_buttons.addWidget(self.comboBox_lossW)
        self.pushButton_pop_lossW_ok = QtWidgets.QPushButton(Form_lossW)
        self.pushButton_pop_lossW_ok.setObjectName("pushButton_pop_lossW_ok")
        self.horizontalLayout_lossW_buttons.addWidget(self.pushButton_pop_lossW_ok)
        self.gridLayout_2.addLayout(self.horizontalLayout_lossW_buttons, 1, 0, 1, 1)

        self.retranslateUi(Form_lossW)
        QtCore.QMetaObject.connectSlotsByName(Form_lossW)


    def retranslateUi(self, Form_lossW):
        _translate = QtCore.QCoreApplication.translate
        Form_lossW.setWindowTitle(_translate("Form_lossW", "Custom loss weights per class", None))
        self.groupBox_lossW.setTitle(_translate("Form_lossW", "Training data - custom class weights", None))
        #self.pushButton_pop_lossW_reset.setText(_translate("Form_lossW", "Reset", None))
        self.pushButton_pop_lossW_cancel.setText(_translate("Form_lossW", "Cancel", None))
        self.pushButton_pop_lossW_ok.setText(_translate("Form_lossW", "OK", None))




class popup_imageLoadResize(QtWidgets.QWidget):
    def setupUi(self, Form_imageResize):
        Form_imageResize.setObjectName("Form_imageResize")
        Form_imageResize.resize(468, 270)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form_imageResize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_imgResize_occurences = QtWidgets.QScrollArea(Form_imageResize)
        self.scrollArea_imgResize_occurences.setWidgetResizable(True)
        self.scrollArea_imgResize_occurences.setObjectName("scrollArea_imgResize_occurences")
        self.scrollAreaWidgetContents_imgResize = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_imgResize.setGeometry(QtCore.QRect(0, 0, 423, 109))
        self.scrollAreaWidgetContents_imgResize.setObjectName("scrollAreaWidgetContents_imgResize")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_imgResize)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_imgResize_occurences = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_imgResize)
        self.textBrowser_imgResize_occurences.setObjectName("textBrowser_imgResize_occurences")
        self.gridLayout.addWidget(self.textBrowser_imgResize_occurences, 0, 0, 1, 1)
        self.scrollArea_imgResize_occurences.setWidget(self.scrollAreaWidgetContents_imgResize)
        self.gridLayout_3.addWidget(self.scrollArea_imgResize_occurences, 2, 0, 1, 1)
        self.gridLayout_imageResizeOptions = QtWidgets.QGridLayout()
        self.gridLayout_imageResizeOptions.setObjectName("gridLayout_imageResizeOptions")
        self.label_imgResize_x_3 = QtWidgets.QLabel(Form_imageResize)
        self.label_imgResize_x_3.setObjectName("label_imgResize_x_3")
        self.gridLayout_imageResizeOptions.addWidget(self.label_imgResize_x_3, 2, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_imageResizeOptions.addItem(spacerItem, 1, 5, 1, 1)
        self.label_imgResize_height = QtWidgets.QLabel(Form_imageResize)
        self.label_imgResize_height.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imgResize_height.setObjectName("label_imgResize_height")
        self.gridLayout_imageResizeOptions.addWidget(self.label_imgResize_height, 0, 1, 1, 2)
        self.spinBox_ingResize_w_2 = QtWidgets.QSpinBox(Form_imageResize)
        self.spinBox_ingResize_w_2.setEnabled(False)
        self.spinBox_ingResize_w_2.setMaximum(999999)
        self.spinBox_ingResize_w_2.setObjectName("spinBox_ingResize_w_2")
        self.gridLayout_imageResizeOptions.addWidget(self.spinBox_ingResize_w_2, 2, 4, 1, 1)
        self.spinBox_ingResize_h_1 = QtWidgets.QSpinBox(Form_imageResize)
        self.spinBox_ingResize_h_1.setEnabled(False)
        self.spinBox_ingResize_h_1.setMaximum(999999)
        self.spinBox_ingResize_h_1.setObjectName("spinBox_ingResize_h_1")
        self.gridLayout_imageResizeOptions.addWidget(self.spinBox_ingResize_h_1, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_imageResizeOptions.addItem(spacerItem1, 0, 5, 1, 1)
        self.pushButton_imgResize_ok = QtWidgets.QPushButton(Form_imageResize)
        self.pushButton_imgResize_ok.setEnabled(False)
        self.pushButton_imgResize_ok.setObjectName("pushButton_imgResize_ok")
        self.gridLayout_imageResizeOptions.addWidget(self.pushButton_imgResize_ok, 3, 5, 1, 1)
        self.spinBox_ingResize_w_1 = QtWidgets.QSpinBox(Form_imageResize)
        self.spinBox_ingResize_w_1.setEnabled(False)
        self.spinBox_ingResize_w_1.setMaximum(999999)
        self.spinBox_ingResize_w_1.setObjectName("spinBox_ingResize_w_1")
        self.gridLayout_imageResizeOptions.addWidget(self.spinBox_ingResize_w_1, 1, 4, 1, 1)
        self.comboBox_resizeMethod = QtWidgets.QComboBox(Form_imageResize)
        self.comboBox_resizeMethod.setEnabled(False)
        self.comboBox_resizeMethod.setObjectName("comboBox_resizeMethod")
        self.comboBox_resizeMethod.addItem("")
        self.comboBox_resizeMethod.addItem("")
        self.comboBox_resizeMethod.addItem("")
        self.comboBox_resizeMethod.addItem("")
        self.comboBox_resizeMethod.addItem("")
        self.gridLayout_imageResizeOptions.addWidget(self.comboBox_resizeMethod, 2, 5, 1, 1)
        self.pushButton_imgResize_cancel = QtWidgets.QPushButton(Form_imageResize)
        self.pushButton_imgResize_cancel.setObjectName("pushButton_imgResize_cancel")
        self.gridLayout_imageResizeOptions.addWidget(self.pushButton_imgResize_cancel, 3, 2, 1, 3)
        self.radioButton_imgResize_cropPad = QtWidgets.QRadioButton(Form_imageResize)
        self.radioButton_imgResize_cropPad.setObjectName("radioButton_imgResize_cropPad")
        self.gridLayout_imageResizeOptions.addWidget(self.radioButton_imgResize_cropPad, 1, 0, 1, 1)
        self.label_imgResize_x_2 = QtWidgets.QLabel(Form_imageResize)
        self.label_imgResize_x_2.setObjectName("label_imgResize_x_2")
        self.gridLayout_imageResizeOptions.addWidget(self.label_imgResize_x_2, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_imageResizeOptions.addItem(spacerItem2, 3, 0, 1, 2)
        self.spinBox_ingResize_h_2 = QtWidgets.QSpinBox(Form_imageResize)
        self.spinBox_ingResize_h_2.setEnabled(False)
        self.spinBox_ingResize_h_2.setMaximum(999999)
        self.spinBox_ingResize_h_2.setObjectName("spinBox_ingResize_h_2")
        self.gridLayout_imageResizeOptions.addWidget(self.spinBox_ingResize_h_2, 2, 1, 1, 2)
        self.label_imgResize_width = QtWidgets.QLabel(Form_imageResize)
        self.label_imgResize_width.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imgResize_width.setObjectName("label_imgResize_width")
        self.gridLayout_imageResizeOptions.addWidget(self.label_imgResize_width, 0, 4, 1, 1)
        self.label_imgResize_method = QtWidgets.QLabel(Form_imageResize)
        self.label_imgResize_method.setObjectName("label_imgResize_method")
        self.gridLayout_imageResizeOptions.addWidget(self.label_imgResize_method, 0, 0, 1, 1)
        self.label_imgResize_x_1 = QtWidgets.QLabel(Form_imageResize)
        self.label_imgResize_x_1.setObjectName("label_imgResize_x_1")
        self.gridLayout_imageResizeOptions.addWidget(self.label_imgResize_x_1, 0, 3, 1, 1)
        self.radioButton_imgResize_interpolate = QtWidgets.QRadioButton(Form_imageResize)
        self.radioButton_imgResize_interpolate.setObjectName("radioButton_imgResize_interpolate")
        self.gridLayout_imageResizeOptions.addWidget(self.radioButton_imgResize_interpolate, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_imageResizeOptions, 1, 0, 1, 1)
        self.label_imgResize_info = QtWidgets.QLabel(Form_imageResize)
        self.label_imgResize_info.setObjectName("label_imgResize_info")
        self.gridLayout_3.addWidget(self.label_imgResize_info, 0, 0, 1, 1)

        self.retranslateUi(Form_imageResize)
        self.radioButton_imgResize_cropPad.toggled['bool'].connect(self.spinBox_ingResize_h_1.setEnabled)
        #self.radioButton_imgResize_cropPad.toggled['bool'].connect(self.spinBox_ingResize_w_1.setEnabled)
        self.radioButton_imgResize_interpolate.toggled['bool'].connect(self.spinBox_ingResize_h_2.setEnabled)
        #self.radioButton_imgResize_interpolate.toggled['bool'].connect(self.spinBox_ingResize_w_2.setEnabled)
        self.radioButton_imgResize_interpolate.toggled['bool'].connect(self.comboBox_resizeMethod.setEnabled)
        self.radioButton_imgResize_cropPad.toggled['bool'].connect(self.pushButton_imgResize_ok.setEnabled)
        self.radioButton_imgResize_interpolate.toggled['bool'].connect(self.pushButton_imgResize_ok.setEnabled)
        self.spinBox_ingResize_h_1.valueChanged['int'].connect(self.spinBox_ingResize_h_2.setValue)
        self.spinBox_ingResize_h_1.valueChanged['int'].connect(self.spinBox_ingResize_w_1.setValue)
        self.spinBox_ingResize_h_1.valueChanged['int'].connect(self.spinBox_ingResize_w_2.setValue)
        self.spinBox_ingResize_h_2.valueChanged['int'].connect(self.spinBox_ingResize_w_1.setValue)
        self.spinBox_ingResize_h_2.valueChanged['int'].connect(self.spinBox_ingResize_w_2.setValue)
        self.spinBox_ingResize_h_2.valueChanged['int'].connect(self.spinBox_ingResize_h_1.setValue)

        QtCore.QMetaObject.connectSlotsByName(Form_imageResize)

    def retranslateUi(self, Form_imageResize):
        _translate = QtCore.QCoreApplication.translate
        Form_imageResize.setWindowTitle(_translate("Form_imageResize", "Import assistant for unequally sized images"))
        self.label_imgResize_x_3.setText(_translate("Form_imageResize", "x"))
        self.label_imgResize_height.setText(_translate("Form_imageResize", "Height"))
        self.pushButton_imgResize_ok.setText(_translate("Form_imageResize", "OK"))
        self.comboBox_resizeMethod.setItemText(0, _translate("Form_imageResize", "Nearest"))
        self.comboBox_resizeMethod.setItemText(1, _translate("Form_imageResize", "Linear"))
        self.comboBox_resizeMethod.setItemText(2, _translate("Form_imageResize", "Area"))
        self.comboBox_resizeMethod.setItemText(3, _translate("Form_imageResize", "Cubic"))
        self.comboBox_resizeMethod.setItemText(4, _translate("Form_imageResize", "Lanczos"))
        self.pushButton_imgResize_cancel.setText(_translate("Form_imageResize", "Cancel"))
        self.radioButton_imgResize_cropPad.setToolTip(_translate("Form_imageResize", "Images are resized by center cropping and/or padding."))
        self.radioButton_imgResize_cropPad.setText(_translate("Form_imageResize", "Crop/pad"))
        self.label_imgResize_x_2.setText(_translate("Form_imageResize", "x"))
        self.label_imgResize_width.setText(_translate("Form_imageResize", "Width"))
        self.label_imgResize_method.setText(_translate("Form_imageResize", "Method"))
        self.label_imgResize_x_1.setText(_translate("Form_imageResize", "x"))
        self.radioButton_imgResize_interpolate.setToolTip(_translate("Form_imageResize", "Images are resized by interpolation"))
        self.radioButton_imgResize_interpolate.setText(_translate("Form_imageResize", "Resize (interp.)"))
        self.label_imgResize_info.setText(_translate("Form_imageResize", "Detected unequal image sizes. Select a method to equalize image sizes:"))


























#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    Form = QtWidgets.QWidget()
#    ui = popup_lossweights()
#    ui.setupUi(Form)
#    Form.show()
#    sys.exit(app.exec_())

