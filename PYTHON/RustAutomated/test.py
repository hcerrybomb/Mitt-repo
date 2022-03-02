from selenium import webdriver

driver = webdriver.Chrome("C:/Users/Gaming Dator VII/Desktop/Mitt-repo/PYTHON/RustAutomated/chromedriver.exe")

driver.get("https://www.battlemetrics.com/players?filter%5Bsearch%5D=КакТак&filter%5BplayerFlags%5D=&filter%5Bserver%5D%5Bsearch%5D=Rustafied%20EU%20Odd&filter%5Bserver%5D%5Bgame%5D=rust&sort=score")

element = driver.find_element_by_xpath('//*[@id="PlayerInstancesPage"]/div/ul/li[1]/p/a')

playerIdLink = element.get_attribute('href')

idLinkSplit = playerIdLink.split("/")

element2 = driver.find_element_by_xpath('//*[@id="PlayerInstancesPage"]/div/ul/li[1]/table/tbody/tr[1]/td[3]/a')
serverIdLink = element2.get_attribute('href')
serverLinkSplit = serverIdLink.split("/")
print(serverLinkSplit[-1])
print(idLinkSplit[-1])


