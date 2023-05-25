from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtWidgets import *

class Payment(QWidget):
    def __init__(self):
        super().__init__()
        
        self.lblTitle = QLabel(self)
        
        self.lblTitle.setText("Public Market Information System")
        self.lblTitle.setGeometry(0, 40, 1280, 70)
        self.lblTitle.setFont(QFont("Inter", 36, QFont.Weight.Bold))
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.lblSubTitle = QLabel(self)
        
        self.lblSubTitle.setText("Payments")
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
            
        self.lblId = QLabel(self)
        self.lblId.setText("Tenant ID:")
        self.lblId.setGeometry(640, 300, 140, 30)
        self.lblId.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        self.lblId.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.lblFname = QLabel(self)
        self.lblFname.setText("Full name:")
        self.lblFname.setGeometry(640, 340, 140, 30)
        self.lblFname.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        self.lblFname.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.lblStallCode = QLabel(self)
        self.lblStallCode.setText("Stall Code:")
        self.lblStallCode.setGeometry(640, 380, 140, 30)
        self.lblStallCode.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        self.lblStallCode.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.lblLastPay = QLabel(self)
        self.lblLastPay.setText("Last Payment:")
        self.lblLastPay.setGeometry(640, 420, 140, 30)
        self.lblLastPay.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        self.lblLastPay.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.lblBalance = QLabel(self)
        self.lblBalance.setText("Balance:")
        self.lblBalance.setGeometry(640, 460, 140, 30)
        self.lblBalance.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        self.lblBalance.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.lblDue = QLabel(self)
        self.lblDue.setText("Due Date:")
        self.lblDue.setGeometry(640, 500, 140, 30)
        self.lblDue.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        self.lblDue.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.lblAmount = QLabel(self)
        self.lblAmount.setText("Amount:")
        self.lblAmount.setGeometry(640, 540, 140, 30)
        self.lblAmount.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        self.lblAmount.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbAmount = QLineEdit(self)
        self.tbAmount.setGeometry(800, 540, 450, 30)
        self.tbAmount.setFont(QFont("Inter", 14, QFont.Weight.Normal))
        self.tbAmount.setValidator(QIntValidator().setBottom(0))
        
        self.lblMethod = QLabel(self)
        self.lblMethod.setText("Method:")
        self.lblMethod.setGeometry(640, 580, 140, 30)
        self.lblMethod.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        self.lblMethod.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbMethod = QComboBox(self)
        self.tbMethod.setGeometry(800, 580, 450, 30)
        self.tbMethod.setFont(QFont("Inter", 14, QFont.Weight.Normal))
        self.tbMethod.setStyleSheet("background-color: #ffffff;")
            
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
