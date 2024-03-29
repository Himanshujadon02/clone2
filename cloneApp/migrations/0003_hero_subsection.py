# Generated by Django 4.2.3 on 2023-12-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloneApp', '0002_popular_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero_subsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='cloneApp/images')),
                ('content', models.TextField()),
            ],
        ),
    ]
