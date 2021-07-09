from Packages import *
from Packages import Function as fn


class AddDetails(QFrame):
    def __init__(self):
        super().__init__()
        loadUi('gui\AddDetails.ui', self)
        self.setFixedSize(633, 326)
        self.con = fn.createConnection()
        self.cursor = self.con.cursor()
        self.btnadd.clicked.connect(self.addfn)
        self.btnaddBrand.clicked.connect(self.addBrand)
        self.cmbBrand.currentTextChanged.connect(self.fetchBrand)
        self.cmbBrand.setPlaceholderText(' ')
        self.populateCombo()
        self.reset()

    def reset(self):
        strsql = 'select max(brandid) ' \
                 'from brand'
        self.cursor.execute(strsql)
        self.rowdata = self.cursor.fetchone()
        if self.rowdata[0] == None:
            self.newbrid = 1
        else:
            self.newbrid = self.rowdata[0] + 1
        strsql = 'select max(modelnumber) ' \
                 'from modeldetails'
        self.cursor.execute(strsql)
        self.rowdata = self.cursor.fetchone()
        if self.rowdata[0] == None:
            self.newid = 1
        else:
            self.newid = self.rowdata[0] + 1
        self.txtmodel.setText('')
        self.txtprice.setText('')
        self.txtquantity.setText('')
        self.txtfeatures.clear()

    def populateCombo(self):
        strsql = 'select brandname ' \
                 'from brand ' \
                 'order by brandname'
        self.cursor.execute(strsql)
        self.dataset = self.cursor.fetchall()
        for data in self.dataset:
            self.cmbBrand.addItem(str(data[0]))

    def fetchBrand(self):
        self.bname = self.cmbBrand.currentText()
        query1 = 'select brandid ' \
                 'from brand ' \
                 'where brandname=%s'
        self.cursor.execute(query1, (self.bname,))
        self.modelset = self.cursor.fetchone()
        try:
            self.brid = self.modelset[0]
        except TypeError:
            pass

    def addfn(self):
        self.model = self.txtmodel.text()
        self.price = self.txtprice.text()
        self.quantity = self.txtquantity.text()
        self.fea = self.txtfeatures.toPlainText()
        if self.cmbBrand.currentIndex() == -1:
            fn.showDialog('Please select Brand first.')
        elif self.model == '' or self.price == '' or self.quantity == '' or self.fea == '':
            fn.showDialog('Please fill all the details.')
        elif int(self.quantity) == 0:
            fn.showDialog("Quantity cannot be zero.")
        else:
            try:
                strinsert = 'insert into modeldetails(modelnumber, brandid, modelname, price, features, quantity) ' \
                            'values (%s,%s,%s,%s,%s,%s)'
                self.cursor.execute(strinsert,
                                    (self.newid, self.brid, self.model, int(self.price), self.fea, int(self.quantity)))
                self.con.commit()
                fn.showDialog('Model added successfully.')
            except:
                fn.showDialog("Another phone with same name already exists!")
        self.reset()

    def addBrand(self):
        self.brname = self.txtname.text()
        if self.brname == '':
            fn.showDialog('Please enter Brand name.')
        else:
            try:
                strinsert = 'insert into brand(brandid, brandname) ' \
                            'values (%s,%s)'
                self.cursor.execute(strinsert, (self.newbrid, self.brname,))
                self.con.commit()
                fn.showDialog('Brand added successfully.')
            except:
                fn.showDialog("Another brand with same name already exists!")
        self.reset()
        self.cmbBrand.clear()
        self.populateCombo()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ad = AddDetails()
    ad.show()
    app.exec_()
