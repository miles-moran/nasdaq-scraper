from selenium import webdriver
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def test():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://listingcenter.nasdaq.com/noncompliantcompanylist.aspx")
    expand = driver.find_element_by_class_name("rgExpand")
    return expand

if __name__ == '__main__':
    app.run()
