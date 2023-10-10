# Generated by Django 4.1.7 on 2023-10-06 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashb', '0008_rename_customeuser_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dashb.user')),
            ],
        ),
        migrations.AlterField(
            model_name='trade',
            name='trader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashb.trader'),
        ),
    ]