#! python3

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re
from tkinter import *
import sys
import os
import psutil




corFundo = "black"
listaEnderecos = ['link_1', 'link_n']


def abriPagina(link, usuario, senha, idLogin, idSenha, classBotao):
    driver = webdriver.Firefox()
    #driver = webdriver.Chrome()
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
     

def login():
    print('=' * 40)
    print('             Área de Login                  ')
    print('=' * 40)
    usuario = input("Usuário: ")
    senha = input("Senha: ")

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
    
    PROCNAME = "geckodriver" # or chromedriver or IEDriverServer
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()


login()

