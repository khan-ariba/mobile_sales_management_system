from Packages import *
from Packages import Function as fn
from AddDetails import AddDetails
from EditDetails import Edit
from Reward import Reward
from Charts import Charts
from Logs import Logs
from Users import Users

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('gui\Menu.ui', self)
        self.setFixedSize(991, 583)
        self.tablesize()
        self.con = fn.createConnection()
        self.cursor = self.con.cursor()
        self.cmbBrand.setPlaceholderText(' ')
        self.populateCombo()
        self.btnshow.clicked.connect(self.btnshowsales)
        self.cmbBrand.currentTextChanged.connect(self.fetchModels)
        self.btnsearch.clicked.connect(self.search)
        self.btnlogout.clicked.connect(self.logout)
        self.txtsearch.setPlaceholderText("Search by transaction ID")
        self.showsales()
        self.actionAdd_New.triggered.connect(lambda: self.loadFrame(self.actionAdd_New))
        self.actionEdit.triggered.connect(lambda: self.loadFrame(self.actionEdit))
        self.actionLucky_Draw.triggered.connect(lambda: self.loadFrame(self.actionLucky_Draw))
        self.actionBest_Selling.triggered.connect(lambda: self.loadFrame(self.actionBest_Selling))
        self.actionUsers.triggered.connect(lambda: self.loadFrame(self.actionUsers))
        self.actionShow_Charts.triggered.connect(lambda: self.loadFrame(self.actionShow_Charts))
        self.actionLogs.triggered.connect(lambda: self.loadFrame(self.actionLogs))

    def loadFrame(self, item):
        caption = item.text()
        if caption == 'Add New':
            self.load = AddDetails()
        elif caption == 'Edit':
            self.load = Edit()
        elif caption == 'Users':
            self.load = Users()
        elif caption == 'Lucky Draw':
            self.load = Reward()
        elif caption == 'Show Charts':
            self.load = Charts()
        elif caption == 'Logs':
            self.load = Logs()
        self.load.show()

    def showsales(self):
        self.table1.setVisible(True)
        self.table2.setVisible(False)
        query = 'select transactionid, c.brandname, modelname, a.quantity, customername, email, address, phone, date, total_bill ' \
                'from sales a, modeldetails b, brand c ' \
                'where a.modelnumber=b.modelnumber and b.brandid=c.brandid ' \
                'order by transactionid desc'
        self.cursor.execute(query)
        self.dataset = self.cursor.fetchall()
        rowcount = len(self.dataset)
        self.table1.setRowCount(rowcount)
        rownum = 0
        for row in self.dataset:
            for column in range(len(row)):
                self.table1.setItem(rownum, column, QTableWidgetItem(str(row[column])))
            rownum = rownum + 1

    def btnshowsales(self):
        query = 'select * ' \
                'from sales'
        self.cursor.execute(query)
        self.dataset = self.cursor.fetchall()
        rowcount = len(self.dataset)
        if rowcount == 0:
            fn.showDialog("No record available!!")
        else:
            self.showsales()

    def populateCombo(self):
        strsql = 'select brandname ' \
                 'from brand ' \
                 'order by brandname'
        self.cursor.execute(strsql)
        self.dataset = self.cursor.fetchall()
        for data in self.dataset:
            self.cmbBrand.addItem(str(data[0]))

    def fetchModels(self):
        self.table1.setVisible(False)
        self.table2.setVisible(True)
        self.bname = self.cmbBrand.currentText()
        query1 = 'select b.brandname, modelname, price, features, quantity ' \
                 'from modeldetails a, brand b ' \
                 'where a.brandid=b.brandid and brandname=%s'
        self.cursor.execute(query1, (self.bname,))
        self.modelset = self.cursor.fetchall()
        rowcount = len(self.modelset)
        if rowcount == 0:
            fn.showDialog("Phones for this brand not available yet.")
        self.table2.setRowCount(rowcount)
        rownum = 0
        for row in self.modelset:
            for column in range(len(row)):
                self.table2.setItem(rownum, column, QTableWidgetItem(str(row[column])))
            rownum = rownum + 1

    def logout(self):
        btn = fn.questionDialog("Confirmation", "Do you want to Logout?")
        if btn == QMessageBox.Yes:
            self.close()


    def search(self):
        self.table1.setVisible(True)
        self.table2.setVisible(False)
        self.searchtext = self.txtsearch.text()
        if self.searchtext == '':
            fn.showDialog('Please enter name of the customer.')
        else:
            query = 'select transactionid, c.brandname, modelname, a.quantity, customername, email, address, phone, date, total_bill ' \
                    'from sales a, modeldetails b, brand c ' \
                    'where a.modelnumber=b.modelnumber and b.brandid=c.brandid and transactionid=%s'
            self.cursor.execute(query, (self.searchtext,))
            self.dataset = self.cursor.fetchall()
            rowcount = len(self.dataset)
            print(rowcount)
            if rowcount == 0:
                fn.showDialog("Record does not exist.")
            self.table1.setRowCount(rowcount)
            rownum = 0
            for row in self.dataset:
                for column in range(len(row)):
                    self.table1.setItem(rownum, column, QTableWidgetItem(str(row[column])))
                rownum = rownum + 1

    def tablesize(self):
        self.table1.setColumnWidth(0, 125)
        self.table1.setColumnWidth(1, 125)
        self.table1.setColumnWidth(3, 110)
        self.table1.setColumnWidth(5, 175)
        self.table1.setColumnWidth(7, 110)
        self.table1.setColumnWidth(8, 110)
        self.table2.setColumnWidth(0, 125)
        self.table2.setColumnWidth(2, 110)
        self.table2.setColumnWidth(3, 350)
        self.table2.setColumnWidth(4, 110)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    app.exec_()
