# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.vaccinLabel = QtWidgets.QLabel(self.centralwidget)
        self.vaccinLabel.setObjectName("vaccinLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vaccinLabel)
        self.vaccinSelector = QtWidgets.QComboBox(self.centralwidget)
        self.vaccinSelector.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.vaccinSelector.setObjectName("vaccinSelector")
        self.vaccinSelector.addItem("")
        self.vaccinSelector.addItem("")
        self.vaccinSelector.addItem("")
        self.vaccinSelector.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.vaccinSelector)
        self.labelLetter = QtWidgets.QLabel(self.centralwidget)
        self.labelLetter.setObjectName("labelLetter")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelLetter)
        self.dateLetter = QtWidgets.QDateEdit(self.centralwidget)
        self.dateLetter.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLetter.setCalendarPopup(True)
        self.dateLetter.setObjectName("dateLetter")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateLetter)
        self.dose1Known = QtWidgets.QCheckBox(self.centralwidget)
        self.dose1Known.setChecked(False)
        self.dose1Known.setObjectName("dose1Known")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.dose1Known)
        self.labelDose1Known = QtWidgets.QLabel(self.centralwidget)
        self.labelDose1Known.setEnabled(False)
        self.labelDose1Known.setObjectName("labelDose1Known")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelDose1Known)
        self.dateDose1Known = QtWidgets.QDateEdit(self.centralwidget)
        self.dateDose1Known.setEnabled(False)
        self.dateDose1Known.setAlignment(QtCore.Qt.AlignCenter)
        self.dateDose1Known.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateDose1Known.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateDose1Known.setCalendarPopup(True)
        self.dateDose1Known.setObjectName("dateDose1Known")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dateDose1Known)
        self.calcbutton = QtWidgets.QPushButton(self.centralwidget)
        self.calcbutton.setCheckable(False)
        self.calcbutton.setObjectName("calcbutton")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.calcbutton)
        self.labelDose1 = QtWidgets.QLabel(self.centralwidget)
        self.labelDose1.setObjectName("labelDose1")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.labelDose1)
        self.dateDose1 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateDose1.setEnabled(True)
        self.dateDose1.setAcceptDrops(False)
        self.dateDose1.setWrapping(False)
        self.dateDose1.setFrame(True)
        self.dateDose1.setAlignment(QtCore.Qt.AlignCenter)
        self.dateDose1.setReadOnly(True)
        self.dateDose1.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateDose1.setProperty("showGroupSeparator", False)
        self.dateDose1.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateDose1.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.dateDose1.setCalendarPopup(False)
        self.dateDose1.setCurrentSectionIndex(0)
        self.dateDose1.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateDose1.setObjectName("dateDose1")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.dateDose1)
        self.labelDose2 = QtWidgets.QLabel(self.centralwidget)
        self.labelDose2.setObjectName("labelDose2")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.labelDose2)
        self.dateDose2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateDose2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateDose2.setReadOnly(True)
        self.dateDose2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateDose2.setObjectName("dateDose2")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.dateDose2)
        self.labelProtected = QtWidgets.QLabel(self.centralwidget)
        self.labelProtected.setObjectName("labelProtected")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.labelProtected)
        self.dateProtected = QtWidgets.QDateEdit(self.centralwidget)
        self.dateProtected.setAutoFillBackground(False)
        self.dateProtected.setAlignment(QtCore.Qt.AlignCenter)
        self.dateProtected.setReadOnly(True)
        self.dateProtected.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateProtected.setObjectName("dateProtected")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.dateProtected)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(21, QtWidgets.QFormLayout.SpanningRole, self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vaccine Date Calculator"))
        self.vaccinLabel.setText(_translate("MainWindow", "Vaccin"))
        self.vaccinSelector.setCurrentText(_translate("MainWindow", "Pfizer/BioNTech"))
        self.vaccinSelector.setItemText(0, _translate("MainWindow", "Pfizer/BioNTech"))
        self.vaccinSelector.setItemText(1, _translate("MainWindow", "J&J"))
        self.vaccinSelector.setItemText(2, _translate("MainWindow", "Moderna"))
        self.vaccinSelector.setItemText(3, _translate("MainWindow", "AstraZeneca/Oxford"))
        self.labelLetter.setText(_translate("MainWindow", "Datum oproepingsbrief *"))
        self.dose1Known.setText(_translate("MainWindow", "datum 1e dosis bekend"))
        self.labelDose1Known.setText(_translate("MainWindow", "Datum 1e dosis"))
        self.calcbutton.setText(_translate("MainWindow", "Bereken data"))
        self.labelDose1.setText(_translate("MainWindow", "1e dosis"))
        self.labelDose2.setText(_translate("MainWindow", "2e dosis"))
        self.labelProtected.setText(_translate("MainWindow", "volledige bescherming"))
        self.label.setText(_translate("MainWindow", "* programma berekent datum 1e dosis als 2 weken na datum oproepingsbrief"))
