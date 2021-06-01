#-*-coding:utf-8-*-
#!/usr/bin/env python
from selenium import webdriver
import time
import os,sys
import glob

options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가

path = "./*"
past_file_list = glob.glob(path)
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
#options.add_argument('user-agent={0}'.format(user_agent))
#options.add_argument("--remote-debugging-port=9222")

# driver 실행
dr = webdriver.Chrome('./chromedriver',options=options)
dr.get('http://data.seoul.go.kr/dataList/OA-15577/S/1/datasetView.do')
dr.find_element_by_xpath('/html/body/div[3]/section/div[2]/div/section/form/div[2]/div[2]/table/tbody/tr/td[6]/a').click()
time.sleep(5)
new_file = None
while True:
	temp = 0
	file_list = glob.glob(path)
	for i in file_list:
		if "crdownload" in i:
			temp = 0
			break
		else:
			temp = 1
	if temp == 1:
		new_file_list = file_list
		break
for i in new_file_list:
	if i in past_file_list:
		continue
	else:
		new_file = i
# driver 종료
dr.quit()
new_file = new_file[2:]
new_file_change=new_file.replace('(','\(').replace(')','\)')
print('new_file = ',new_file_change)
text = 'unzip '+new_file_change+' -d ./store'
print('text = ',text)
text2 = 'rm -rf '+new_file_change
os.system(text)
os.system(text2)
