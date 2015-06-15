# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qemu_image_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_QemuImageWizard:

    def setupUi(self, QemuImageWizard):
        QemuImageWizard.setObjectName("QemuImageWizard")
        QemuImageWizard.resize(420, 300)
        QemuImageWizard.setModal(True)
        QemuImageWizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        self.uiBinaryWizardPage = QtWidgets.QWizardPage()
        self.uiBinaryWizardPage.setObjectName("uiBinaryWizardPage")
        self.formLayout_2 = QtWidgets.QFormLayout(self.uiBinaryWizardPage)
        self.formLayout_2.setObjectName("formLayout_2")
        self.uiBinaryLabel = QtWidgets.QLabel(self.uiBinaryWizardPage)
        self.uiBinaryLabel.setObjectName("uiBinaryLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiBinaryLabel)
        self.uiBinaryComboBox = QtWidgets.QComboBox(self.uiBinaryWizardPage)
        self.uiBinaryComboBox.setObjectName("uiBinaryComboBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiBinaryComboBox)
        self.uiFormatLabel = QtWidgets.QLabel(self.uiBinaryWizardPage)
        self.uiFormatLabel.setObjectName("uiFormatLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiFormatLabel)
        self.uiFormatFrame = QtWidgets.QFrame(self.uiBinaryWizardPage)
        self.uiFormatFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uiFormatFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uiFormatFrame.setObjectName("uiFormatFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiFormatFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiFormatQcow2Radio = QtWidgets.QRadioButton(self.uiFormatFrame)
        self.uiFormatQcow2Radio.setText("Qcow2")
        self.uiFormatQcow2Radio.setObjectName("uiFormatQcow2Radio")
        self.uiFormatRadios = QtWidgets.QButtonGroup(QemuImageWizard)
        self.uiFormatRadios.setObjectName("uiFormatRadios")
        self.uiFormatRadios.addButton(self.uiFormatQcow2Radio)
        self.verticalLayout.addWidget(self.uiFormatQcow2Radio)
        self.uiFormatQcowRadio = QtWidgets.QRadioButton(self.uiFormatFrame)
        self.uiFormatQcowRadio.setText("Qcow")
        self.uiFormatQcowRadio.setObjectName("uiFormatQcowRadio")
        self.uiFormatRadios.addButton(self.uiFormatQcowRadio)
        self.verticalLayout.addWidget(self.uiFormatQcowRadio)
        self.uiFormatVhdRadio = QtWidgets.QRadioButton(self.uiFormatFrame)
        self.uiFormatVhdRadio.setText("VHD")
        self.uiFormatVhdRadio.setObjectName("uiFormatVhdRadio")
        self.uiFormatRadios.addButton(self.uiFormatVhdRadio)
        self.verticalLayout.addWidget(self.uiFormatVhdRadio)
        self.uiFormatVdiRadio = QtWidgets.QRadioButton(self.uiFormatFrame)
        self.uiFormatVdiRadio.setText("VDI")
        self.uiFormatVdiRadio.setObjectName("uiFormatVdiRadio")
        self.uiFormatRadios.addButton(self.uiFormatVdiRadio)
        self.verticalLayout.addWidget(self.uiFormatVdiRadio)
        self.uiFormatVmdkRadio = QtWidgets.QRadioButton(self.uiFormatFrame)
        self.uiFormatVmdkRadio.setText("VMDK")
        self.uiFormatVmdkRadio.setObjectName("uiFormatVmdkRadio")
        self.uiFormatRadios.addButton(self.uiFormatVmdkRadio)
        self.verticalLayout.addWidget(self.uiFormatVmdkRadio)
        self.uiFormatRawRadio = QtWidgets.QRadioButton(self.uiFormatFrame)
        self.uiFormatRawRadio.setObjectName("uiFormatRawRadio")
        self.uiFormatRadios.addButton(self.uiFormatRawRadio)
        self.verticalLayout.addWidget(self.uiFormatRawRadio)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiFormatFrame)
        QemuImageWizard.addPage(self.uiBinaryWizardPage)
        self.uiQcow2OptionsWizardPage = QtWidgets.QWizardPage()
        self.uiQcow2OptionsWizardPage.setObjectName("uiQcow2OptionsWizardPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.uiQcow2OptionsWizardPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiSizeOptionsGroupBox = QtWidgets.QGroupBox(self.uiQcow2OptionsWizardPage)
        self.uiSizeOptionsGroupBox.setObjectName("uiSizeOptionsGroupBox")
        self.uiQcow2SizeOptionsLayout = QtWidgets.QFormLayout(self.uiSizeOptionsGroupBox)
        self.uiQcow2SizeOptionsLayout.setObjectName("uiQcow2SizeOptionsLayout")
        self.uiPreallocationLabel = QtWidgets.QLabel(self.uiSizeOptionsGroupBox)
        self.uiPreallocationLabel.setObjectName("uiPreallocationLabel")
        self.uiQcow2SizeOptionsLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiPreallocationLabel)
        self.uiQcow2PreallocationFrame = QtWidgets.QFrame(self.uiSizeOptionsGroupBox)
        self.uiQcow2PreallocationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uiQcow2PreallocationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uiQcow2PreallocationFrame.setObjectName("uiQcow2PreallocationFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.uiQcow2PreallocationFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiQcow2PreallocationOffRadio = QtWidgets.QRadioButton(self.uiQcow2PreallocationFrame)
        self.uiQcow2PreallocationOffRadio.setObjectName("uiQcow2PreallocationOffRadio")
        self.uiQcow2PreallocationRadios = QtWidgets.QButtonGroup(QemuImageWizard)
        self.uiQcow2PreallocationRadios.setObjectName("uiQcow2PreallocationRadios")
        self.uiQcow2PreallocationRadios.addButton(self.uiQcow2PreallocationOffRadio)
        self.horizontalLayout.addWidget(self.uiQcow2PreallocationOffRadio)
        self.uiQcow2PreallocationMetadataRadio = QtWidgets.QRadioButton(self.uiQcow2PreallocationFrame)
        self.uiQcow2PreallocationMetadataRadio.setObjectName("uiQcow2PreallocationMetadataRadio")
        self.uiQcow2PreallocationRadios.addButton(self.uiQcow2PreallocationMetadataRadio)
        self.horizontalLayout.addWidget(self.uiQcow2PreallocationMetadataRadio)
        self.uiQcow2PreallocationFallocRadio = QtWidgets.QRadioButton(self.uiQcow2PreallocationFrame)
        self.uiQcow2PreallocationFallocRadio.setObjectName("uiQcow2PreallocationFallocRadio")
        self.uiQcow2PreallocationRadios.addButton(self.uiQcow2PreallocationFallocRadio)
        self.horizontalLayout.addWidget(self.uiQcow2PreallocationFallocRadio)
        self.uiQcow2PreallocationFullRadio = QtWidgets.QRadioButton(self.uiQcow2PreallocationFrame)
        self.uiQcow2PreallocationFullRadio.setObjectName("uiQcow2PreallocationFullRadio")
        self.uiQcow2PreallocationRadios.addButton(self.uiQcow2PreallocationFullRadio)
        self.horizontalLayout.addWidget(self.uiQcow2PreallocationFullRadio)
        self.uiQcow2SizeOptionsLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiQcow2PreallocationFrame)
        self.uiClusterSizeLabel = QtWidgets.QLabel(self.uiSizeOptionsGroupBox)
        self.uiClusterSizeLabel.setObjectName("uiClusterSizeLabel")
        self.uiQcow2SizeOptionsLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiClusterSizeLabel)
        self.uiQcow2ClusterSizeComboBox = QtWidgets.QComboBox(self.uiSizeOptionsGroupBox)
        self.uiQcow2ClusterSizeComboBox.setObjectName("uiQcow2ClusterSizeComboBox")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2ClusterSizeComboBox.addItem("")
        self.uiQcow2SizeOptionsLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiQcow2ClusterSizeComboBox)
        self.verticalLayout_2.addWidget(self.uiSizeOptionsGroupBox)
        self.uiRefcountsGroupBox = QtWidgets.QGroupBox(self.uiQcow2OptionsWizardPage)
        self.uiRefcountsGroupBox.setObjectName("uiRefcountsGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.uiRefcountsGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiRefcountEntryFormLayout = QtWidgets.QFormLayout()
        self.uiRefcountEntryFormLayout.setObjectName("uiRefcountEntryFormLayout")
        self.uiRefcountEntrySizeLabel = QtWidgets.QLabel(self.uiRefcountsGroupBox)
        self.uiRefcountEntrySizeLabel.setObjectName("uiRefcountEntrySizeLabel")
        self.uiRefcountEntryFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiRefcountEntrySizeLabel)
        self.uiRefcountEntrySizeComboBox = QtWidgets.QComboBox(self.uiRefcountsGroupBox)
        self.uiRefcountEntrySizeComboBox.setObjectName("uiRefcountEntrySizeComboBox")
        self.uiRefcountEntrySizeComboBox.addItem("")
        self.uiRefcountEntrySizeComboBox.addItem("")
        self.uiRefcountEntrySizeComboBox.addItem("")
        self.uiRefcountEntrySizeComboBox.addItem("")
        self.uiRefcountEntrySizeComboBox.addItem("")
        self.uiRefcountEntrySizeComboBox.addItem("")
        self.uiRefcountEntrySizeComboBox.addItem("")
        self.uiRefcountEntrySizeComboBox.addItem("")
        self.uiRefcountEntryFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiRefcountEntrySizeComboBox)
        self.verticalLayout_3.addLayout(self.uiRefcountEntryFormLayout)
        self.uiLazyRefcountsCheckBox = QtWidgets.QCheckBox(self.uiRefcountsGroupBox)
        self.uiLazyRefcountsCheckBox.setTristate(False)
        self.uiLazyRefcountsCheckBox.setObjectName("uiLazyRefcountsCheckBox")
        self.verticalLayout_3.addWidget(self.uiLazyRefcountsCheckBox)
        self.verticalLayout_2.addWidget(self.uiRefcountsGroupBox)
        QemuImageWizard.addPage(self.uiQcow2OptionsWizardPage)
        self.uiVhdOptionsWizardPage = QtWidgets.QWizardPage()
        self.uiVhdOptionsWizardPage.setObjectName("uiVhdOptionsWizardPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.uiVhdOptionsWizardPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.uiVhdFileSizeModeGroupBox = QtWidgets.QGroupBox(self.uiVhdOptionsWizardPage)
        self.uiVhdFileSizeModeGroupBox.setObjectName("uiVhdFileSizeModeGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.uiVhdFileSizeModeGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiVhdFileSizeModeDynamicRadio = QtWidgets.QRadioButton(self.uiVhdFileSizeModeGroupBox)
        self.uiVhdFileSizeModeDynamicRadio.setObjectName("uiVhdFileSizeModeDynamicRadio")
        self.uiVhdSizeModeRadios = QtWidgets.QButtonGroup(QemuImageWizard)
        self.uiVhdSizeModeRadios.setObjectName("uiVhdSizeModeRadios")
        self.uiVhdSizeModeRadios.addButton(self.uiVhdFileSizeModeDynamicRadio)
        self.horizontalLayout_2.addWidget(self.uiVhdFileSizeModeDynamicRadio)
        self.uiVhdFileSizeModeFixedRadio = QtWidgets.QRadioButton(self.uiVhdFileSizeModeGroupBox)
        self.uiVhdFileSizeModeFixedRadio.setObjectName("uiVhdFileSizeModeFixedRadio")
        self.uiVhdSizeModeRadios.addButton(self.uiVhdFileSizeModeFixedRadio)
        self.horizontalLayout_2.addWidget(self.uiVhdFileSizeModeFixedRadio)
        self.verticalLayout_4.addWidget(self.uiVhdFileSizeModeGroupBox)
        QemuImageWizard.addPage(self.uiVhdOptionsWizardPage)
        self.uiVdiOptionsWizardPage = QtWidgets.QWizardPage()
        self.uiVdiOptionsWizardPage.setObjectName("uiVdiOptionsWizardPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.uiVdiOptionsWizardPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.uiVdiFileSizeModeGroupBox = QtWidgets.QGroupBox(self.uiVdiOptionsWizardPage)
        self.uiVdiFileSizeModeGroupBox.setObjectName("uiVdiFileSizeModeGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.uiVdiFileSizeModeGroupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiVdiFileSizeModeDynamicRadio = QtWidgets.QRadioButton(self.uiVdiFileSizeModeGroupBox)
        self.uiVdiFileSizeModeDynamicRadio.setObjectName("uiVdiFileSizeModeDynamicRadio")
        self.uiVdiSizeModeRadios = QtWidgets.QButtonGroup(QemuImageWizard)
        self.uiVdiSizeModeRadios.setObjectName("uiVdiSizeModeRadios")
        self.uiVdiSizeModeRadios.addButton(self.uiVdiFileSizeModeDynamicRadio)
        self.horizontalLayout_3.addWidget(self.uiVdiFileSizeModeDynamicRadio)
        self.uiVdiFileSizeModeFixedRadio = QtWidgets.QRadioButton(self.uiVdiFileSizeModeGroupBox)
        self.uiVdiFileSizeModeFixedRadio.setObjectName("uiVdiFileSizeModeFixedRadio")
        self.uiVdiSizeModeRadios.addButton(self.uiVdiFileSizeModeFixedRadio)
        self.horizontalLayout_3.addWidget(self.uiVdiFileSizeModeFixedRadio)
        self.verticalLayout_5.addWidget(self.uiVdiFileSizeModeGroupBox)
        QemuImageWizard.addPage(self.uiVdiOptionsWizardPage)
        self.uiVmdkOptionsWizardPage = QtWidgets.QWizardPage()
        self.uiVmdkOptionsWizardPage.setObjectName("uiVmdkOptionsWizardPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.uiVmdkOptionsWizardPage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.uiVmdkAdapterTypeGroupBox = QtWidgets.QGroupBox(self.uiVmdkOptionsWizardPage)
        self.uiVmdkAdapterTypeGroupBox.setObjectName("uiVmdkAdapterTypeGroupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.uiVmdkAdapterTypeGroupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiVmdkAdapterTypeIdeRadio = QtWidgets.QRadioButton(self.uiVmdkAdapterTypeGroupBox)
        self.uiVmdkAdapterTypeIdeRadio.setObjectName("uiVmdkAdapterTypeIdeRadio")
        self.uiVmdkAdapterRadios = QtWidgets.QButtonGroup(QemuImageWizard)
        self.uiVmdkAdapterRadios.setObjectName("uiVmdkAdapterRadios")
        self.uiVmdkAdapterRadios.addButton(self.uiVmdkAdapterTypeIdeRadio)
        self.horizontalLayout_4.addWidget(self.uiVmdkAdapterTypeIdeRadio)
        self.uiVmdkAdapterTypeLsiRadio = QtWidgets.QRadioButton(self.uiVmdkAdapterTypeGroupBox)
        self.uiVmdkAdapterTypeLsiRadio.setObjectName("uiVmdkAdapterTypeLsiRadio")
        self.uiVmdkAdapterRadios.addButton(self.uiVmdkAdapterTypeLsiRadio)
        self.horizontalLayout_4.addWidget(self.uiVmdkAdapterTypeLsiRadio)
        self.uiVmdkAdapterTypeBusRadio = QtWidgets.QRadioButton(self.uiVmdkAdapterTypeGroupBox)
        self.uiVmdkAdapterTypeBusRadio.setObjectName("uiVmdkAdapterTypeBusRadio")
        self.uiVmdkAdapterRadios.addButton(self.uiVmdkAdapterTypeBusRadio)
        self.horizontalLayout_4.addWidget(self.uiVmdkAdapterTypeBusRadio)
        self.uiVmdkAdapterTypeEsxRadio = QtWidgets.QRadioButton(self.uiVmdkAdapterTypeGroupBox)
        self.uiVmdkAdapterTypeEsxRadio.setObjectName("uiVmdkAdapterTypeEsxRadio")
        self.uiVmdkAdapterRadios.addButton(self.uiVmdkAdapterTypeEsxRadio)
        self.horizontalLayout_4.addWidget(self.uiVmdkAdapterTypeEsxRadio)
        self.verticalLayout_6.addWidget(self.uiVmdkAdapterTypeGroupBox)
        self.uiVmdkFileSizeModeGroupBox = QtWidgets.QGroupBox(self.uiVmdkOptionsWizardPage)
        self.uiVmdkFileSizeModeGroupBox.setObjectName("uiVmdkFileSizeModeGroupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.uiVmdkFileSizeModeGroupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiVmdkFileSizeModeSparseRadio = QtWidgets.QRadioButton(self.uiVmdkFileSizeModeGroupBox)
        self.uiVmdkFileSizeModeSparseRadio.setObjectName("uiVmdkFileSizeModeSparseRadio")
        self.uiVmdkSizeModeRadios = QtWidgets.QButtonGroup(QemuImageWizard)
        self.uiVmdkSizeModeRadios.setObjectName("uiVmdkSizeModeRadios")
        self.uiVmdkSizeModeRadios.addButton(self.uiVmdkFileSizeModeSparseRadio)
        self.horizontalLayout_5.addWidget(self.uiVmdkFileSizeModeSparseRadio)
        self.uiVmdkFileSizeModeFlatRadio = QtWidgets.QRadioButton(self.uiVmdkFileSizeModeGroupBox)
        self.uiVmdkFileSizeModeFlatRadio.setObjectName("uiVmdkFileSizeModeFlatRadio")
        self.uiVmdkSizeModeRadios.addButton(self.uiVmdkFileSizeModeFlatRadio)
        self.horizontalLayout_5.addWidget(self.uiVmdkFileSizeModeFlatRadio)
        self.verticalLayout_6.addWidget(self.uiVmdkFileSizeModeGroupBox)
        self.uiVmdkMiscGroupBox = QtWidgets.QGroupBox(self.uiVmdkOptionsWizardPage)
        self.uiVmdkMiscGroupBox.setObjectName("uiVmdkMiscGroupBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.uiVmdkMiscGroupBox)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.uiVmdkStreamOptimizedCheckBox = QtWidgets.QCheckBox(self.uiVmdkMiscGroupBox)
        self.uiVmdkStreamOptimizedCheckBox.setObjectName("uiVmdkStreamOptimizedCheckBox")
        self.horizontalLayout_6.addWidget(self.uiVmdkStreamOptimizedCheckBox)
        self.uiVmdkSplit2gCheckBox = QtWidgets.QCheckBox(self.uiVmdkMiscGroupBox)
        self.uiVmdkSplit2gCheckBox.setObjectName("uiVmdkSplit2gCheckBox")
        self.horizontalLayout_6.addWidget(self.uiVmdkSplit2gCheckBox)
        self.uiVmdkZeroedGrainCheckBox = QtWidgets.QCheckBox(self.uiVmdkMiscGroupBox)
        self.uiVmdkZeroedGrainCheckBox.setObjectName("uiVmdkZeroedGrainCheckBox")
        self.horizontalLayout_6.addWidget(self.uiVmdkZeroedGrainCheckBox)
        self.verticalLayout_6.addWidget(self.uiVmdkMiscGroupBox)
        QemuImageWizard.addPage(self.uiVmdkOptionsWizardPage)
        self.uiSizeAndLocationWizardPage = QtWidgets.QWizardPage()
        self.uiSizeAndLocationWizardPage.setObjectName("uiSizeAndLocationWizardPage")
        self.formLayout = QtWidgets.QFormLayout(self.uiSizeAndLocationWizardPage)
        self.formLayout.setObjectName("formLayout")
        self.uiLocationLabel = QtWidgets.QLabel(self.uiSizeAndLocationWizardPage)
        self.uiLocationLabel.setObjectName("uiLocationLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiLocationLabel)
        self.uiLocationFrame = QtWidgets.QFrame(self.uiSizeAndLocationWizardPage)
        self.uiLocationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uiLocationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uiLocationFrame.setObjectName("uiLocationFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.uiLocationFrame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiLocationLineEdit = QtWidgets.QLineEdit(self.uiLocationFrame)
        self.uiLocationLineEdit.setObjectName("uiLocationLineEdit")
        self.horizontalLayout_7.addWidget(self.uiLocationLineEdit)
        self.uiLocationBrowseToolButton = QtWidgets.QToolButton(self.uiLocationFrame)
        self.uiLocationBrowseToolButton.setObjectName("uiLocationBrowseToolButton")
        self.horizontalLayout_7.addWidget(self.uiLocationBrowseToolButton)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiLocationFrame)
        self.uiSizeLabel = QtWidgets.QLabel(self.uiSizeAndLocationWizardPage)
        self.uiSizeLabel.setObjectName("uiSizeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.uiSizeLabel)
        self.uiSizeFrame = QtWidgets.QFrame(self.uiSizeAndLocationWizardPage)
        self.uiSizeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uiSizeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uiSizeFrame.setObjectName("uiSizeFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.uiSizeFrame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uiSizeSlider = QtWidgets.QSlider(self.uiSizeFrame)
        self.uiSizeSlider.setMaximum(2000000)
        self.uiSizeSlider.setSingleStep(1000)
        self.uiSizeSlider.setPageStep(10000)
        self.uiSizeSlider.setProperty("value", 30000)
        self.uiSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.uiSizeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.uiSizeSlider.setTickInterval(100000)
        self.uiSizeSlider.setObjectName("uiSizeSlider")
        self.horizontalLayout_8.addWidget(self.uiSizeSlider)
        self.uiSizeSpinBox = QtWidgets.QSpinBox(self.uiSizeFrame)
        self.uiSizeSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.uiSizeSpinBox.setProperty("showGroupSeparator", True)
        self.uiSizeSpinBox.setMaximum(2000000)
        self.uiSizeSpinBox.setSingleStep(1000)
        self.uiSizeSpinBox.setProperty("value", 30000)
        self.uiSizeSpinBox.setObjectName("uiSizeSpinBox")
        self.horizontalLayout_8.addWidget(self.uiSizeSpinBox)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiSizeFrame)
        QemuImageWizard.addPage(self.uiSizeAndLocationWizardPage)

        self.retranslateUi(QemuImageWizard)
        self.uiSizeSlider.valueChanged['int'].connect(self.uiSizeSpinBox.setValue)
        self.uiSizeSpinBox.valueChanged['int'].connect(self.uiSizeSlider.setValue)
        self.uiVmdkStreamOptimizedCheckBox.toggled['bool'].connect(self.uiVmdkFileSizeModeFlatRadio.setDisabled)
        self.uiVmdkStreamOptimizedCheckBox.toggled['bool'].connect(self.uiVmdkSplit2gCheckBox.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(QemuImageWizard)

    def retranslateUi(self, QemuImageWizard):
        _translate = gns3.qt.translate
        QemuImageWizard.setWindowTitle(_translate("QemuImageWizard", "Qemu image creator"))
        self.uiBinaryWizardPage.setTitle(_translate("QemuImageWizard", "Binary and format"))
        self.uiBinaryWizardPage.setSubTitle(_translate("QemuImageWizard", "Please select a qemu-img binary, and the format for your new image."))
        self.uiBinaryLabel.setText(_translate("QemuImageWizard", "Qemu-img binary:"))
        self.uiFormatLabel.setText(_translate("QemuImageWizard", "Image format:"))
        self.uiFormatQcow2Radio.setToolTip(_translate("QemuImageWizard", "Qcow2 is the current Qemu format, supporting many special features."))
        self.uiFormatQcowRadio.setToolTip(_translate("QemuImageWizard", "Qcow is a legacy Qemu format that is also supported by VirtualBox."))
        self.uiFormatVhdRadio.setToolTip(_translate("QemuImageWizard", "VHD is the format used by Microsoft VirtualPC, and is also supported by Qemu and VirtualBox.\n"
                                                    "On Windows 7 and above, it can be mounted on the host PC."))
        self.uiFormatVdiRadio.setToolTip(_translate("QemuImageWizard", "VDI is the native format of VirtualBox"))
        self.uiFormatVmdkRadio.setToolTip(_translate("QemuImageWizard", "VMDK is the native format for VMware and is also supported by Qemu and VirtualBox."))
        self.uiFormatRawRadio.setToolTip(_translate("QemuImageWizard", "Raw image files represent the actual data on the image, with zero special features.\n"
                                                    "It can easily be converted to various other formats by various utilities, making it the most portable format."))
        self.uiFormatRawRadio.setText(_translate("QemuImageWizard", "Raw"))
        self.uiQcow2OptionsWizardPage.setTitle(_translate("QemuImageWizard", "Qcow2 options"))
        self.uiSizeOptionsGroupBox.setTitle(_translate("QemuImageWizard", "Size options"))
        self.uiPreallocationLabel.setText(_translate("QemuImageWizard", "Preallocation:"))
        self.uiQcow2PreallocationOffRadio.setToolTip(_translate("QemuImageWizard", "The file only takes as much space from the host as needed. The VM will still see the full capacity you specify."))
        self.uiQcow2PreallocationOffRadio.setText(_translate("QemuImageWizard", "off"))
        self.uiQcow2PreallocationMetadataRadio.setToolTip(_translate("QemuImageWizard", "Same as \"off\", but preallocates enough space to hold any potenial metadata for the HDD.\n"
                                                                     "This improves performance when the image file needs to grow."))
        self.uiQcow2PreallocationMetadataRadio.setText(_translate("QemuImageWizard", "metadata"))
        self.uiQcow2PreallocationFallocRadio.setToolTip(_translate("QemuImageWizard", "Same as \"full\", but uses C\'s posix_fallocate() if available on the host, instead of zero filling the file."))
        self.uiQcow2PreallocationFallocRadio.setText(_translate("QemuImageWizard", "falloc"))
        self.uiQcow2PreallocationFullRadio.setToolTip(_translate("QemuImageWizard", "The file will start off at the full size you specify.\n"
                                                                 "Free space will be zero filled."))
        self.uiQcow2PreallocationFullRadio.setText(_translate("QemuImageWizard", "full"))
        self.uiClusterSizeLabel.setText(_translate("QemuImageWizard", "Cluster size:"))
        self.uiQcow2ClusterSizeComboBox.setItemText(0, _translate("QemuImageWizard", "<default>"))
        self.uiQcow2ClusterSizeComboBox.setItemText(1, _translate("QemuImageWizard", "512"))
        self.uiQcow2ClusterSizeComboBox.setItemText(2, _translate("QemuImageWizard", "1k"))
        self.uiQcow2ClusterSizeComboBox.setItemText(3, _translate("QemuImageWizard", "2k"))
        self.uiQcow2ClusterSizeComboBox.setItemText(4, _translate("QemuImageWizard", "4k"))
        self.uiQcow2ClusterSizeComboBox.setItemText(5, _translate("QemuImageWizard", "8k"))
        self.uiQcow2ClusterSizeComboBox.setItemText(6, _translate("QemuImageWizard", "16k"))
        self.uiQcow2ClusterSizeComboBox.setItemText(7, _translate("QemuImageWizard", "32k"))
        self.uiQcow2ClusterSizeComboBox.setItemText(8, _translate("QemuImageWizard", "64k"))
        self.uiQcow2ClusterSizeComboBox.setItemText(9, _translate("QemuImageWizard", "128k"))
        self.uiQcow2ClusterSizeComboBox.setItemText(10, _translate("QemuImageWizard", "256k"))
        self.uiQcow2ClusterSizeComboBox.setItemText(11, _translate("QemuImageWizard", "512k"))
        self.uiQcow2ClusterSizeComboBox.setItemText(12, _translate("QemuImageWizard", "1024k"))
        self.uiQcow2ClusterSizeComboBox.setItemText(13, _translate("QemuImageWizard", "2048k"))
        self.uiRefcountsGroupBox.setTitle(_translate("QemuImageWizard", "Refcounts"))
        self.uiRefcountEntrySizeLabel.setText(_translate("QemuImageWizard", "Refcount entry size:"))
        self.uiRefcountEntrySizeComboBox.setItemText(0, _translate("QemuImageWizard", "<default>"))
        self.uiRefcountEntrySizeComboBox.setItemText(1, _translate("QemuImageWizard", "1"))
        self.uiRefcountEntrySizeComboBox.setItemText(2, _translate("QemuImageWizard", "2"))
        self.uiRefcountEntrySizeComboBox.setItemText(3, _translate("QemuImageWizard", "4"))
        self.uiRefcountEntrySizeComboBox.setItemText(4, _translate("QemuImageWizard", "8"))
        self.uiRefcountEntrySizeComboBox.setItemText(5, _translate("QemuImageWizard", "16"))
        self.uiRefcountEntrySizeComboBox.setItemText(6, _translate("QemuImageWizard", "32"))
        self.uiRefcountEntrySizeComboBox.setItemText(7, _translate("QemuImageWizard", "64"))
        self.uiLazyRefcountsCheckBox.setText(_translate("QemuImageWizard", "Lazy refcounts"))
        self.uiVhdOptionsWizardPage.setTitle(_translate("QemuImageWizard", "VHD options"))
        self.uiVhdFileSizeModeGroupBox.setTitle(_translate("QemuImageWizard", "Image file sizing mode"))
        self.uiVhdFileSizeModeDynamicRadio.setToolTip(_translate("QemuImageWizard", "The file only takes as much space from the host as needed. The VM will still see the full capacity you specify."))
        self.uiVhdFileSizeModeDynamicRadio.setText(_translate("QemuImageWizard", "Dynamic"))
        self.uiVhdFileSizeModeFixedRadio.setToolTip(_translate("QemuImageWizard", "The file will start off at the full size you specify."))
        self.uiVhdFileSizeModeFixedRadio.setText(_translate("QemuImageWizard", "Fixed"))
        self.uiVdiOptionsWizardPage.setTitle(_translate("QemuImageWizard", "VDI options"))
        self.uiVdiFileSizeModeGroupBox.setTitle(_translate("QemuImageWizard", "Image file sizing mode"))
        self.uiVdiFileSizeModeDynamicRadio.setToolTip(_translate("QemuImageWizard", "The file only takes as much space from the host as needed. The VM will still see the full capacity you specify."))
        self.uiVdiFileSizeModeDynamicRadio.setText(_translate("QemuImageWizard", "Dynamic"))
        self.uiVdiFileSizeModeFixedRadio.setToolTip(_translate("QemuImageWizard", "The file will start off at the full size you specify."))
        self.uiVdiFileSizeModeFixedRadio.setText(_translate("QemuImageWizard", "Fixed"))
        self.uiVmdkOptionsWizardPage.setTitle(_translate("QemuImageWizard", "VMDK options"))
        self.uiVmdkAdapterTypeGroupBox.setTitle(_translate("QemuImageWizard", "Adapter type"))
        self.uiVmdkAdapterTypeIdeRadio.setText(_translate("QemuImageWizard", "IDE"))
        self.uiVmdkAdapterTypeLsiRadio.setText(_translate("QemuImageWizard", "LSI Logic"))
        self.uiVmdkAdapterTypeBusRadio.setText(_translate("QemuImageWizard", "BusLogic"))
        self.uiVmdkAdapterTypeEsxRadio.setText(_translate("QemuImageWizard", "Legacy (ESX)"))
        self.uiVmdkFileSizeModeGroupBox.setTitle(_translate("QemuImageWizard", "Image file sizing mode"))
        self.uiVmdkFileSizeModeSparseRadio.setToolTip(_translate("QemuImageWizard", "The file only takes as much space from the host as needed. The VM will still see the full capacity you specify."))
        self.uiVmdkFileSizeModeSparseRadio.setText(_translate("QemuImageWizard", "Sparse"))
        self.uiVmdkFileSizeModeFlatRadio.setToolTip(_translate("QemuImageWizard", "The file will start off at the full size you specify."))
        self.uiVmdkFileSizeModeFlatRadio.setText(_translate("QemuImageWizard", "Flat"))
        self.uiVmdkMiscGroupBox.setTitle(_translate("QemuImageWizard", "Misc"))
        self.uiVmdkStreamOptimizedCheckBox.setText(_translate("QemuImageWizard", "Stream optimized"))
        self.uiVmdkSplit2gCheckBox.setText(_translate("QemuImageWizard", "Split every 2 GiB"))
        self.uiVmdkZeroedGrainCheckBox.setText(_translate("QemuImageWizard", "Zeroed grain"))
        self.uiSizeAndLocationWizardPage.setTitle(_translate("QemuImageWizard", "Size and location"))
        self.uiLocationLabel.setText(_translate("QemuImageWizard", "File location:"))
        self.uiLocationBrowseToolButton.setText(_translate("QemuImageWizard", "Browse"))
        self.uiSizeLabel.setText(_translate("QemuImageWizard", "Disk size:"))
        self.uiSizeSpinBox.setSuffix(_translate("QemuImageWizard", " MiB"))
