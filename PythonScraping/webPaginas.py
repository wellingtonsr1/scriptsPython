#! python3

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re
from tkinter import *

corFundo = "black"
listaEnderecos = ['http://helpdesk.ipmjp.pb.gov.br/', 'https://mail.ipmjp.pb.gov.br/', 'https://www.ipmjp.pb.gov.br/ramais/']
#listaEnderecos = ['https://www.ipmjp.pb.gov.br/ramais/']
     
def abriPagina(link, usuario, senha, idLogin, idSenha, classBotao):
    driver = webdriver.Firefox()
    driver.get(link)

    campoUsuario = driver.find_element(By.ID, idLogin)
    campoSenha = driver.find_element(By.ID, idSenha)
    btn = driver.find_element(By.CLASS_NAME, classBotao)

    sleep(1)
    campoUsuario.send_keys(usuario)
    sleep(1.5)
    campoSenha.send_keys(senha)
    sleep(1)
    btn.click()

def criarJanela():
    janela = Tk()
    janela.title("Login")
    janela['bg'] = corFundo

    lUsuario = Label(janela, text="Usuário:", font="Arial 12 bold italic", bg=corFundo, fg='white')
    lSenha = Label(janela, text="Senha:", font="Arial 12 bold italic", bg=corFundo, fg='white')
    areaUsuario = Entry(janela, width=25)
    areaSenha = Entry(janela, width=25, show='*')
    btn = Button(janela, text="Acessar", command=lambda: click(areaUsuario.get(), areaSenha.get()))

    lUsuario.grid(row=0, column=0,pady=20)
    lSenha.grid(row=1, column=0)
    areaUsuario.grid(row=0, column=1)
    areaSenha.grid(row=1, column=1)
    btn.grid(row=2, column=0, padx=15, pady=20)

    janela.geometry("245x150+800+400")
    janela.resizable(width=0, height=0)
    janela.mainloop()

def click(usuario, senha):
    for link in listaEnderecos:
        if re.search('helpdesk', link):
            dadosAcesso = (link, 'login_name', 'login_password', 'submit')
        elif re.search('mail', link):
            dadosAcesso = (link, 'username', 'password', 'ZLoginButton')
        elif re.search('ramais', link):
            dadosAcesso = (link, 'None', 'None', 'None')
        
        abriPagina(dadosAcesso[0], 'None', 'None', dadosAcesso[1], dadosAcesso[2], dadosAcesso[3])
        
    print('-' * 30)
    print('*******      Done!     *******')
    print('-' * 30)
    exit(0)

criarJanela()






