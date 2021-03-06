# Generated by Django 3.0.6 on 2020-05-16 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='question_id',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='book',
            name='question_type',
            field=models.CharField(default='0', max_length=5),
        ),
        migrations.AddField(
            model_name='book',
            name='set_id',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='book',
            name='user_id',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
