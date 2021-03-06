# Generated by Django 3.1.5 on 2021-01-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
                ('tagline', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='shop/images')),
            ],
        ),
    ]
