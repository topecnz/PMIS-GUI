import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import QFont, QScreen, QGuiApplication
from PyQt6.QtWidgets import *

# import UI
from UI import login, menu, tenant, inventory, payment, report, staff

#database
from db import connection

#session
import session

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(1280, 720))
        
        # Create an objects
        self.wLogin = login.Main(widget, cookies)
        self.wMenu = menu.Menu(widget, cookies)
        self.wTenant = tenant.Tenant(widget, cookies)
        self.wInventory = inventory.Inventory(widget, cookies)
        self.wPayment = payment.Payment(widget, cookies)
        self.wReport = report.Report(widget, cookies)
        self.wStaff = staff.Staff(widget, cookies)
        
        # Add objects to widget
        widget.addWidget(self.wLogin)
        widget.addWidget(self.wMenu)
        widget.addWidget(self.wTenant)
        widget.addWidget(self.wInventory)
        widget.addWidget(self.wPayment)
        widget.addWidget(self.wReport)
        widget.addWidget(self.wStaff)
        
        self.login() # default
        
    def login(self):
        widget.setCurrentWidget(self.wLogin)
        self.wLogin.btnLogin.clicked.connect(self.login_check)
        
        # When Enter key is pressed
        self.wLogin.tbUser.returnPressed.connect(self.login_check)
        self.wLogin.tbPass.returnPressed.connect(self.login_check)
        
    def login_check(self):
        username = self.wLogin.tbUser.text()
        password = self.wLogin.tbPass.text()
        data = postgres.select(f"SELECT ACC_ID, ACC_TYPE_ID, ACC_USERNAME FROM ACCOUNT WHERE ACC_USERNAME = '{username}' AND ACC_PASSWORD = '{password}';")
        if data:
            data = data[0]
            cookies.data['id'] = data[0]
            cookies.data['type'] = data[1]
            cookies.data['username'] = data[2]
            self.wLogin.tbPass.setText("") # remove password after logging in.
            self.menu()
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

    def menu(self):
        # self.wLogin.deleteLater()
        
        widget.setCurrentWidget(self.wMenu)
        self.wMenu.welcome.setText(f"Welcome back, {cookies.data['username']} ({cookies.data['id']})!")
        
        # button listener
        self.wMenu.btnLogout.clicked.connect(self.logout)
        self.wMenu.btnTenant.clicked.connect(self.tenant)
        self.wMenu.btnInv.clicked.connect(self.inventory)
        self.wMenu.btnPayment.clicked.connect(self.payment)
        self.wMenu.btnReport.clicked.connect(self.report)
        self.wMenu.btnStaff.clicked.connect(self.staff)
        
        # Check if the user is not staff, display Staff button.
        if cookies.data['type'] != 1:
            self.wMenu.btnStaff.show()
        else:
            self.wMenu.btnStaff.hide()

    # for back button listener only
    
    def logout(self):
        cookies.data.clear() # remove all credentials
        widget.setCurrentWidget(self.wLogin)
        
    def tenant(self):
        widget.setCurrentWidget(self.wTenant)
        self.wTenant.stallCat()
        self.wTenant.displayTable()
        self.wTenant.clearFields() # just to clear everything.
        self.wTenant.btnBack.clicked.connect(self.back)

    def inventory(self):        
        widget.setCurrentWidget(self.wInventory)
        self.wInventory.displayTable()
        self.wInventory.clearFields() # just to clear everything.
        self.wInventory.btnBack.clicked.connect(self.back)

    def payment(self):        
        widget.setCurrentWidget(self.wPayment)
        self.wPayment.displayTable()
        self.wPayment.clearFields()
        self.wPayment.btnBack.clicked.connect(self.back)

    def report(self):        
        widget.setCurrentWidget(self.wReport)
        self.wReport.displayTable()
        self.wReport.btnBack.clicked.connect(self.back)

    def staff(self):        
        widget.setCurrentWidget(self.wStaff)
        self.wStaff.staffPos()
        self.wStaff.displayTable()
        self.wStaff.clearFields() # just to clear everything.
        self.wStaff.btnBack.clicked.connect(self.back)
    
    # When back button is clicked
    def back(self):
        widget.setCurrentWidget(self.wMenu)
        

# Creating an object    
app = QApplication(sys.argv)
widget = QStackedWidget()
postgres = connection.PostgreSQL()
cookies = session.Session()

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
        
        
        