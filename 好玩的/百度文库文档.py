# -*- codeing=utf-8 -*-
# @Time:2021/7/30 12:06
# @Atuhor:@lwtyh
# @File:demo.py
# @Software:PyCharm

import pandas
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from docx.oxml.ns import qn  # 中文格式
from docx import Document  # 需要安装第三方库python-docx
from docx.shared import Pt  # 用于设置字体样式
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(".\chromedriver.exe")		# 将chromedriver.exe保存在当前目录下
driver.get("https://wenku.baidu.com/view/d16c2b246f85ec3a87c24028915f804d2b1687d6.html?fr=hp_Database&_wkts_=1678093085491&bdQuery=%E7%99%BE%E5%BA%A6%E6%96%87%E5%BA%93")

time.sleep(3)
driver.maximize_window()     # 自动将网页放大至最大化
# 为了避免百度页面变为旧版页面，需要刷新
driver.refresh()
time.sleep(2)
# 点击登录
account_login_button = driver.find_element(By.XPATH, '//div[@class="right-box"]/div[4]')
account_login_button.click()
# 账号密码登录
time.sleep(3)
account_login_button = driver.find_element(By.XPATH, '//div[@class="tang-pass-footerBar"]/p[2]')
account_login_button.click()

time.sleep(4)
# 输入账号
input_account = driver.find_element_by_id('TANGRAM__PSP_11__userName')
input_account.send_keys('请输入账号')
time.sleep(4)
# 输入密码
input_password = driver.find_element_by_id('TANGRAM__PSP_11__password')
input_password.send_keys('请输入密码')
time.sleep(2)
# 点击登录按钮
login_button = driver.find_element_by_id('TANGRAM__PSP_11__submit')
login_button.click()

time.sleep(2)

account_login_button = driver.find_element(By.XPATH, '//div[@class="vcode-body vcode-body-spin"]/div[2]')        # 去掉验证
account_login_button.click()
# 点击登录按钮（重新）
time.sleep(3)
login_button = driver.find_element_by_id('TANGRAM__PSP_11__submit')
login_button.click()

time.sleep(5)

account_login_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div[3]/div[4]/div/div[2]/i')        # 去掉广告
account_login_button.click()


time.sleep(2)
driver.execute_script("window.scrollTo(0,4004)")  # 跳转到页面“阅读所有页面”的位置
time.sleep(3)
driver.find_element(By.XPATH, "//div[@class='fold-page-text']").click()  # 点击“阅读所有页面“
time.sleep(2)


driver.execute_script("window.scrollTo(0,400)")  # 跳转到页面初始位置


#得到当前总页面
all_page = driver.find_element(By.XPATH, "//div[@class='goto-page']").text.replace("/ ", "")

result_text = ""
i = 1
while (i <= int(all_page)):
    driver.find_element(By.XPATH, "//input[@class='cur-page']").clear()  #清除输入值
    driver.find_element(By.XPATH, "//input[@class='cur-page']").send_keys(i)  #设置跳转页面编号
    driver.find_element(By.XPATH, "//input[@class='cur-page']").send_keys(Keys.ENTER, '\ue007')  # 回车键
    time.sleep(2)
    result_text = result_text + driver.find_element(By.XPATH, "//div[@id='pageNo-{0}']".format(i)).text  #得到页面的文本
    time.sleep(2)
    i += 1

result_text = result_text.replace("\n", "")
zf = 0
while zf <= 9:
    s = str(zf) + "、"
    # print (s)
    result_text = result_text.replace(s, "\n" + s)
    zf += 1
for zf_s in ('一', '二', '三', '四', '五', '六', '七', 'A', 'B', 'C', 'D', 'E'):
    s = zf_s + "、"
    t = zf_s + "."
    result_text = result_text.replace(s, "\n" + s).replace(t, "\n" + t)
result_text = result_text.replace("\n\n", "\n")

docx_path = "课程设计.docx"
doc = Document()
doc.styles["Normal"].font.name = u"宋体"  # 设置字体样式
doc.styles["Normal"].font.size = Pt(14)  # 设置字体大小
doc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')  # 设置文档的基础样式
doc.add_paragraph(result_text)  # 增加一个paragraph,写入内容
doc.save(docx_path)  # 保存文档
