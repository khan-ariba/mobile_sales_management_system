from Packages import *
from Packages import Function as fn

class Logs(QFrame):
    def __init__(self):
        super().__init__()
        loadUi('gui\Logs.ui', self)
        self.setFixedSize(711, 404)
        self.con = fn.createConnection()
        self.cursor = self.con.cursor()
        self.btnsearch.clicked.connect(self.search)
        self.btnreset.clicked.connect(self.reset)
        d = QDate.currentDate()
        self.dateEdit.setDate(d)
        self.reset()

    def reset(self):
        self.label.setVisible(True)
        self.btnreset.setVisible(False)
        query = 'select timestamp, username, remarks ' \
                'from userlogs ' \
                'order by timestamp desc ' \
                'limit 5'
        self.cursor.execute(query)
        self.dataset = self.cursor.fetchall()
        rowcount = len(self.dataset)
        self.table.setRowCount(rowcount)
        rownum = 0
        for row in self.dataset:
            for column in range(len(row)):
                self.table.setItem(rownum, column, QTableWidgetItem(str(row[column])))
            rownum = rownum + 1

    def search(self):
        self.label.setVisible(False)
        self.btnreset.setVisible(True)
        value = self.dateEdit.date()
        self.date = value.toString(Qt.ISODate)
        query = 'select timestamp, username, remarks ' \
                'from userlogs ' \
                'where date(timestamp)=%s ' \
                'order by timestamp desc'
        self.cursor.execute(query, (self.date,))
        self.dataset = self.cursor.fetchall()
        rowcount = len(self.dataset)
        if rowcount == 0:
            fn.showDialog("Record does not exist.")
        self.table.setRowCount(rowcount)
        rownum = 0
        for row in self.dataset:
            for column in range(len(row)):
                self.table.setItem(rownum, column, QTableWidgetItem(str(row[column])))
            rownum = rownum + 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Logs()
    menu.show()
    app.exec_()