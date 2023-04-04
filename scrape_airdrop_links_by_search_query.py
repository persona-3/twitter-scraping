from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time
import pandas as pd
import os

options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")
DRIVER_PATH = r"C:\Users\91893\Downloads\twitter_scraper\chromedriver.exe"

driver = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)

#manual login
# driver.get('https://twitter.com/login')
# time.sleep(30)


#https://twitter.com/ETHPNFTUNK/status/1548581188549447683
url = 'https://twitter.com/search?q=eth%20%2B%20address%20%2B%20drop&src=typed_query&f=top'
driver.get(url)
time.sleep(7)

elements = driver.find_elements(By.CLASS_NAME, 'css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1pi2tsx')
print(len(elements))
for elem in elements:
    page_link = elem.get_attribute('href')
    print(page_link)


data = {"name" : [], "twitter_handle" : [], "wallet" : []}
scroll = 0
temp = 1500
count = 0
prev = 0
run = 0

unique_addresses = set()

# while True:
#     print("Current no of unique addresses------------->", len(unique_addresses))
#     scroll += temp
#     if run == 30:
#         break
#     if count == 5:
#         driver.get(url)
#         run += 1
#     time.sleep(7)
#     #<span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">0xdabeecf497755130a9d4708db05f12c75cd3d9a2</span>
#     #element = driver.find_elements(By.CLASS_NAME, 'css-1dbjc4n.r-j5o65s.r-qklmqi.r-1adg3ll.r-1ny4l3l')
#     #element = driver.find_elements(By.CLASS_NAME, 'css-901oao')
#     element = driver.find_elements(By.CSS_SELECTOR,'article[data-testid="tweet"]')
#     #element2 = driver
#     print("No of elements captured --------->", len(element))
#     if count == 10:
#         break
#     print("num element- ", len(element))
#     if len(element) == prev:
#         count += 1
#     else:
#         prev = len(element)
#         count = 0
#     # count = 1
#     for e in element:
#         try:
#             val = e.text
#             print("tweet text------------> ", val)
#             success = False
            
#             val = val.split('\n')
#             for z1 in val:
#                 if(z1[:2] == "0x"):
#                     print("address---------------------->", z1)
#                     unique_addresses.add(z1)
#                     print("Current no of unique addresses------------->", len(unique_addresses))
#                     data["wallet"].append(z1)
#                     data["name"].append(val[0])
#                     data["twitter_handle"].append(val[1])
                    
                    
                    
#             # if 'Replying to' in val and '0x' in val:
#             #     val = val.split('\n')
#             #     for vl in val:
#             #         vl = vl.split(' ')
#             #         for v in vl:
#             #             if '0x' in v:
#             #                 wallet = v
#             #                 success = True
#             #                 break
#             #     if success == True:
#             #         data["wallet"].append(wallet)
#             #         data["name"].append(val[0])
#             #         data["twitter_handle"].append(val[1])
#             # print(val[0], val[1], val[6])
#         except:
#             continue
#     df = pd.DataFrame(data)
#     df.drop_duplicates(inplace = True)
#     csv_file_name = url.split('/')[3] + "_with_login_" + ".csv"
#     #print(os.path.join(os.getcwd(), csv_file_name))
#     file_path = os.path.join(os.getcwd(), csv_file_name)
#     df.to_csv(file_path, index = False, mode = "w")
#     driver.execute_script(f"window.scrollTo(0,{scroll})")