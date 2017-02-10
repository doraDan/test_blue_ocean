# -*- coding: utf8 -*-

class Url:
    def __init__(self):
        pass

    http = "http://"
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
        "accouting": http + "192.168.1.150:20010" + interface["accounting"]
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
        "business_coupon": http + "10.9.96.95:80" + interface["business_coupon"]
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
        "accouting": "true",
        "business_coupon": ""
    }
