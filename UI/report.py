from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize, QDate
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtWidgets import *

from db import connection
from datetime import datetime

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
        self.table.setColumnCount(7)
        
        self.table.setHorizontalHeaderLabels(['Invoice ID', 'Tenant ID', 'Tenant Name', 'Stall Type', 'Amount', 'Payment ID', 'Date Dute'])
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
        
        self.lblRevenue = QLabel(self)
        self.lblRevenue.setText("")
        self.lblRevenue.setGeometry(20, 650, 750, 30)
        self.lblRevenue.setFont(QFont("Inter", 12, QFont.Weight.Bold))
            
        self.lblReportDate = QLabel(self)
        self.lblReportDate.setText("Report Date")
        self.lblReportDate.setGeometry(800, 250, 450, 30)
        self.lblReportDate.setFont(QFont("Inter", 12, QFont.Weight.Bold))
        self.lblReportDate.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
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
        self.tbDateFrom.setDate(QDate.currentDate())
        self.tbDateFrom.setMaximumDate(QDate.currentDate())
        
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
        self.tbDateTo.setDate(QDate.currentDate())
        self.tbDateTo.setMaximumDate(QDate.currentDate())
        
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
        self.btnView.setCursor(Qt.CursorShape.PointingHandCursor)
        
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
        self.btnView7D.setCursor(Qt.CursorShape.PointingHandCursor)
        
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
        self.btnView30D.setCursor(Qt.CursorShape.PointingHandCursor)

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
        self.btnView90D.setCursor(Qt.CursorShape.PointingHandCursor)

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
        self.btnView365D.setCursor(Qt.CursorShape.PointingHandCursor)

        #Listeners
        
        self.btnView.clicked.connect(self.view)
        self.btnView7D.clicked.connect(self.view7D)
        self.btnView30D.clicked.connect(self.view30D)
        self.btnView90D.clicked.connect(self.view90D)
        self.btnView365D.clicked.connect(self.view365D)
            
    def popupMessage(self, message):
        msg = QMessageBox(self)
        msg.setWindowTitle("Message")
        msg.setText(message)
        msg.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        msg.setFixedSize(QSize(500, 250))
        # msg.setIcon(QMessageBox.Icon.Critical)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg.exec()
        
    def view(self):
        self.table.clearContents()
        
        dateFrom = self.tbDateFrom.text()
        dateTo = self.tbDateTo.text()
        
        if (datetime.strptime(dateTo, '%Y/%m/%d') - datetime.strptime(dateFrom, '%Y/%m/%d')).days < 0:
            self.popupMessage("You can't view reports that the Date To is lesser than Date From")
            return
        
        data = postgres.select(f"SELECT INV_ID, TEN_ID, CONCAT(TEN_FNAME, ' ', TEN_LNAME) AS TEN_NAME, STA_TYPE_NAME, INV_AMOUNT, PAY_ID, INV_DATE FROM INVOICE INNER JOIN TENANT USING (TEN_ID) INNER JOIN STALL USING (TEN_ID) INNER JOIN STALL_TYPE USING (STA_TYPE_ID) WHERE INV_DATE BETWEEN '{dateFrom}' AND '{dateTo}' ORDER BY INV_ID;")
        
        if data:
            self.displayTable(data)
        else:
            self.popupMessage("Records are empty!")
        
    def view7D(self):
        self.table.clearContents()
        data = postgres.select("SELECT INV_ID, TEN_ID, CONCAT(TEN_FNAME, ' ', TEN_LNAME) AS TEN_NAME, STA_TYPE_NAME, INV_AMOUNT, PAY_ID, INV_DATE FROM INVOICE INNER JOIN TENANT USING (TEN_ID) INNER JOIN STALL USING (TEN_ID) INNER JOIN STALL_TYPE USING (STA_TYPE_ID) WHERE INV_DATE BETWEEN CURRENT_DATE - INTERVAL '7 DAY' AND CURRENT_DATE ORDER BY INV_ID;")
        
        if data:
            self.displayTable(data)
        else:
            self.popupMessage("Records are empty!")

    def view30D(self):
        self.table.clearContents()
        data = postgres.select("SELECT INV_ID, TEN_ID, CONCAT(TEN_FNAME, ' ', TEN_LNAME) AS TEN_NAME, STA_TYPE_NAME, INV_AMOUNT, PAY_ID, INV_DATE FROM INVOICE INNER JOIN TENANT USING (TEN_ID) INNER JOIN STALL USING (TEN_ID) INNER JOIN STALL_TYPE USING (STA_TYPE_ID) WHERE INV_DATE BETWEEN CURRENT_DATE - INTERVAL '30 DAY' AND CURRENT_DATE ORDER BY INV_ID;")
        
        if data:
            self.displayTable(data)
        else:
            self.popupMessage("Records are empty!")

    def view90D(self):
        self.table.clearContents()
        data = postgres.select("SELECT INV_ID, TEN_ID, CONCAT(TEN_FNAME, ' ', TEN_LNAME) AS TEN_NAME, STA_TYPE_NAME, INV_AMOUNT, PAY_ID, INV_DATE FROM INVOICE INNER JOIN TENANT USING (TEN_ID) INNER JOIN STALL USING (TEN_ID) INNER JOIN STALL_TYPE USING (STA_TYPE_ID) WHERE INV_DATE BETWEEN CURRENT_DATE - INTERVAL '90 DAY' AND CURRENT_DATE ORDER BY INV_ID;")
        
        if data:
            self.displayTable(data)
        else:
            self.popupMessage("Records are empty!")

    def view365D(self):
        self.table.clearContents()
        data = postgres.select("SELECT INV_ID, TEN_ID, CONCAT(TEN_FNAME, ' ', TEN_LNAME) AS TEN_NAME, STA_TYPE_NAME, INV_AMOUNT, PAY_ID, INV_DATE FROM INVOICE INNER JOIN TENANT USING (TEN_ID) INNER JOIN STALL USING (TEN_ID) INNER JOIN STALL_TYPE USING (STA_TYPE_ID) WHERE INV_DATE BETWEEN CURRENT_DATE - INTERVAL '365 DAY' AND CURRENT_DATE ORDER BY INV_ID;")
        
        if data:
            self.displayTable(data)
        else:
            self.popupMessage("Records are empty!")

        
    def displayTable(self, data=None):
        if not data:
            self.view7D()
            return
        
        row = 0 # default
        revenue = 0
        self.table.setRowCount(len(data))
        for res in data:
            self.table.setItem(row, 0, QTableWidgetItem(str(res[0])))
            self.table.setItem(row, 1, QTableWidgetItem(str(res[1])))
            self.table.setItem(row, 2, QTableWidgetItem(res[2]))
            self.table.setItem(row, 3, QTableWidgetItem(res[3]))
            self.table.setItem(row, 4, QTableWidgetItem(str(res[4])))
            self.table.setItem(row, 5, QTableWidgetItem(str(res[5])))
            self.table.setItem(row, 6, QTableWidgetItem(str(datetime.strptime(str(res[6]).split(" ")[0], "%Y-%m-%d").strftime("%Y/%m/%d"))))
            row = row + 1
            
            # calculate revenue
            revenue += res[4]
        
        self.lblRevenue.setText(f"Revenue: {revenue}")

# initialize some objects here
postgres = connection.PostgreSQL()
