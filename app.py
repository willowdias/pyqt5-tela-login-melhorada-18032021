from os import error, name, truncate
import sqlite3
from sqlite3.dbapi2 import Row
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import *
from main import*
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton
from urllib.request import urlretrieve
from abrir import *
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from main_login import*
from sistemayou import*
from PyQt5.QtGui import QPixmap,QIcon
import sys
from datetime import date
from PyQt5.QtCore import QBasicTimer

class app_sistema(QMainWindow,QDialog,QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icon/app.png"))
        #
        self.ui.chamar.clicked.connect(self.lista_de_usuario)#mostra usuario
        self.ui.deletar_us.clicked.connect(self.deleta_user)#deletar usuario
         
        #tela login
        self.ui.bt_connectar.clicked.connect(self.tela_logado)#botao abrir tela login
        self.ui.bt_cancelar.clicked.connect(self.hide)#botao fecha tela login
        
        #tela cadastro usuario
        self.ui.Button_Cadastro.clicked.connect(self.cadastro_user)
        #data
        self.time = QBasicTimer()
        self.step =0

    def up(self,):#barra de carregamento
        import time, sys

        for i in range(0, 101):
            sys.stdout.write("\r{}".format(i))
            sys.stdout.flush()
            time.sleep(0.1)
            self.ui.progressBar.setValue(i)
            
            
            
            


       
        
    
######Clear########
    def limpar(self):#limpar registro depois de cadastrar
        self.ui.nome_usuario.setText("")
        self.ui.log_cadastro.setText("")
        self.ui.senha_cs1.setText("")
        self.ui.senha_cs2.setText("")
    
    def limparuser(self):
        self.ui.login.setText("")#limpar
        self.ui.senha.setText("") 
    
#############      
    def tela_logado(self):#tela login aprovar cliente  
        login = str(self.ui.login.text())
        senhauser = str(self.ui.senha.text())  
        self.logado =login # usuario tela login   
     
        try:

            if login =='willow' and senhauser=='soft':#usuario padrao
                QMessageBox.about(self, "Title", "Usuario sistema")
                self.up()
                self.sistemayou=sistema(self.logado)#usuario logado
                self.sistemayou.show()
                self.limparuser()
            
               
                
            
            if login =='WILLOW' and senhauser=='SOFT':#usuario padrao
                QMessageBox.about(self, "Title", "Usuario sistema")
                self.up()
                self.sistemayou=sistema(self.logado)
                self.sistemayou.show()
                self.limparuser()
                
                   
                                
            banco = sqlite3.connect('appsistema.db') 
            cursor = banco.cursor()
            cursor.execute('SELECT * FROM dados WHERE user = ? and senha = ?',(login,senhauser))
            data = cursor.fetchone()
            banco.commit()
            
            if data != None:
                        
                (data[2],data[3])
                banco.close()
                self.up()
                self.sistemayou=sistema(self.logado)
                self.sistemayou.show()
                self.hide()
                
            else:
                self.ui.label_conexao.setText("Erro Usuario")   
        except:error
            
        
       

    def cadastro_user(self):
        nome=self.ui.nome_usuario.text()
        login=self.ui.log_cadastro.text()
        senha_sn = self.ui.senha_cs1.text()
        senha_2 = self.ui.senha_cs2.text()
        if name == "" or login=="" or senha_sn=="" or senha_2=="":
            QMessageBox.about(self, "Title", "CAMPO VAZIO PREENCHAR")
            return False
            
            
        if (senha_sn == senha_2):
            try:
                    banco = sqlite3.connect('appsistema.db') 
                    cursor = banco.cursor()
                    cursor.execute("CREATE TABLE IF NOT EXISTS dados (id INTEGER PRIMARY KEY,nome text NOT NULL ,user text NOT NULL,senha text NOT NULL);")
                    cursor.execute("INSERT INTO dados VALUES (null,'"+nome+"','"+login+"','"+senha_sn+"')")
                    banco.commit()
                    banco.close()#consulta dados do banco de dados
                    self.ui.label_cadastro.setText("SUCESSO")
                    self.limpar()
            
            except:
                sys.exit
        else:
            self.ui.label_cadastro.setText("DADOS INCORRETO")        
    def lista_de_usuario(self):#lista de usuario cadastrado
        try:
            banco = sqlite3.connect('appsistema.db') 
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM dados")
            dados_lidos = cursor.fetchall()
            self.ui.tableWidget.setRowCount(20)
            for i in range(0, len(dados_lidos)):
                for j in range(0,4):
                    self.ui.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
                    
        except:error
    def deleta_user(self):#deleta usuario
        linha = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(linha)
        try:
            
            
            banco = sqlite3.connect('appsistema.db') 
            cursor = banco.cursor()
            cursor.execute ('DELETE FROM dados where id ='+linha)
            print('deu certo')
            banco.commit()
            banco.close
                 
            
                       
        except:error      
    
            
if __name__ == '__main__':
    
    app = QApplication([sys.argv])
    window = app_sistema()
    window.show()
    sys.exit(app.exec_())