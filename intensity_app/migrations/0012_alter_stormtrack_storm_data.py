# Generated by Django 3.2.8 on 2022-02-28 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intensity_app', '0011_auto_20220225_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stormtrack',
            name='storm_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storm_track_list', to='intensity_app.stormdata'),
        ),
    ]
