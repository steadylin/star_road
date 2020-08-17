from rest_framework import serializers
from . import models
from user.models import User
from rest_framework.exceptions import ValidationError


class OrderSerializer(serializers.ModelSerializer):
    num = serializers.CharField()
    class Meta:
        model = models.Order
        fields = ['total_amount', 'subject', 'pay_type', 'num']
        extra_kwargs = {
            'total_amount': {'required': True},
            'pay_type': {'required': True},
            'num': {'write_only': True},
        }

    def _check_price(self, attrs):
        total_amount = attrs.get('total_amount')
        num = attrs.pop('num')
        total_price = 6*int(num)
        if total_amount == total_price:
            return total_amount
        else:
            raise ValidationError('总价非法')

    def _gen_out_trade_no(self):
        import uuid
        return str(uuid.uuid4()).replace('-', '')

    def _get_user(self):
        # 需要request对象(需要视图通过context把reuqest对象传入。重写create方法)
        request = self.context.get('request')
        return request.user

    def _gen_pay_url(self, out_trade_no, total_amout, subject):
        # total_amout是Decimal类型，识别不了，需要转换成float类型
        from star_roadapi.libs.ali_pay import alipay, gateway
        from django.conf import settings
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=out_trade_no,
            total_amount=float(total_amout),
            subject=subject,
            return_url=settings.RETURN_URL,  # get回调，前台地址
            notify_url=settings.NOTIFY_URL  # post回调，后台地址
        )
        return gateway + order_string

    def _before_create(self, attrs, user, pay_url, out_trade_no):
        attrs['user'] = user
        attrs['out_trade_no'] = out_trade_no

        self.context['pay_url'] = pay_url

    def validate(self, attrs):
        '''
        # 1）订单总价校验
        # 2）生成订单号
        # 3）支付用户：request.user
        # 4）支付链接生成
        # 5）入库(两个表)的信息准备
        '''
        # 1）订单总价校验
        total_amout = self._check_price(attrs)
        # 2）生成订单号
        out_trade_no = self._gen_out_trade_no()
        # 3）支付用户：request.user
        user = self._get_user()
        # 4）支付链接生成
        pay_url = self._gen_pay_url(out_trade_no, total_amout, attrs.get('subject'))
        # 5）入库(两个表)的信息准备
        self._before_create(attrs, user, pay_url, out_trade_no)
        return attrs

    def create(self, validated_data):

        order = models.Order.objects.create(**validated_data)

        # username = validated_data.get('user')
        # User.objects.filter(username=username).update(is_vip=1)
        return order
