from rest_framework.throttling import SimpleRateThrottle


class SMSThrotting(SimpleRateThrottle):
    scope = 'sms'

    def get_cache_key(self, request, view):
        print('00')
        mobilephone = request.query_params.get('mobilephone')
        return self.cache_format % {'scope': self.scope, 'ident': mobilephone}


