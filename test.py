from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.binary_location = "/usr/bin/google-chrome"
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# This is the line that fixed the "Status code 1" error by bypassing Snap
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://localhost")
    time.sleep(2)
    assert "Hello CI/CD World" in driver.page_source
    print("TEST PASSED")
except Exception as e:
    print(f"TEST FAILED: {e}")
    exit(1) # Important: Tell Jenkins the test failed
finally:
    driver.quit()