from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *

class Menu(QWidget):
    def __init__(self, widget, cookies):
        super().__init__()
        
        # store data
        self.widget = widget
        self.cookies = cookies
        
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
        self.btnLogout.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btnTenant = QPushButton(self)
        self.btnTenant.setText("Tenant Inforamtion")
        self.btnTenant.setGeometry(660, 200, 600, 60)
        self.btnTenant.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnTenant.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnTenant.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btnInv = QPushButton(self)
        self.btnInv.setText("Market Inventories")
        self.btnInv.setGeometry(660, 280, 600, 60)
        self.btnInv.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnInv.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnInv.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btnPayment = QPushButton(self)
        self.btnPayment.setText("Payment")
        self.btnPayment.setGeometry(660, 360, 600, 60)
        self.btnPayment.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnPayment.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnPayment.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btnReport = QPushButton(self)
        self.btnReport.setText("Revenue Report")
        self.btnReport.setGeometry(660, 440, 600, 60)
        self.btnReport.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnReport.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnReport.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btnStall = QPushButton(self)
        self.btnStall.setText("Stall Information")
        self.btnStall.setGeometry(660, 520, 600, 60)
        self.btnStall.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnStall.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnStaff.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btnStaff = QPushButton(self)
        self.btnStaff.setText("Staff Information")
        self.btnStaff.setGeometry(660, 520, 600, 60)
        self.btnStaff.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnStaff.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnStaff.setCursor(Qt.CursorShape.PointingHandCursor)
        
    def update_clock(self):
        current_datetime = QDateTime.currentDateTime()
        date = current_datetime.toString("yyyy/MM/dd")
        time = current_datetime.toString("hh:mm:ss AP")
        self.datetime.setText("Today is " + date + " at " + time)
