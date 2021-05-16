from selenium import webdriver
import time
import pyautogui


browser = webdriver.Firefox()
browser.get("https://www.instagram.com")
time.sleep(2)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("udemyicin")
password.send_keys("selenium")
time.sleep(2)
try:
    login = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
    login.click()
    time.sleep(2)
except:
    login = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
    login.click()
    time.sleep(2)
    try:
        login = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
        login.click()
        time.sleep(2)
    except:
        print("Giris yapa tiklayamadik \n")

time.sleep(1)

with open("file/just_1_name.txt","r") as Takipet:
    count=1
    listele = Takipet.readlines()
    for i in listele:
        if count == 28:
            count = 1
            print("***"*10)
            time.sleep(600)

        try:
            browser.get("https://www.instagram.com/{}/".format(i))

            time.sleep(5)


            bunatikla2 = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button")
            time.sleep(4)
            print ("ilk deneme")
            print(count)
            bunatikla2.click()
            count += 1
            time.sleep(3)

        except :
            try:
                bunatikla2 = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button")
                print("ikinci deneme")
                time.sleep(4)
                print(count)
                bunatikla2.click()
                count +=1
                time.sleep(3)
            except :
                try:
                    bunatikla3 = browser.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div")
                    print("3 deneme")
                    time.sleep(4)
                    print(count)
                    bunatikla3.click()
                    count +=1
                    time.sleep(3)
                except :
                    try:
                        bunatikla = browser.find_element_by_xpath( "/html/body/div[1]/section/main/div/header/section/div[1]/button")
                        time.sleep(7)
                        print(count)
                        bunatikla.click()
                        count += 1
                    except:
                        print(browser.get("https://www.instagram.com/{}/".format(i)) , "hesabına istek atılamadı yahu \n")

        time.sleep(0.2)
time.sleep(30)
browser.close()










