import pyqrcode
# url = pyqrcode.create('https://www.linkedin.com/in/igishaan-gupta-0191031bb/')
# url.svg('ISH_LINkedIN.svg',scale=5)
# url.eps('ISH_LINkedIN.eps',scale=2.5)
#
big_code = pyqrcode.create('https://www.linkedin.com/in/igishaan-gupta-0191031bb/', error='L', version=5, mode='binary')
big_code.png('ISH_LINkedIN.png', scale=5, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
big_code.show()