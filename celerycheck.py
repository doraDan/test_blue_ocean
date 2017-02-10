# -*- coding: utf8 -*-
import commands
import os

class Celerycheck:
    def __init__(self):
        pass

    dev_host = {
        "order_celery": '''ssh dada@192.168.1.201 "ps -ef |grep order_celery | grep '/data/log/uwsgi/dev/' | grep -v grep"''',
        "celery_python": '''ssh dada@192.168.1.201 "ps -ef |grep celery | grep '/data/log/uwsgi/dev/' | grep -v grep"''',
        "celery_java": '''ssh dada@192.168.1.202 "ps -ef |grep celery | grep '/data/log/uwsgi/dev/' | grep -v grep"''',
    }

    qa_host = {
        "order_celery": '''ssh app@10.9.111.183 "ps -ef |grep order_celery | grep -v grep"''',
        "celery_python": '''ssh app@10.9.158.110 "ps -ef |grep celery | grep -v grep"''',
    }

    def check(self):
        # output = os.popen(self.dev_host['celery_python'])
        # print self.dev_host['celery_python']
        # print output.read()
        # assert output.read().__contains__("worker")
        # assert output.read() != ""
        # assert 1 != 2
        for key, value in self.qa_host.iteritems():
            output = os.popen(self.qa_host[key])
            str_output = output.read()
            print self.qa_host[key]
            # print str_output
            print str_output.__len__()
            try:
                assert str_output.__len__() > 0
                print key, "ok"
            except Exception, e:
                print e
                print key, "fail"

if __name__ == "__main__":
    Celerycheck().check()