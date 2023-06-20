from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *

class Main(QWidget):
    def __init__(self, widget, cookies):
        super().__init__()
        
        # store data
        self.widget = widget
        self.cookies = cookies
        
        #components
        # self.setFixedSize(QSize(1280, 720));
        self.lblTitle = QLabel(self)
        self.lblLogin = QLabel(self)
        self.lblUser = QLabel(self)
        self.lblPass = QLabel(self)
        
        # self.loginFrame = QFrame(self)
        self.tbUser = QLineEdit(self)
        self.tbPass =  QLineEdit(self)
        self.btnLogin = QPushButton(self)
        
        self.lblTitle.setText("Public Market Information System")
        self.lblTitle.setGeometry(0, 40, 1280, 70)
        self.lblTitle.setFont(QFont("Inter", 48, QFont.Weight.Bold))
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.lblLogin.setText("Login")
        self.lblLogin.setGeometry(0, 250, 1280, 50)
        self.lblLogin.setFont(QFont("Inter", 20, QFont.Weight.Bold))
        self.lblLogin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.lblUser.setText("Username:")
        self.lblUser.setGeometry(400, 360, 120, 50)
        self.lblUser.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.lblUser.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.tbUser.setGeometry(540, 350, 300, 40)
        self.tbUser.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
        self.lblPass.setText("Pass:")
        self.lblPass.setGeometry(400, 410, 120, 50)
        self.lblPass.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.lblPass.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.tbPass.setGeometry(540, 400, 300, 40)
        self.tbPass.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbPass.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.btnLogin.setText("Login")
        self.btnLogin.setGeometry(420, 500, 450, 40)
        self.btnLogin.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnLogin.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnLogin.setCursor(Qt.CursorShape.PointingHandCursor)
        # self.btnLogin.setAlignment(Qt.AlignmentFlag.AlignCenter)
