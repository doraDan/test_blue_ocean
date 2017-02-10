# encoding:utf-8
import os
import unittest


class CeleryCheck(unittest.TestCase):
    """celery环境检查"""

    celery_dict = {

    }
    dev_host = {
        "order_celery": '''ssh dada@192.168.1.201 "ps -ef |grep order_celery | \
        grep '/data/log/uwsgi/dev/' | grep -v grep"''',
        "celery_python": '''ssh dada@192.168.1.201 "ps -ef |grep celery | grep '/data/log/uwsgi/dev/' | grep -v grep"''',
        "celery_java": '''ssh dada@192.168.1.202 "ps -ef |grep celery | grep '/data/log/uwsgi/dev/' | grep -v grep"''',
    }

    qa_host = {
        "order_celery": '''ssh app@10.9.111.183 "ps -ef |grep order_celery | grep -v grep"''',
        "celery_python": '''ssh app@10.9.158.110 "ps -ef |grep celery | grep -v grep"''',
    }

    def test_check(self):
        """celery检查"""
        host = self.celery_dict
        for key, value in host.iteritems():
            output = os.popen(host[key])
            str_output = output.read()
            try:
                assert str_output.__len__() > 0
                print key, "ok"
            except Exception, e:
                print key, "fail"

