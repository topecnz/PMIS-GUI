from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize, QDate, QRegularExpression
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from db import connection
from datetime import datetime 

class Staff(QWidget):
    def __init__(self, widget, cookies):
        super().__init__()
        
        # store data
        self.widget = widget
        self.cookies = cookies
        self.position = ['']
        
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
        
        self.table.setHorizontalHeaderLabels(['Employee ID', 'Lastname', 'Firstname', 'Phone', 'Date Added'])
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

        self.lblEmp = QLabel(self)
        self.lblEmp.setText("")
        self.lblEmp.setGeometry(640, 220, 140, 30)
        self.lblEmp.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblEmp.setAlignment(Qt.AlignmentFlag.AlignRight)
        
        self.lblId = QLabel(self)
        self.lblId.setText("")
        self.lblId.setGeometry(800, 215, 450, 30)
        self.lblId.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        
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
        self.tbPasword.setEchoMode(QLineEdit.EchoMode.Password)
            
        self.lblPosition = QLabel(self)
        self.lblPosition.setText("Position:")
        self.lblPosition.setGeometry(640, 340, 140, 30)
        self.lblPosition.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblPosition.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbPosition = QComboBox(self)
        self.tbPosition.setGeometry(800, 340, 450, 30)
        self.tbPosition.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        self.tbPosition.setStyleSheet("background-color: #ffffff;")
        
        self.lblFname = QLabel(self)
        self.lblFname.setText("First name:")
        self.lblFname.setGeometry(640, 420, 140, 30)
        self.lblFname.setFont(QFont("Inter", 16, QFont.Weight.Bold))
        self.lblFname.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.tbFname = QLineEdit(self)
        self.tbFname.setGeometry(800, 420, 450, 30)
        self.tbFname.setFont(QFont("Inter", 16, QFont.Weight.Normal))
        
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
        self.btnAdd.clicked.connect(self.addStaff)
        self.btnUpdate.clicked.connect(self.updateStaff)
        self.btnRemove.clicked.connect(self.removeStaff)
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
    
    def search(self):
        search = self.tbSearch.text()
        self.table.clearContents() # clear everything before adding rows
        data = postgres.select(f"SELECT EMP_ID, PER_LNAME, PER_FNAME, PER_PHONE, PER_CREATED_AT FROM PERSONAL INNER JOIN EMPLOYEE USING (PER_ID) WHERE EMP_TYPE_ID != 3 AND EMP_STATUS != 'Removed' AND LOWER(CONCAT(EMP_ID, ' ', PER_FNAME, ' ', PER_LNAME)) LIKE LOWER('%{search}%') AND EMP_TYPE_ID != 3 ORDER BY EMP_ID")
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

    def validate(self):
        fname = self.tbFname.text()
        lname = self.tbLname.text()
        bd = self.tbBirth.text()
        address = self.tbAdd.text()
        phone = self.tbPhone.text()
        username = self.tbUser.text()
        password = self.tbPasword.text()
        acc_type = self.tbPosition.currentIndex()
        
        validate = [
            fname, lname, bd, address, phone, username, password, acc_type
        ]
        found = True
        
        for v in validate:
            if not v:
                found = False
                break
            
        return found
    
    def addStaff(self):
        fname = self.tbFname.text()
        lname = self.tbLname.text()
        bd = self.tbBirth.text()
        address = self.tbAdd.text()
        phone = self.tbPhone.text()
        username = self.tbUser.text()
        password = self.tbPasword.text()
        acc_type = self.tbPosition.currentIndex()
            
        if not self.validate():
            self.popupMessage("You must filled all fields!")
            return
        
        data = postgres.query(f"INSERT INTO PERSONAL (PER_FNAME, PER_LNAME, PER_BIRTHDATE, PER_ADDRESS, PER_PHONE, PER_TYPE_ID) VALUES ('{fname}', '{lname}', '{bd}', '{address}', '{phone}', 1) RETURNING PER_ID")
        if data:
            data = postgres.query(f"INSERT INTO EMPLOYEE (PER_ID, EMP_TYPE_ID) VALUES ({data[0]}, {acc_type}) RETURNING EMP_ID;")
            if data:
                data = postgres.query(f"INSERT INTO ACCOUNT (EMP_ID, ACC_USERNAME, ACC_PASSWORD) VALUES ({data[0]}, '{username}', '{password}') RETURNING EMP_ID;")
                if data:
                    self.popupMessage("Staff info added!")
                    self.displayTable()
                else:
                    self.popupMessage("Something went wrong!")
            else:
                self.popupMessage("Something went wrong!")
        else:
            self.popupMessage("Something went wrong!")
            
        self.clearFields()
            
    def updateStaff(self):
        id = self.lblId.text().split('-')
        fname = self.tbFname.text()
        lname = self.tbLname.text()
        bd = self.tbBirth.text()
        address = self.tbAdd.text()
        phone = self.tbPhone.text()
        username = self.tbUser.text()
        password = self.tbPasword.text()
        acc_type = self.tbPosition.currentIndex()
        
        if not self.validate():
            self.popupMessage("You must filled all fields!")
            return

        data = postgres.query(f"UPDATE PERSONAL SET PER_FNAME = '{fname}', PER_LNAME = '{lname}', PER_BIRTHDATE = '{bd}', PER_ADDRESS = '{address}', PER_PHONE = '{phone}', PER_UPDATED_AT = CURRENT_TIMESTAMP WHERE PER_ID = {id[0]} RETURNING PER_ID")

        if data:
            data = postgres.query(f"UPDATE EMPLOYEE SET EMP_TYPE_ID = {acc_type} WHERE EMP_ID = {id[1]} RETURNING EMP_ID")
            if data:
                data = postgres.query(f"UPDATE ACCOUNT SET ACC_USERNAME = '{username}', ACC_PASSWORD = '{password}' WHERE EMP_ID = {data[0]} RETURNING EMP_ID")
                if data:
                    self.popupMessage("Staff info updated!")
                    self.clearFields()
                    self.displayTable()
                else:
                    self.popupMessage("Someting went wrong!")
            else:
                self.popupMessage("Someting went wrong!")
        else:
            self.popupMessage("Someting went wrong!")
        
        self.clearFields()

    def removeStaff(self):
        id = self.lblId.text().split('-')[1]
        data = postgres.query(f"UPDATE EMPLOYEE SET EMP_STATUS = 'Removed', EMP_UPDATED_AT = CURRENT_TIMESTAMP WHERE EMP_ID = {id} RETURNING EMP_ID")
        if data:
            self.popupMessage("staff info removed!")

        self.clearFields()
        self.displayTable()

    def clearFields(self):
        # update buttons
        self.btnAdd.setVisible(True)
        self.btnUpdate.setVisible(False)
        self.btnRemove.setVisible(False)
        self.btnClear.setVisible(False)
        
        self.lblEmp.setText("")
        self.lblId.setText("")
        self.tbUser.clear()
        self.tbPasword.clear()
        self.staffPos()
        self.tbPosition.setCurrentIndex(-1)
        self.tbPosition.setDisabled(False)
        self.tbFname.clear()
        self.tbLname.clear()
        self.tbBirth.setDate(QDate())
        self.tbAdd.clear()
        self.tbPhone.clear()
    
    def displayTable(self):
        self.table.clearContents() # clear everything before adding rows
        data = postgres.select("SELECT EMP_ID, PER_LNAME, PER_FNAME, PER_PHONE, PER_CREATED_AT FROM PERSONAL INNER JOIN EMPLOYEE USING (PER_ID) WHERE EMP_TYPE_ID != 3 AND EMP_STATUS != 'Removed' ORDER BY EMP_ID;")
        
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
        
        self.clearFields() # just to be sure
        row = self.table.row(item[0])
        id = self.table.item(row, 0).text()
        res = postgres.select(f"SELECT PER_ID, EMP_ID, ACC_USERNAME, ACC_PASSWORD, EMP_TYPE_ID, PER_FNAME, PER_LNAME, PER_BIRTHDATE, PER_ADDRESS, PER_PHONE FROM ACCOUNT INNER JOIN EMPLOYEE USING (EMP_ID) INNER JOIN PERSONAL USING (PER_ID) WHERE EMP_ID = '{id}' AND EMP_STATUS != 'Removed';")
        
        # fetch data from account id
        data = res[0]
        
        self.lblEmp.setText("Employee ID:")
        self.lblId.setText(str(data[0]) + "-" + str(data[1]))
        self.tbUser.setText(data[2])
        self.tbPasword.setText(data[3])
        self.tbPosition.clear()
        self.tbPosition.addItems(self.position)
        self.tbPosition.setCurrentIndex(int(data[4]))
        self.tbFname.setText(data[5])
        self.tbLname.setText(data[6])
        self.tbBirth.setDate(QDate.fromString(str(data[7]), "yyyy-MM-dd"))
        self.tbAdd.setText(data[8])
        self.tbPhone.setText(data[9])

        # update buttons
        self.btnAdd.setVisible(False)
        self.btnUpdate.setVisible(True)
        self.btnRemove.setVisible(True)
        self.btnClear.setVisible(True)
                
        # Disable position field section if the user is admin.
        # The owner can change to their employees.
        if self.cookies.data['type'] == 2:
            self.tbPosition.setDisabled(True)
            
        # Admins can't remove themselves.
        if self.cookies.data['type'] == data[4]:
            self.btnRemove.setVisible(False)
        
    
    # just to initialize the position
    def staffPos(self):
        self.position.clear()
        self.tbPosition.clear()
        data = postgres.select("SELECT EMP_TYPE_ID, EMP_TYPE_NAME FROM EMPLOYEE_TYPE WHERE EMP_TYPE_ID != 3 ORDER BY EMP_TYPE_ID;")
        for r in data:
            self.position.append(r[1])

        self.position.insert(0, '')
        lists = self.position if self.cookies.data["type"] == 3 else ['', 'Staff']
        self.tbPosition.addItems(lists)
        

# initialize some objects here
postgres = connection.PostgreSQL()
