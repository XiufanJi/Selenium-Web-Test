# coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import unittest
import os
from utils.common import Utils
# 测试网站登录功能


class test(unittest.TestCase):
    def setUp(self):
        # 指定测试所用的浏览器（chrome、Firefox、IE、edge、Safari...）
        self.driver = webdriver.Chrome()
        self.utils = Utils()

    '''测试邮箱登录'''
    def test_login(self):
        try:
            print(os.path.relpath('D:\selenium\Autoselenium\screenShot'))
            self.driver.get('https://mail.163.com/')
            print("页面标题：{}".format(self.driver.title))
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_link_text("密码登录").click()
            print("页面标题：{}".format(self.driver.title))
            desired_caps = DC.CHROME
            desired_caps['pageLoadStrategy'] = 'none'
            print("当前页面的句柄：{}".format(self.driver.current_window_handle))
            # self.driver.implicitly_wait(5)
            account = self.driver.find_element_by_css_selector('input[placeholder="邮箱帐号或手机号码"]')
            account.clear()
            account.send_keys('haha')
            password = self.driver.find_element_by_css_selector('input[placeholder="输入密码"]')
            password.clear()
            password.send_keys('123456')
            # account = self.driver.find_element_by_css_selector("input[placeholder='电子邮件、电话或 Skype']")
            # locator = (By.CSS_SELECTOR, "input[placeholder='电子邮件、电话或 Skype']")
            # el_account = WebDriverWait(self.driver, timeout=10).until(\
            #     EC.presence_of_element_located(locator))
        except Exception as e:
            """错误截图保存"""
            self.utils.get_screenShot(self.driver)
            raise e
        finally:
            self.driver.close()
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()

