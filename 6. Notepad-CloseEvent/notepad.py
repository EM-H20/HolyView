import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


#만들어진 ui 가져오기
form_class = uic.loadUiType("C:\\coding_File\\vscode\\PyQt_study\\6. Notepad-CloseEvent\\notepad.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self): #생성자
        super().__init__()
        self.setupUi(self)

        #열기, 저장, 다른이름으로 저장, 끝내기 트리거
        self.action_open.triggered.connect(self.openFunction)
        self.action_save.triggered.connect(self.saveFunction)
        self.action_saveas.triggered.connect(self.saveAsFunction)
        self.action_close.triggered.connect(self.close)

        self.opened = False
        self.opened_file_path = ''

    #끝내기 함수
    def closeEvent(self, event):
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