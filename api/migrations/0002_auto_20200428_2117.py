# Generated by Django 3.0.5 on 2020-04-28 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]