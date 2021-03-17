from time import sleep
from selenium import webdriver 
driver = webdriver.Firefox()
driver.get('https://jira.usf.edu/login.jsp?os_destination=%2Fsecure%2FRapidBoard.jspa%3FrapidView%3D1318%26projectKey%3DTECHSTRAT')

sleep(1)

username_input = driver.find_element_by_id('login-form-username')
password_input = driver.find_element_by_id('login-form-password')

username_input.send_keys('georgewolf')
password_input.send_keys('Omgmine01@')

login_button = driver.find_element_by_id('login-form-submit')
login_button.click()


