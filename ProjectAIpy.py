from PyQt5 import QtCore, QtGui, QtWidgets
from youtube_dl import YoutubeDL
import speech_recognition as sr 
import moviepy.editor as mp
import youtube_dl
import ffmpeg
import os
from time import sleep
import re
from google_trans_new import google_translator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(34, 38, 107, 255), stop:0.558704 rgba(22, 24, 66, 255));\n"
"border-radius : 10px;")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.frame_title = QtWidgets.QFrame(self.drop_shadow_frame)
        self.frame_title.setGeometry(QtCore.QRect(10, 0, 741, 40))
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayoutWidget = QtWidgets.QWidget(self.drop_shadow_frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 781, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.frame_5.setStyleSheet("background-color:transparent;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.textEdit_12 = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit_12.setEnabled(False)
        self.textEdit_12.setGeometry(QtCore.QRect(10, 551, 761, 191))
        self.textEdit_12.setStyleSheet("background-color:transparent;\n"
"color: #fff;")
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit_13.setEnabled(False)
        self.textEdit_13.setGeometry(QtCore.QRect(470, 550, 531, 191))
        self.textEdit_13.setStyleSheet("background-color:transparent;\n"
"color: #fff;")
        self.textEdit_13.setObjectName("textEdit_13")
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setGeometry(QtCore.QRect(10, 260, 801, 191))
        self.frame_3.setStyleSheet("background-color:transparent;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_5.setEnabled(False)
        self.textEdit_5.setGeometry(QtCore.QRect(0, 20, 571, 31))
        self.textEdit_5.setStyleSheet("background-color:transparent;\n"
"color: #fff;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.subtitleButton = QtWidgets.QPushButton(self.frame_3)
        self.subtitleButton.setGeometry(QtCore.QRect(530, 18, 121, 31))
        self.subtitleButton.setStyleSheet("background-color: rgb(49, 208, 190);")
        self.subtitleButton.setObjectName("subtitleButton")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setGeometry(QtCore.QRect(-10, 40, 431, 80))
        self.frame.setStyleSheet("background-color: transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit_6 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_6.setEnabled(False)
        self.textEdit_6.setGeometry(QtCore.QRect(10, 30, 421, 30))
        self.textEdit_6.setObjectName("textEdit_6")
        self.generateButton = QtWidgets.QPushButton(self.frame_3)
        self.generateButton.setGeometry(QtCore.QRect(530, 68, 121, 31))
        self.generateButton.setStyleSheet("background-color: rgb(49, 208, 190);")
        self.generateButton.setObjectName("generateButton")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setGeometry(QtCore.QRect(-10, 110, 431, 71))
        self.frame_7.setStyleSheet("background-color: transparent;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.textEdit_10 = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_10.setEnabled(False)
        self.textEdit_10.setGeometry(QtCore.QRect(10, 10, 421, 31))
        self.textEdit_10.setObjectName("textEdit_10")
        self.mergeButton = QtWidgets.QPushButton(self.frame_3)
        self.mergeButton.setGeometry(QtCore.QRect(530, 116, 121, 31))
        self.mergeButton.setStyleSheet("background-color: rgb(49, 208, 190);")
        self.mergeButton.setObjectName("mergeButton")
        self.videoLang = QtWidgets.QComboBox(self.frame_3)
        self.videoLang.setGeometry(QtCore.QRect(440, 23, 61, 21))
        self.videoLang.setStyleSheet("color:black;\n"
"background-color:rgb(202, 204, 203);\n"
"border-radius : 0px;\n"
"")
        self.videoLang.setObjectName("videoLang")
        self.videoLang.addItem("")
        self.videoLang.addItem("")
        self.videoLang.addItem("")
        self.videoLang.addItem("")
        self.listLang = QtWidgets.QComboBox(self.frame_3)
        self.listLang.setGeometry(QtCore.QRect(440, 73, 61, 21))
        self.listLang.setStyleSheet("color:black;\n"
"background-color:rgb(202, 204, 203);\n"
"border-radius : 0px;")
        self.listLang.setObjectName("listLang")
        self.listLang.addItem("")
        self.listLang.addItem("")
        self.listLang.addItem("")
        self.listLang.addItem("")
        self.listLang2 = QtWidgets.QComboBox(self.frame_3)
        self.listLang2.setGeometry(QtCore.QRect(440, 121, 61, 21))
        self.listLang2.setStyleSheet("color:black;\n"
"background-color:rgb(202, 204, 203);\n"
"border-radius : 0px;")
        self.listLang2.setObjectName("listLang2")
        self.listLang2.addItem("")
        self.listLang2.addItem("")
        self.listLang2.addItem("")
        self.listLang2.addItem("")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setGeometry(QtCore.QRect(0, 160, 741, 101))
        self.frame_4.setStyleSheet("background-color:transparent;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.textEdit = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 771, 31))
        self.textEdit.setStyleSheet("background-color:transparent;\n"
"color: #fff;")
        self.textEdit.setObjectName("textEdit")
        self.linkText = QtWidgets.QTextEdit(self.frame_4)
        self.linkText.setGeometry(QtCore.QRect(10, 40, 481, 51))
        self.linkText.setStyleSheet("background-color: transparent;\n"
"color : #b8b8b8;\n"
"border: 1px solid rgb(49, 208, 190);\n"
"padding-top:12px;\n"
"padding-left:10px;\n"
"")
        self.linkText.setObjectName("linkText")
        self.nameText = QtWidgets.QTextEdit(self.frame_4)
        self.nameText.setGeometry(QtCore.QRect(500, 40, 111, 51))
        self.nameText.setStyleSheet("background-color: transparent;\n"
"color : #b8b8b8;\n"
"border: 1px solid rgb(49, 208, 190);\n"
"padding-top:12px;\n"
"padding-left:10px;\n"
"")
        self.nameText.setObjectName("nameText")
        self.downloadButton = QtWidgets.QPushButton(self.frame_4)
        self.downloadButton.setEnabled(True)
        self.downloadButton.setGeometry(QtCore.QRect(620, 40, 111, 51))
        self.downloadButton.setStyleSheet("background-color: rgb(49, 208, 190);")
        self.downloadButton.setObjectName("downloadButton")
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setGeometry(QtCore.QRect(90, 0, 551, 121))
        self.frame_2.setStyleSheet("background-color: transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(130, 20, 321, 61))
        self.label.setStyleSheet("color: rgb(49, 208, 190);\n"
"font-size: 24px;\n"
"font-familly:\"Roboto\";\n"
"background-color:transparent;\n"
"font-size:42px;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(170, 80, 241, 20))
        self.label_3.setStyleSheet("background-color:transparent;\n"
"font-size : 14px;\n"
"color: #fff;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.frame_5, 0, 0, 1, 1)
        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionDisplay = QtWidgets.QAction(MainWindow)
        self.actionDisplay.setObjectName("actionDisplay")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.downloadButton.clicked.connect(self.downloadVideo)
        self.subtitleButton.clicked.connect(self.getSrtFile)
        self.generateButton.clicked.connect(self.translate)
        self.mergeButton.clicked.connect(self.attachSrtFile)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt; font-weight:600;\">Ai</span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt;\"> </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:10pt;\">Project - Ensa 2021 </span><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:11pt;\">©</span></p></body></html>"))
        self.textEdit_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:12pt; font-weight:600;\">Thanks for choosing our application !</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt;\">2- Give Video Language to Generate Subtitle File :</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:13pt;\"><br /></p></body></html>"))
        self.subtitleButton.setText(_translate("MainWindow", "Submit"))
        self.textEdit_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; color:#ffffff;\">3- Translate Subtitle File to This Language :</span></p></body></html>"))
        self.generateButton.setText(_translate("MainWindow", "Submit"))
        self.textEdit_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; color:#ffffff;\">4- Merge Desired Subtitle File with Video :</span></p></body></html>"))
        self.mergeButton.setText(_translate("MainWindow", "Submit"))
        self.videoLang.setItemText(0, _translate("MainWindow", "ar"))
        self.videoLang.setItemText(1, _translate("MainWindow", "en"))
        self.videoLang.setItemText(2, _translate("MainWindow", "fr"))
        self.videoLang.setItemText(3, _translate("MainWindow", "es"))
        self.listLang.setItemText(0, _translate("MainWindow", "ar"))
        self.listLang.setItemText(1, _translate("MainWindow", "en"))
        self.listLang.setItemText(2, _translate("MainWindow", "fr"))
        self.listLang.setItemText(3, _translate("MainWindow", "es"))
        self.listLang2.setItemText(0, _translate("MainWindow", "ar"))
        self.listLang2.setItemText(1, _translate("MainWindow", "en"))
        self.listLang2.setItemText(2, _translate("MainWindow", "fr"))
        self.listLang2.setItemText(3, _translate("MainWindow", "es"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt;\">1- Enter youtube link, video name &amp; language to download video</span></p></body></html>"))
        self.linkText.setPlaceholderText(_translate("MainWindow", "Enter your Link Here"))
        self.nameText.setPlaceholderText(_translate("MainWindow", "Enter Name"))
        self.downloadButton.setText(_translate("MainWindow", "Download Video"))
        self.label.setText(_translate("MainWindow", "Youtube Subtitles"))
        self.label_3.setText(_translate("MainWindow", "Your favorite subtitles app generator"))
        self.actionDisplay.setText(_translate("MainWindow", "Display"))

    def downloadVideo(self):
        #download video as mp4
        data_text = self.linkText.toPlainText()
        videonametext = self.nameText.toPlainText()
        print(videonametext)
        ydl_opts = {
            'outtmpl': videonametext+'.%(ext)s',
            'format': '22',
                    }     
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
             ydl.download([data_text]) 
        info = ydl.extract_info(data_text, download=False)
        name = "{0}.{1}".format(videonametext, 'mp4')
        
        

        print('download finished !!!!!')

    def getSrtFile(self):
        #get srt subtitle file
        comboV = str(self.videoLang.currentText())
        videonametext = self.nameText.toPlainText()
        os.system('autosub -S '+comboV+' -D '+comboV+' '+videonametext+'.mp4')
        print('srt file generated !!!!!')

    def translate(self):
        #translate and write in srt file
        videonametext = self.nameText.toPlainText()
        combo = str(self.listLang.currentText())

        f = open(videonametext+'.srt', 'r',encoding='utf-8')
        t = open(videonametext+'-'+combo+'.srt', 'w',encoding='utf-8')
        if f.mode == 'r':
            file_translate = google_translator()
            for i, line in enumerate(f):
                if re.search('[a-zA-Z]', line):
                    result = file_translate.translate(line, lang_tgt=combo)
                    t.write(result+'\n')
                else:
                    t.write(line)

        print('translate finished !!!!!!!!')

    def attachSrtFile(self):
        videonametext = self.nameText.toPlainText()
        combo = str(self.listLang2.currentText())
        os.system('ffmpeg -i '+videonametext+'.mp4 -vf subtitles='+videonametext+'-'+combo+'.srt'+' '+videonametext+'-'+combo+'.mp4')
        print('finish him')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())