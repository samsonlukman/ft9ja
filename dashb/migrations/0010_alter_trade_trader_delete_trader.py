# Generated by Django 4.1.7 on 2023-10-06 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashb', '0009_trader_alter_trade_trader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='trader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trade_user', to='dashb.user'),
        ),
        migrations.DeleteModel(
            name='Trader',
        ),
    ]
