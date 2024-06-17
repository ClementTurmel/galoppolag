# Generated by Django 5.0.6 on 2024-06-17 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equines', '0006_rider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='couple',
            old_name='Equine',
            new_name='equine',
        ),
        migrations.RemoveField(
            model_name='couple',
            name='Person',
        ),
        migrations.AddField(
            model_name='couple',
            name='rider',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='equines.rider'),
            preserve_default=False,
        ),
    ]
