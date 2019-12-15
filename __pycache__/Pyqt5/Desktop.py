# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pianyuan.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets,Qt,QtSql
import sys
import MySQLdb
from PyQt5.QtWidgets import  QTableView,QAbstractItemView,QHeaderView,QTableWidget, QTableWidgetItem, QMessageBox,QListWidget,QListWidgetItem, QStatusBar,  QMenuBar,QMenu,QAction,QLineEdit,QStyle,QFormLayout,   QVBoxLayout,QWidget,QApplication ,QHBoxLayout, QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QStandardItem,QStandardItemModel,QCursor
from PyQt5.QtCore import QStringListModel,QAbstractListModel,QModelIndex,QSize,Qt



'''
class Ui_WindowAboutUs(object):
    def setupUi(self, WindowAboutUs):
        WindowAboutUs.setObjectName("WindowAboutUs")
        WindowAboutUs.resize(253, 178)
        self.centralwidget = QtWidgets.QWidget(WindowAboutUs)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 121, 51))
        self.label.setObjectName("label")
        WindowAboutUs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowAboutUs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 253, 18))
        self.menubar.setObjectName("menubar")
        WindowAboutUs.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowAboutUs)
        self.statusbar.setObjectName("statusbar")
        WindowAboutUs.setStatusBar(self.statusbar)

        self.retranslateUi(WindowAboutUs)
        QtCore.QMetaObject.connectSlotsByName(WindowAboutUs)

    def retranslateUi(self, WindowAboutUs):
        _translate = QtCore.QCoreApplication.translate
        WindowAboutUs.setWindowTitle(_translate("WindowAboutUs", "关于我们"))
        self.label.setText(_translate("WindowAboutUs", "这里可以写点个人信息"))

'''

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1024, 960)
        icon = QtGui.QIcon.fromTheme("C:\\Users\\97607\\Desktop\\bitbug_favicon.ico")
        mainWindow.setWindowIcon(icon)
        mainWindow.setWindowOpacity(0.9)
        mainWindow.setDocumentMode(False)
        #mainWindow.setWindowFlags(Qt.Qt.CustomizeWindowHint)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")




#######################################  Four main Button   ##################################################
        self.Button_recommand = QtWidgets.QPushButton(self.centralwidget)
        self.Button_recommand.setGeometry(QtCore.QRect(30, 300, 171, 61))
        self.Button_recommand.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_recommand.setObjectName("Button_recommand")
        self.Button_recommand.clicked.connect(self.but_recommad)
        self.Button_recommand.setStyleSheet('''
    QPushButton{border:none;color:black;}
    QPushButton#left_label{
        border:none;
        border-bottom:1px solid white;
        font-size:18px;
        font-weight:700;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
    QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
''')

        self.Button_search = QtWidgets.QPushButton(self.centralwidget)
        self.Button_search.setGeometry(QtCore.QRect(30, 420, 171, 61))
        self.Button_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_search.setObjectName("Button_search")
        self.Button_search.clicked.connect(self.but_search)
        self.Button_search.setStyleSheet('''
    QPushButton{border:none;color:black;}
    QPushButton#left_label{
        border:none;
        border-bottom:1px solid white;
        font-size:18px;
        font-weight:700;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
    QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
''')

        self.Button_History = QtWidgets.QPushButton(self.centralwidget)
        self.Button_History.setGeometry(QtCore.QRect(30, 540, 171, 61))
        self.Button_History.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_History.setObjectName("Button_History")
        self.Button_History.clicked.connect(self.but_history)
        self.Button_History.setStyleSheet('''
    QPushButton{border:none;color:black;}
    QPushButton#left_label{
        border:none;
        border-bottom:1px solid white;
        font-size:18px;
        font-weight:700;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
    QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
''')
        

        self.Button_About = QtWidgets.QPushButton(self.centralwidget)
        self.Button_About.setGeometry(QtCore.QRect(30, 660, 171, 61))
        self.Button_About.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_About.setObjectName("Button_About")
        self.Button_About.setStyleSheet('''
    QPushButton{border:none;color:black;}
    QPushButton#left_label{
        border:none;
        border-bottom:1px solid white;
        font-size:18px;
        font-weight:700;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
    QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
''')
        #self.Button_About.clicked.connect(self.but_aboutus)


#######################################  Frame of Recommand   ##################################################


        self.frameRecommad = QtWidgets.QFrame(self.centralwidget)
        self.frameRecommad.setEnabled(False)
        self.frameRecommad.setGeometry(QtCore.QRect(215, 30, 790, 881))
        self.frameRecommad.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frameRecommad.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameRecommad.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameRecommad.setObjectName("frameRecommad")
        self.frameRecommad.setStyleSheet('''
    QWidget#right_widget{
        color:#232C51;
        background:white;
        border-top:1px solid darkGray;
        border-bottom:1px solid darkGray;
        border-right:1px solid darkGray;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;
    }
    QLabel#right_lable{
        border:none;
        font-size:16px;
        font-weight:700;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
''')

        self.label_recommand = QtWidgets.QLabel(self.frameRecommad)
        self.label_recommand.setEnabled(True)
        self.label_recommand.setGeometry(QtCore.QRect(40, 20, 99, 61))

        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label_recommand.setFont(font)
        self.label_recommand.setToolTipDuration(0)
        self.label_recommand.setIndent(0)
        self.label_recommand.setObjectName("label_recommand")

