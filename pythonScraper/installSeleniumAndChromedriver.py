'''
# Install selenium
->: python pip install selenium
'''

# webdriver install
## Download webdriver in program
'''
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
'''

## Copy chromedriver to the project root directory
'''
[chromedriver downloadsite](https://sites.google.com/a/chromium.org/chromedriver/home)
'''


from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://cfe.sh/")
