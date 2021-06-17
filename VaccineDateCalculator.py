# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from calcVacc import calcVacc
import datetime

texttodata = {
    "Pfizer/BioNTech": "pfizer",
    "J&J": "jj",
    "Moderna": "moderna",
    "AstraZeneca/Oxford": "az"
}
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Vaccin Date Calculator")
        MainWindow.resize(600, 384)
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
        self.dateLetter.setDateTime(QtCore.QDateTime(datetime.date.today(), QtCore.QTime(0, 0, 0)))
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateLetter)
        self.dateDose2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateDose2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateDose2.setReadOnly(True)
        self.dateDose2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateDose2.setObjectName("dateDose2")
        self.dateDose2.setDateTime(QtCore.QDateTime(datetime.date.today(), QtCore.QTime(0, 0, 0)))
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.dateDose2)
        self.Qvax = QtWidgets.QCheckBox(self.centralwidget)
        self.Qvax.setObjectName("Qvax")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Qvax)
        self.labelQvax = QtWidgets.QLabel(self.centralwidget)
        self.labelQvax.setEnabled(False)
        self.labelQvax.setObjectName("labelQvax")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelQvax)
        self.dateQvax = QtWidgets.QDateEdit(self.centralwidget)
        self.dateQvax.setEnabled(False)
        self.dateQvax.setAlignment(QtCore.Qt.AlignCenter)
        self.dateQvax.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateQvax.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateQvax.setCalendarPopup(True)
        self.dateQvax.setObjectName("dateQvax")
        self.dateQvax.setDateTime(QtCore.QDateTime(datetime.date.today(), QtCore.QTime(0, 0, 0)))
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dateQvax)
        self.calcbutton = QtWidgets.QPushButton(self.centralwidget)
        self.calcbutton.setObjectName("calcbutton")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.calcbutton)
        self.labelDose1 = QtWidgets.QLabel(self.centralwidget)
        self.labelDose1.setObjectName("labelDose1")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.labelDose1)
        self.labelDose2 = QtWidgets.QLabel(self.centralwidget)
        self.labelDose2.setObjectName("labelDose2")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.labelDose2)
        self.dateProtected = QtWidgets.QDateEdit(self.centralwidget)
        self.dateProtected.setAutoFillBackground(False)
        self.dateProtected.setAlignment(QtCore.Qt.AlignCenter)
        self.dateProtected.setReadOnly(True)
        self.dateProtected.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateProtected.setObjectName("dateProtected")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.dateProtected)
        self.dateDose1 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateDose1.setAcceptDrops(False)
        self.dateDose1.setWrapping(False)
        self.dateDose1.setAlignment(QtCore.Qt.AlignCenter)
        self.dateDose1.setReadOnly(True)
        self.dateDose1.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateDose1.setProperty("showGroupSeparator", False)
        self.dateDose1.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.dateDose1.setCalendarPopup(False)
        self.dateDose1.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateDose1.setObjectName("dateDose1")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.dateDose1)
        self.labelProtected = QtWidgets.QLabel(self.centralwidget)
        self.labelProtected.setObjectName("labelProtected")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.labelProtected)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.calcbutton.clicked.connect(self.on_click)
        self.Qvax.toggled.connect(self.on_select)
        self.vaccinSelector.textActivated.connect(self.on_JJ)
    
    def on_click(self):
        qv = self.Qvax.isChecked()
        if qv:
            dl = self.dateQvax.dateTime().toPyDateTime()
        else:
            dl = self.dateLetter.dateTime().toPyDateTime()
        keycheckup = self.vaccinSelector.currentText()
        vc = texttodata[keycheckup]
        dates=calcVacc(vc, dl, qv)
        self.dateDose1.setDateTime(QtCore.QDateTime(dates[0], QtCore.QTime(0, 0, 0)))
        self.dateDose2.setDateTime(QtCore.QDateTime(dates[1], QtCore.QTime(0, 0, 0)))
        self.dateProtected.setDateTime(QtCore.QDateTime(dates[2], QtCore.QTime(0, 0, 0)))

    def on_select(self):
        vinkje = self.Qvax.isChecked()
        self.dateQvax.setEnabled(vinkje)
        self.labelQvax.setEnabled(vinkje)
        self.dateLetter.setEnabled(not vinkje)
        self.labelLetter.setEnabled(not vinkje)
        if vinkje:
            self.dateDose1.hide()
            self.labelDose1.hide()
        else:
            self.dateDose1.show()
            self.labelDose1.show()

    def on_JJ(self):
        if self.vaccinSelector.currentText() == 'J&J':
            self.dateDose2.hide()
            self.labelDose2.hide()
        else:
            self.dateDose2.show()
            self.labelDose2.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Vaccine Date Calculator", "Vaccine Date Calculator"))
        self.vaccinLabel.setText(_translate("Vaccine Date Calculator", "Vaccin"))
        self.vaccinSelector.setCurrentText(_translate("Vaccine Date Calculator", "Pfizer/BioNTech"))
        self.vaccinSelector.setItemText(0, _translate("Vaccine Date Calculator", "Pfizer/BioNTech"))
        self.vaccinSelector.setItemText(1, _translate("Vaccine Date Calculator", "J&J"))
        self.vaccinSelector.setItemText(2, _translate("Vaccine Date Calculator", "Moderna"))
        self.vaccinSelector.setItemText(3, _translate("Vaccine Date Calculator", "AstraZeneca/Oxford"))
        self.labelLetter.setText(_translate("Vaccine Date Calculator", "Datum oproepingsbrief"))
        self.Qvax.setText(_translate("Vaccine Date Calculator", "QVax"))
        self.labelQvax.setText(_translate("Vaccine Date Calculator", "Datum QVax afspraak"))
        self.calcbutton.setText(_translate("Vaccine Date Calculator", "Bereken data"))
        self.labelDose1.setText(_translate("Vaccine Date Calculator", "1e dosis"))
        self.labelDose2.setText(_translate("Vaccine Date Calculator", "2e dosis"))
        self.labelProtected.setText(_translate("Vaccine Date Calculator", "volledige bescherming"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())