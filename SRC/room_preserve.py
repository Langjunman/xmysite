# -*- coding: utf-8 -*-
import top.api

url = "http://gw.api.taobao.com/router/rest"
port = 9000

req=top.api.AlibabaAliqinFcSmsNumSendRequest(url,port)
req.set_app_info(top.appinfo(appid,secret))

req.extend="123456"
req.sms_type="normal"
req.sms_free_sign_name="阿里大于"
req.sms_param="{\"code\":\"1234\",\"product\":\"alidayu\"}"
req.rec_num=""
req.sms_template_code="SMS_585014"
try:
    resp= req.getResponse()
    print(resp)
except Exception as e:
    print(e)
