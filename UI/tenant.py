from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize, QDate, QRegularExpression
from PyQt6.QtGui import QFont, QIntValidator, QRegularExpressionValidator
from PyQt6.QtWidgets import *

from db import connection
from datetime import datetime 

class Tenant(QWidget):
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
        
        self.lblSubTitle.setText("Tenant Information")
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
        
        self.lblTenant = QLabel(self)
        self.lblTenant.setText("")
        self.lblTenant.setGeometry(640, 300, 140, 30)
        self.lblTenant.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblTenant.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.lblId = QLabel(self)
        self.lblId.setText("")
        self.lblId.setGeometry(800, 295, 450, 30)
        self.lblId.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        
        self.lblFname = QLabel(self)
        self.lblFname.setText("First name:")
        self.lblFname.setGeometry(640, 340, 140, 30)
        self.lblFname.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblFname.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbFname = QLineEdit(self)
        self.tbFname.setGeometry(800, 340, 450, 30)
        self.tbFname.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
        self.lblLname = QLabel(self)
        self.lblLname.setText("Last name:")
        self.lblLname.setGeometry(640, 380, 140, 30)
        self.lblLname.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblLname.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbLname = QLineEdit(self)
        self.tbLname.setGeometry(800, 380, 450, 30)
        self.tbLname.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
        self.lblBirth = QLabel(self)
        self.lblBirth.setText("Birthdate:")
        self.lblBirth.setGeometry(640, 420, 140, 30)
        self.lblBirth.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblBirth.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbBirth = QDateEdit(self)
        self.tbBirth.setGeometry(800, 420, 450, 30)
        self.tbBirth.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbBirth.setCalendarPopup(True)
        self.tbBirth.setDisplayFormat("yyyy/MM/dd")
        
        self.lblAdd = QLabel(self)
        self.lblAdd.setText("Address:")
        self.lblAdd.setGeometry(640, 460, 140, 30)
        self.lblAdd.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblAdd.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbAdd = QLineEdit(self)
        self.tbAdd.setGeometry(800, 460, 450, 30)
        self.tbAdd.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
        self.lblPhone = QLabel(self)
        self.lblPhone.setText("Phone:")
        self.lblPhone.setGeometry(640, 500, 140, 30)
        self.lblPhone.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblPhone.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbPhone = QLineEdit(self)
        self.tbPhone.setGeometry(800, 500, 450, 30)
        self.tbPhone.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbPhone.setValidator(QRegularExpressionValidator(QRegularExpression(r"\d{0,12}")))
        
        self.lblCat = QLabel(self)
        self.lblCat.setText("Stall Type:")
        self.lblCat.setGeometry(640, 540, 140, 30)
        self.lblCat.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblCat.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbCat = QComboBox(self)
        self.tbCat.setGeometry(800, 540, 450, 30)
        self.tbCat.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbCat.addItems(self.category)
        self.tbCat.setStyleSheet("background-color: #ffffff;")
        
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
        self.btnAdd.clicked.connect(self.addTenant)
        self.btnUpdate.clicked.connect(self.updateTenant)
        self.btnRemove.clicked.connect(self.removeTenant)
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
        fname = self.tbFname.text()
        lname = self.tbLname.text()
        bd = self.tbBirth.text()
        address = self.tbAdd.text()
        phone = self.tbPhone.text()
        category = self.tbCat.currentText().split(" ")[0]
        
        validate = [
            fname, lname, bd, address, phone, category
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
        data = postgres.select(f"SELECT TEN_ID, PER_LNAME, PER_FNAME, PER_PHONE, TEN_CREATED_AT FROM TENANT INNER JOIN PERSON (PER_ID) WHERE TEN_STATUS != 'Removed' AND LOWER(CONCAT(TEN_ID, ' ', PER_FNAME, ' ', PER_LNAME)) LIKE LOWER('%{search}%') ORDER BY TEN_ID")
        if data:
            self.table.setRowCount(len(data))
            row = 0 # default
            for res in data:
                self.table.setItem(row, 0, QTableWidgetItem(str(res[0])))
                self.table.setItem(row, 1, QTableWidgetItem(res[1]))
                self.table.setItem(row, 2, QTableWidgetItem(res[2]))
                self.table.setItem(row, 3, QTableWidgetItem(res[3]))
                self.table.setItem(row, 4, QTableWidgetItem(str(datetime.strptime(str(res[4]).split(" ")[0], "%Y-%m-%d").strftime("%Y/%m/%d"))))
                row = row + 1
        else:
            self.popupMessage("Entry not found!")
    
    def addTenant(self):
        fname = self.tbFname.text()
        lname = self.tbLname.text()
        bd = self.tbBirth.text()
        address = self.tbAdd.text()
        phone = self.tbPhone.text()
        category = self.tbCat.currentText().split(" ")[0]
            
        if not self.validate():
            self.popupMessage("You must filled all fields!")
            return
        
        data = postgres.query(f"INSERT INTO PERSON (PER_FNAME, PER_LNAME, PER_BIRTHDATE, PER_ADDRESS, PER_PHONE, PER_IS_EMP) VALUES ('{fname}', '{lname}', '{bd}', '{address}', '{phone}', true) ON CONFLICT (PER_FNAME, PER_LNAME, PER_BIRTHDATE) DO UPDATE SET PER_ADDRESS = '{address}', PER_PHONE = '{phone}', PER_IS_EMP = true, PER_UPDATED_AT = CURRENT_TIMESTAMP RETURNING PER_ID")
        if data:
            data = postgres.query(f"INSERT INTO TENANT (PER_ID) VALUES ({data[0]}) ON CONFLICT (PER_ID) DO UPDATE SET TEN_STATUS = 'Active', TEN_UPDATED_AT = CURRENT_TIMESTAMP RETURNING TEN_ID;")
            if data:
                data = postgres.query(f"INSERT INTO STALL (STA_TYPE_ID, TEN_ID) VALUES ({category}, {data[0]}) ON CONFLICT (TEN_ID) DO UPDATE SET STA_TYPE_ID = {category},  STA_STATUS = 'Active', STA_UPDATED_AT = CURRENT_TIMESTAMP RETURNING STA_ID;")
                if data:
                    self.popupMessage("Tenant info added!")
                    self.displayTable()
                else:
                    self.popupMessage("Something went wrong!")
            else:
                self.popupMessage("Something went wrong!")
        else:
            self.popupMessage("Something went wrong!")
            
        self.clearFields()
        
    def updateTenant(self):
        id = self.lblId.text().split('-')
        fname = self.tbFname.text()
        lname = self.tbLname.text()
        bd = self.tbBirth.text()
        address = self.tbAdd.text()
        phone = self.tbPhone.text()
        category = self.tbCat.currentText().split(" ")[0]
        
        if not self.validate():
            self.popupMessage("You must filled all fields!")
            return
        
        data = postgres.query(f"UPDATE PERSON SET PER_FNAME = '{fname}', PER_LNAME = '{lname}', PER_BIRTHDATE = '{bd}', PER_ADDRESS = '{address}', PER_PHONE = '{phone}', PER_UPDATED_AT = CURRENT_TIMESTAMP WHERE PER_ID = {id[0]} RETURNING PER_ID")

        if data:    
            data = postgres.query(f"UPDATE STALL SET STA_TYPE_ID = {category} WHERE TEN_ID = {id[1]} RETURNING TEN_ID")
            if data:
                self.popupMessage("Tenant info updated!")
                self.clearFields()
                self.displayTable()
            else:
                self.popupMessage("Something went wrong!")
        else:
            self.popupMessage("Something went wrong!")
        
        self.clearFields()
        
    def removeTenant(self):
        id = self.lblId.text().split('-')[1]
        data = postgres.query(f"UPDATE TENANT SET TEN_STATUS = 'Removed', TEN_UPDATED_AT = CURRENT_TIMESTAMP WHERE TEN_ID = {id} RETURNING TEN_ID")
        if data:
            self.popupMessage("tenant info removed!")

        self.clearFields()
        self.displayTable()

    def clearFields(self):
        self.btnAdd.setVisible(True)
        self.btnUpdate.setVisible(False)
        self.btnRemove.setVisible(False)
        self.btnClear.setVisible(False)
        
        self.lblTenant.setText("")
        self.lblId.setText("")
        self.tbCat.setCurrentIndex(-1)
        self.tbFname.clear()
        self.tbLname.clear()
        self.tbBirth.setDate(QDate())
        self.tbAdd.clear()
        self.tbPhone.clear()
    
    def displayTable(self):
        self.table.clearContents() # clear everything before adding rows
        data = postgres.select("SELECT TEN_ID, PER_LNAME, PER_FNAME, PER_PHONE, TEN_CREATED_AT FROM TENANT INNER JOIN PERSON USING (PER_ID) WHERE TEN_STATUS != 'Removed' ORDER BY TEN_ID;")
        
        self.table.setRowCount(len(data))
        row = 0 # default
        for res in data:
            self.table.setItem(row, 0, QTableWidgetItem(str(res[0])))
            self.table.setItem(row, 1, QTableWidgetItem(res[1]))
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
        res = postgres.select(f"SELECT PER_ID, TEN_ID, PER_FNAME, PER_LNAME, PER_BIRTHDATE, PER_ADDRESS, PER_PHONE, STA_TYPE_ID, STA_TYPE_NAME FROM PERSON INNER JOIN TENANT USING (PER_ID) INNER JOIN STALL USING (TEN_ID) INNER JOIN STALL_TYPE USING (STA_TYPE_ID) WHERE TEN_ID = '{id}' AND TEN_STATUS != 'Removed';")
        
        # fetch data from account id
        data = res[0]
        
        self.lblTenant.setText("Tenant ID:")
        self.lblId.setText(str(data[0]) + "-" + str(data[1]))
        self.tbFname.setText(data[2])
        self.tbLname.setText(data[3])
        self.tbBirth.setDate(QDate.fromString(str(data[4]), "yyyy-MM-dd"))
        self.tbAdd.setText(data[5])
        self.tbPhone.setText(data[6])
        self.tbCat.setCurrentText(f"{data[7]} {data[8]}")
        
        # update buttons
        self.btnAdd.setVisible(False)
        self.btnUpdate.setVisible(True)
        self.btnRemove.setVisible(True)
        self.btnClear.setVisible(True)
    
    def stallCat(self):
        self.category.clear()
        self.tbCat.clear()
        data = postgres.select("SELECT STA_TYPE_ID, STA_TYPE_NAME FROM STALL_TYPE WHERE STA_TYPE_STATUS = 'Available' ORDER BY STA_TYPE_ID;")
        for r in data:
            self.category.append(f"{r[0]} {r[1]}")
            
        self.tbCat.addItems(self.category)

# initialize some objects here
postgres = connection.PostgreSQL()
