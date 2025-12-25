from asyncio import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://codolio.com/leaderboard")

wait = WebDriverWait(driver, 10)

time.sleep(30)  # wait for JS to load

# section = wait.until(
#     EC.presence_of_element_located((
#         By.CSS_SELECTOR,
#         "div.flex.flex-col.gap-4"
#     ))
# )


# links = section.find_elements(By.TAG_NAME, "a")

# hrefs = [a.get_attribute("href") for a in links if a.get_attribute("href")]


# print("All hrefs:")
# print(hrefs)

# unique_profiles = []
# seen = set()

# for href in hrefs:
#     if href and "/profile/" in href:
#         if href not in seen:
#             seen.add(href)
#             unique_profiles.append(href)
# print("Unique profile links:")
# print(unique_profiles)


count1 = 0
count2 = 0
count3 = 0
bigList = []
for i in range(131):
    listOfData  = []
    

    elements = driver.find_elements(
        By.CSS_SELECTOR,
        "div.font-medium.text-gray-900.dark\\:text-darkText-300"
    )
    
    for e in elements:
        listOfData.append([e.text])
        count1 += 1
        print(e.text)

    time.sleep(10) 

    elements = driver.find_elements(
        By.CSS_SELECTOR,
        "div.col-span-2.py-3.px-4.text-center.font-medium"
    )
    
    for e in elements:
        listOfData[count2].append(e.text)
        count2 += 1
        print(e.text)
    

    time.sleep(10) 
    
    section = wait.until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR,
        "div.flex.flex-col.gap-4"
        ))
    )


    divs = section.find_elements(
        By.CSS_SELECTOR,
        "div.text-xs.text-gray-500"
    )

    texts = [div.text.strip() for div in divs if div.text.strip()]
    print(texts)

    listOfData.append(texts)


    buttons = wait.until(
        EC.presence_of_all_elements_located((
            By.CSS_SELECTOR,
            "button.px-2.py-2.text-xs.border"
        ))
    )

    second_button = buttons[1]

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        second_button
    )

    driver.execute_script("arguments[0].click();", second_button)
    bigList.append(listOfData)
    try:
        File = open("data.txt", "a")
        for data in listOfData:
            File.write(str(data) + "\n")
        File.close()
    except Exception as e:
        print("Error writing to file:", e)
    time.sleep(15)

time.sleep(20)

print("Final Data:")
for data in bigList:
    print(data)


try:
    File = open("BigData.txt", "a")
    for data in bigList:
        File.write(str(data) + "\n")
        File.close()
except Exception as e:
    print("Error writing to file:", e)

# for i in range(3):
#     elements = driver.find_elements(
#         By.CSS_SELECTOR,
#         "div.font-medium.text-gray-900.dark\\:text-darkText-300"
#     )
    
#     for e in elements:
#         print(e.text)

#     elements = driver.find_elements(
#         By.CSS_SELECTOR,
#         "div.col-span-2.py-3.px-4.text-center.font-medium"
#     )
    
#     for e in elements:
#         print(e.text)
    

#     time.sleep(3) 

#     button = wait.until(
#         EC.element_to_be_clickable((
#             By.CSS_SELECTOR,
#             "button.px-2.py-2.text-xs.border"
#         ))
#     )

#     button.click()

#     time.sleep(3) 






driver.quit()