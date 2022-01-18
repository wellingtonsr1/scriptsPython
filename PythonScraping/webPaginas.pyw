#! python3

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re
from tkinter import *

corFundo = "black"
listaEnderecos = ['link_1', 'link_n']


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
    areaUsuario = Entry(janela, width=20)
    areaSenha = Entry(janela, width=20, show='*')
    btn = Button(janela, width=7, text="Acessar", command=lambda: click(areaUsuario.get(), areaSenha.get()))
   
    lUsuario.grid(row=0, column=0,pady=20)
    lSenha.grid(row=1, column=0)
    areaUsuario.grid(row=0, column=1)
    areaSenha.grid(row=1, column=1)
    btn.grid(row=2, column=0, padx=15, pady=25)
    
    janela.geometry("220x160+800+400")
    janela.resizable(width=0, height=0)
    janela.mainloop()


def click(usuario, senha):
    for link in listaEnderecos:
        if re.search('helpdesk', link):
            idLogin = 'login_name'
            idSenha = 'login_password'
            classBotao = 'submit'
        elif re.search('mail', link):
            idLogin = 'username'
            idSenha = 'password'
            classBotao = 'ZLoginButton'
                    
        abriPagina(link, usuario, senha, idLogin, idSenha, classBotao)
    exit(0)
    
criarJanela()
