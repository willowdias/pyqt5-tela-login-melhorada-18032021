#from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
#from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
#from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QFileDialog
#from PyQt5.QtGui import QPixmap
from os import error
from PyQt5.QtWidgets import *
from main import*
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton
from urllib.request import urlretrieve
from abrir import *
import time
import sys
from app import*
from PyQt5.QtGui import QPixmap,QIcon

class sistema(QMainWindow,QDialog):
    def __init__(self,logado):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icon/app.png"))
        self.userlog = logado
        self.ui.login_logado.setText(self.userlog)#usuario logado
        
         # PAGE 1
        #self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        # PAGE 2
        #self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2))
        # PAGE 3
        #self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pagina3))
        #icone
        #Imagens:::
        self.ui.btnEscolherArquivo.clicked.connect(self.abrir_imagem)#abrir foto
        self.ui.btnRedimensionar.clicked.connect(self.redimensionar)#colocar no tamanho
        self.ui.btnSalvar.clicked.connect(self.salvar)#salvar foto
        self.ui.ver_link_2.clicked.connect(self.abrir_imagem_pagina3)#abrir imagen
    
        self.ui.baixa_link.clicked.connect(self.opcao)#opcao baixa
        self.ui.pushButton.clicked.connect(self.box)# ver imagen
        #MENU BAR CHAMAR PAGINA
        self.ui.actionPAGINA1.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        self.ui.actionPAGINA2.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2))
        self.ui.actionPAGINA3.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pagina3)) 
        self.ui.actionPAGINA4.triggered.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pagin4_cadastro)) 
        self.ui.actionFECHAR.triggered.connect(self.menu_inicial)
        
    def menu_inicial(self):#volta tela de login
        quit()

  
    
     
        
    def box (self):#seta combox
        item= self.ui.comboBox.currentText()
        self.ui.label_pagina2.setText(item)
    
    
    def opcao(self):#selecionar opcao
        baixa_musica= self.ui.caixa_link_2.text()
        baixa_foto= self.ui.caixa_link_2.text()
        baixa_video= self.ui.caixa_link_2.text()
        if self.ui.radioButton_image.isChecked():#baixa image
            try:
                self.ui.tela_2.setText("baixando")
                baixa_foto==urlretrieve(baixa_foto,"imagen.png")                
                time.sleep(2)             
            except:            
                QMessageBox.about(self, "Title", "Imagen")        
                time.sleep(2)
                self.sistema=Imagen()
                self.sistema.show()
                self.ui.tela_2.setText("")
                self.ui.caixa_link_2.setText("")              
        
        if self.ui.radioButton_musica.isChecked():#baixa musica
            try:
                baixa_musica==urlretrieve(baixa_musica,"musica.mp3")
                self.ui.tela_2.setText("baixando")
                time.sleep(2)
            
            except:                
                QMessageBox.about(self, "Title", "Musica")
                self.ui.tela_2.setText("") 
                self.ui.caixa_link_2.setText("") 
                
                
        if self.ui.radioButton_video_2.isChecked():#video
            try:
                self.ui.tela_2.setText("baixando")
                baixa_video==urlretrieve(baixa_video,"video.mp4")                
                time.sleep(2)             
            except:                
                QMessageBox.about(self, "Title", "Video")
                self.ui.tela_2.setText("")
                self.ui.caixa_link_2.setText("")  
            
             
            
        
    ###############################################
    def abrir_imagem(self):#imagens
        imagem, _ = QFileDialog.getOpenFileName(
            self.ui.centralwidget,
            'Abrir imagem',
            r'/home/luizotavio/Imagens/',
            options=QFileDialog.DontUseNativeDialog
        )
        self.ui.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.ui.labelImg.setPixmap(self.original_img)
        self.ui.inputLargura.setText(str(self.original_img.width()))
        self.ui.inputAltura.setText(str(self.original_img.height()))
        
    def redimensionar(self):#imagens
        largura = int(self.ui.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.ui.labelImg.setPixmap(self.nova_imagem)
        self.ui.inputLargura.setText(str(self.nova_imagem.width()))
        self.ui.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):#imagens
        imagem, _ = QFileDialog.getSaveFileName(
            self.ui.centralwidget,
            'Salvar imagem',
            r'/home/luizotavio/Desktop/',
            options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(imagem, 'PNG')
    ############################################## 
    def abrir_imagem_pagina3(self):#imagens pagina 3
        imagem, _ = QFileDialog.getOpenFileName(
            self.ui.centralwidget,
            'Ver Imagen',
            r'/home/luizotavio/Imagens/',
            options=QFileDialog.DontUseNativeDialog
        )
        self.ui.inputAbrirArquivo_2.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.ui.Open_pagina2.setPixmap(self.original_img)
       
