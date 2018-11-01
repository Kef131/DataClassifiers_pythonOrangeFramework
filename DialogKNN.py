# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogKNN.ui'
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

class Ui_DialogKNN(object):
    def setupUi(self, DialogKNN):
        DialogKNN.setObjectName(_fromUtf8("DialogKNN"))
        DialogKNN.resize(387, 248)
        self.frame = QtGui.QFrame(DialogKNN)
        self.frame.setGeometry(QtCore.QRect(20, 10, 341, 221))
        self.frame.setStyleSheet(_fromUtf8("#frame {\n"
"border: 2px solid gray;\n"
"background: white;\n"
"\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.buttonBox = QtGui.QDialogButtonBox(self.frame)
        self.buttonBox.setGeometry(QtCore.QRect(90, 170, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 321, 131))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox_numVecinos = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_numVecinos.setMinimum(1)
        self.spinBox_numVecinos.setObjectName(_fromUtf8("spinBox_numVecinos"))
        self.horizontalLayout.addWidget(self.spinBox_numVecinos)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_metrica = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox_metrica.setObjectName(_fromUtf8("comboBox_metrica"))
        self.comboBox_metrica.addItem(_fromUtf8(""))
        self.comboBox_metrica.addItem(_fromUtf8(""))
        self.comboBox_metrica.addItem(_fromUtf8(""))
        self.comboBox_metrica.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboBox_metrica)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox_peso = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox_peso.setObjectName(_fromUtf8("comboBox_peso"))
        self.comboBox_peso.addItem(_fromUtf8(""))
        self.comboBox_peso.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_peso)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DialogKNN)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogKNN.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogKNN.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogKNN)

    def retranslateUi(self, DialogKNN):
        DialogKNN.setWindowTitle(_translate("DialogKNN", "Parametros KNN", None))
        self.label.setText(_translate("DialogKNN", "Parametros KNN", None))
        self.label_2.setText(_translate("DialogKNN", "Numero de Vecinos:", None))
        self.label_3.setText(_translate("DialogKNN", "Metrica", None))
        self.comboBox_metrica.setItemText(0, _translate("DialogKNN", "euclidean", None))
        self.comboBox_metrica.setItemText(1, _translate("DialogKNN", "manhattan", None))
        self.comboBox_metrica.setItemText(2, _translate("DialogKNN", "maximal", None))
        self.comboBox_metrica.setItemText(3, _translate("DialogKNN", "mahalanobis", None))
        self.label_4.setText(_translate("DialogKNN", "Peso", None))
        self.comboBox_peso.setItemText(0, _translate("DialogKNN", "uniform", None))
        self.comboBox_peso.setItemText(1, _translate("DialogKNN", "distance", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogKNN = QtGui.QDialog()
    ui = Ui_DialogKNN()
    ui.setupUi(DialogKNN)
    DialogKNN.show()
    sys.exit(app.exec_())

