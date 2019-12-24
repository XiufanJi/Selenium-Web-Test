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
from utils.common import utils
# 测试网站登录功能


class test(unittest.TestCase):
    def setUp(self):
        # 指定测试所用的浏览器（chrome、Firefox、IE、edge、Safari...）
        self.driver = webdriver.Chrome()
        self.utils = utils()
        # self.options = DC

    '''测试邮箱登录'''
    def test_login(self):
        try:
            print(os.path.relpath('D:\selenium\Autoselenium\screenShot'))
            self.driver.get('https://discuss.appium.io/')
            # desired_caps = DC.CHROME
            # desired_caps['pageLoadStrategy'] = 'none'
            # print("当前页面的句柄：{}".format(self.driver.current_window_handle))
            # self.driver.implicitly_wait(5)
            # login = self.driver.find_element_by_css_selector('button.login-button')
            # login.click()
            # sleep(3)
            # # 找到带官网字样的链接地址
            # self.driver.find_element_by_css_selector('button.github').click()
            # handles = self.driver.window_handles
            # print("当前的所有句柄为：{}".format(handles))
            # self.driver.switch_to.window(handles[1])
            # handles = self.driver.window_handles
            # self.driver.switch_to.window(handles[1])
            # self.driver.implicitly_wait(3)
            # print("跳转后页面的句柄：{}".format(self.driver.current_window_handle))
            # account = self.driver.find_element_by_id("login_field")
            # account.clear()
            # account.send_keys('your email address')
            # password = self.driver.find_element_by_id("password")
            # password.clear()
            # password.send_keys("your password")
            self.driver.find_element_by_name("commit").click()
            self.driver.implicitly_wait(3)
            # account = self.driver.find_element_by_css_selector("input[placeholder='电子邮件、电话或 Skype']")
            # locator = (By.CSS_SELECTOR, "input[placeholder='电子邮件、电话或 Skype']")
            # el_account = WebDriverWait(self.driver, timeout=10).until(\
            #     EC.presence_of_element_located(locator))
            # if el_account.is_displayed:
            #     account.clear()
            #     account.send_keys("your account")
            #     nextStep = self.driver.find_element_by_css_selector("input[value='下一步']")
            #     nextStep.click()
            #     sleep(3)
            #     password = self.driver.find_element_by_css_selector('input[placeholder="密码"]')
            #     password.send_keys('your password')
            #     login = self.driver.find_element_by_css_selector('input[value="登录"]')
            #     login.click()
            #     sleep(3)
            #     self.assertEquals("", "")
        except Exception as e:
            """错误截图保存"""
            self.utils.get_screenShot(self.driver)
            raise e
        finally:
            self.driver.close()
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()

