from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtWidgets import *

class Report(QWidget):
    def __init__(self, widget, cookies):
        super().__init__()
        
        # store data
        self.widget = widget
        self.cookies = cookies
        
        self.lblTitle = QLabel(self)
        
        self.lblTitle.setText("Public Market Information System")
        self.lblTitle.setGeometry(0, 40, 1280, 70)
        self.lblTitle.setFont(QFont("Inter", 36, QFont.Weight.Bold))
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.lblSubTitle = QLabel(self)
        
        self.lblSubTitle.setText("Report")
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
        
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 250, 750, 400)
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
            
        self.lblFname = QLabel(self)
        self.lblFname.setText("Report Date")
        self.lblFname.setGeometry(800, 250, 450, 30)
        self.lblFname.setFont(QFont("Inter", 12, QFont.Weight.Bold))
        self.lblFname.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.lblDateFrom = QLabel(self)
        self.lblDateFrom.setText("Date From")
        self.lblDateFrom.setGeometry(850, 270, 150, 30)
        self.lblDateFrom.setFont(QFont("Inter", 10, QFont.Weight.Bold))
        self.lblDateFrom.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tbDateFrom = QDateEdit(self)
        self.tbDateFrom.setGeometry(850, 300, 150, 30)
        self.tbDateFrom.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbDateFrom.setCalendarPopup(True)
        self.tbDateFrom.setDisplayFormat("yyyy/MM/dd")
        
        self.lblDateFrom = QLabel(self)
        self.lblDateFrom.setText("Date To")
        self.lblDateFrom.setGeometry(1050, 270, 150, 30)
        self.lblDateFrom.setFont(QFont("Inter", 10, QFont.Weight.Bold))
        self.lblDateFrom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.tbDateTo = QDateEdit(self)
        self.tbDateTo.setGeometry(1050, 300, 150, 30)
        self.tbDateTo.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbDateTo.setCalendarPopup(True)
        self.tbDateTo.setDisplayFormat("yyyy/MM/dd")
        
        self.btnView = QPushButton(self)
        self.btnView.setText("View")
        self.btnView.setGeometry(950, 350, 150, 30)
        self.btnView.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnView.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.btnView7D = QPushButton(self)
        self.btnView7D.setText("View 7D")
        self.btnView7D.setGeometry(850, 450, 350, 30)
        self.btnView7D.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnView7D.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.btnView30D = QPushButton(self)
        self.btnView30D.setText("View 30D")
        self.btnView30D.setGeometry(850, 490, 350, 30)
        self.btnView30D.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnView30D.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.btnView90D = QPushButton(self)
        self.btnView90D.setText("View 90D")
        self.btnView90D.setGeometry(850, 530, 350, 30)
        self.btnView90D.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnView90D.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        
        self.btnView365D = QPushButton(self)
        self.btnView365D.setText("View 365D")
        self.btnView365D.setGeometry(850, 570, 350, 30)
        self.btnView365D.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnView365D.setStyleSheet(
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
