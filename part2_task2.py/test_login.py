import os
import zipfile
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# --- Step 1: Download ChromeDriver automatically if missing ---
CHROME_DRIVER_DIR = r"C:\chromedriver-win64"
CHROME_DRIVER_PATH = os.path.join(CHROME_DRIVER_DIR, "chromedriver.exe")
ZIP_PATH = os.path.join(CHROME_DRIVER_DIR, "chromedriver-win64.zip")

# Public ChromeDriver URL (match your Chrome version)
CHROMEDRIVER_URL = "https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.69/win64/chromedriver-win64.zip"

if not os.path.exists(CHROME_DRIVER_PATH):
    print("ChromeDriver not found. Downloading...")
    os.makedirs(CHROME_DRIVER_DIR, exist_ok=True)

    response = requests.get(CHROMEDRIVER_URL)
    with open(ZIP_PATH, "wb") as file:
        file.write(response.content)

    print("Download complete. Extracting...")
    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall(CHROME_DRIVER_DIR)

    print("Extraction done ✅")
else:
    print("ChromeDriver already exists ✅")

# --- Step 2: Configure Selenium WebDriver ---
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# --- Step 3: Example Test ---
def test_login_valid():
    driver.get("https://example.com")
    assert "Example" in driver.title
    driver.quit()
    if __name__ == "__main__":
        test_login_valid()