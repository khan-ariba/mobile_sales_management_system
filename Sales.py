from Packages import *
from Packages import Function as fn


class Sales(QFrame):
    def __init__(self):
        super().__init__()
        loadUi('gui\Sales.ui', self)
        self.setFixedSize(724, 412)
        self.con = fn.createConnection()
        self.cursor = self.con.cursor()
        self.btnadd.clicked.connect(self.addfn)
        self.btnlogout.clicked.connect(self.logout)
        self.txtid.setReadOnly(True)
        self.txtbill.setReadOnly(True)
        self.reset()
        self.cmbBrand.currentTextChanged.connect(self.fetchModels)
        self.cmbModel.currentTextChanged.connect(self.fetchData)
        self.cmbQuantity.currentTextChanged.connect(self.total)
        self.cmbBrand.setPlaceholderText(' ')
        self.populateCombo()
        self.cmbModel.setPlaceholderText(' ')

    def reset(self):

        strsql = 'select max(transactionid) ' \
                 'from sales'
        self.cursor.execute(strsql)
        self.rowdata = self.cursor.fetchone()
        if self.rowdata[0] == None:
            self.newid = 1
        else:
            self.newid = self.rowdata[0] + 1
        self.txtid.setText(str(self.newid))
        self.cmbQuantity.clear()
        self.cmbQuantity.addItems(['1', '2', '3', '4', '5'])
        self.txtcname.clear()
        self.txtemail.clear()
        self.txtphone.clear()
        self.txtaddress.clear()

    def populateCombo(self):
        strsql = 'select brandname ' \
                 'from brand ' \
                 'order by brandname'
        self.cursor.execute(strsql)
        self.dataset = self.cursor.fetchall()
        for data in self.dataset:
            self.cmbBrand.addItem(str(data[0]))

    def fetchModels(self):
        self.cmbModel.clear()
        self.bname = self.cmbBrand.currentText()
        query1 = 'select a.modelname ' \
                 'from modeldetails a, brand b ' \
                 'where a.brandid=b.brandid and b.brandname=%s'
        self.cursor.execute(query1, (self.bname,))
        self.modelset = self.cursor.fetchall()
        for item in self.modelset:
            self.cmbModel.addItem(str(item[0]))

    def fetchData(self):
        self.mname = self.cmbModel.currentText()
        query1 = 'select modelnumber ' \
                 'from modeldetails ' \
                 'where modelname=%s'
        self.cursor.execute(query1, (self.mname,))
        self.modelset = self.cursor.fetchone()
        self.mnum = self.modelset[0]
        self.total()

    def logout(self):
        btn = fn.questionDialog("Confirmation", "Do you want to Logout?")
        if btn == QMessageBox.Yes:
            self.close()

    def addfn(self):
        self.quantity = self.cmbQuantity.currentText()
        self.cname = self.txtcname.text()
        self.email = self.txtemail.text()
        self.phone = self.txtphone.text()
        self.add = self.txtaddress.toPlainText()
        now = QDate.currentDate()
        self.date = now.toString(Qt.ISODate)
        try:
            if self.phone != '':
                int(self.phone)
        except ValueError:
            fn.showDialog('Please enter a valid phone number.')
            return self.reset()
        if self.cmbBrand.currentIndex() == -1 or self.cmbModel.currentIndex() == -1:
            fn.showDialog('Please select Brand and Model.')
        elif self.cname == '' or self.email == '' or self.phone == '':
            fn.showDialog('Please enter customer details.')
        elif len(self.phone) != 10:
            fn.showDialog("Phone number should be of 10 digits.")
        else:
            strqua = 'select quantity, price ' \
                     'from modeldetails ' \
                     'where modelnumber=%s'
            self.cursor.execute(strqua, (self.mnum,))
            self.rowdata = self.cursor.fetchone()
            self.qua = self.rowdata[0]
            self.price = self.rowdata[1]
            self.qua2 = int(self.quantity)
            if self.qua < self.qua2:
                fn.showDialog('Quantity exceeded!!')
            else:
                self.total_bill = self.price * int(self.quantity)

                btn = fn.questionDialog('Confirmation', 'Payment Received??')
                if btn == QMessageBox.Yes:
                    strinsert = 'insert into sales(transactionid, modelnumber, quantity, customername, email, address, phone, total_bill, date) ' \
                                'values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    self.cursor.execute(strinsert,
                                        (int(self.newid), self.mnum, int(self.quantity), self.cname, self.email,
                                         self.add, self.phone, self.total_bill, self.date,))
                    self.con.commit()
                    fn.showDialog('Data inserted successfully.')
                    strdec = 'update modeldetails ' \
                             'set quantity=quantity - %s ' \
                             'where modelnumber=%s'
                    self.cursor.execute(strdec, (int(self.quantity), self.mnum,))
                    self.con.commit()
        self.reset()

    def total(self):
        self.quantity = self.cmbQuantity.currentText()
        strqua = 'select price ' \
                 'from modeldetails ' \
                 'where modelnumber=%s'
        try:
            self.cursor.execute(strqua, (self.mnum,))
            self.rowdata = self.cursor.fetchone()
            price = self.rowdata[0]
            total = price * float(self.quantity)
            self.txtbill.setText(str(total))
        except (AttributeError, ValueError):
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sales = Sales()
    sales.show()
    app.exec_()
