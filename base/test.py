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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
# 测试网站登录功能


class test(unittest.TestCase):
    def setUp(self):
        # 指定测试所用的浏览器（chrome、Firefox、IE、edge、Safari...）
        self.driver = webdriver.Firefox()
        self.utils = Utils()

    '''测试邮箱登录'''
    @unittest.skip('暂不测试')
    def test_login(self):
        try:
            print(os.path.relpath('D:\selenium\Autoselenium\screenShot'))
            self.driver.get('https://mail.163.com/')
            """全屏显示窗口"""
            self.driver.maximize_window()
            print("页面标题：{}".format(self.driver.title))
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_link_text("密码登录").click()
            """设置页面加载模式page loading strategy"""
            desired_caps = DC.CHROME
            desired_caps['pageLoadStrategy'] = 'none'
            print("当前页面的句柄：{}".format(self.driver.current_window_handle))
            self.driver.implicitly_wait(10)
            """进行iframe切换"""
            iframe = self.driver.find_element_by_tag_name("iframe")
            self.driver.switch_to.frame(iframe)
            self.driver.implicitly_wait(3)
            account = self.driver.find_element_by_css_selector('input[placeholder="邮箱帐号或手机号码"]')
            account.clear()
            account.send_keys('haha')
            self.driver.implicitly_wait(3)
            password = self.driver.find_element_by_css_selector('input[placeholder="输入密码"]')
            password.clear()
            password.send_keys('123456')
            self.driver.implicitly_wait(3)
            login = self.driver.find_element_by_link_text("登  录")
            login.click()
            sleep(3)
            verify = self.driver.find_element_by_css_selector("div#ScapTcha")
            actions = ActionChains(self.driver)
            actions.move_to_element(verify).perform()
            self.driver.implicitly_wait(3)
            hover_img = self.driver.find_element_by_css_selector("span.yidun_tips__point")
            answer = hover_img.text
            print("需要验证的文字为：{},类型为：{}".format(answer, type(answer)))
            self.driver.implicitly_wait(3)
            verify_img = self.driver.find_element_by_css_selector("img.yidun_bg-img")
            sleep(3)
            print("图片上的验证文字为：{}".format(verify_img.text))
            # account = self.driver.find_element_by_css_selector("input[placeholder='电子邮件、电话或 Skype']")
            # locator = (By.CSS_SELECTOR, "input[placeholder='电子邮件、电话或 Skype']")
            # el_account = WebDriverWait(self.driver, timeout=10).until(\
            #     EC.presence_of_element_located(locator))
            """切换返回当前窗口"""
            self.driver.switch_to.window(self.driver.current_window_handle)
        except Exception as e:
            """错误截图保存"""
            self.utils.get_screenShot(self.driver)
            raise e
        finally:
            self.driver.close()
            self.driver.quit()

    """测试下拉选择框，局部控件滑动"""
    def test_select(self):
        try:
            self.driver.get("http://company.conlin360.com:81/zentao/user-login.html")
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()
            account = self.driver.find_element_by_name("account")
            account.clear()
            account.send_keys("gaosha")
            password = self.driver.find_element_by_name("password")
            password.clear()
            password.send_keys("gs123456")
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_css_selector("button#submit").click()
            sleep(3)
            self.driver.find_element_by_link_text("测试").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_css_selector("li[data-id='bug']").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_link_text("提Bug").click()
            self.driver.implicitly_wait(3)
            self.driver.find_element_by_css_selector("a.chosen-single").click()
            """使用js脚本进行局部部件的滚动条滑动:scrollTop =0为滑动至顶端"""
            js = "document.getElementsByClassName('chosen-drop')[0].scrollTop=10000"
            self.driver.execute_script(js)
            sleep(3)
            select = self.driver.find_element_by_css_selector("li[title='微信小程序']")
            select.click()
            sleep(3)
        except Exception as e:
            self.utils.get_screenShot(self.driver)
            raise e
        finally:
            self.driver.close()
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()

