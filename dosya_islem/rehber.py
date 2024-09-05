import sys
from PyQt6.QtWidgets import *

class TicariWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rehberim")
        

        central_widget = QWidget()
        layout = QVBoxLayout()

        label_baslik = QLabel("Rehhber 1.0:")
        layout.addWidget(label_baslik)

    
        button_listele = QPushButton("Listele")
        button_listele.clicked.connect(self.mesaj)
        layout.addWidget(button_listele)

        button_ekle = QPushButton("Ekle")
        button_ekle.clicked.connect(self.mesaj)
        layout.addWidget(button_ekle)

        button_degistir= QPushButton("Değiştir")
        button_degistir.clicked.connect(self.mesaj)
        layout.addWidget(button_degistir)


        
    def mesaj(self):
        cmdeger = int(self.cmdeger_input.text()) * 2
        self.inch_input.setText(str(cmdeger))
       
def main():
    app = QApplication(sys.argv)
    window = TicariWindow()
    QMessageBox.information(window, "Cm-Inch Çevirici", "Inch çevirici uygulamasına hoş geldiniz.")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
