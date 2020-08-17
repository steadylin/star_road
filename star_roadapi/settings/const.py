
# 首页轮播图个数
BANNER_COUNTER=5

# 手机验证码缓存的key值
PHONE_CACHE_KEY = 'sms_cache_%s'

# luffyapi\settings\dev.py配置短信发送频率的key

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'star_roadapi.utils.exceptions.common_exception_handler',
    # 短信发送频率限制的key
    'DEFAULT_THROTTLE_RATES': {'sms': '1/m'}  # key要跟类中的scop对应
}
