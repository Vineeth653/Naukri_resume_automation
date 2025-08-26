import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---- Credentials from environment variables ----
print("Starting refresh_resume.py")
NAUKRI_EMAIL = os.getenv("NAUKRI_EMAIL")
NAUKRI_PASSWORD = os.getenv("NAUKRI_PASSWORD")
RESUME_PATH = os.getenv("RESUME_PATH", "vineeth_DevSecOps.pdf")  # defaults to repo root
print("Collected email, password, and pdf file")
if not (NAUKRI_EMAIL and NAUKRI_PASSWORD):
    raise ValueError("❌ Missing NAUKRI_EMAIL or NAUKRI_PASSWORD in environment")

def refresh_resume():
    print("Inside refresh_resume funct")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu") 
    options.add_argument("--remote-debugging-port=9222")  


    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
    print("Moving into login")
    try:
        # Step 1: Login
        driver.get("https://www.naukri.com/nlogin/login")
        driver.save_screenshot("login_page.png")

        username = wait.until(EC.presence_of_element_located((By.ID, "usernameField")))
        username.clear()
        username.send_keys(NAUKRI_EMAIL)

        password = wait.until(EC.presence_of_element_located((By.ID, "passwordField")))
        password.clear()
        password.send_keys(NAUKRI_PASSWORD)

        login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_btn.click()

        time.sleep(5)  # let login settle
        print("Login success")
        # Step 2: Go to profile
        driver.get("https://www.naukri.com/mnjuser/profile")
        print("Reached Profile")

        # Step 3: Upload resume
        print("Trying to upload resume")
        upload = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
        upload.send_keys(os.path.abspath(RESUME_PATH))

        print("✅ Resume refreshed successfully!")

    except Exception as e:
        print(f"❌ Error refreshing resume: {e}")
        driver.save_screenshot("error.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    refresh_resume()
