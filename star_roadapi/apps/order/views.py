from django.shortcuts import render

# Create your views here.


from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from . import models, serializer
from rest_framework.response import Response


class PayView(GenericViewSet, CreateModelMixin):
    queryset = models.Order.objects.all()
    serializer_class = serializer.OrderSerializer

    # 重写create方法
    def create(self, request, *args, **kwargs):
        # print(request.data)
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.context.get('pay_url'))


# 支付成功回调
from rest_framework.views import APIView
from user.models import User


class SuccessView(APIView):
    authentication_classes = []  # 禁用jwt

    def get(self, request, *args, **kwargs):
        # print(request.query_params)
        out_trade_no = request.query_params.get('out_trade_no')
        order = models.Order.objects.filter(out_trade_no=out_trade_no).first()
        if order.order_status == 1:
            return Response(True)
        else:
            return Response(False)

    def post(self, request, *args, **kwargs):
        '''
        支付宝回调接口
        '''
        print('post')
        from star_roadapi.libs.ali_pay import alipay
        from star_roadapi.utils.logger import log
        # 注意这个小细节,把他转成字典
        data = request.data.dict()
        out_trade_no = data.get('out_trade_no', None)
        gmt_payment = data.get('gmt_payment', None)
        signature = data.pop("sign")
        # 验证签名
        success = alipay.verify(data, signature)
        if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
            order_obj = models.Order.objects.filter(out_trade_no=out_trade_no).update(order_status=1,
                                                                                      pay_time=gmt_payment)
            id = order_obj.user_id
            num = order_obj.month_num
            res = User.objects.filter(id=id).update(is_vip=1)
            import time
            vip_expire = time.time() + 86400*30*num
            res2 = User.objects.filter(id=id).update(vip_expire=vip_expire)
            if res and res2:
                log.info(f'用户id{id}的权限、过期时间修改完成')
            log.info('%s订单支付成功' % out_trade_no)
            return Response('success')
        else:
            log.info('%s订单有问题' % out_trade_no)
            return Response('error')






