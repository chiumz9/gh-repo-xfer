from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.path.append('../../../ghcreds/')
from ghcreds import ghuser, ghpass
#PROMPTS USER FOR USER & PASSWORD

#user = input("Github email address:  " )
#password = input("Github password:  ")

#IMPORTED CREDS
user = ghuser
password = ghpass

#CHROME DRIVER PATH LOCATIONS
PATH = "/Users/mbp/Desktop/ChromeTool/chromedriver"
driver = webdriver.Chrome(PATH)

#REQUEST TO GA GITHUB
driver.get("https://git.generalassemb.ly")

#QUERIES FOR USER & PASSWORD FIELDS
driver.implicitly_wait(5)
gh_user = driver.find_element("id", "login_field")
gh_password = driver.find_element("id","password")

#FILLS USER INPUTS TO ACCORDING FIELDS QUERIED ABOVE
gh_user.send_keys(user)
gh_password.send_keys(password)

#QUERIES FOR SUBMIT BUTTON & CLICKS

print(driver.find_element("name", "commit"))
driver.find_element("name", "commit").click()

driver.implicitly_wait(5)
#QUERY FOR "Show more"
showmore_btn = driver.find_element("name", "button").click()

driver.implicitly_wait(5)
#List<WebElement> objlnks = driver.find_element("id", "repos-container")
#print(objlnks)
