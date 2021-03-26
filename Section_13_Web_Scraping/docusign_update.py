# Import for the modules used 
from time import sleep # for sleep functions to wait
from datetime import date # to get current date
from selenium import webdriver # to utilize selenium 
import glob # for finding location of latest downloaded document
import os # import operating system library 
import shutil 
import sys # import sys to close program 

driver = webdriver.Edge(r"C:\Users\georgewolf\Documents\Python\AutomateTheBoringStuff\Section_13_Web_Scraping\msedgedriver.exe") # use the Edge webdriver
# Open the DocuSign login page
driver.get('https://account.docusign.com/oauth/auth?response_type=code&scope=all%20click.manage%20me_profile%20room_forms%20inproductcommunication_read%20data_explorer_signing_insights%20notary_read%20notary_write&client_id=2CC56DC9-4BCD-4B55-8AB0-8BA60BAE1065&redirect_uri=https%3A%2F%2Fapp.docusign.com%2Foauth%2Fcallback&state=%7B%22authTxnId%22%3A%22eaf9dc9b-7556-4d9e-8c50-b0a16a3ef260%22%7D#/username')


sleep(1)

# Find the element for username
username_input = driver.find_element_by_id('username')

# Input the username for login
username_input.send_keys('georgewolf@usf.edu')


#login_button = driver.find_element_by_type('submit')
login_button = driver.find_element_by_xpath("//*[@class='btn btn-main btn-lg']")
login_button.click()


# Get the current date for the filter
current_date = date.today() 
# pass current date to the url for docusign downloads
filter_select = f"https://app.docusign.com/documents?label=completed&from={current_date}&to={current_date}&type=envelopes"
# open the webpage filtered to the downloads available for the current day
driver.get(filter_select)
sleep(8)
# Find all elements for current date to download

try: # try to create the below variable and click it
    download_list = driver.find_elements_by_xpath("//*[@class='css-us18jn']") # currently only grabs first item, likely we only have 1 per day
    print(download_list)
except: # if error occurs print 'No files to download', sleep for 10s and exit program
    print("No files to download")
    driver.close() # Closes web browser
    sys.exit(1)

sleep(5)

# Example list from download_list:
# [<selenium.webdriver.remote.webelement.WebElement (session="0efd5aa0cb171df3f1b4c1a3d128b885", element="b277b36b-305c-465d-83ff-de7b215ff24b")>, 
# <selenium.webdriver.remote.webelement.WebElement (session="0efd5aa0cb171df3f1b4c1a3d128b885", element="0ee49409-dce6-4c3c-9582-0d74ef87b46d")>, 
# <selenium.webdriver.remote.webelement.WebElement (session="0efd5aa0cb171df3f1b4c1a3d128b885", element="01120feb-30ad-43dc-ac55-7fec444c6721")>]

for val in download_list: # For each value in 'download_list'
    download_package = download_list # New variable download_package set to equal download_list, probably redundant
    x = 0 # x set equal to 0 to iterate over the list
    y = 0
    if x <= len(download_list): # while x is less than the total length of the downloaded list
        download_package[x].click() # open the download link
        download = driver.find_element_by_xpath("//*[@class='olv-button olv-ignore-transform css-zhf2g3']") # find the download button
        download.click() #download the zip
        sleep(5)
        latest_downloads = glob.glob('C:/Users/georgewolf/Downloads/*.zip') # variable with the contents of 'Downloads' which are .zip
        latest_download = max(latest_downloads, key=os.path.getmtime) # grabs the latest downloaded file from the latest_downloads variable
        #box_folder = "C:/Users/georgewolf/Box/Project Portfolio/Concept Proposals/Test_Folder/{y}" # variable to store the location of the Box folder to move items
        try:
            shutil.move(latest_download, f"C:/Users/georgewolf/Box/Project Portfolio/Concept Proposals/Test_Folder/{y}.zip") # Moves the latest downlaoded file from 'Downloads' to the specified Box folder.
        except:
            print('Please review the files and clean up any completed items')
        x += 1 # increment the value of x by 1 to move to the next index in the list
        y += 1
    else:
        driver.quit() # Closes the web browser when done






