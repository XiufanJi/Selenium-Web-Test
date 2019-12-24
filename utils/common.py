import os
import time


class utils():
    def get_screenShot(self, driver):
        """在进行截图保存的时候，需要注意文件名，windows系统中，文件名不
        能包括特殊字符，否则会保存失败"""
        folder = time.strftime("%Y%m%d")
        filepath = '../screenShots'
        now = time.strftime("%H%M%S")
        if os.path.exists(filepath):
            driver.get_screenshot_as_file(filepath+'/{}/{}.png'.format(folder, now))
        else:
            """在指定的目录下创建子目录"""
            os.makedirs('../screenShots'+'./{}'.format(folder))
            driver.get_screenshot_as_file(filepath+"/{}/{}.png".format(folder, now))


# if __name__ == '__main__':
#     utils = utils()
#     utils.get_screenShot()



