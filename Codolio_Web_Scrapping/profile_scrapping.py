from asyncio import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


with open("final_ids.txt", "r", encoding="utf-8") as f:
    for line in f:
        list = [line.strip()]
        for username in list:
            profile_url = f"https://codolio.com/profile/{username.lstrip('@')}"
            driver.get(profile_url)
            wait = WebDriverWait(driver, 10)
            time.sleep(10)

            elements = driver.find_elements(
            By.CSS_SELECTOR,
            "span.text-5xl.font-sans.font-extrabold"
            )

            totalQs = []
            for e in elements:
                print(e.text)
                totalQs.append(e.text)

            elements = driver.find_elements(
            By.CSS_SELECTOR,
            "span.text-2xl.font-extrabold"
            )


            name = driver.find_element(
                By.CSS_SELECTOR,
                "h3.text-xl.font-semibold"
            ).text
        
            dsaQs = []
            for e in elements:
                dsaQs.append(e.text)
                print(e.text)

            with open("output.txt", "a", encoding="utf-8") as f:
                f.write(f"{name},{username.strip()},{str(totalQs)},{str(dsaQs)}\n")

            

    




driver.quit()