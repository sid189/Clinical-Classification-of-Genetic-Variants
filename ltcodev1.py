# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectgui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import pandas as pd
import numpy as np
import csv
import string
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

global fname,dname,final_str,mlcfname


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
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 731, 531))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 2)
	self.label2 = QtGui.QLabel(self.layoutWidget)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.gridLayout.addWidget(self.label2, 0, 3, 1, 4)
	self.label3 = QtGui.QLabel(self.layoutWidget)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.gridLayout.addWidget(self.label3, 1, 3, 1, 4)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 4)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 2)
        self.radioButton_2 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout.addWidget(self.radioButton_2, 4, 0, 1, 2)
        self.checkBox = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 5, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 11, 4, 1, 2)
        self.checkBox_2 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 5, 1, 1, 1)
	self.checkBox_3 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout.addWidget(self.checkBox_3, 5, 2, 1, 1)
	self.checkBox_4 = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout.addWidget(self.checkBox_4, 5, 3, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 9, 0, 1, 2)
        self.radioButton = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout.addWidget(self.radioButton, 3, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 2)
        self.pushButton_4 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 11, 0, 1, 2)
	self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 15, 0, 1, 4)
        
	MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Select File", None))
        self.pushButton.clicked.connect(self.getfiles)
        self.pushButton_2.setText(_translate("MainWindow", "Select Database", None))
        self.pushButton_2.clicked.connect(self.getdb)
        self.label.setText(_translate("MainWindow", "Would you like to select specific fields?", None))
	self.label2.setText(_translate("MainWindow", "No File Selected", None))
	self.label3.setText(_translate("MainWindow", "No File Selected", None))
	self.label_5.setText(_translate("MainWindow", "No File Selected", None))
        self.radioButton_2.setText(_translate("MainWindow", "No", None))
        self.checkBox.setText(_translate("MainWindow", "CLNDN", None))
        #self.checkBox.stateChanged.connect(self.f1)
        self.pushButton_5.setText(_translate("MainWindow", "Find Result", None))
	self.pushButton_5.clicked.connect(self.runml)
        self.checkBox_2.setText(_translate("MainWindow", "CLNSIG", None))
	self.checkBox_3.setText(_translate("MainWindow", "RS", None))
	self.checkBox_4.setText(_translate("MainWindow", "GENEINFO", None))
        #self.checkBox_2.stateChanged.connect(self.f2)
        self.pushButton_3.setText(_translate("MainWindow", "Search", None))
	self.pushButton_3.clicked.connect(self.preprocess)
        self.radioButton.setText(_translate("MainWindow", "Yes", None))
        self.radioButton.setChecked(True)
        
        self.label_2.setText(_translate("MainWindow", "Experimental Section", None))
        self.pushButton_4.setText(_translate("MainWindow", "Input File", None))
	self.pushButton_4.clicked.connect(self.mlcfile)
        self.radioButton.toggled.connect(self.refresh_button_state)
        self.radioButton_2.toggled.connect(self.refresh_button_state)
        self.refresh_button_state()
	        


    def getfiles(self):
      dlg = QFileDialog()
      dlg.setFileMode(QFileDialog.AnyFile)
      dlg.setFilter("Text files (*.vcf *.bam)")
      filenames = QStringList()
      
      if dlg.exec_():
      	filenames = dlg.selectedFiles()
      	self.fname = str(filenames[0])
	self.label2.setText(self.fname)
	'''tofi=self.fname[-3:]
	#print tofi
	if tofi=="bam":
		print "bam selected"'''
	#self.preprocess()
      	#dbname = input("\n\nEnter reference database name: ")
      	'''f = open(filenames[0], 'r')
      	
      	with f:
      		data = f.read()
      		print(data)'''
      	
    def getdb(self, fname):
       dlg = QFileDialog()
       dlg.setFileMode(QFileDialog.AnyFile)
       dlg.setFilter("Text files (*.vcf)")
       dbname = QStringList() 
       print "This is: ",self.fname
       
       if dlg.exec_():
      	dbname = dlg.selectedFiles()
        self.dname = str(dbname[0])
	self.label3.setText(self.dname)
        #self.annotate(self.fname,dname)

    def mlcfile(self):
      dlg = QFileDialog()
      dlg.setFileMode(QFileDialog.AnyFile)
      dlg.setFilter("Comma separated (*.csv)")
      filenames = QStringList()
      
      if dlg.exec_():
      	filenames = dlg.selectedFiles()
      	self.mlcfname = str(filenames[0])
	self.label_5.setText(self.mlcfname)
	#self.runml(self.mlcfname)

    
    def runml(self):
	dataset1 = pd.read_csv(self.mlcfname)
	#print (dataset.head())
	dataset = pd.read_csv('/home/manu/be_project/snpEff_latest_core/snpEff/FinalData.csv')
	dataset = dataset.fillna(dataset.median(axis=0))
	dataset1 = dataset1.fillna(dataset.median(axis=0))
	df_x = dataset.iloc[:,:-1]
	df_y = dataset.iloc[:,-1]
	df1_x = dataset1.iloc[:,:-1]
	df1_y = dataset1.iloc[:,-1]
	df_x['REF'] = df_x['REF'].apply(ord)
	df_x['ALT'] = df_x['ALT'].apply(ord)
	df1_x['REF'] = df1_x['REF'].apply(ord)
	df1_x['ALT'] = df1_x['ALT'].apply(ord)
	clf = RandomForestClassifier(n_estimators=250)
	clf.fit(df_x, df_y)

	print(df_x)
	print(df1_x)
	print(clf)

	predictions = clf.predict(df1_x)

	print("Train Accuracy :: ", accuracy_score(df_y, clf.predict(df_x)))
	print("Test Accuracy  :: ", accuracy_score(df1_y, predictions))
	print(" Confusion matrix ", confusion_matrix(df1_y, predictions))
	
	opstr1=("Train Accuracy :: ", accuracy_score(df_y, clf.predict(df_x)))
	sopstr1=str(opstr1)
	opstr2=("Test Accuracy  :: ", accuracy_score(df1_y, predictions))
	sopstr2=str(opstr2)
	opstr3=(" Confusion matrix ", confusion_matrix(df1_y, predictions)) 
	sopstr3=str(opstr3)
	fh3=open("rfop.txt",'w')
	fh3.write("Random Forest Algorithm Results")
	fh3.write("\n")
	fh3.write(sopstr1)
	fh3.write("\n")
	fh3.write(sopstr2)
	fh3.write("\n")
	fh3.write(sopstr3)
	
	fh3.close()


	#KNN

	clf = KNeighborsClassifier()
	clf.fit(df_x, df_y)

	print(df_x)
	print(df1_x)
	print(clf)

	predictions = clf.predict(df1_x)

	print("Train Accuracy :: ", accuracy_score(df_y, clf.predict(df_x)))
	print("Test Accuracy  :: ", accuracy_score(df1_y, predictions))
	print(" Confusion matrix ", confusion_matrix(df1_y, predictions)) 
	opstr1=("Train Accuracy :: ", accuracy_score(df_y, clf.predict(df_x)))
	sopstr1=str(opstr1)
	opstr2=("Test Accuracy  :: ", accuracy_score(df1_y, predictions))
	sopstr2=str(opstr2)
	opstr3=(" Confusion matrix ", confusion_matrix(df1_y, predictions)) 
	sopstr3=str(opstr3)
	fh2=open("knnop.txt",'w')
	fh2.write("K Nearest Neighbour Algorithm Results")
	fh2.write("\n")
	fh2.write(sopstr1)
	fh2.write("\n")
	fh2.write(sopstr2)
	fh2.write("\n")
	fh2.write(sopstr3)
	
	fh2.close()

	#DecisionTree

	clf = DecisionTreeClassifier()
	clf.fit(df_x, df_y)

	print(df_x)
	print(df1_x)
	print(clf)

	predictions = clf.predict(df1_x)

	print("Train Accuracy :: ", accuracy_score(df_y, clf.predict(df_x)))
	print("Test Accuracy  :: ", accuracy_score(df1_y, predictions))
	print(" Confusion matrix ", confusion_matrix(df1_y, predictions)) 
	opstr1=("Train Accuracy :: ", accuracy_score(df_y, clf.predict(df_x)))
	sopstr1=str(opstr1)
	opstr2=("Test Accuracy  :: ", accuracy_score(df1_y, predictions))
	sopstr2=str(opstr2)
	opstr3=(" Confusion matrix ", confusion_matrix(df1_y, predictions)) 
	sopstr3=str(opstr3)
	fh1=open("dtreeop.txt",'w')
	fh1.write("Decision Tree Algorithm Results")
	fh1.write("\n")
	fh1.write(sopstr1)
	fh1.write("\n")
	fh1.write(sopstr2)
	fh1.write("\n")
	fh1.write(sopstr3)
	
	fh1.close()


	#SVM

	'''clf = svm.SVC()
	clf.fit(df_x, df_y)
	
	#fh=open("svmop.txt",'w')
	


	print(df_x)
	print(df1_x)
	print(clf)

	predictions = clf.predict(df1_x)

	print("Train Accuracy :: ", accuracy_score(df_y, clf.predict(df_x)))
	print("Test Accuracy  :: ", accuracy_score(df1_y, predictions))
	print(" Confusion matrix ", confusion_matrix(df1_y, predictions)) 
	opstr1=("Train Accuracy :: ", accuracy_score(df_y, clf.predict(df_x)))
	sopstr1=str(opstr1)
	opstr2=("Test Accuracy  :: ", accuracy_score(df1_y, predictions))
	sopstr2=str(opstr2)
	opstr3=(" Confusion matrix ", confusion_matrix(df1_y, predictions)) 
	sopstr3=str(opstr3)
	fh4=open("svmop.txt",'w')
	fh4.write("Support Vector Machine Algorithm Results")
	fh4.write("\n")
	fh4.write(sopstr1)
	fh4.write("\n")
	fh4.write(sopstr2)
	fh4.write("\n")
	fh4.write(sopstr3)
	
	fh4.close()''' 


    def prthefiles(self):
	os.system("java -jar SnpSift.jar annotate "+self.dname+" "+self.fname+" > "+self.fname[:-4]+"_annotated.vcf")
        print("\nFile "+self.fname+" has been annotated successfully!\n")
	
	if self.radioButton.isChecked():
		if self.checkBox.isChecked() == True:
			str1 = self.checkBox.text()
			str1 = str(str1)+" "
		else:
			str1 = ""
			
		if self.checkBox_2.isChecked() == True:
			str2 = self.checkBox_2.text()
			str2 = str(str2)+" "
		else:
			str2 = ""
		if self.checkBox_3.isChecked() == True:
			str3 = self.checkBox_3.text()
			str3 = str(str3)+" "
		else:
			str3 = ""
		if self.checkBox_4.isChecked() == True:
			str4 = self.checkBox_4.text()
			str4 = str(str4)+" "
		else:
			str4 = ""
		final_str2 = str1 + str2 +str3 + str4
		print final_str2
		os.system("java -jar SnpSift.jar extractFields "+self.fname[:-4]+"_annotated.vcf CHROM POS ID REF ALT "+final_str2+"> "+self.fname[:-4]+"_Extracted.tsv")
	else:
		os.system("java -jar SnpSift.jar extractFields "+self.fname[:-4]+"_annotated.vcf CHROM POS ID REF ALT CLNSIG RS GENEINFO CLNDN> "+self.fname[:-4]+"_Extracted.tsv")
	print("\nFile "+self.fname+" has been extracted successfully!\n")
	#os.system("libreoffice --calc " +self.fname[:-4]+"_Extracted.tsv")
	#exit()

    def refresh_button_state(self):
       if self.radioButton.isChecked():
         self.checkBox.setEnabled(True)
	 self.checkBox_2.setEnabled(True)
	 self.checkBox_3.setEnabled(True)
	 self.checkBox_4.setEnabled(True)
       else:
	 self.checkBox.setEnabled(False)
	 self.checkBox_2.setEnabled(False)
	 self.checkBox_3.setEnabled(False)
	 self.checkBox_4.setEnabled(False)

    #Pre-Processing        
    def preprocess(self):
	#print self.fname
	tofi=self.fname[-3:]
	tofibeg=self.fname[:-3]
	ffname=self.fname
	if tofi=="bam":
		#print tofi
		#print tofibeg
		#print self.fname
		os.system("samtools mpileup -C 50 -d 1000000 -L 1000001 -g -u -f ucsc.hg19.fasta "+self.fname+" > "+tofibeg+"bcf") #BAM to BCF conversion
		os.system("bcftools view -m -Ov -v "+tofibeg+"bcf | /home/manu/Downloads/bcftools-1.8/misc/vcfutils.pl varFilter - > "+tofibeg+"vcf") #BCF to VCF conversion
	if self.radioButton.isChecked():
		if self.checkBox.isChecked() == True:
			str1 = self.checkBox.text()
			str1 = str(str1)+" "
		else:
			str1 = ""
			
		if self.checkBox_2.isChecked() == True:
			str2 = self.checkBox_2.text()
			str2 = str(str2)+" "
		else:
			str2 = ""
		if self.checkBox_3.isChecked() == True:
			str3 = self.checkBox_3.text()
			str3 = str(str3)+" "
		else:
			str3 = ""
		if self.checkBox_4.isChecked() == True:
			str4 = self.checkBox_4.text()
			str4 = str(str4)+" "
		else:
			str4 = ""
		final_str2 = str1 + str2 +str3 + str4
		print final_str2
	tofibeg4=self.fname[:-4]
	os.system("java -jar SnpSift.jar annotate /home/manu/be_project/snpEff_latest_core/snpEff/clinvar37.vcf "+tofibeg4+".vcf > "+tofibeg4+"_ann.vcf") #Annotation
	print(" annotated")
	os.system("java -jar SnpSift.jar extractFields "+tofibeg4+"_ann.vcf CHROM POS REF ALT CLNSIG > "+tofibeg4+"_Extracted.tsv") #Converting the Annotated File to a TSV File by extracting the important fields
	print(" extracted")
	csv_name=tofibeg4+".csv" 
	tsv_file=tofibeg4+"_Extracted.tsv" 
	csv_table=pd.read_table(tsv_file,sep='\t')
	csv_table.to_csv(csv_name,index=False)
	input = open(csv_name,'r')
	csvopname=tofibeg4+"_op.csv"
	output = open(csvopname,'w')
	writer = csv.writer(output)
	headers = ['CHROM','POS','REF','ALT','CLNSIG']
	writer.writerow(headers)


	data = pd.read_csv(input)
	input.close()
	rep = { 'chr1': 1,'chr2': 2,'chr3': 3,'chr4': 4,'chr5': 5,'chr6': 6,'chr7': 7,'chr8': 8,'chr9': 9,'chr10': 10,'chr11': 11,'chr12': 12,'chr13': 13,'chr14': 14,'chr15': 15,'chr16': 16,'chr17': 17,'chr18': 18,'chr19': 19,'chr20': 20,'chr21': 21,'chr22': 22,'chrX': 23,'chrY': 24,'chrM': 25} #Converting strings in the CHROM column to integer
	
	data.CHROM = [rep[item] for item in data.CHROM]
	inmfname=tofibeg4+"inm.csv"
	data.to_csv(inmfname)
		
	input2=	open(inmfname,'r')

	
		
	for row in csv.reader(input2):
		if((row[4]=='A' or row[4]=='T' or row[4]=='G' or row[4]=='C') and (row[3]=='A' or row[3]=='T' or row[3]=='G' or row[3]=='C') and (row[5]!='')): #Removing the rows containing multiple letters in the REF/ALT column
			writer.writerow(row[1:])	
			
	
	input2.close()
	output.close()          

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

