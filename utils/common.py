import os
import time


class Utils():
    def get_screenShot(self, driver):
        """
        :param driver: 浏览器驱动
        :return:
        """
        """在进行截图保存的时候，需要注意文件名，windows系统中，文件名不
        能包括特殊字符，否则会保存失败"""
        folder = time.strftime("%Y%m%d")
        filepath = '../screenShots'
        pic_name = time.strftime("%H%M%S")
        """进行路径组合，还可以使用os.path.join方法"""
        if os.path.exists(filepath):
            if os.path.exists(filepath+'/'+folder):
                driver.get_screenshot_as_file(filepath+'/{}/{}.png'.format(folder, pic_name))
            else:
                os.makedirs(filepath + './{}'.format(folder))
                driver.get_screenshot_as_file(filepath + '/{}/{}.png'.format(folder, pic_name))
        else:
            """创建一级目录"""
            os.mkdir(filepath)
            """在指定的目录下创建子目录"""
            os.makedirs(filepath+'./{}'.format(folder))
            driver.get_screenshot_as_file(filepath+"/{}/{}.png".format(folder, pic_name))


# if __name__ == '__main__':
#     utils = Utils()
#     utils.get_screenShot(webdriver.Chrome())

