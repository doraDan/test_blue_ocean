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
        "business_coupon": "/coupon_service/healthcheck",
        "bdapi": "/health/check"
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
        "accouting": http + "192.168.1.150:20010" + interface["accounting"],
        "bdapi": http + "bdapi.dev.imdada.cn" + interface["bdapi"]
    }

    urls_qa = {
        "openapi_new": http + "newopen.qa.imdada.cn" + interface["openapi_new"],
        "openapi_old": http + "public.qa.imdada.cn" + interface["openapi_old"],
        "dfinance": http + "10.9.126.32:8080" + interface["dfinance"],
        "modelservice": http + "10.9.158.77:8080" + interface['modelservice'],
        "api": http + "api.qa.imdada.cn" + interface["api"],
        "order": http + "10.9.178.162:80" + interface["order"],
        "basic_server": http + "10.9.174.15:8080" + interface["basic_server"],
        "dfinance_coupon": http + "10.9.105.87:8080" + interface["dfinance_coupon"],
        "accouting": http + "10.9.110.207:8080" + interface["accounting"],
        "business_coupon": http + "10.9.96.95:80" + interface["business_coupon"],
        "bdapi": http + "bdapi.qa.imdada.cn" + interface["bdapi"]

    }

    check_str = {
        "openapi_old": "ok",
        "openapi_new": "success",
        "dfinance": "true",
        "modelservice": "status",
        "api": "status",
        "order": "ok",
        "basic_server": "",
        "dfinance_coupon": "true",
        "business_coupon": "",
        "accouting": "true",
        "bdapi": "ok"
    }

    def test_check_openapi_old(self):
        """openAPI_老服务"""
        resopnse = requests.get(self.urls_dict["openapi_old"])
        assert resopnse.status_code == 200
        assert resopnse.text.__contains__(self.check_str["openapi_old"])

    def test_check_openapi_new(self):
        """openAPI_新服务"""
        resopnse = requests.get(self.urls_dict["openapi_new"])
        assert resopnse.status_code == 200
        assert resopnse.text.__contains__(self.check_str["openapi_new"])

    def test_check_dfinance(self):
        """账户"""
        resopnse = requests.get(self.urls_dict["dfinance"])
        assert resopnse.status_code == 200
        assert resopnse.text.__contains__(self.check_str["dfinance"])

    def test_check_modelservice(self):
        """modelservice"""
        resopnse = requests.get(self.urls_dict["modelservice"])
        assert resopnse.status_code == 200
        assert resopnse.text.__contains__(self.check_str["modelservice"])

    def test_check_api(self):
        """api"""
        resopnse = requests.get(self.urls_dict["api"])
        assert resopnse.status_code == 200
        assert resopnse.text.__contains__(self.check_str["api"])

    def test_check_order(self):
        """订单(order/orderadd)"""
        resopnse = requests.get(self.urls_dict["order"])
        assert resopnse.status_code == 200
        assert resopnse.text.__contains__(self.check_str["order"])

    def test_check_basic_server(self):
        """运费服务"""
        resopnse = requests.get(self.urls_dict["basic_server"])
        assert resopnse.status_code == 200
        assert resopnse.text.__contains__(self.check_str["basic_server"])

    def test_check_dfinance_coupon(self):
        """优惠券-账户"""
        resopnse = requests.get(self.urls_dict["dfinance_coupon"])
        assert resopnse.status_code == 200
        assert resopnse.text.__contains__(self.check_str["dfinance_coupon"])

    def test_check_business_coupon(self):
        """优惠券-业务"""
        resopnse = requests.get(self.urls_dict["business_coupon"])
        assert resopnse.status_code == 200
        assert resopnse.text.__contains__(self.check_str["business_coupon"])

    def test_check_accouting(self):
        """记账服务"""
        resopnse = requests.get(self.urls_dict["accouting"])
        assert resopnse.status_code == 200
        assert resopnse.text.__contains__(self.check_str["accouting"])

    def test_check_bdapi(self):
        """openAPI_老服务"""
        resopnse = requests.get(self.urls_dict["bdapi"])
        assert resopnse.status_code == 200
        assert resopnse.text.__contains__(self.check_str["bdapi"])

    # def test_check_server(self):
    #     """
    #         环境服务是否启动
    #     """
    #     urls_dict = self.urls_dict
    #     for key, value in urls_dict.iteritems():
    #         print
    #         print key
    #         response = requests.get(urls_dict[key])
    #         try:
    #             assert response.status_code == 200
    #             assert response.text.__contains__(self.check_str[key])
    #             print urls_dict[key], response.status_code
    #         except Exception, e:
    #             print e
    #             print key, "fail"