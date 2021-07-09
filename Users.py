from Packages import *
from Packages import Function as fn

class Users(QFrame):
    def __init__(self):
        super().__init__()
        loadUi('gui\loginUsers.ui',self)
        self.setFixedSize(654, 438)
        self.con = fn.createConnection()
        self.cursor = self.con.cursor()
        self.showUsers()
        self.cmb.setPlaceholderText('x')
        self.populateCombo()
        self.radioButtonAdmin.setChecked(True)
        self.check()
        self.radioButtonAdmin.toggled.connect(self.check)
        self.radioButtonUser.toggled.connect(self.check)
        self.cmb.currentTextChanged.connect(self.fetchData)
        self.btnAdmin.clicked.connect(self.changeType)
        self.btnUser.clicked.connect(self.changeType)
        self.btnDelete.clicked.connect(self.deleteID)

    def showUsers(self):
        query = 'select userid, type ' \
                'from logindetails'
        self.cursor.execute(query)
        self.dataset = self.cursor.fetchall()
        rowcount = len(self.dataset)
        if rowcount == 0:
            self.showDialog("Record does not exist.")
        self.table.setRowCount(rowcount)
        rownum = 0
        for row in self.dataset:
            for column in range(len(row)):
                self.table.setItem(rownum, column, QTableWidgetItem(str(row[column])))
            rownum = rownum + 1

    def populateCombo(self):
        strsql = 'select userid ' \
                 'from logindetails ' \
                 'order by userid'
        self.cursor.execute(strsql)
        self.dataset = self.cursor.fetchall()
        for data in self.dataset:
            self.cmb.addItem(str(data[0]))

    def fetchData(self):
        self.uid = self.cmb.currentText()
        query1 = 'select type ' \
                 'from logindetails ' \
                 'where userid=%s'
        self.cursor.execute(query1, (self.uid,))
        self.prevType = self.cursor.fetchone()

    def check(self):
        if self.radioButtonAdmin.isChecked():
            self.btnUser.setVisible(False)
            self.btnAdmin.setVisible(True)
        elif self.radioButtonUser.isChecked():
            self.btnAdmin.setVisible(False)
            self.btnUser.setVisible(True)

    def changeType(self):
        if self.cmb.currentIndex()==-1:
            print('x')
            fn.showDialog("Please select userid first!")
        elif self.radioButtonAdmin.isChecked():
            if self.prevType[0]=='Admin':
                fn.showDialog('Type is already Admin')
            else:
                querych = 'update logindetails ' \
                          'set type="Admin" ' \
                          'where userid=%s'
                self.cursor.execute(querych, (self.uid,))
                self.con.commit()
                fn.showDialog("Type changed to Admin!")
        elif self.radioButtonUser.isChecked():
            if self.prevType[0] == 'User':
                fn.showDialog('Type is already User!')
            else:
                quer='select * ' \
                     'from logindetails ' \
                     'where type="Admin"'
                self.cursor.execute(quer)
                self.adminNum = self.cursor.fetchall()
                self.adminRow=len(self.adminNum)
                if self.adminRow==1:
                    fn.showDialog("Atleast one Admin is required!")
                else:
                    querych = 'update logindetails ' \
                              'set type="User" ' \
                              'where userid=%s'
                    self.cursor.execute(querych, (self.uid,))
                    self.con.commit()
                    fn.showDialog("Type changed to User!")
        self.showUsers()
        self.fetchData()

    def deleteID(self):
        self.fetchData()
        if self.cmb.currentIndex()==-1:
            fn.showDialog("Please select userid first")
        else:
            quer = 'select * ' \
                   'from logindetails ' \
                   'where type="Admin"'
            self.cursor.execute(quer)
            self.adminNum = self.cursor.fetchall()
            self.adminRow = len(self.adminNum)
            if self.adminRow == 1 and self.prevType[0] == 'Admin':
                fn.showDialog("Atleast one Admin is required!")
            else:
                strdelete = 'delete ' \
                            'from logindetails ' \
                            'where userid=%s'
                self.cursor.execute(strdelete, (self.uid,))
                self.con.commit()
                fn.showDialog('Data deleted Successfully!')
        self.showUsers()
        self.fetchData()
        self.cmb.clear()
        self.populateCombo()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    users = Users()
    users.show()
    app.exec_()