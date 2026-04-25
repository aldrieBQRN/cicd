from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.binary_location = "/usr/bin/google-chrome" # The path from your install output
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://localhost")
    time.sleep(2)
    assert "Hello CI/CD World" in driver.page_source
    print("TEST PASSED")
except Exception as e:
    print(f"TEST FAILED: {e}")
finally:
    driver.quit()