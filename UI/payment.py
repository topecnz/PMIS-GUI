from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtWidgets import *

from db import connection
from datetime import datetime 
class Payment(QWidget):
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
        self.btnBack.setCursor(Qt.CursorShape.PointingHandCursor)
        
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
        self.table.setColumnCount(6)
        self.table.setRowCount(15)
        
        self.table.setHorizontalHeaderLabels(['Payment ID', 'Full Name', 'Stall Type', 'Balance', 'Status', 'Date Due'])
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
            
        self.lblId = QLabel(self)
        self.lblId.setText("")
        self.lblId.setGeometry(640, 220, 600, 30)
        self.lblId.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        
        self.lblPid = QLabel(self)
        self.lblPid.setText("")
        self.lblPid.setGeometry(640, 260, 600, 30)
        self.lblPid.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        
        self.lblFname = QLabel(self)
        self.lblFname.setText("")
        self.lblFname.setGeometry(640, 300, 600, 30)
        self.lblFname.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        
        self.lblStall = QLabel(self)
        self.lblStall.setText("")
        self.lblStall.setGeometry(640, 340, 600, 30)
        self.lblStall.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        
        self.lblStatus = QLabel(self)
        self.lblStatus.setText("")
        self.lblStatus.setGeometry(640, 380, 600, 30)
        self.lblStatus.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        
        self.lblPrice = QLabel(self)
        self.lblPrice.setText("")
        self.lblPrice.setGeometry(640, 420, 600, 30)
        self.lblPrice.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        
        self.lblDue = QLabel(self)
        self.lblDue.setText("")
        self.lblDue.setGeometry(640, 460, 600, 30)
        self.lblDue.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        
        self.lblBalance = QLabel(self)
        self.lblBalance.setText("")
        self.lblBalance.setGeometry(640, 500, 600, 30)
        self.lblBalance.setFont(QFont("Inter", 14, QFont.Weight.Bold))
        
        self.lblAmount = QLabel(self)
        self.lblAmount.setText("")
        self.lblAmount.setGeometry(640, 540, 140, 30)
        self.lblAmount.setFont(QFont("Inter", 14, QFont.Weight.Bold))

        self.tbAmount = QLineEdit(self)
        self.tbAmount.setGeometry(800, 540, 450, 30)
        self.tbAmount.setFont(QFont("Inter", 14, QFont.Weight.Normal))
        self.tbAmount.setValidator(QIntValidator().setBottom(0))
        self.tbAmount.setVisible(False)
        
        self.btnUpdate = QPushButton(self)
        self.btnUpdate.setText("Pay")
        self.btnUpdate.setGeometry(660, 640, 180, 40)
        self.btnUpdate.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnUpdate.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnUpdate.setVisible(False)
        self.btnUpdate.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btnClear = QPushButton(self)
        self.btnClear.setText("Clear")
        self.btnClear.setGeometry(1060, 640, 180, 40)
        self.btnClear.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnClear.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnClear.setVisible(False)
        self.btnClear.setCursor(Qt.CursorShape.PointingHandCursor)
        
        #Listeners
        
        self.table.itemSelectionChanged.connect(self.updateFields)
        self.tbSearch.returnPressed.connect(self.search)
        self.btnUpdate.clicked.connect(self.updatePayment)
        self.btnClear.clicked.connect(self.clearFields)
        
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
            
    def search(self):
        search = self.tbSearch.text()
        self.table.clearContents()
        data = postgres.select(f"SELECT PAY_ID, CONCAT(TEN_FNAME, ' ', TEN_LNAME) AS TEN_NAME, STA_TYPE_NAME, PAY_AMOUNT - PAY_AMOUNT_PAID AS BALANCE, PAY_STATUS, PAY_DUE_DATE FROM PAYMENT INNER JOIN STALL USING (STA_ID) INNER JOIN TENANT USING (TEN_ID) INNER JOIN STALL_TYPE USING (STA_TYPE_ID) WHERE TEN_STATUS != 'Removed' AND (PAY_DUE_DATE >= CURRENT_DATE OR PAY_STATUS = 'Overdue') AND LOWER(CONCAT(PAY_ID,' ', TEN_FNAME, ' ', TEN_LNAME, ' ', STA_TYPE_NAME)) LIKE LOWER('%{search}%') AND PAY_STATUS != 'Paid' ORDER BY PAY_ID;")

        if data:
            self.table.setRowCount(len(data))
            row = 0 # default
            for res in data:
                self.table.setItem(row, 0, QTableWidgetItem(str(res[0])))
                self.table.setItem(row, 1, QTableWidgetItem(res[1]))
                self.table.setItem(row, 2, QTableWidgetItem(res[2]))
                self.table.setItem(row, 3, QTableWidgetItem(str(res[3])))
                self.table.setItem(row, 4, QTableWidgetItem(res[4]))
                self.table.setItem(row, 5, QTableWidgetItem(str(datetime.strptime(str(res[5]).split(" ")[0], "%Y-%m-%d").strftime("%Y/%m/%d"))))
                row = row + 1
        else:
            self.popupMessage("Entry not found!")
            
    def updatePayment(self):
        id = self.lblPid.text().split('\t')[1]
        balance = self.lblBalance.text().split('\t')[1].split('.')[0]
        amount = self.tbAmount.text()
        
        if not amount:
            self.popupMessage("Please enter amount")
            return
        elif int(balance) < int(amount):
            self.popupMessage(f"You can't pay more than {balance}.")
            return
        elif int(amount) <= 0:
            self.popupMessage(f"You must enter from 1 to {balance}.")
            return
        
        data = postgres.query(f"UPDATE PAYMENT SET PAY_AMOUNT_PAID = PAY_AMOUNT_PAID + {int(amount)} WHERE PAY_ID = {id} RETURNING PAY_ID")
        if data:            
            self.popupMessage("Tenant payment updated!")
            self.displayTable()

        self.clearFields()
        
    def clearFields(self):
        self.btnUpdate.setVisible(False)
        self.btnClear.setVisible(False)
        
        self.lblId.setText("")
        self.lblPid.setText("")
        self.lblFname.setText("")
        self.lblStall.setText("")
        self.lblStatus.setText("")
        self.lblPrice.setText("")
        self.lblDue.setText("")
        self.lblBalance.setText("")
        self.lblAmount.setText("")
        self.tbAmount.clear()
        self.tbAmount.setVisible(False)
        
    def displayTable(self):
        self.table.clearContents()
        data = postgres.select("SELECT PAY_ID, CONCAT(TEN_FNAME, ' ', TEN_LNAME) AS TEN_NAME, STA_TYPE_NAME, PAY_AMOUNT - PAY_AMOUNT_PAID AS BALANCE, PAY_STATUS, PAY_DUE_DATE FROM PAYMENT INNER JOIN STALL USING (STA_ID) INNER JOIN TENANT USING (TEN_ID) INNER JOIN STALL_TYPE USING (STA_TYPE_ID) WHERE TEN_STATUS != 'Removed' AND (PAY_DUE_DATE >= CURRENT_DATE OR PAY_STATUS = 'Overdue') AND PAY_STATUS != 'Paid' ORDER BY PAY_ID;")
        
        self.table.setRowCount(len(data))
        row = 0 # default
        for res in data:
            self.table.setItem(row, 0, QTableWidgetItem(str(res[0])))
            self.table.setItem(row, 1, QTableWidgetItem(res[1]))
            self.table.setItem(row, 2, QTableWidgetItem(res[2]))
            self.table.setItem(row, 3, QTableWidgetItem(str(res[3])))
            self.table.setItem(row, 4, QTableWidgetItem(res[4]))
            self.table.setItem(row, 5, QTableWidgetItem(str(datetime.strptime(str(res[5]).split(" ")[0], "%Y-%m-%d").strftime("%Y/%m/%d"))))
            row = row + 1
            
    def updateFields(self):
        self.clearFields()
        item = self.table.selectedItems()
        
        if len(item) == 0:
            return
        
        row = self.table.row(item[0])
        id = self.table.item(row, 0).text()
        res = postgres.select(f"SELECT TEN_ID, PAY_ID, CONCAT(TEN_FNAME, ' ', TEN_LNAME) AS TEN_NAME, STA_TYPE_NAME, PAY_STATUS, PAY_AMOUNT, PAY_DUE_DATE, PAY_AMOUNT - PAY_AMOUNT_PAID AS BALANCE FROM PAYMENT INNER JOIN INVOICE USING (INV_ID) INNER JOIN TENANT USING (TEN_ID) INNER JOIN STALL USING (TEN_ID) INNER JOIN STALL_TYPE USING (STA_TYPE_ID) WHERE PAY_ID = {id};")
        
        # fetch data from tenant id
        data = res[0]
        
        self.lblId.setText("Tenant ID: \t" + str(data[0]))
        self.lblPid.setText("Payment ID: \t" + str(data[1]))
        self.lblFname.setText("Full Name: \t" + data[2])
        self.lblStall.setText("Stall Type: \t" + data[3])
        self.lblStatus.setText("Payment Status: \t" + data[4])
        self.lblPrice.setText("Stall Price: \t" + str(data[5]))
        self.lblDue.setText("Due Date: \t" + str(data[6]))
        self.lblBalance.setText("Balance: \t" + str(data[7]))
        
        if data[4] != 'Paid':
            self.lblAmount.setText("Amount:")
            self.tbAmount.setVisible(True)        
            self.btnUpdate.setVisible(True)
            
        self.btnClear.setVisible(True)
        
        
# initialize some objects here
postgres = connection.PostgreSQL()
