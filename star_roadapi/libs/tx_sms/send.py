from qcloudsms_py import SmsSingleSender
from star_roadapi.utils.logger import log
from . import settings


# 生成4位随机验证码
def get_code():
    import random
    str_code = ''
    for i in range(4):
        str_code += str(random.randint(0, 9))  # int需要转成str
    print(str_code)
    return str_code


# 发送验证码
def send_str_code(phone, str_code):
    print('sms')
    sender = SmsSingleSender(settings.appid, settings.appkey)
    params = [str_code, '3']  # 3指短信过期时间3分钟
    try:
        result = sender.send_with_param(86, phone, settings.template_id, params, sign=settings.sms_sign, extend="",
                                        ext="")
        if result.get('result') == 0:
            return True
        else:
            return False
    except Exception as e:
        log.error(f'手机号{phone}短信发送失败，错误为{str(e)}')
