#! python3

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from tkinter import *
import re


backgroundColor = "black"
addressList = ['http://helpdesk.ipmjp.pb.gov.br/', 'https://mail.ipmjp.pb.gov.br/']   


def dislplayLoginWindow():
    window = Tk()
    window.title("Login")
    window['bg'] = backgroundColor

    lUser = Label(window, text="Usuário:", font="Arial 12 bold italic", bg=backgroundColor, fg='white')
    lPassword = Label(window, text="Senha:", font="Arial 12 bold italic", bg=backgroundColor, fg='white')
    userLoginField = Entry(window, width=25)
    passwordLoginField = Entry(window, width=25, show='*')
    btn = Button(window, text="Acessar", command=lambda: btnClick(userLoginField.get(), passwordLoginField.get()))

    lUser.grid(row=0, column=0,pady=20)
    lPassword.grid(row=1, column=0)
    userLoginField.grid(row=0, column=1)
    passwordLoginField.grid(row=1, column=1)
    btn.grid(row=2, column=0, padx=15, pady=20)

    window.geometry("245x150+800+400")
    window.resizable(width=0, height=0)
    window.mainloop()

def btnClick(user, password):
    driver = webdriver.Firefox()

    for idx in range(len(addressList)):
        if re.search('helpdesk', addressList[idx]):
            accessData = (addressList[idx], 'login_name', 'login_password', 'submit')
        elif re.search('mail', addressList[idx]):
            accessData = (addressList[idx], 'username', 'password', 'ZLoginButton')
        elif re.search('ramais', addressList[idx]):
            accessData = (addressList[idx], 'None', 'None', 'None')
        elif re.search('114', addressList[idx]):
            accessData = (addressList[idx], 'username', 'password', 'submit')

        flag = idx
        openWebBrowser(accessData[0], user, password, accessData[1], accessData[2], accessData[3], flag, driver)

    print('-' * 30)
    print('*******      Done!     *******')
    print('-' * 30)
    exit(0)

def openWebBrowser(link, user, password, loginId, passowrdId, btnClass, flag, driver):
    if flag != 0:
        driver.execute_script("window.open('');") 
        driver.switch_to.window(driver.window_handles[flag])

    driver.get(link)
    driver.maximize_window() 
    driver.implicitly_wait(20) 

    userElementField = driver.find_element(By.ID, loginId)
    passwordElementField = driver.find_element(By.ID, passowrdId)
    btn = driver.find_element(By.CLASS_NAME, btnClass)
    #btn = driver.find_element(By.ID, btnClass)

    sleep(1)
    userElementField.send_keys(user)
    sleep(1.5)
    passwordElementField.send_keys(password)
    sleep(1)
    btn.click()


if __name__ == '__main__':
   dislplayLoginWindow()






