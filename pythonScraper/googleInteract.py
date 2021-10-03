from selenium import webdriver
import time

browser = webdriver.Chrome()

url = 'https://google.com'
browser.get(url)



# Parse and locate element
## Enter search query
'''
<input type='text' class='' id='' name='??'>
<textarea name='??'><textarea>
<input type='text' name='q'>
'''
time.sleep(3)

# name = 'q'
search_el = browser.find_element_by_name('q')

# Send text to search element
search_el.send_keys('selenium python')




# Submit form, click button
'''
<input type='submit' />
<button type='submit' />
<form></form>

<input type="submit" >
'''

submit_btn_el = browser.find_element_by_css_selector(
    "input[type='submit']")
# print(submit_btn_el.get_attribute('name'))
time.sleep(3)
submit_btn_el.click()

