import time
from selenium import webdriver

def initChromeDriver():
    global chromeDriver
    chromeDriver = webdriver.Chrome()
    time.sleep(2)

url = 'https://login.104.com.tw/login.cfm?frombar=jbbar_login'
def getPage(inputUrl):
    global chromeDriver
    chromeDriver.get(inputUrl)
    time.sleep(3)

initChromeDriver()
getPage(url)

userNameEle = chromeDriver.find_element_by_id('id_name')
passEle = chromeDriver.find_element_by_id('password')

userNameEle.send_keys('')
passEle.send_keys('')

buttonELe = chromeDriver.find_element_by_xpath('//input[@type="submit"]')
buttonELe.click()


for i in range(1, 104):

    getPage('https://www.104.com.tw/jobbank/joblist/joblist.cfm?jobsource=n104bank1&ro=2&area=6001014002%2C6001014007&order=2&asc=0&page='+str(i))


    applyLen = len(chromeDriver.find_elements_by_css_selector('input.apply_job'))
    print('there are',applyLen,'buttons')
    chromeDriver.set_window_size(1600, 1000)

    for i in range(0, applyLen):
        time.sleep(5)
        chromeDriver.execute_script('$("input.apply_job")['+str(i)+'].click();')
        time.sleep(2)
        print(chromeDriver.window_handles)
        chromeDriver.switch_to_window(chromeDriver.window_handles[1])

        time.sleep(5)

        buttonApply = chromeDriver.find_element_by_css_selector('#btSend')
        buttonApply.click()

        time.sleep(4)

        chromeDriver.close()
        print(chromeDriver.window_handles)
        time.sleep(2)
        chromeDriver.switch_to_window(chromeDriver.window_handles[0])
