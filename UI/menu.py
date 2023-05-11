from PyQt6.QtCore import Qt, QTimer, QDateTime
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        
        self.lblTitle = QLabel(self)
        
        self.lblTitle.setText("Public Market Information System")
        self.lblTitle.setGeometry(0, 40, 1280, 70)
        self.lblTitle.setFont(QFont("Inter", 48, QFont.Weight.Bold))
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.welcome = QLabel(self)
        # self.welcome.setText("Welcome back, topecnz!")
        self.welcome.setGeometry(40, 200, 640, 40)
        self.welcome.setFont(QFont("Inter", 24, QFont.Weight.Bold))
        # self.welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.datetime = QLabel(self)
        self.datetime.setGeometry(40, 280, 640, 40)
        self.datetime.setFont(QFont("Inter", 24, QFont.Weight.Bold))
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)
        self.update_clock()
        
        self.btnLogout = QPushButton(self)
        self.btnLogout.setText("Logout")
        self.btnLogout.setGeometry(150, 600, 300, 60)
        self.btnLogout.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnLogout.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.btnTenant = QPushButton(self)
        self.btnTenant.setText("Tenant Inforamtion")
        self.btnTenant.setGeometry(660, 240, 600, 60)
        self.btnTenant.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnTenant.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.btnInv = QPushButton(self)
        self.btnInv.setText("Market Inventories")
        self.btnInv.setGeometry(660, 320, 600, 60)
        self.btnInv.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnInv.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.btnPayment = QPushButton(self)
        self.btnPayment.setText("Payment")
        self.btnPayment.setGeometry(660, 400, 600, 60)
        self.btnPayment.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnPayment.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.btnReport = QPushButton(self)
        self.btnReport.setText("Revenue Report")
        self.btnReport.setGeometry(660, 480, 600, 60)
        self.btnReport.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnReport.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.btnStaff = QPushButton(self)
        self.btnStaff.setText("Staff")
        self.btnStaff.setGeometry(660, 560, 600, 60)
        self.btnStaff.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnStaff.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnStaff.hide()
        
    def update_clock(self):
        current_datetime = QDateTime.currentDateTime()
        date = current_datetime.toString("yyyy/MM/dd")
        time = current_datetime.toString("hh:mm:ss AP")
        self.datetime.setText("Today is " + date + " at " + time)