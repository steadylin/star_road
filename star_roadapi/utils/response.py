from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, code=100, msg='成功', data=None, status=None, headerrs=None, **kwargs):
        dic = {'code': code, 'msg': msg}
        if data:
            dic = {'code': code, 'msg': msg, 'data': data}
        dic.update(kwargs)
        super().__init__(data=dic, status=status, headers=headerrs)





