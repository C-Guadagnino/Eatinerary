# Generated by Django 4.0.3 on 2022-06-29 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eateries_rest', '0016_rename_tag_eaterytag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eaterylocation',
            name='city',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
