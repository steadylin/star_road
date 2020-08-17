from django.db import models

# Create your models here.
from user.models import User


class Order(models.Model):
    """订单模型"""
    status_choices = (
        (0, '未支付'),
        (1, '已支付'),
        (2, '已取消'),
        (3, '超时取消'),
    )
    pay_choices = (
        (1, '支付宝'),
        (2, '微信支付'),
    )
    subject = models.CharField(max_length=150, verbose_name="订单标题")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="订单总价", default=0)
    out_trade_no = models.CharField(max_length=64, verbose_name="订单号", unique=True)
    trade_no = models.CharField(max_length=64, null=True, verbose_name="流水号")  # 支付宝生成回来的
    order_status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="订单状态")
    pay_type = models.SmallIntegerField(choices=pay_choices, default=1, verbose_name="支付方式")
    pay_time = models.DateTimeField(null=True, verbose_name="支付时间")
    # 一个用户可以下多个订单，一个订单只属于一个用户，一对多的关系，关联字段写在多个一方，写在order方
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.DO_NOTHING, db_constraint=False,
                             verbose_name="下单用户")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    month_num = models.CharField(max_length=5, verbose_name='购买的月数', null=True)

    class Meta:
        db_table = "star_road_order"
        verbose_name = "订单记录"
        verbose_name_plural = "订单记录"

    def __str__(self):
        return "%s - ￥%s" % (self.subject, self.total_amount)
