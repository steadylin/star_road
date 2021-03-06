# Generated by Django 2.0.7 on 2020-08-12 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150, verbose_name='订单标题')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='订单总价')),
                ('out_trade_no', models.CharField(max_length=64, unique=True, verbose_name='订单号')),
                ('trade_no', models.CharField(max_length=64, null=True, verbose_name='流水号')),
                ('order_status', models.SmallIntegerField(choices=[(0, '未支付'), (1, '已支付'), (2, '已取消'), (3, '超时取消')], default=0, verbose_name='订单状态')),
                ('pay_type', models.SmallIntegerField(choices=[(1, '支付宝'), (2, '微信支付')], default=1, verbose_name='支付方式')),
                ('pay_time', models.DateTimeField(null=True, verbose_name='支付时间')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_user', to=settings.AUTH_USER_MODEL, verbose_name='下单用户')),
            ],
            options={
                'verbose_name': '订单记录',
                'verbose_name_plural': '订单记录',
                'db_table': 'star_road_order',
            },
        ),
    ]
