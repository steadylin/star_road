import os

# 支付宝沙箱应用appid
APPID = 2021000116660237
# 自己生成的私钥
APP_PRIVATE_KEY_STRING = open(os.path.join(os.path.dirname(__file__), 'pem', 'private_key.pem')).read()
# 沙箱公钥
ALIPAY_PUBLIC_KEY_STRING = open(os.path.join(os.path.dirname(__file__), 'pem', 'al_public_key.pem')).read()
# 秘钥长度
SIGN_TYPE = 'RSA2'
DEBUG = True
GATEWAY = 'https://openapi.alipaydev.com/gateway.do?' if DEBUG else 'https://openapi.alipay.com/gateway.do?'
