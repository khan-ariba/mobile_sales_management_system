from Packages import *
from Packages import Function as fn


class Edit(QFrame):
    def __init__(self):
        super().__init__()
        loadUi('gui\edit.ui', self)
        self.setFixedSize(567, 419)
        self.con = fn.createConnection()
        self.cursor = self.con.cursor()
        self.btnupdate.clicked.connect(self.update_det)
        self.cmbBrand.setPlaceholderText(' ')
        self.populateCombo()
        self.cmbModel.setPlaceholderText(' ')
        self.cmbBrand.currentTextChanged.connect(self.fetchModels)
        self.cmbModel.currentTextChanged.connect(self.fetchData)

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
        self.bname=self.cmbBrand.currentText()
        query1='select a.modelname ' \
               'from modeldetails a, brand b ' \
               'where a.brandid=b.brandid and b.brandname=%s'
        self.cursor.execute(query1, (self.bname,))
        self.modelset=self.cursor.fetchall()
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
        query1='select modelname, price,quantity,features ' \
               'from modeldetails ' \
               'where modelnumber=%s'
        self.cursor.execute(query1, (self.mnum,))
        self.data=self.cursor.fetchone()
        self.txtmodel.setText(self.data[0])
        self.txtprice.setText(str(self.data[1]))
        self.txtquantity.setText(str(self.data[2]))
        self.txtFeatures.setText(self.data[3])

    def update_det(self):
        self.model=self.txtmodel.text()
        self.price=self.txtprice.text()
        self.quantity=self.txtquantity.text()
        self.features=self.txtFeatures.toPlainText()

        if self.model == '' or self.price == '' or self.quantity == '' or self.features == '' or self.cmbModel.currentIndex()==-1:
            fn.showDialog("Please enter details after selecting the model")
        else:
            try:
                query2 = 'update modeldetails ' \
                         'set modelname=%s, price=%s, quantity=%s, features=%s ' \
                         'where modelnumber=%s'
                self.cursor.execute(query2,
                                    (self.model, float(self.price), int(self.quantity), self.features, int(self.mnum),))
                self.con.commit()
                fn.showDialog("Data Updated!!")
                self.txtmodel.setText('')
                self.txtprice.setText('')
                self.txtquantity.setText('')
                self.txtFeatures.clear()
            except:
                fn.showDialog("Another phone with same name already exists!")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    edit = Edit()
    edit.show()
    app.exec_()