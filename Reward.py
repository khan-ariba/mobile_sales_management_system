from Packages import *
from Packages import Function as fn
import random
import smtplib
import ssl


class Reward(QFrame):
    def __init__(self):
        super().__init__()
        loadUi('gui/Reward.ui', self)
        self.setFixedSize(394, 378)
        self.con = fn.createConnection()
        self.cursor = self.con.cursor()
        self.btnstart.clicked.connect(self.findlucky)
        self.btnmail.clicked.connect(self.sendmail)
        self.rowcount = 0

    def findlucky(self):
        self.set = []
        query = 'select transactionid ' \
                'from sales ' \
                'where MONTH(DATE)=MONTH(CURRENT_TIMESTAMP) AND YEAR(DATE)=YEAR(CURRENT_TIMESTAMP)'
        self.cursor.execute(query)
        self.ids = self.cursor.fetchall()
        if self.ids == []:
            return fn.showDialog("No sales in current month yet.")
        self.idset = []
        for item in self.ids:
            self.idset.append(item[0])
        while len(self.set) != 2:
            self.randomid = random.choice(self.idset)
            query1 = 'select customername, email ' \
                     'from sales ' \
                     'where transactionid=%s'
            self.cursor.execute(query1, (int(self.randomid),))
            self.dataset = self.cursor.fetchone()
            self.set.append(self.dataset)

        self.rowcount = len(self.set)
        if self.rowcount == 0:
            fn.showDialog("No records found!!.")
        self.table.setRowCount(self.rowcount)
        rownum = 0
        for row in self.set:
            for column in range(len(row)):
                self.table.setItem(
                    rownum, column, QTableWidgetItem(str(row[column])))
            rownum = rownum + 1

        self.maillist = []
        self.maillist.append(self.set[0][1])
        self.maillist.append(self.set[1][1])

    def sendmail(self):
        if self.rowcount == 0:
            fn.showDialog("Please click on START first!!")
        else:
            btn = fn.questionDialog('Confirmation', 'Are you sure??')
            if btn == QMessageBox.Yes:
                for mailid in self.maillist:
                    try:
                        port = 465  # For SSL
                        smtp_server = "smtp.gmail.com"
                        sender_email = "abc@xyz.com"  # Enter your address
                        password = "your_password_here"
                        message = """\
                        Subject: Congratulations!!!
Dear Customer,\nYou are our lucky winner and won a brand new mobile phone.\nPlease visit our store to claim your reward.\n\nRegards,\nSmiling Mobiles."""
                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                            server.login(sender_email, password)
                            server.sendmail(sender_email, mailid, message)
                    except:
                        fn.showDialog(
                            "Email not sent!!\nCheck your internet connection")
                    else:
                        fn.showDialog("Email sent successfully!!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Reward()
    menu.show()
    app.exec_()
