# encoding:utf-8

# 检查
import sys
import unittest

import HTMLTestRunner
from celerycheck import CeleryCheck
from urls import Url
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    Url.urls_dict = Url.urls_qa
    CeleryCheck.celery_dict = CeleryCheck.qa_host
    result_path = "result.html"
    fp = file(result_path, "wb")
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(CeleryCheck))
    suit.addTest(unittest.makeSuite(Url))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="environment check result", description="")
    result = unittest.TextTestResult("result.html","environment check","check_dev.py")
    runner.run(suit)

