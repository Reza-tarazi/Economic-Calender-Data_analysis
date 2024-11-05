from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
import re
#=======================================================================
browser = webdriver.Firefox()
browser.get('https://tradingeconomics.com/calendar')
time.sleep(2)
#------------------------------------------------------------------------
"""
فیلترکردن کشورها برای ماژورها و جلسات 

"""
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/table/tbody/tr/td[1]/div/button/span').click()
#کلیک برروی کشورها
time.sleep(1)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/div[2]/div[1]/a').click()
#کلیک برروی پاک کردن با دستور clear
time.sleep(0.5)
#فیلترکردن کشورها
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[1]/li[7]/input').click()
#َاسترالیا
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[2]/li[3]/input').click()
#اتحادیه اروپا
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[2]/li[5]/input').click()
#فرانسه
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[2]/li[7]/input').click()
#G20
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[2]/li[8]/input').click()
#G7
time.sleep(0.5)
browser.find_element(By.XPATH , '//html/body/form/div[3]/div/div/span/div/span/ul[2]/li[9]/input').click()
#آلمان
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[2]/li[22]/input').click()
#ایتالیا
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[3]/li[16]/input').click()
#نیوزلند
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[1]/li[22]/input').click()
#کانادا
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[4]/li[11]/input').click()
#اسپانیا
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[4]/li[15]/input').click()
#سوییس
time.sleep(0.5)
browser.execute_script('window.scrollTo(0,300)')
#اسکرول به پایین
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[4]/li[26]/input').click()
#انگلیس
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[4]/li[27]/input').click()
#آمریکا
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[2]/li[25]/input').click()
#ژاپن
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/span/ul[1]/li[25]/input').click()
#چین
browser.execute_script('window.scrollTo(300,0)')
#اسکرول به بالا
time.sleep(0.5)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/span/div/div[2]/div[3]/a').click()
#save  
#---------------------------------------------------------------------------------
#today
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/table/tbody/tr/td[1]/div/div[1]/button/span').click()
time.sleep(2)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/table/tbody/tr/td[1]/div/div[1]/ul/li[2]/a/input').click()

#---------------------------------------------------------------------------------
"""
High Impact
"""
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/table/tbody/tr/td[1]/div/div[2]/button/span').click()
time.sleep(2)
browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/table/tbody/tr/td[1]/div/div[2]/ul/li[2]/a/input').click()
#---------------------------------------------------------------------------------
#s = str(browser.find_element(By.XPATH , '//*[@id="calendar"]/tbody[1]/tr['+str(i)+']/td[1]/span').text)
#t = str(browser.find_element(By.XPATH , '//*[@id="calendar"]/tbody[1]/tr['+str(i)+']/td[3]/a').text)
'''
we need to creat a list about some details that exist in calender value that remove from our variables
after that, we analysis the data 
'''
i = 1
Radif=""
NameData = []
EcoDataInx= []
while True:
        try:
                NameIndex1 =browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/div[3]/table/tbody[1]/tr['+str(i)+']/td[3]').text
                NameIndex2 =browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/div[3]/table/tbody[1]/tr['+str(i)+']/td[2]').text
                NameIndex = NameIndex1 + " " + NameIndex2
                NameData.append(NameIndex)
                #===========================
                EcoDataIn =[]
                Forecast =browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/div[3]/table/tbody[1]/tr['+str(i)+']/td[7]').text
                Forecastnumbers = re.sub(r'[^\d.-]', '', Forecast)
                EcoDataIn.append(Forecastnumbers)
                #--------------------------------------
                Consensus =browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/div[3]/table/tbody[1]/tr['+str(i)+']/td[6]').text
                Consensusnumbers = re.sub(r'[^\d.-]', '', Consensus)
                EcoDataIn.append(Consensusnumbers)
                #--------------------------------------
                Previous =browser.find_element(By.XPATH , '/html/body/form/div[3]/div/div/div[3]/table/tbody[1]/tr['+str(i)+']/td[5]').text
                Previousnumbers = re.sub(r'[^\d.-]', '', Previous)
                EcoDataIn.append(Previousnumbers)
                #===========================
                EcoDataInx.append(EcoDataIn)
                #===========================
                Radif +='📊'+" NameIndex: " + NameIndex +"  " +"\n"
                Radif +='⏰'+" Forecast: " + Forecast +"  " +"\n"
                Radif +='🔴'+" Consensus: " + Consensus +"\n"
                Radif +='🔴'+" Previous: " + Previous +"\n"
                #===========================
                i+=1

        except NoSuchElementException:
                print("Element not found")
                break
browser.quit()
#===================================================================
print(NameData)
print(EcoDataInx)
alldata = str(NameData) + "\n" + str(EcoDataInx)
f = open("Economic-Calender-Data_analysis.txt", "a")
f.write(alldata)
f.close()
#=========================================================
#======================DataFrames=========================
#=========================================================
topic = ['Forecast','Consensus','Previous']
df = pd.DataFrame(data=EcoDataInx,index=NameData,columns=topic)
DFstr=df.to_string(index=True)
#-----------------------------------------------------
Bearish = df[(df['Forecast'] < df['Consensus']) &
        (df['Forecast'] < df['Previous'])]
Bearish = Bearish[['Forecast','Previous','Consensus']]
Bearishdata_str_with_index = Bearish.to_string(index=True)
Bearishtext= "Bearish Index"+"\n""\n"
Bearishtext += Bearishdata_str_with_index
f = open("Bearish.txt", "a")   
f.write(Bearishtext)
f.close()
#-----------------------------------------------------
Bullish = df[(df['Forecast'] > df['Consensus']) &
        (df['Forecast'] > df['Previous'])]
Bullish = Bullish[['Forecast','Previous','Consensus']]
Bullishdata_str_with_index = Bullish.to_string(index=True)
Bullishtext= "Bearish Index"+"\n""\n"
Bullishtext += Bullishdata_str_with_index
f = open("Bullish.txt", "a")   
f.write(Bullishtext)
f.close()
#-----------------------------------------------------
print(EcoDataInx)
f = open("Economic-Calender-Data_analysis2.txt", "a")
f.write(DFstr)
f.close()