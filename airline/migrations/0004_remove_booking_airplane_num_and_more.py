# Generated by Django 4.0.4 on 2022-04-27 02:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0003_alter_airplane_airplane_date_of_departure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='airplane_num',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user_email',
        ),
        migrations.AddField(
            model_name='booking',
            name='airplane',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='airline.airplane', verbose_name='Airplane'),
        ),
        migrations.AddField(
            model_name='booking',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
