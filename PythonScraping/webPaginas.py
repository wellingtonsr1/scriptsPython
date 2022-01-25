#! python3

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re
from tkinter import *

corFundo = "black"
listaEnderecos = ['link_1', 'Link_n']   


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
    driver = webdriver.Firefox()

    for idx in range(len(listaEnderecos)):
        if re.search('helpdesk', listaEnderecos[idx]):
            dadosAcesso = (listaEnderecos[idx], 'login_name', 'login_password', 'submit')
        elif re.search('mail', listaEnderecos[idx]):
            dadosAcesso = (listaEnderecos[idx], 'username', 'password', 'ZLoginButton')
        elif re.search('ramais', listaEnderecos[idx]):
            dadosAcesso = (listaEnderecos[idx], 'None', 'None', 'None')
        elif re.search('114', listaEnderecos[idx]):
            dadosAcesso = (listaEnderecos[idx], 'username', 'password', 'submit')

        flag = idx
        abriPagina(dadosAcesso[0], usuario, senha, dadosAcesso[1], dadosAcesso[2], dadosAcesso[3], flag, driver)

    print('-' * 30)
    print('*******      Done!     *******')
    print('-' * 30)
    exit(0)

def abriPagina(link, usuario, senha, idLogin, idSenha, classBotao, flag, driver):
    if flag != 0:
        driver.execute_script("window.open('');") 
        driver.switch_to.window(driver.window_handles[flag])

    driver.get(link)
    driver.maximize_window() 
    driver.implicitly_wait(20) 

    campoUsuario = driver.find_element(By.ID, idLogin)
    campoSenha = driver.find_element(By.ID, idSenha)
    #btn = driver.find_element(By.CLASS_NAME, classBotao)
    btn = driver.find_element(By.ID, classBotao)

    sleep(1)
    campoUsuario.send_keys(usuario)
    sleep(1.5)
    campoSenha.send_keys(senha)
    sleep(1)
    btn.click()


if __name__ == '__main__':
   criarJanela()






