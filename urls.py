# encoding:utf-8
import unittest

import requests


class Url(unittest.TestCase):
    """检查各个环境服务是否启动"""
    http = "http://"
    urls_dict = {

    }
    interface = {
        "openapi_new": "/health",
        "openapi_old": "/openapi/healthcheck",
        "dfinance": "/dfinance/health",
        "modelservice": "/modelservice/task/v2/list/cityId/1",
        "api": "/api/healthcheck",
        "order": "/tequila/healthcheck",
        "accounting": "/accounting/health",
        "basic_server": "/basic-service-0.2.0/health",
        "dfinance_coupon": "/coupon/health",
        "business_coupon": "/coupon_service/healthcheck"
    }
    urls_dev = {
        "openapi_new": http + "192.168.1.202:8981" + interface["openapi_new"],
        "openapi_old": http + "public.dev.imdada.cn" + interface["openapi_old"],
        "dfinance": http + "dfinance.dev.imdada.cn" + interface["dfinance"],
        "modelservice": http + "192.168.1.202:8080" + interface['modelservice'],
        "api": http + "api.dev.imdada.cn" + interface["api"],
        "order": http + "192.168.1.201:80" + interface["order"],
        "basic_server": http + "192.168.1.202:8090" + interface["basic_server"],
        "dfinance_coupon": http + "192.168.1.150:13101" + interface["dfinance_coupon"],
        "business_coupon": http + "192.168.1.201:8092" + interface["business_coupon"],
    }
    # "accouting": http + "192.168.1.150:20010" + interface["accounting"],
    urls_qa = {
        "openapi_new": http + "newopen.qa.imdada.cn" + interface["openapi_new"],
        "openapi_old": http + "public.qa.imdada.cn" + interface["openapi_old"],
        "dfinance": http + "10.9.126.32:8080" + interface["dfinance"],
        "modelservice": http + "10.9.158.77:8080" + interface['modelservice'],
        "api": http + "api.qa.imdada.cn" + interface["api"],
        "order": http + "10.9.178.162:80" + interface["order"],
        "basic_server": http + "10.9.174.15:8080" + interface["basic_server"],
        "dfinance_coupon": http + "10.9.105.87:8080" + interface["dfinance_coupon"],
        "business_coupon": http + "10.9.96.95:80" + interface["business_coupon"]
    }
    # "accouting": http + "10.9.110.207:8080" + interface["accounting"],
    check_str = {
        "openapi_old": "ok",
        "openapi_new": "success",
        "dfinance": "true",
        "modelservice": "status",
        "api": "status",
        "order": "ok",
        "basic_server": "",
        "dfinance_coupon": "true",
        "business_coupon": ""
    }
    # "accouting": "true",

    def test_check_server(self):
        """
            环境服务是否启动
        """
        urls_dict = self.urls_dict
        for key, value in urls_dict.iteritems():
            print
            response = requests.get(urls_dict[key])
            # print urls_dict[key]
            # print response.status_code
            try:
                assert response.status_code == 200
                assert response.text.__contains__(self.check_str[key])
                print key, urls_dict[key], response.status_code
            except Exception, e:
                print e
                print key, "fail"
