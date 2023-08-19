from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.ap=app #declare an application member
        self.setWindowTitle("First App")
        
        menu=self.menuBar()
        file_menu=menu.addMenu("File")
        quit_action=file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit)
        edit_menu=menu.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Copy")
        
        button=QPushButton("Click Me!")
        self.setCentralWidget(button)
    
    def quit(self):
       self.ap.quit()
