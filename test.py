from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import traceback # Add this at the top

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
   
    # Let's see what the page actually says
    print(f"Current Page Title: {driver.title}")
   
    # Check if the text exists
    assert "Hello CI/CD World" in driver.page_source
    print("TEST PASSED")
except Exception as e:
    print("TEST FAILED")
    print(traceback.format_exc()) # This will show us the EXACT line that failed
    exit(1)
finally:
    driver.quit()