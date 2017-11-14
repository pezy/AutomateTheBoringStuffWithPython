#!python3
# cmd_email.py - send email by command

from selenium import webdriver
from time import sleep
import sys

if len(sys.argv) < 3:
    print('Usage: python cmd_email.py [sendto] [message]')
    sys.exit()

browser = webdriver.Chrome()
browser.get('https://ui.ptlogin2.qq.com/cgi-bin/login?style=9&appid=522005705&daid=4&s_url=https%3A%2F%2Fw.mail.qq.com%2Fcgi-bin%2Flogin%3Fvt%3Dpassport%26vm%3Dwsk%26delegate_url%3D%26f%3Dxhtml%26target%3D&hln_css=http%3A%2F%2Fmail.qq.com%2Fzh_CN%2Fhtmledition%2Fimages%2Flogo%2Fqqmail%2Fqqmail_logo_default_200h.png&low_login=1&hln_autologin=%E8%AE%B0%E4%BD%8F%E7%99%BB%E5%BD%95%E7%8A%B6%E6%80%81&pt_no_onekey=1')
sleep(1)
try:
    qq = browser.find_element_by_id('u')
    qq.send_keys('') # qq
    password = browser.find_element_by_id('p')
    password.send_keys('') ## qq password
    go = browser.find_element_by_id('go')
    go.click()
    sleep(1)
    password2 = browser.find_element_by_id('pwd')
    password2.send_keys('') # mail password
    password2.submit()
    sleep(1)
    write = browser.find_element_by_css_selector('.qm_btnIcon')
    write.click()
    sendto = browser.find_element_by_id('showto')
    sendto.send_keys(sys.argv[1])
    subject = browser.find_element_by_id('subject')
    subject.send_keys('System mail by python')
    content = browser.find_element_by_id('content')
    content.send_keys(' '.join(sys.argv[2:]))
    sleep(2)
    submit = browser.find_element_by_css_selector('.qm_btn.qm_btn_Blue')
    submit.click()
except:
    print('Was not able to find an element with your qq.')
