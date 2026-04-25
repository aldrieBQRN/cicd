from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Setup Options
options = Options()
options.binary_location = "/usr/bin/google-chrome" # The .deb version we installed
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# 2. Automatically download/use the matching driver (Bypasses SNAP)
service = Service(ChromeDriverManager().install())

# 3. Initialize Driver
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