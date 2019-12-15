import MySQLdb   
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from Table import Ui_MainWindow
import sys
 
class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.table()
    def table(self):
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(2)
        j = 0#第几行（从0开始）
        i = 0#第几列（从0开始）
        Value = "test"#内容
        self.tableWidget.setItem(j, i, QTableWidgetItem(Value))#设置j行i列的内容为Value
        self.tableWidget.setColumnWidth(j,80)#设置j列的宽度
        self.tableWidget.setRowHeight(i,50)#设置i行的高度
        self.tableWidget.verticalHeader().setVisible(False)#隐藏垂直表头
        self.tableWidget.horizontalHeader().setVisible(False)#隐藏水平表头
if __name__=="__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
