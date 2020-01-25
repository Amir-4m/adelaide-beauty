# Generated by Django 2.2.5 on 2020-01-24 16:48

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=120)),
                ('brand', models.CharField(default='brand', max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(default='description', null=True)),
                ('short_description', models.TextField(default='s-desc', null=True)),
                ('pros', models.TextField(default='pros', null=True)),
                ('cons', models.TextField(default='cons', null=True)),
                ('old_price', models.DecimalField(decimal_places=3, default=0.0, max_digits=20)),
                ('price', models.DecimalField(decimal_places=3, default=0.0, max_digits=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.upload_image_path)),
                ('sale', models.BooleanField(default=False)),
                ('popular', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Category')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
