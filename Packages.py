from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import mysql.connector as mysql
from PyQt5.uic import loadUi
import sys
import gui.project51


class Function:
    @staticmethod
    def createConnection():
        con = mysql.connect(host='localhost', database='mobile_sales', user='root', password='')
        return con

    def showDialog(txt):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Message.')
        msg.setText(txt)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def questionDialog(title, txt):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle(title)
        msg.setText(txt)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        btnstatus = msg.exec_()
        return btnstatus
