# -*- coding: utf8 -*-

import requests

# 检查
import sys

from celerycheck import Celerycheck
from urls import Url

if sys.argv[1] == "dev":
    urlsdict = Url.urls_dev
elif sys.argv[1] == "qa":
    urlsdict = Url.urls_qa
checkstr = Url.check_str

for key, value in urlsdict.iteritems():
    print
    print key
    response = requests.get(urlsdict[key])
    print urlsdict[key]
    print response.status_code
    # print urlsdict[key] + response.text
    try:
        assert response.status_code == 200
        assert response.text.__contains__(checkstr[key])
    except Exception,e:
        print e

Celerycheck().check()
