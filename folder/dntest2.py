from selenium import webdriver

source = "http://www.i-sys.ru"
driver = webdriver.Firefox()
driver.get(source)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

test1 = driver.execute_script("return window.performance.timing.navigationStart")
test2 = driver.execute_script("return window.performance.timing.unloadEventEnd")
test3 = test2-test1

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart

print (test3)


print (backendPerformance)
print (frontendPerformance)

driver.quit()