# Generated by Django 4.0.3 on 2022-06-16 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodies_rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eateryopenhoursvo',
            old_name='eatery',
            new_name='eatery_vo',
        ),
        migrations.RemoveField(
            model_name='skeweredeatery',
            name='eatery',
        ),
        migrations.AddField(
            model_name='review',
            name='eatery_vo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='foodies_rest.eateryvo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skeweredeatery',
            name='eatery_vo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='skewered_eateries', to='foodies_rest.eateryvo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foodie',
            name='google_calendar',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skeweredeatery',
            name='foodie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skewered_eateries', to='foodies_rest.foodie'),
        ),
    ]
