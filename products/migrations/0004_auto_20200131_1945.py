# Generated by Django 2.2.5 on 2020-01-31 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200131_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, max_length=620, null=True),
        ),
    ]