#######################################  Function Button   ##################################################

        """

        self.left_close = QtWidgets.QPushButton(self.centralwidget)
        self.left_close.setGeometry(QtCore.QRect(950, 30, 20, 20))
        self.left_close.setText("")
        self.left_close.setObjectName("Button_control1")
        #self.left_close.clicked.connect(self.close)

        self.left_visit = QtWidgets.QPushButton(self.centralwidget)
        self.left_visit.setGeometry(QtCore.QRect(900, 30, 20, 20))
        self.left_visit.setText("")
        self.left_visit.setObjectName("Button_control2")

        self.left_mini = QtWidgets.QPushButton(self.centralwidget)
        self.left_mini.setGeometry(QtCore.QRect(850, 30, 20, 20))
        self.left_mini.setText("")
        self.left_mini.setObjectName("Button_control3")

        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
       
        """
        


#######################################  Frame of History   ##################################################



        self.frameHistory = QtWidgets.QFrame(self.centralwidget)
        self.frameHistory.setGeometry(QtCore.QRect(215, 30, 790, 881))
        self.frameHistory.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frameHistory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHistory.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHistory.setObjectName("frameHistory")
        self.frameHistory.setStyleSheet('''
    QWidget#right_widget{
        color:#232C51;
        background:white;
        border-top:1px solid darkGray;
        border-bottom:1px solid darkGray;
        border-right:1px solid darkGray;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;
    }
    QLabel#right_lable{
        border:none;
        font-size:16px;
        font-weight:700;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
''')

        self.label_history = QtWidgets.QLabel(self.frameHistory)
        self.label_history.setEnabled(True)
        self.label_history.setGeometry(QtCore.QRect(40, 20, 99, 61))

        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label_history.setFont(font)
        self.label_history.setToolTipDuration(0)
        self.label_history.setIndent(0)
        self.label_history.setObjectName("label_history")

        self.table_history = QtWidgets.QTableView(self.frameHistory)
        self.table_history.setGeometry(QtCore.QRect(40,100,700,750))

#######################################  Frame of Search   ##################################################



        self.frameSearch = QtWidgets.QFrame(self.centralwidget)
        self.frameSearch.setEnabled(False)
        self.frameSearch.setGeometry(QtCore.QRect(215, 30, 790, 881))
        self.frameSearch.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.frameSearch.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSearch.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSearch.setObjectName("frameSearch_2")
        self.frameSearch.setStyleSheet('''
    QWidget#right_widget{
        color:#232C51;
        background:white;
        border-top:1px solid darkGray;
        border-bottom:1px solid darkGray;
        border-right:1px solid darkGray;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;
    }
    QLabel#right_lable{
        border:none;
        font-size:16px;
        font-weight:700;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
''')

        self.label_Search = QtWidgets.QLabel(self.frameSearch)
        self.label_Search.setEnabled(True)
        self.label_Search.setGeometry(QtCore.QRect(40, 20, 99, 61))

        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        
        self.label_Search.setFont(font)
        self.label_Search.setToolTipDuration(0)
        self.label_Search.setIndent(0)
        self.label_Search.setObjectName("label_Search")



        result = self.database()
        result_main = result[0]

        
        self.table_search = QTableWidget(self.frameSearch)
        self.table_search.setColumnCount(result[1])
        self.table_search.setRowCount(result[2])
        self.table_search.horizontalHeader().setDefaultSectionSize(190)     #760/n
        self.table_search.setGeometry(QtCore.QRect(0,100,760,700))
        self.table_search.  (QAbstractItemView.)

                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,THERE!!!!
                #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        
        for i in range(result[2]):
            result_child = result_main[i]
            
            for j in range(result[1]):
                self.Item = QTableWidgetItem(result_child[j])
                self.table_search.setItem(i,j,self.Item)
                
        

        # self.table_search.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)    
        
    


        #self.table_search.setItem(row,column,)



#######################################  Some initalization   ##################################################

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 18))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.frameRecommad.setVisible(True)
        self.frameHistory.setVisible(False)
        self.frameSearch.setVisible(False)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)



    #Choose the Frame
    def but_recommad(self):
        self.frameRecommad.setVisible(True)
        self.frameHistory.setVisible(False)
        self.frameSearch.setVisible(False)

    def but_history(self):
        self.frameRecommad.setVisible(False)
        self.frameHistory.setVisible(True)
        self.frameSearch.setVisible(False)

    def but_search(self):
        self.frameRecommad.setVisible(False)
        self.frameHistory.setVisible(False)
        self.frameSearch.setVisible(True)


    #def but_aboutus(self):
 


    def closeWindow(self):
        self.mainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)


    '''
    def but_aboutus(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_WindowAboutUs()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    '''
        


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "片源网下载器"))
        self.Button_recommand.setText(_translate("mainWindow", "今日推荐"))
        self.Button_search.setText(_translate("mainWindow", "电影查询"))
        self.Button_History.setText(_translate("mainWindow", "历史记录"))
        self.Button_About.setText(_translate("mainWindow", "关于我们"))
        self.label_recommand.setText(_translate("mainWindow", "今日推荐"))
        self.label_history.setText(_translate("mainWindow", "历史记录"))
        self.label_Search.setText(_translate("mainWindow", "电影查询"))



    def database(self):         #This argument may influenced by the PyQt5
        db = MySQLdb.connect(
            "localhost","root","root","world"
        )

        cursor = db.cursor()
        row = cursor.execute("select * from country;")
        result = cursor.fetchall()
        column = len(result[0]) #You need to use the first of the tuple's data to recognize how much columns it have
        db.close()
        
        return result,column,row




if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
