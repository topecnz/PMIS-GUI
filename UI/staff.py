from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtWidgets import *

class Staff(QWidget):
    def __init__(self):
        super().__init__()
        
        self.lblTitle = QLabel(self)
        
        self.lblTitle.setText("Public Market Information System")
        self.lblTitle.setGeometry(0, 40, 1280, 70)
        self.lblTitle.setFont(QFont("Inter", 36, QFont.Weight.Bold))
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.lblSubTitle = QLabel(self)
        
        self.lblSubTitle.setText("Staff Information")
        self.lblSubTitle.setGeometry(0, 90, 1280, 70)
        self.lblSubTitle.setFont(QFont("Inter", 28, QFont.Weight.Bold))
        self.lblSubTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.btnBack = QPushButton(self)
        self.btnBack.setText("Back")
        self.btnBack.setGeometry(20, 200, 150, 40)
        self.btnBack.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnBack.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.lblSearch = QLabel(self)
        self.lblSearch.setText("Search:")
        self.lblSearch.setGeometry(20, 250, 150, 30)
        self.lblSearch.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        
        self.tbSearch = QLineEdit(self)
        self.tbSearch.setGeometry(120, 250, 480, 30)
        self.tbSearch.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbSearch.returnPressed.connect(self.search)
        
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 290, 600, 400)
        self.table.setColumnCount(5)
        self.table.setRowCount(15)
        
        self.table.setHorizontalHeaderLabels(['Tenant ID', 'Lastname', 'Firstname', 'Phone', 'Date Added'])
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setStyleSheet(
            """
                QHeaderView::section {
                    background-color: #B3B3B3;
                    border: transparent;
                    font-weight: 700;
                    font-size: 12px;
                }
            """
        )
        self.btnBack.setCursor(Qt.CursorShape.PointingHandCursor)
        
        for row in range(15):
            self.table.setItem(row, 0, QTableWidgetItem(str(row + 1)))
            self.table.setItem(row, 1, QTableWidgetItem("10001"))
            self.table.setItem(row, 2, QTableWidgetItem("10001"))
            self.table.setItem(row, 3, QTableWidgetItem("10001"))
            self.table.setItem(row, 4, QTableWidgetItem("10001"))
            
        self.lblUser = QLabel(self)
        self.lblUser.setText("Username:")
        self.lblUser.setGeometry(640, 260, 140, 30)
        self.lblUser.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblUser.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbUser = QLineEdit(self)
        self.tbUser.setGeometry(800, 260, 450, 30)
        self.tbUser.setFont(QFont("Inter", 16, QFont.Weight.Normal))
            
        self.lblPasword = QLabel(self)
        self.lblPasword.setText("Password:")
        self.lblPasword.setGeometry(640, 300, 140, 30)
        self.lblPasword.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblPasword.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbPasword = QLineEdit(self)
        self.tbPasword.setGeometry(800, 300, 450, 30)
        self.tbPasword.setFont(QFont("Inter", 16, QFont.Weight.Normal))
            
        self.lblPosition = QLabel(self)
        self.lblPosition.setText("Position:")
        self.lblPosition.setGeometry(640, 340, 140, 30)
        self.lblPosition.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblPosition.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbPosition = QComboBox(self)
        self.tbPosition.setGeometry(800, 340, 450, 30)
        self.tbPosition.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbPosition.addItems(['','Staff', 'Admin'])
        self.tbPosition.setStyleSheet("background-color: #ffffff;")
        
        self.lblFname = QLabel(self)
        self.lblFname.setText("First name:")
        self.lblFname.setGeometry(640, 380, 140, 30)
        self.lblFname.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblFname.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbFname = QLineEdit(self)
        self.tbFname.setGeometry(800, 380, 450, 30)
        self.tbFname.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
        self.lblMname = QLabel(self)
        self.lblMname.setText("Middle name:")
        self.lblMname.setGeometry(640, 420, 140, 30)
        self.lblMname.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblMname.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbMname = QLineEdit(self)
        self.tbMname.setGeometry(800, 420, 450, 30)
        self.tbMname.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
        self.lblLname = QLabel(self)
        self.lblLname.setText("Last name:")
        self.lblLname.setGeometry(640, 460, 140, 30)
        self.lblLname.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblLname.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbLname = QLineEdit(self)
        self.tbLname.setGeometry(800, 460, 450, 30)
        self.tbLname.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
        self.lblBirth = QLabel(self)
        self.lblBirth.setText("Birthdate:")
        self.lblBirth.setGeometry(640, 500, 140, 30)
        self.lblBirth.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblBirth.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbBirth = QDateEdit(self)
        self.tbBirth.setGeometry(800, 500, 450, 30)
        self.tbBirth.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbBirth.setCalendarPopup(True)
        self.tbBirth.setDisplayFormat("yyyy/MM/dd")
        
        self.lblAdd = QLabel(self)
        self.lblAdd.setText("Address:")
        self.lblAdd.setGeometry(640, 540, 140, 30)
        self.lblAdd.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblAdd.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbAdd = QLineEdit(self)
        self.tbAdd.setGeometry(800, 540, 450, 30)
        self.tbAdd.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
        self.lblPhone = QLabel(self)
        self.lblPhone.setText("Phone:")
        self.lblPhone.setGeometry(640, 580, 140, 30)
        self.lblPhone.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblPhone.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbPhone = QLineEdit(self)
        self.tbPhone.setGeometry(800, 580, 450, 30)
        self.tbPhone.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbPhone.setValidator(QIntValidator().setBottom(0))
        
        self.btnAdd = QPushButton(self)
        self.btnAdd.setText("Add")
        self.btnAdd.setGeometry(660, 640, 180, 40)
        self.btnAdd.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnAdd.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.btnUpdate = QPushButton(self)
        self.btnUpdate.setText("Update")
        self.btnUpdate.setGeometry(860, 640, 180, 40)
        self.btnUpdate.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnUpdate.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.btnRemove = QPushButton(self)
        self.btnRemove.setText("Remove")
        self.btnRemove.setGeometry(1060, 640, 180, 40)
        self.btnRemove.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnRemove.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
            
    def search(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Message")
        msg.setText("Hello!")
        msg.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        msg.setFixedSize(QSize(500, 250))
        # msg.setIcon(QMessageBox.Icon.Critical)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()
