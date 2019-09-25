from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv

ids = [] # list of user id
is_first = True # flag to determine whether do login or not

with open('nlist.csv') as csvfile:
    i = 0
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if i >=7:
            id = row[0]
            ids.append(id)
        i+=1

driver = webdriver.Chrome('/Users/parkjunhong/Downloads/chromedriver')
driver.implicitly_wait(3)

for uid in ids:
    usrid = uid
    url = 'https://analytics.google.com/analytics/web/#/report/app-visitors-user-activity/a113876882w169675624p197020837/_u.date00=20190703&_u.date01=20190906&_r.userId='+usrid+'&_r.userListReportStates=%3F_u.date00=20190703%2526_u.date01=20190906%2526explorer-table.plotKeys=%5B%5D%2526explorer-table.rowStart=0%2526explorer-table.rowCount=1000&_r.userListReportId=app-visitors-user-id'
    driver.get(url)
    if is_first == True: # do login
        driver.find_element_by_name('identifier').send_keys('panda6515')
        idlogin = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
        idlogin.click()

        driver.find_element_by_name('password').send_keys('wnsghd6515')
        element = driver.find_element_by_id('passwordNext')
        driver.execute_script("arguments[0].click();", element)
        is_first = False
    #change to iframe
    driver.switch_to.frame('galaxy')
    driver.find_element_by_xpath('//button[@data-name="ID-export"]').click() # download user data
