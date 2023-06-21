from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize, QDate
from PyQt6.QtGui import QFont, QIntValidator
from PyQt6.QtWidgets import *

from db import connection
from datetime import datetime 

class Stall(QWidget):
    def __init__(self, widget, cookies):
        super().__init__()
        
        # store data
        self.widget = widget
        self.cookies = cookies
        self.category = ['']
        
        self.lblTitle = QLabel(self)
        
        self.lblTitle.setText("Public Market Information System")
        self.lblTitle.setGeometry(0, 40, 1280, 70)
        self.lblTitle.setFont(QFont("Inter", 36, QFont.Weight.Bold))
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.lblSubTitle = QLabel(self)
        
        self.lblSubTitle.setText("Stall Information")
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
        self.table.setColumnCount(6)
        
        self.table.setHorizontalHeaderLabels(['Type ID', 'Name', 'Description', 'Price', 'Status', 'Date Added'])
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
        
        self.lblStall = QLabel()
        self.lblStall.setText("")
        self.lblStall.setGeometry(640, 300, 140, 30)
        self.lblStall.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblStall.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.lblId = QLabel()
        self.lblId.setText("")
        self.lblId.setGeometry(800, 300, 140, 30)
        self.lblId.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        
        self.lblName = QLabel(self)
        self.lblName.setText("Stall Name:")
        self.lblName.setGeometry(640, 340, 140, 30)
        self.lblName.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblName.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbName = QLineEdit(self)
        self.tbName.setGeometry(800, 340, 450, 30)
        self.tbName.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
        self.lblDescription = QLabel(self)
        self.lblDescription.setText("Description:")
        self.lblDescription.setGeometry(640, 380, 140, 30)
        self.lblDescription.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblDescription.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbDescription = QPlainTextEdit(self)
        self.tbDescription.setGeometry(800, 380, 450, 110)
        self.tbDescription.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
        self.lblPrice = QLabel(self)
        self.lblPrice.setText("Price:")
        self.lblPrice.setGeometry(640, 500, 140, 30)
        self.lblPrice.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblPrice.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbPrice = QLineEdit(self)
        self.tbPrice.setGeometry(800, 500, 450, 30)
        self.tbPrice.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbPrice.setValidator(QIntValidator().setBottom(0))
        
        self.lblStatus = QLabel(self)
        self.lblStatus.setText("Status:")
        self.lblStatus.setGeometry(640, 540, 140, 30)
        self.lblStatus.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblStatus.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbStatus = QComboBox(self)
        self.tbStatus.setGeometry(800, 540, 450, 30)
        self.tbStatus.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbStatus.addItems(['Available', 'Unavailable'])
        self.tbStatus.setCurrentIndex(-1)
        self.tbStatus.setStyleSheet("background-color: #ffffff;")
        
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
        self.btnAdd.setCursor(Qt.CursorShape.PointingHandCursor)

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
        self.btnUpdate.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btnRemove = QPushButton(self)
        self.btnRemove.setText("Remove")
        self.btnRemove.setGeometry(860, 640, 180, 40)
        self.btnRemove.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.btnRemove.setStyleSheet(
            """
                border-radius: 10px;
                background-color: #ffffff;
            """
        )
        self.btnRemove.setVisible(False)
        self.btnRemove.setCursor(Qt.CursorShape.PointingHandCursor)
        
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
        self.btnAdd.clicked.connect(self.addStall)
        self.btnUpdate.clicked.connect(self.updateStall)
        self.btnRemove.clicked.connect(self.removeStall)
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
    
    # functionalities
    
    def validate(self):
        name = self.tbName.text()
        price = self.tbPrice.text()
        status = self.tbStatus.currentText()
        
        validate = [
            name, price, status
        ]
        found = True
        
        for v in validate:
            if not v:
                found = False
                break
            
        return found 
    
    def search(self):
        search = self.tbSearch.text()
        self.table.clearContents() # clear everything before adding rows
        data = postgres.select(f"SELECT STA_TYPE_ID, STA_TYPE_NAME, STA_TYPE_DESCRIPTION, STA_TYPE_PRICE, STA_TYPE_STATUS, STA_TYPE_CREATED_AT FROM STALL_TYPE WHERE STA_TYPE_STATUS != 'Removed' AND LOWER(CONCAT(STA_TYPE_ID, ' ',STA_TYPE_NAME)) LIKE LOWER('%{search}%') ORDER BY STA_TYPE_ID")
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
    
    def addStall(self):
        name = self.tbName.text()
        desc = self.tbDescription.toPlainText()
        price = self.tbPrice.text()
        status = self.tbStatus.currentText()
            
        if not self.validate():
            self.popupMessage("You must filled all fields!")
            return
        
        data = postgres.query(f"INSERT INTO STALL_TYPE (STA_TYPE_NAME, STA_TYPE_DESCRIPTION, STA_TYPE_PRICE, STA_TYPE_STATUS) VALUES ('{name}', '{desc}', {price}, '{status}') RETURNING STA_TYPE_ID")
        if data:
            self.popupMessage("Stall info added!")
            self.displayTable()
        else:
            self.popupMessage("Something went wrong!")
            
        self.clearFields()
        
    def updateStall(self):
        id = self.lblId.text()
        name = self.tbName.text()
        desc = self.tbDescription.toPlainText()
        price = self.tbPrice.text()
        status = self.tbStatus.currentText()
            
        if not self.validate():
            self.popupMessage("You must filled all fields!")
            return
        
        data = postgres.query(f"UPDATE STALL_TYPE SET STA_TYPE_NAME = '{name}', STA_TYPE_DESCRIPTION = '{desc}', STA_TYPE_PRICE = {price}, STA_TYPE_STATUS = '{status}', STA_TYPE_UPDATED_AT = CURRENT_TIMESTAMP WHERE STA_TYPE_ID = {id} RETURNING STA_TYPE_ID")

        if data:            
            self.popupMessage("Stall info updated!")
            self.displayTable()
        
        self.clearFields()
        
    def removeStall(self):
        id = self.lblId.text()
        data = postgres.query(f"UPDATE STALL_TYPE SET STA_TYPE_STATUS = 'Removed', STA_TYPE_UPDATED_AT = CURRENT_TIMESTAMP WHERE STA_TYPE_ID = {id} RETURNING STA_TYPE_ID")
        if data:
            self.popupMessage("Stall info removed!")

        self.clearFields()
        self.displayTable()

    def clearFields(self):
        self.btnAdd.setVisible(True)
        self.btnUpdate.setVisible(False)
        self.btnRemove.setVisible(False)
        self.btnClear.setVisible(False)
        
        self.lblStall.setText("")
        self.lblId.setText("")
        self.tbStatus.setCurrentIndex(-1)
        self.tbName.clear()
        self.tbDescription.clear()
        self.tbPrice.clear()
    
    def displayTable(self):
        self.table.clearContents() # clear everything before adding rows
        data = postgres.select("SELECT STA_TYPE_ID, STA_TYPE_NAME, STA_TYPE_DESCRIPTION, STA_TYPE_PRICE, STA_TYPE_STATUS, STA_TYPE_CREATED_AT FROM STALL_TYPE WHERE STA_TYPE_STATUS != 'Removed' ORDER BY STA_TYPE_ID;")
        
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
        item = self.table.selectedItems()
        
        if len(item) == 0:
            return
        
        row = self.table.row(item[0])
        id = self.table.item(row, 0).text()
        res = postgres.select(f"SELECT STA_TYPE_ID, STA_TYPE_NAME, STA_TYPE_DESCRIPTION, STA_TYPE_PRICE, STA_TYPE_STATUS, STA_TYPE_CREATED_AT FROM STALL_TYPE WHERE STA_TYPE_ID = '{id}' AND STA_TYPE_STATUS != 'Removed' ORDER BY STA_TYPE_ID;")
        
        # fetch data from stall type id
        data = res[0]
        
        self.lblStall.setText("Type ID:")
        self.lblId.setText(str(data[0]))
        self.tbName.setText(data[1])
        self.tbDescription.setPlainText(data[2])
        self.tbPrice.setText(str(data[3]))
        self.tbStatus.setCurrentText(data[4])
        
        # update buttons
        self.btnAdd.setVisible(False)
        self.btnUpdate.setVisible(True)
        self.btnRemove.setVisible(True)
        self.btnClear.setVisible(True)

# initialize some objects here
postgres = connection.PostgreSQL()
