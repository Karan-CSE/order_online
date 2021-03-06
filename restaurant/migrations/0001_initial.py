# Generated by Django 2.0.2 on 2018-04-05 05:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('ITEMID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=20)),
                ('image', models.ImageField(default='images/none/noimg.png', upload_to='images')),
                ('item_price', models.PositiveIntegerField()),
                ('reviews', models.CharField(max_length=100)),
            ],
        ),
    ]
