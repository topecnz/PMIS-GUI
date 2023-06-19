from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtWidgets import *

from db import connection
from datetime import datetime 

class Inventory(QWidget):
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
        
        self.lblSubTitle.setText("Market Inventories")
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
        
        self.table = QTableWidget(self)
        self.table.setGeometry(20, 290, 600, 400)
        self.table.setColumnCount(5)
        self.table.setRowCount(15)
        
        self.table.setHorizontalHeaderLabels(['Tenant ID', 'Stall ID', 'Stall Type', 'Name', 'Date Added'])
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
 
        self.lblTenant = QLabel(self)
        self.lblTenant.setText("Tenant ID:")
        self.lblTenant.setGeometry(640, 300, 140, 30)
        self.lblTenant.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblTenant.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.lblId = QLabel(self)
        self.lblId.setText("")
        self.lblId.setGeometry(800, 295, 140, 30)
        self.lblId.setFont(QFont("Inter", 16, QFont.Weight.Bold))

        self.lblFn = QLabel(self)
        self.lblFn.setText("Full Name:")
        self.lblFn.setGeometry(640, 340, 140, 30)
        self.lblFn.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblFn.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.lblFname = QLabel(self)
        self.lblFname.setText("")
        self.lblFname.setGeometry(800, 335, 140, 30)
        self.lblFname.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        
        self.lblItem = QLabel(self)
        self.lblItem.setText("Item(s):")
        self.lblItem.setGeometry(640, 380, 140, 30)
        self.lblItem.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblItem.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbItem = QPlainTextEdit(self)
        self.tbItem.setGeometry(800, 380, 450, 250)
        self.tbItem.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
        self.btnUpdate = QPushButton(self)
        self.btnUpdate.setText("Update")
        self.btnUpdate.setGeometry(660, 640, 180, 40)
        self.btnUpdate.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnUpdate.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnUpdate.setVisible(False)
        
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
        
        #Listeners
        
        self.table.itemSelectionChanged.connect(self.updateFields)
        self.tbSearch.returnPressed.connect(self.search)
        self.btnUpdate.clicked.connect(self.updateInventory)
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
        data = postgres.select(f"SELECT TEN_ID, STA_ID, STA_TYPE_NAME, CONCAT(TEN_FNAME, ' ', TEN_LNAME) AS TEN_NAME, TEN_CREATED_AT FROM TENANT INNER JOIN STALL USING (TEN_ID) INNER JOIN STALL_TYPE USING (STA_TYPE_ID) WHERE LOWER(CONCAT(TEN_ID, ' ', TEN_FNAME, ' ', TEN_LNAME, ' ', STA_ID, ' ', STA_TYPE_NAME)) LIKE LOWER('%{search}%') AND TEN_STATUS != 'Removed' ORDER BY TEN_ID;")
        
        if data:
            self.table.setRowCount(len(data))
            row = 0
            for res in data:
                self.table.setItem(row, 0, QTableWidgetItem(str(res[0])))
                self.table.setItem(row, 1, QTableWidgetItem(str(res[1])))
                self.table.setItem(row, 2, QTableWidgetItem(res[2]))
                self.table.setItem(row, 3, QTableWidgetItem(res[3]))
                self.table.setItem(row, 4, QTableWidgetItem(str(datetime.strptime(str(res[4]).split(" ")[0], "%Y-%m-%d").strftime("%Y/%m/%d"))))
                row = row + 1
        else:
            self.popupMessage("Entry not found!")
    
    def updateInventory(self):
        id = self.lblId.text()
        item = self.tbItem.toPlainText()
        data = postgres.query(f"UPDATE INVENTORY SET INT_ITEM = '{item}' WHERE TEN_ID = {id} RETURNING TEN_ID")
        if data:            
            self.popupMessage("Tenant info updated!")
            self.displayTable()
        
        self.clearFields()
    
    def clearFields(self):
        self.btnUpdate.setVisible(False)
        self.btnClear.setVisible(False)
        
        self.lblId.setText("")
        self.lblFname.setText("")
        self.tbItem.clear()
    
    def displayTable(self):
        self.table.clearContents() # clear everything before adding rows
        data = postgres.select("SELECT TEN_ID, STA_ID, STA_TYPE_NAME, CONCAT(TEN_FNAME, ' ', TEN_LNAME) AS TEN_NAME, TEN_CREATED_AT FROM TENANT INNER JOIN STALL USING (TEN_ID) INNER JOIN STALL_TYPE USING (STA_TYPE_ID) WHERE TEN_STATUS != 'Removed' ORDER BY TEN_ID;")
        
        self.table.setRowCount(len(data))
        row = 0 # default
        for res in data:
            self.table.setItem(row, 0, QTableWidgetItem(str(res[0])))
            self.table.setItem(row, 1, QTableWidgetItem(str(res[1])))
            self.table.setItem(row, 2, QTableWidgetItem(res[2]))
            self.table.setItem(row, 3, QTableWidgetItem(res[3]))
            self.table.setItem(row, 4, QTableWidgetItem(str(datetime.strptime(str(res[4]).split(" ")[0], "%Y-%m-%d").strftime("%Y/%m/%d"))))
            row = row + 1

    def updateFields(self):
        item = self.table.selectedItems()
        
        if len(item) == 0:
            return
        
        row = self.table.row(item[0])
        id = self.table.item(row, 0).text()
        res = postgres.select(f"SELECT * FROM INVENTORY WHERE TEN_ID = {id};")
        
        # fetch data from tenant id
        data = res[0]

        self.lblId.setText(str(data[0]))
        self.lblFname.setText(self.table.item(row, 3).text())
        self.tbItem.setPlainText(data[1])
        
        self.btnUpdate.setVisible(True)
        self.btnClear.setVisible(True)

# initialize some objects here
postgres = connection.PostgreSQL()