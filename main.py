# -*- coding: utf-8 -*-
from PyQt4 import QtGui, uic, QtCore  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
import Orange
import numpy as np
import olveraProject_Kef
import random
import pandas as pd
import matplotlib.pyplot as plt
import itertools

class ClasificadorApp(QtGui.QMainWindow, olveraProject_Kef.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        self.fileTraining_btn.clicked.connect(self.openFileTraining)  
        self.fileTest_btn.clicked.connect(self.openFileTest) 
        self.btn_setParam.clicked.connect(self.setParameters) 
        self.label_PARAM.hide()
        self.tab_knn.setEnabled(False)
        self.chooseClass_btn.clicked.connect(self.createLearner)
        self.btn_setParam.setEnabled(False)
        self.connect(self.fileTraining_btn, QtCore.SIGNAL("clicked()"), self.checkSteps)
        self.connect(self.fileTest_btn, QtCore.SIGNAL("clicked()"), self.checkSteps)
        self.btn_setParam.clicked.connect(self.setParameters)
        self.btn_train.clicked.connect(self.Training)
        self.btn_test.setEnabled(False)
        self._4step.setEnabled(False)
        self.fileTraining =""
        self.fileTest =""
        self.btn_test.clicked.connect(self.Testing)
        self.btn_cross.clicked.connect(self.Cross)
        
        self.btn_scatter.clicked.connect(self.Scatter)
        self.btn_matrix.clicked.connect(self.confusionMat)
        self.matplotW.hide()
        
    def Scatter(self):
        data = Orange.data.Table.from_file(self.fileTraining)
        cm=matrixConf
        plt.imshow(matrixConf,interpolation='nearest',cmap=plt.cm.Blues) 
        plt.colorbar()
        tick_marks = np.arange(len(data.domain.class_var.values))
        plt.xticks(tick_marks,data.domain.class_var.values, rotation=45)
        plt.yticks(tick_marks,data.domain.class_var.values)
        colormap = np.array(['blue', 'green', 'black'])
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i][j], '.1f'), horizontalalignment="center",   color="black") 
            if matrixConf[i][j]!=0:
                ran=matrixConf[i][j]
                for a in range(ran):
                    rand=random.uniform(i-.4,i+.4)
                    rand1=random.uniform(j-.4,j+.4)
                    if i==j:
                        plt.scatter(rand, rand1,c=colormap[0])
                    else:
                        plt.scatter(rand, rand1,c=colormap[1]) 
        plt.tight_layout()
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        plt.show()
        
    def grafica3(self):
        data = Orange.data.Table("iris")
        cm=matrixConf
        plt.imshow(matrixConf,interpolation='nearest',cmap=plt.cm.Oranges) # imshow
        #plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(data.domain.class_var.values))
        plt.xticks(tick_marks,data.domain.class_var.values, rotation=45)
        plt.yticks(tick_marks,data.domain.class_var.values)
        colormap = np.array(['orange', 'red', 'black'])
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i][j], '.1f'),
                horizontalalignment="center",
                color="black") #if format(cm[i][j],'.1f') > thresh else "black"
            if matrixConf[i][j]!=0:
                ran=matrixConf[i][j]
                print(ran)
                for a in range(ran):
                    rand=random.uniform(i-.4,i+.4)
                    rand1=random.uniform(j-.4,j+.4)
                    if i==j:
                        plt.scatter(rand, rand1,c=colormap[0])
                    else:
                        plt.scatter(rand, rand1,c=colormap[1]) 
        plt.tight_layout()
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        plt.show()
        
    def grafica(self):
        lr = linear_model.LinearRegression()
        boston = datasets.load_boston()
        y = boston.target
        
        # cross_val_predict returns an array of the same size as `y` where each entry
        # is a prediction obtained by cross validation:
        predicted = cross_val_predict(lr, boston.data, y, cv=10)
        
        fig, ax = plt.subplots()
        ax.scatter(y, predicted)
        ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
        ax.set_xlabel('Measured')
        ax.set_ylabel('Predicted')
        plt.show()
        
    def confusionMat(self):
        table 	= self.tableWidget
        data = Orange.data.Table.from_file(self.fileTraining)
        
        table.setRowCount(len(data.domain.class_var.values))
        table.setColumnCount(len(data.domain.class_var.values))
        
        knnLearner = Orange.classification.knn.KNNLearner(n_neighbors=self.spinBox__KNN_numVecinos.value(), weights=str(self.comboBox_KNN_peso.currentText()), algorithm=str(self.comboBox_KNN_algo.currentText()),  metric=str(self.comboBox_KNN_metrica.currentText()))
        classifiers=knnLearner(data)
        y_actu = pd.Series(data.Y, name='Actual')
        y_pred = pd.Series(classifiers(data), name='Predicted')
        
        table.setHorizontalHeaderLabels(data.domain.class_var.values)
        table.setVerticalHeaderLabels(data.domain.class_var.values)
  
        # set data
        for i in range(len(data.domain.class_var.values)):
            for j in range(len(data.domain.class_var.values)):
                table.setItem(i,j, QtGui.QTableWidgetItem(str(matrixConf[j][i])))

        
    def openFileTraining(self,MainWindow):       
        
        self.fileTraining = QtGui.QFileDialog.getOpenFileName(self,"Choose your training set")
        
       
        if self.fileTraining: # if user didn't pick a directory don't continue
            tableTraining = Orange.data.Table.from_file(self.fileTraining)  
            if tableTraining:
                self.fileOpen_lbl.setText("Training Set File Loaded")
    
    def openFileTest(self,MainWindow):       
        self.fileTest = QtGui.QFileDialog.getOpenFileName(self,"Choose your test set")
        
       
        if self.fileTest: # if user didn't pick a directory don't continue
            tableTest = Orange.data.Table.from_file(self.fileTest)  
            if tableTest:
                self.fileOpen_lbl_2.setText("Test Set File Loaded" )
    
    def createLearner(self):
        
        if(self.radio_knn.isChecked() ==True):
            self.tab_knn.setEnabled(True)
            self.label_classifier.setText("KNN Loaded")
            self.btn_setParam.setEnabled(True)
        elif(self.radio_ctree.isChecked() ==True):
            print("hola")

            print("adios")
            self.label_classifier.setText("SimpleTreeLearner Loaded")
   
    def isBlank(myString):
        if myString and myString.strip():
            #myString is not None AND myString is not empty or blank
            return False
        #myString is None OR myString is empty or blank
        return True
    
    def setParameters(self):
         
         if(self.radio_knn.isChecked() ==True and self.fileTraining != "" ):
            self._4step.setEnabled(True)
            self.label_PARAM.show()
         else:
            self.fileOpen_lbl.setText("ADD TRAINING SET")

        
    def Training(self):
       
            tableTraining = Orange.data.Table.from_file(self.fileTraining)
            knnLearner = Orange.classification.knn.KNNLearner(n_neighbors=self.spinBox__KNN_numVecinos.value(), weights=str(self.comboBox_KNN_peso.currentText()), algorithm=str(self.comboBox_KNN_algo.currentText()),  metric=str(self.comboBox_KNN_metrica.currentText()))
            
            res = Orange.evaluation.TestOnTrainingData(tableTraining, [knnLearner])
            res1 = res.predicted
            res2 = res.actual
            global matrixConf
            matrixConf = pd.crosstab(res2, res1[0])
            
            self.label_AUC.setText("Accuracy: %.3f" % Orange.evaluation.scoring.AUC(res)[0])
            self.label_CA.setText("CA: %.3f" % Orange.evaluation.scoring.CA(res)[0])
            self.label_F1.setText("F1: %.3f" % Orange.evaluation.scoring.F1(res)[0])
            self.label_PRECISION.setText("Precision: %.3f" % Orange.evaluation.scoring.Precision(res)[0])
            self.label_RECALL.setText("Recall: %.3f" % Orange.evaluation.scoring.Recall(res)[0])

            self.btn_test.setEnabled(True)
     
            
    def Testing(self):
         if( self.fileTest != ""):   
            tableTraining = Orange.data.Table.from_file(self.fileTraining)
            tableTest = Orange.data.Table.from_file(self.fileTest)
            knnLearner = Orange.classification.knn.KNNLearner(n_neighbors=self.spinBox__KNN_numVecinos.value(), weights=str(self.comboBox_KNN_peso.currentText()), algorithm=str(self.comboBox_KNN_algo.currentText()),  metric=str(self.comboBox_KNN_metrica.currentText()))
         
            res = Orange.evaluation.TestOnTestData (tableTraining,tableTest ,[knnLearner])
            res1 = res.predicted
            res2 = res.actual
            global matrixConf
            matrixConf = pd.crosstab(res2, res1[0])
            self.label_AUC.setText("Accuracy: %.3f" % Orange.evaluation.scoring.AUC(res)[0])
            self.label_CA.setText("CA: %.3f" % Orange.evaluation.scoring.CA(res)[0])
            self.label_F1.setText("F1: %.3f" % Orange.evaluation.scoring.F1(res)[0])
            self.label_PRECISION.setText("Precision: %.3f" % Orange.evaluation.scoring.Precision(res)[0])
            self.label_RECALL.setText("Recall: %.3f" % Orange.evaluation.scoring.Recall(res)[0])
         else:
            self.fileOpen_lbl_2.setText("ADD TEST SET")
    def Cross(self):
  
            tableTraining = Orange.data.Table.from_file(self.fileTraining)
            knnLearner = Orange.classification.knn.KNNLearner(n_neighbors=self.spinBox__KNN_numVecinos.value(), weights=str(self.comboBox_KNN_peso.currentText()), algorithm=str(self.comboBox_KNN_algo.currentText()),  metric=str(self.comboBox_KNN_metrica.currentText()))
            res = Orange.evaluation.CrossValidation(tableTraining, [knnLearner], k=self.spin_folds.value())
            res1 = res.predicted
            res2 = res.actual
            global matrixConf
            matrixConf = pd.crosstab(res2, res1[0])
            self.label_AUC.setText("Accuracy: %.3f" % Orange.evaluation.scoring.AUC(res)[0])
            self.label_CA.setText("CA: %.3f" % Orange.evaluation.scoring.CA(res)[0])
            self.label_F1.setText("F1: %.3f" % Orange.evaluation.scoring.F1(res)[0])
            self.label_PRECISION.setText("Precision: %.3f" % Orange.evaluation.scoring.Precision(res)[0])
            self.label_RECALL.setText("Recall: %.3f" % Orange.evaluation.scoring.Recall(res))

     
    def checkSteps(self):
        if (self.fileOpen_lbl.text() == "Training Set File Loaded" and 
            self.fileOpen_lbl_2.text() == "Test Set File Loaded" ):
            self._2step.setEnabled(True)
            self.label_step2.setEnabled(True)
            print("Step 2 Enabled")
    
 
        
    def grafica2(self):
        print("HOLA")
        plt.figure(figsize=(14,7))

  
        x = np.arange(0,5,0.5)
        y = np.sin(x)
        self.matplotW.axes.plot(x, y)
        self.matplotW.draw()

 
        print("adios")    
                


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ClasificadorApp()  # We set the form to be our ClasificadorApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app
    

if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
    

