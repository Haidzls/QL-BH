# Generated by Django 4.2.7 on 2023-12-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.CharField(max_length=255)),
                ('shortDescription', models.CharField(max_length=100)),
                ('slkbd', models.IntegerField(default=0)),
                ('slk', models.IntegerField(default=0)),
                ('slb', models.IntegerField(default=0)),
                ('gianhap', models.IntegerField(default=0)),
                ('giaban', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=50)),
            ],
        ),
    ]
