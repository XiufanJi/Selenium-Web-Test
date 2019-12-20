# coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DC
import time
# 测试网站登录功能


class test():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.options = DC

    def login(self):
        try:
            self.driver.get('http://www.baidu.com')
            sleep(3)
            print("当前页面的句柄：{}".format(self.driver.current_window_handle))
            search = self.driver.find_element_by_id("kw")
            search.clear()
            search.send_keys("outlook")
            # 模拟enter键操作
            self.driver.find_element_by_id("kw").submit()
            sleep(3)
            # 找到带官网字样的链接地址
            self.driver.find_element_by_partial_link_text("Outlook - 来自 Microsoft").click()
            desired_caps = DC.CHROME
            desired_caps['pageLoadStrategy'] = 'none'
            print("跳转后页面的句柄：{}".format(self.driver.window_handles))
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[1])
            sleep(3)
            self.driver.find_element_by_link_text("登录").click()
            # self.driver.find_element_by_css_selector("ul>li:nth-child(2)").click()
            sleep(3)
            password = WebDriverWait(self.driver, timeout=10).until(self.driver.find_element_by_css_selector\
                                                             ("div.placeholderContainer>input:nth-child(1)"))
            print('')
            password.clear()
            password.send_keys("timegao@outlook.com")
            nextStep = self.driver.find_element_by_css_selector("input[value=下一步]")
            nextStep.click()
            sleep(3)
        except Exception as e:
            self.driver.get_screenshot_as_file('../screenShot/{}.png'.format(time.strftime("%Y-%m-%d %H:%M:%S")))
            raise e
        finally:
            self.driver.close()
            self.driver.quit()


if __name__ == '__main__':
    test().login()

