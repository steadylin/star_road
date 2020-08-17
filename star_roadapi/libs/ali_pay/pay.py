# luffyapi\libs\ali_pay\pay.py

from alipay import AliPay
from . import settings

alipay = AliPay(
    appid=settings.APPID,
    app_notify_url='http://127.0.0.1:8000/home/',  # 支付结果回调地址
    app_private_key_string=settings.APP_PRIVATE_KEY_STRING,  # 生成的私钥
    alipay_public_key_string=settings.ALIPAY_PUBLIC_KEY_STRING,  # 沙箱公钥
    sign_type=settings.SIGN_TYPE,  # RSA or RSA2#秘钥长度
    debug=settings.DEBUG  # False by default
)
gateway = settings.GATEWAY  # 网关
