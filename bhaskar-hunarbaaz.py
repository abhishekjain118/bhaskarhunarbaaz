from selenium import webdriver
import time

#driverFirefox = webdriver.Firefox()
driverChrome = webdriver.Chrome()
urlGm = "https://www.bhaskar.com/hunarbaaz/videos/292563/"

driverChrome.get(urlGm)
print("tab1: " + driverChrome.title)

# driverChrome.find_element_by_css_selector("a[data-g-label='Create an account button']").click()
driverChrome.find_element_by_xpath("//div[@class='toggleslide']/span[3]").click()
time.sleep(1)
driverChrome.find_element_by_xpath("//div[@id='declineA']/span[3]").click()
time.sleep(1)
driverChrome.find_element_by_xpath("//a[@id='confirmGdprPopup']").click()
time.sleep(2)

likes = 900 # edit this
pageRefreshTimer = 10 # edit this

for count in range(0,likes):
    driverChrome.get(urlGm)
    element = driverChrome.find_element_by_xpath("//div[@id='vid_292563']")
    time.sleep(1)
    element.click()

    print("\n"+str(count))
    time.sleep(pageRefreshTimer)

driverChrome.close()
driverChrome.quit()
