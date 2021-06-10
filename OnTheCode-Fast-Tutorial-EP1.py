import os, time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC          #call out the functions from the module and library
from selenium.webdriver.chrome.options import Options                     #เรียกใช้ฟังค์ชั่นภายในโมดูล และเรียกใช้ โมดูล



options = webdriver.ChromeOptions()   # ChromeOptions declaration   ประกาศตัวแปรเป็นออปชั่นของโครมไดรเวอร์
options.add_argument('--log-level=3') # disable spam logging        ตั่งค่าให้ตัวแปรที่ประกาศออกมา เพิ่มออปชั่นตั่งค่าให้ ปิดลอกเลเวล3
                                                                    #หมายถึงปิดการแสปมลอคขยะที่ทำหน้าที่ทำให้หน้าเทอร์มินัลรกเฉยๆ

driver = webdriver.Chrome('chromedriver.exe', options=options)  # driver declaration (drivernames.exe, options=options) call driver and setting option 
                                                                #ประกาศตัวแปรไดรเวอร์โครม จากตำแหน่ง ไดรเวอร์นั้นๆชื่อนั้นๆ กับการตั่งค่าตามออปชั่นนั้นๆ

os.system('cls') # Clear the Terminal สำหรับล้างหน้าเทอร์มินัล

First_name = 'First name'             #Information declaration for use it to input inside the fill form on web automation
Last_name = 'Last name'               #ประกาศตัวแปลและค่าในตัวแปลเพื่อใช้สำหรับกรอกข้อมูลไปในหน้ารับข้อมูลเว็ปเพจนั้นๆ
email = 'email@email.com'
password = 'password'


try:


    driver.get('https://panel.dritestudio.co.th/register')  #Driver open the web browser on this url : https://panel.dritestudio.co.th/register
                                                            #เรียกตัวแปรไดรเวอร์ให้ทำการเปิด เว็ปตามURL ดังกล่าว คือ https://panel.dritestudio.co.th/register


    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.Xpath, '//*[@id="__layout"]/div/div[2]/div/div/div/div/div[2]/div/form/div[1]/input')))
        
        start_time = time.time()          #เริ่มนับเวลา start counting time
        
        elem = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div/div/div/div/div[2]/div/form/div[1]/input')  #find Xpath element on Firstname inputbox and declare it to variable called 'elem'
                                                                                                                            #หา element แบบ Xpath ของ ช่องกรอกข้อมูล สำหรับช่อง ชื่อFirstname ละประกาศเข้าตัวแปร elem

        elem.send_keys(First_name,Keys.TAB,Last_name,Keys.TAB,email,Keys.TAB,password,Keys.TAB) #Everytime after the Information typed inside the input box then it will skip lines by pressing TAB
                                                                                                #This way is faster than find many element and send information inside the input box

                                                                                                #ทุกๆครั้งที่ข้อมูลจากตัวแปรที่ประกาศ ส่งไปในช่องกรอกข้อมูลมันจะทำการกด TAB เพื่อประหยัดเวลาการต้องไปนั่งหาโค้ดหน้าเว็ปเพื่อหาช่องต่างๆ
                                                                                                #วิธีนี้จะเร็วสุด เร็วกว่าการที่จะให้มันมา คุ้ยหน้าเว็ปทีละบรรทัดๆจนกว่าจะเจอช่องๆนั้น


        print("--- %s seconds ---" % (time.time() - start_time)) #Showing up the time how long does the code take to run until this line
                                                                 #แสดงผล ว่ากี่วินาที โค้ดในกรอบถึงทำงานจวบจนถึงบรรทัดนี้
    except TimeoutException:
        print('timeout error') #แสดงผลว่า ช่อง สำหรับกรอกข้อมูล มันไม่ขึ้นมาเป็นระยะเวลา เกิน30วิแล้วที่ไม่ตอบสนอง


    sleep(10)
    driver.close()

except Exception as e:
    print(e)                          #print out the error  แสดงผลข้อผิดพลาดของโค้ดข้างบนในกรอบ try แรก บรรทัดที่ 29

except KeyboardInterrupt:  #if press CTRL+C then clean theh terminal หากกดปุ่มยุติคำสั่งจะทำการล้างหน้าเทอร์มินัล
    os.system('cls')



