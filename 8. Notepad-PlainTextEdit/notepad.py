import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


#만들어진 ui 가져오기
form_class = uic.loadUiType("C:\\coding_File\\vscode\\PyQt_study\\8. Notepad-PlainTextEdit\\notepad.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self): #생성자
        super().__init__()
        self.setupUi(self)

        #각종 트리거
        self.action_open.triggered.connect(self.openFunction)     #열기
        self.action_save.triggered.connect(self.saveFunction)     #저장
        self.action_saveas.triggered.connect(self.saveAsFunction) #다름이름으로 저장
        self.action_close.triggered.connect(self.close)           #끝내기

        self.opened = False
        self.opened_file_path = '제목 없음'

    #저장, 저장 안 함, 취소 MessageBox 
    def save_changed_data(self):
        msgBox = QMessageBox()
        msgBox.setText("변경 내용을 {}에 저장하시겠습니까?".format(self.opened_file_path))
        msgBox.addButton('저장', QMessageBox.YesRole) #0
        msgBox.addButton('저장 안 함', QMessageBox.NoRole) #1
        msgBox.addButton('취소', QMessageBox.RejectRole) #2
        return msgBox.exec_()        

    #끝내기 함수
    def closeEvent(self, event):
        if self.save_changed_data() == 2: #취소버튼 눌렀을 때
            event.ignore() #이벤트 무시

        print("Close test")
  
        
    #저장파일
    def save_file(self, fname):
        # 데이터 불러오고
        data = self.plainTextEdit.toPlainText()
            
        #write 모드로 하고, 데이터 쓰기
        with open(fname, 'w', encoding='UTF8') as f:  
            f.write(data)
          
        #열렸다는 거 할려주는 flag
        self.opened = True
        self.opened_file_path = fname  
 
        print("save {}!!".format(fname))

    #열기파일
    def open_file(self, fname):
        #read 모드로 하고, 데이터 읽기
        with open(fname, encoding='UTF8') as f:
            data = f.read()
        self.plainTextEdit.setPlainText(data)

        #열렸다는 거 할려주는 flag
        self.opened = True
        self.opened_file_path = fname

        print("open {}!!".format(fname))

    #열기 함수
    def openFunction(self):
        #open 형태로 데이터 가져올 거
        fname = QFileDialog.getOpenFileName(self)
        if fname[0]: # 파일 읽기
            self.open_file(fname[0])
       
    #저장 함수
    def saveFunction(self):
        #열려 있으면 열기 파일로 이동
        if self.opened:
            self.save_file(self.opened_file_path)
        #안 열려 있으면 다름이름으로 저장으로 이동
        else:
            self.saveAsFunction()

    #다른이름으로 저장 함수
    def saveAsFunction(self):
        #저장 형태로 데이터 가져올 것
        fname = QFileDialog.getSaveFileName(self) 

        if fname[0]: # 파일 쓰기
            self.save_file(fname[0])


app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()