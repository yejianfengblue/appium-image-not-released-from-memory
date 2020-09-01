from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
device = "n2"
udid = device + ":5555"
caps = dict(
            platformName='Android',
            platformVersion='23',
            automationName='uiautomator2',
            deviceName=device,
            udid=udid,
            newCommandTimeout=3600,
            noReset=True
        )
driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
while True:
    try:
        driver.find_element_by_image('./okabe.png')
        print("okabe.png found")
    except NoSuchElementException :
        print("okabe.png not found")
