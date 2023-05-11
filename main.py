import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import QFont, QScreen, QGuiApplication
from PyQt6.QtWidgets import *

# import UI
from UI import login, menu, tenant, inventory, payment, report, staff

#database
from db import connection

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(1280, 720))
        
        self.wLogin = login.Main()
        self.wMenu = menu.Menu()
        self.wTenant = tenant.Tenant()
        self.wInventory = inventory.Inventory()
        self.wPayment = payment.Payment()
        self.wReport = report.Report()
        self.wStaff = staff.Staff()
        
        widget.addWidget(self.wLogin)
        widget.addWidget(self.wMenu)
        widget.addWidget(self.wTenant)
        widget.addWidget(self.wInventory)
        widget.addWidget(self.wPayment)
        widget.addWidget(self.wReport)
        widget.addWidget(self.wStaff)
        
        self.login() #default
        
    def login(self):
        widget.setCurrentWidget(self.wLogin)
        self.wLogin.btnLogin.clicked.connect(self.login_check)
        # widget.setCurrentWidget(widget.currentIndex() + 1)
        
    def login_check(self):
        if self.wLogin.tbPass.text() == 'a':
            self.menu(self.wLogin.tbUser.text())
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Message")
            msg.setText("Invalid Account or Pass.\nTry again later.")
            msg.setFont(QFont("Inter", 16, QFont.Weight.Bold))
            msg.setFixedSize(QSize(500, 250))
            # msg.setIcon(QMessageBox.Icon.Critical)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.setDefaultButton(QMessageBox.StandardButton.Ok)
            msg.exec()

    def menu(self, username):
        # self.wLogin.deleteLater()
        
        widget.setCurrentWidget(self.wMenu)
        self.wMenu.welcome.setText("Welcome back, %s!" % username)
        self.wMenu.btnLogout.clicked.connect(self.logout)
        self.wMenu.btnTenant.clicked.connect(self.tenant)
        self.wMenu.btnInv.clicked.connect(self.inventory)
        self.wMenu.btnPayment.clicked.connect(self.payment)
        self.wMenu.btnReport.clicked.connect(self.report)
        self.wMenu.btnStaff.clicked.connect(self.staff)
        
        if username == 'topecnz':
            self.wMenu.btnStaff.show()
        
    def logout(self):
        widget.setCurrentWidget(self.wLogin)
        
    def tenant(self):
        widget.setCurrentWidget(self.wTenant)
        self.wTenant.btnBack.clicked.connect(self.back)

    def inventory(self):        
        widget.setCurrentWidget(self.wInventory)
        self.wInventory.btnBack.clicked.connect(self.back)

    def payment(self):        
        widget.setCurrentWidget(self.wPayment)
        self.wPayment.btnBack.clicked.connect(self.back)

    def report(self):        
        widget.setCurrentWidget(self.wReport)
        self.wReport.btnBack.clicked.connect(self.back)

    def staff(self):        
        widget.setCurrentWidget(self.wStaff)
        self.wStaff.btnBack.clicked.connect(self.back)
        
    def back(self):
        widget.setCurrentWidget(self.wMenu)
        

# Creating Object    
app = QApplication(sys.argv)
widget = QStackedWidget()

window = Main()
widget.addWidget(window)
widget.setWindowTitle("Public Market Information System")
widget.setGeometry(0, 0, 1280, 720)
widget.show()

# Set the application at the center of the screen
screen = QGuiApplication.primaryScreen()
screen_geometry = screen.geometry()
x = (screen_geometry.width() - widget.width()) // 2
y = (screen_geometry.height() - widget.height()) // 2
widget.move(x, y)

# Set default bg color
widget.setStyleSheet(
    """
        QStackedWidget {
            background-color: #C7C7C7;
        }                 
    """
    )

# run the program
app.exec()
        
        
        