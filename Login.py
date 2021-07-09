from Packages import *
from Packages import Function as fn
from Sales import Sales
from Menu import Menu

class Login(QFrame):
    def __init__(self):
        super().__init__()
        loadUi('gui\login.ui', self)
        self.setFixedSize(396, 277)
        self.con = fn.createConnection()
        self.cursor = self.con.cursor()
        self.btnsubmit.clicked.connect(self.checkLogin)
        self.btnsignup.clicked.connect(self.signup)
        self.btnback.clicked.connect(self.back)
        self.btnabout.clicked.connect(self.about)
        self.btnproceed.clicked.connect(self.proceed)
        self.btnproceed2.clicked.connect(self.proceed2)
        self.back()
        self.txtuserid_2.setPlaceholderText("username")
        self.txtuserpass_2.setPlaceholderText("password")
        self.txtcpass.setPlaceholderText("confirm password")
        self.txtuserid.setPlaceholderText("username")
        self.txtuserpass.setPlaceholderText("password")

    def checkLogin(self):

        self.uid = self.txtuserid.text()
        self.upass = self.txtuserpass.text()
        query1 = 'select * ' \
                 'from logindetails ' \
                 'where userid=%s and password=%s'
        self.cursor.execute(query1, (self.uid, self.upass,))
        self.data = self.cursor.fetchone()
        self.status = self.cursor.rowcount

        if self.uid == '' or self.upass == '':
            fn.showDialog('Please enter your details')
        elif self.status > 0:
            admincheck = 'select type ' \
                         'from logindetails ' \
                         'where userid=%s'
            self.cursor.execute(admincheck, (self.uid,))
            self.typedata = self.cursor.fetchone()
            if self.typedata[0] == 'Admin':
                btn = fn.questionDialog('Confirmation', 'Hello Admin!\nDo you want to open Admin Dashboard?')
                if btn == QMessageBox.Yes:
                    self.logon = Menu()
                else:
                    self.logon = Sales()
            else:
                self.logon = Sales()
            self.logon.show()
            self.close()
            self.logEntry("Successful")
        else:
            fn.showDialog('Incorrect username or password!!')
            self.logEntry("Incorrect Details")

    def logEntry(self, remark):
        query2 = 'insert into userlogs(username, remarks) ' \
                 'values (%s,%s)'
        self.cursor.execute(query2, (self.uid, remark,))
        self.con.commit()

    def proceed(self):

        self.uid2 = self.txtuserid_2.text()
        self.upass2 = self.txtuserpass_2.text()
        self.cpass = self.txtcpass.text()
        self.skey = self.txtskey.text()
        if self.uid2 == '' or self.upass2 == '' or self.cpass == '':
            fn.showDialog('Please enter your details')
        elif self.upass2 != self.cpass:
            fn.showDialog('Password does not match!!')
        else:
            query1 = 'select * ' \
                     'from logindetails ' \
                     'where userid=%s'
            self.cursor.execute(query1, (self.uid2,))
            self.data = self.cursor.fetchone()
            self.status = self.cursor.rowcount
            qskeychk = 'select * ' \
                       'from logindetails ' \
                       'where adminkey=%s'
            self.cursor.execute(qskeychk, (self.skey,))
            self.keychk = self.cursor.fetchone()
            self.keystatus = self.cursor.rowcount
            if self.status > 0:
                fn.showDialog('ID already exists!')
            elif self.keystatus == -1:
                fn.showDialog('Wrong Security key!!')
            else:
                strinsert = 'insert into logindetails(userid, password) ' \
                            'values (%s,%s)'
                self.cursor.execute(strinsert, (self.uid2, self.upass2,))
                self.con.commit()
                fn.showDialog('ID created!')
                self.back()

    def proceed2(self):
        self.uid2 = self.txtuserid_2.text()
        self.upass2 = self.txtuserpass_2.text()
        self.cpass = self.txtcpass.text()
        self.skey = self.txtskey.text()
        if self.uid2 == '' or self.upass2 == '' or self.cpass == '' or self.skey == '':
            fn.showDialog('Please enter your details')
        elif self.upass2 != self.cpass:
            fn.showDialog('Password does not match!!')
        else:
            strinsert = 'insert into logindetails(userid, password, type, adminkey) ' \
                        'values (%s,%s,%s,%s)'
            self.cursor.execute(strinsert, (self.uid2, self.upass2, "Admin", self.skey,))
            self.con.commit()
            fn.showDialog('Admin ID created!')
            self.back()

    def signup(self):
        self.txtskey.setVisible(True)
        self.txtuserid_2.setVisible(True)
        self.txtuserpass_2.setVisible(True)
        self.txtcpass.setVisible(True)
        self.label_3.setVisible(False)
        self.label.setVisible(False)
        self.label_4.setVisible(True)
        self.txtuserid.setVisible(False)
        self.txtuserpass.setVisible(False)
        self.btnback.setVisible(True)
        self.btnproceed.setVisible(True)
        self.btnsubmit.setVisible(False)
        queryad = 'select * ' \
                  'from logindetails'
        self.cursor.execute(queryad)
        self.ad = self.cursor.fetchall()
        self.adstatus = self.cursor.rowcount
        if self.adstatus == 0:
            fn.showDialog('This is your first ID and it has to be of Admin type')
            self.btnproceed.setVisible(False)
            self.btnproceed2.setVisible(True)
            self.label_2.setVisible(True)
            self.txtskey.setPlaceholderText("new security key")

    def back(self):
        self.label_2.setVisible(False)
        self.txtskey.setPlaceholderText("admin security key")
        self.btnproceed2.setVisible(False)
        self.txtskey.setVisible(False)
        self.btnback.setVisible(False)
        self.btnproceed.setVisible(False)
        self.label_3.setVisible(True)
        self.label.setVisible(True)
        self.label_4.setVisible(False)
        self.txtuserid.setVisible(True)
        self.txtuserpass.setVisible(True)
        self.txtuserid_2.setVisible(False)
        self.txtuserpass_2.setVisible(False)
        self.txtcpass.setVisible(False)
        self.btnsubmit.setVisible(True)
        self.txtuserid_2.setText('')
        self.txtuserpass_2.setText('')
        self.txtcpass.setText('')
        self.txtskey.setText('')

    def about(self):
        fn.showDialog("This project is made by:-\n1. Anirudh Dabral\n2. Ariba Khan\nusing python, sql and pyqt5 designer.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    app.exec_()
