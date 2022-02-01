#! python3

#+--------------------------------------------------Descrição-------------------------------------------------------+
#| - Faz login de forma automática em algumas páginas web     		                                                |
#+----------------------------------------------------Autor---------------------------------------------------------+
#| - Wellington        									         	                                                |
#+----------------------------------------------Sistemas testados---------------------------------------------------+
#| - Windows 10(x64)		                    				 		                                            |
#+-------------------------------------------------IMPORTANTE-------------------------------------------------------+
#|                                                                                                                  |								               
#+------------------------------------------------------------------------------------------------------------------+


from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from tkinter import *
import re


background_color = "black"
address_list = ['link_1', 'link_n']   


def display_login_window():
    window = Tk()
    window.title("Login")
    window['bg'] = background_color

    label_user = Label(window, text="Usuário:", font="Arial 12 bold italic", bg=background_color, fg='white')
    label_password = Label(window, text="Senha:", font="Arial 12 bold italic", bg=background_color, fg='white')
    user_login_field = Entry(window, width=25)
    password_login_field = Entry(window, width=25, show='*')
    btn = Button(window, text="Acessar", command=lambda: btn_click(user_login_field.get(), password_login_field.get()))

    label_user.grid(row=0, column=0,pady=20)
    label_password.grid(row=1, column=0)
    user_login_field.grid(row=0, column=1)
    password_login_field.grid(row=1, column=1)
    btn.grid(row=2, column=0, padx=15, pady=20)

    window.geometry("245x150+800+400")
    window.resizable(width=0, height=0)
    window.mainloop()


def btn_click(user, password):
    driver = webdriver.Firefox()

    for idx in range(len(address_list)):
        if re.search('helpdesk', address_list[idx]):
            access_data = (address_list[idx], 'login_name', 'login_password', 'submit')
        elif re.search('mail', address_list[idx]):
            access_data = (address_list[idx], 'username', 'password', 'ZLoginButton')
        elif re.search('ramais', address_list[idx]):
            access_data = (address_list[idx], 'None', 'None', 'None')
        elif re.search('114', address_list[idx]):
            access_data = (address_list[idx], 'username', 'password', 'submit')

        if user == '' or password == '':
            print('-' * 40)
            print('* Favor, verficar os dados informados. *'.center(40))
            print('-' * 40)
            driver.quit()
            sleep(3)
            raise SystemExit()

        open_web_browser(access_data[0], user, password, access_data[1], access_data[2], access_data[3], idx, driver)
        
    print('-' * 30)
    print('*******      Done!     *******')
    print('-' * 30)
    raise SystemExit()


def open_web_browser(link, user, password, login_id, passowrd_id, btn_class, flag, driver):
    if flag != 0:
        driver.execute_script("window.open('');") 
        driver.switch_to.window(driver.window_handles[flag])

    driver.get(link)
    driver.maximize_window() 
    driver.implicitly_wait(20) 

    user_element_field = driver.find_element(By.ID, login_id)
    password_element_field = driver.find_element(By.ID, passowrd_id)
    btn = driver.find_element(By.CLASS_NAME, btn_class)
    #btn = driver.find_element(By.ID, btn_class)

    sleep(1)
    user_element_field.send_keys(user)
    sleep(1.5)
    password_element_field.send_keys(password)
    sleep(1)
    btn.click()


if __name__ == '__main__':
   display_login_window()






