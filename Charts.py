from Packages import *
from Packages import Function as fn
import numpy as np
import matplotlib.pyplot as plt


class Charts(QFrame):
    def __init__(self):
        super().__init__()
        loadUi('gui\Charts.ui', self)
        self.setFixedSize(424, 341)
        self.con = fn.createConnection()
        self.cursor = self.con.cursor()
        self.btnshow.clicked.connect(self.showit)
        self.btnback.clicked.connect(self.back)
        self.btnbest.clicked.connect(self.best)
        self.btnshare.clicked.connect(self.share)
        self.rbtnf.clicked.connect(self.flagship)
        self.rbtnm.clicked.connect(self.midrange)
        self.rbtnb.clicked.connect(self.budget)
        self.back()

    def countX(self, lst, z):
        count = 0
        for ele in lst:
            if (ele == z):
                count += 1
        return count

    def best(self):
        plt.close()
        now2 = QDate.month(QDate.currentDate())
        query = 'select c.brandname ' \
                'from sales a, modeldetails b, brand c ' \
                'where a.modelnumber=b.modelnumber and b.brandid=c.brandid and month(date)=%s'
        self.cursor.execute(query, (now2,))
        dataset = self.cursor.fetchall()
        list1 = []
        for data in dataset:
            list1.append(data[0])
        query2 = 'select distinct(c.brandname) ' \
                 'from sales a, modeldetails b, brand c ' \
                 'where a.modelnumber=b.modelnumber and b.brandid=c.brandid and month(date)=%s'
        self.cursor.execute(query2, (now2,))
        dataset2 = self.cursor.fetchall()
        list2 = []
        for data in dataset2:
            list2.append(data[0])
        series = {}
        for dis in list2:
            co = self.countX(list1, dis)
            series.update({dis: co})
        y_pos = np.arange(len(series.keys()))
        plt.bar(y_pos, series.values(), align='center', alpha=0.5, color='red')
        plt.xticks(y_pos, series.keys())
        plt.ylabel("No. of unis sold.", fontsize=15)
        plt.xlabel("Brand", fontsize=15)
        plt.title("Best selling Brand of the month", fontsize=20)
        plt.show()

    def share(self):
        plt.close()
        query = 'select c.brandname ' \
                'from sales a, modeldetails b, brand c ' \
                'where a.modelnumber=b.modelnumber and b.brandid=c.brandid'
        self.cursor.execute(query)
        dataset = self.cursor.fetchall()
        list1 = []
        for data in dataset:
            list1.append(data[0])
        query2 = 'select distinct(c.brandname) ' \
                 'from sales a, modeldetails b, brand c ' \
                 'where a.modelnumber=b.modelnumber and b.brandid=c.brandid'
        self.cursor.execute(query2)
        dataset2 = self.cursor.fetchall()
        list2 = []
        for data in dataset2:
            list2.append(data[0])
        series = {}
        for dis in list2:
            co = self.countX(list1, dis)
            series.update({dis: co})
        colors = ['#69FFA1', '#FF5757', '#6DA8FF', '#FFFF67', '#D88AFF', '#FFC259', '#FF7EFF']
        explode = []
        for i in range(len(dataset2)):
            explode.append(0.025)
        figure, ax = plt.subplots()
        ax.pie(series.values(), labels=series.keys(), explode=explode, colors=colors, autopct='%1.1f%%', startangle=90,
               textprops={'color': "#606060"})  # autopct shows decimal point
        ax.axis('equal')
        plt.title("Market Share", fontsize=20)
        plt.show()

    def flagship(self):
        plt.close()
        query = "select c.brandname " \
                "from sales a, modeldetails b, brand c " \
                "where a.modelnumber=b.modelnumber and b.brandid=c.brandid and price>'35000'"
        self.cursor.execute(query)
        dataset = self.cursor.fetchall()
        list1 = []
        for data in dataset:
            list1.append(data[0])
        query2 = "select distinct(c.brandname) " \
                 "from sales a, modeldetails b, brand c " \
                 "where a.modelnumber=b.modelnumber and b.brandid=c.brandid and price>'35000'"
        self.cursor.execute(query2)
        dataset2 = self.cursor.fetchall()
        list2 = []
        for data in dataset2:
            list2.append(data[0])
        self.series2 = {}
        for dis in list2:
            co = self.countX(list1, dis)
            self.series2.update({dis: co})
        y_pos = np.arange(len(self.series2.keys()))
        plt.bar(y_pos, self.series2.values(), align='center', alpha=0.95, color="#FFC259")
        plt.xticks(y_pos, self.series2.keys())
        plt.ylabel("No. of unis sold.", fontsize=15)
        plt.xlabel("Brand", fontsize=15)
        plt.title("Monthly Sales of Flagship phones", fontsize=20)
        plt.show()

    def midrange(self):
        plt.close()
        query = "select c.brandname " \
                "from sales a, modeldetails b, brand c " \
                "where a.modelnumber=b.modelnumber and b.brandid=c.brandid and price>'15000' and price<='35000'"
        self.cursor.execute(query)
        dataset = self.cursor.fetchall()
        list1 = []
        for data in dataset:
            list1.append(data[0])
        query2 = "select distinct(c.brandname) " \
                 "from sales a, modeldetails b, brand c " \
                 "where a.modelnumber=b.modelnumber and b.brandid=c.brandid and price>'15000'and price<='35000'"
        self.cursor.execute(query2)
        dataset2 = self.cursor.fetchall()
        list2 = []
        for data in dataset2:
            list2.append(data[0])
        self.series3 = {}
        for dis in list2:
            co = self.countX(list1, dis)
            self.series3.update({dis: co})
        y_pos = np.arange(len(self.series3.keys()))
        plt.bar(y_pos, self.series3.values(), align='center', alpha=0.5, color="#00C3FF")
        plt.xticks(y_pos, self.series3.keys())
        plt.ylabel("No. of unis sold.", fontsize=15)
        plt.xlabel("Brand", fontsize=15)
        plt.title("Monthly Sales of Mid-range phones", fontsize=20)
        plt.show()

    def budget(self):
        plt.close()
        query = "select c.brandname " \
                "from sales a, modeldetails b, brand c " \
                "where a.modelnumber=b.modelnumber and b.brandid=c.brandid and price<='15000'"
        self.cursor.execute(query)
        dataset = self.cursor.fetchall()
        list1 = []
        for data in dataset:
            list1.append(data[0])
        query2 = "select distinct(c.brandname) " \
                 "from sales a, modeldetails b, brand c " \
                 "where a.modelnumber=b.modelnumber and b.brandid=c.brandid and price<='15000'"
        self.cursor.execute(query2)
        dataset2 = self.cursor.fetchall()
        list2 = []
        for data in dataset2:
            list2.append(data[0])
        self.series4 = {}
        for dis in list2:
            co = self.countX(list1, dis)
            self.series4.update({dis: co})
            self
        y_pos = np.arange(len(self.series4.keys()))
        plt.bar(y_pos, self.series4.values(), align='center', alpha=0.5, color="#00FF5F")
        plt.xticks(y_pos, self.series4.keys())
        plt.ylabel("No. of unis sold.", fontsize=15)
        plt.xlabel("Brand", fontsize=15)
        plt.title("Monthly Sales of Budget phones", fontsize=20)
        plt.show()

    def back(self):
        self.btnshow.setVisible(True)
        self.rbtnf.setVisible(False)
        self.rbtnm.setVisible(False)
        self.rbtnb.setVisible(False)
        self.btnback.setVisible(False)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label_4.setVisible(False)

    def showit(self):
        self.btnshow.setVisible(False)
        self.rbtnf.setVisible(True)
        self.rbtnm.setVisible(True)
        self.rbtnb.setVisible(True)
        self.btnback.setVisible(True)
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.label_4.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ch = Charts()
    ch.show()
    app.exec_()
