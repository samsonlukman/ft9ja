# Generated by Django 4.1.7 on 2023-10-07 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashb', '0010_alter_trade_trader_delete_trader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='trade',
            name='trader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashb.trader'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
