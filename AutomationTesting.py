from selenium import webdriver

ws = webdriver.Chrome(r'.\chromedriver')

ws.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

input_text = ws.find_element_by_id('user-message')
input_text.clear()
input_text.send_keys('Sandeep Thokala')

button = ws.find_element_by_class_name('btn-default')
button.click()

output = ws.find_element_by_id('display')
print(output.text)

ws.quit()