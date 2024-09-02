# from PyQt6.QtWidgets import *

# app = QApplication([])
# label = QLabel("Merhaba!")
# label.show()

# app.exec()

# xxx = QApplication([])
# label = label = QLabel("Merhaba2!")
# label.show()
# app.exec()

# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

# app = QApplication(sys.argv) # type: ignore

# x = QWidget()

# x.setWindowTitle("Deneme")
# x.resize(300,100)
# # x.setFixedSize(100, 100)

# x.show()


# window1 = QPushButton("tıkla")
# x.setWindowTitle("Deneme22")
# x.resize(300,100)
# # x.setFixedSize(100, 100)


# window1.show()
# aa = QLabel("MERHABA")
# aa.show()

# app.exec()

# from PyQt6.QtWidgets import *

# class CeviriPenceresi(QMainWindow):

#     def __init__(self,baslik,g=0,y=0):
#         super().__init__() 
#         super().setWindowTitle(baslik)
#         if g!=0: and y!=0: self.resize(g,y)

#         içerik = QVBoxLayout()

#         içerik.addWidget(QLabel("Çevrilecek :"))
#         içerik.addWidget(QLineEdit(""))
#         içerik.addWidget(QPushButton("Çevir"))
#         içerik.addWidget(QLabel("Sonuç : "))

#         araclar = QWidget()
#         araclar.setLayout(içerik)
#         self.setCentralWidget(araclar)

# uygulama = QApplication([])

# pencere = CeviriPenceresi("Pencere1")
# pencere2 = CeviriPenceresi("Pencere2")
# pencere.show()
# pencere2.show()
         
# uygulama.exec()

#Login ekranı Tasarımı
# import sys 

# from PyQt6.QtWidgets import QLineEdit, QApplication, QMainWindow, QVBoxLayout, QLabel, QLayout,QCheckBox,QPushButton,QWidget

# app = QApplication(sys.argv)

# widget =QWidget()
# layout = QVBoxLayout()  #layout = QHBoxLayout() ---->>> YAN YANA SIRALAR
# window = QMainWindow()
# window.setWindowTitle("... Uygulaması")
# window.setFixedWidth(300)
# window.setFixedHeight(300)

# layout.addWidget(QLabel("Kullanıcı Adı : "))
# layout.addWidget(QLineEdit())
# layout.addWidget(QLabel("Şifre :"))
# layout.addWidget(QLineEdit())
# layout.addWidget(QCheckBox("Beni Hatırla"))
# layout.addWidget(QPushButton("Giriş Yap"))



# window.setCentralWidget(widget)
# widget.setLayout(layout)

# window.show()

# app.exec()

# UYGULAMAYI İÇ İÇE NASIL KULLANIRIZ (LAYOUT)

#--------------------------ÇALIŞALACAK

