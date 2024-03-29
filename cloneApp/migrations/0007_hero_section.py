# Generated by Django 4.2.3 on 2023-12-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloneApp', '0006_why_netcore'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='', upload_to='cloneApp/images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
