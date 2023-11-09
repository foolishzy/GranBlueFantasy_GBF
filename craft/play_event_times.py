from selenium import webdriver


from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=chrome_options)

times = 1 
while times > 0:
    times = times - 1
    #play
    driver.get("https://game.granbluefantasy.jp/#quest/supporter/909341/1")
    ele = driver.find_element_by_class_name("prt-button-cover")
    ele.click()
    ele = driver.find_element_by_class_name("btn-usual-ok se-quest-start")
    ele.click()
    ele = driver.find_element_by_class_name("btn-auto")
    ele.click()
    #ele = driver.find_element_by_class_name("prt-popup-header")



