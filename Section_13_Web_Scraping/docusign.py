# Import for the modules used 
from time import sleep # for sleep functions to wait
from datetime import date # to get current date
from selenium import webdriver # to utilize selenium 
import glob # for finding location of latest downloaded document
import os # import operating system library 
import shutil 
import sys # import sys to close program 

driver = webdriver.Edge(r"msedgedriver.exe") # use the Edge webdriver
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
    download_list = driver.find_element_by_xpath("//*[@class='css-us18jn']") # currently only grabs first item, likely we only have 1 per day
    download_list.click()
except: # if error occurs print 'No files to download', sleep for 10s and exit program
    print("No files to download")
    driver.close() # Closes web browser
    sys.exit(1)

sleep(5)

# Experimental area to uncheck and remove the download of Zip folder, not in use now.
""" 
document = driver.find_element_by_css_selector("[data-qa='download-document-label']")
document.click() 
"""

# Download the files to local drive (currently ZIP of all files)
download_package = driver.find_element_by_xpath("//*[@class='olv-button olv-ignore-transform css-zhf2g3']") # currently downloads full zip
download_package.click()

# Move the files to the Box folder
latest_downloads = glob.glob('C:/Users/georgewolf/Downloads/*.zip') # variable with the contents of 'Downloads' which are .zip
latest_download = max(latest_downloads, key=os.path.getmtime) # grabs the latest downloaded file from the latest_downloads variable
box_folder = "C:/Users/georgewolf/Box/Project Portfolio/Concept Proposals/Test_Folder" # variable to store the location of the Box folder to move items
shutil.move(latest_download, box_folder) # Moves the latest downlaoded file from 'Downloads' to the specified Box folder.




