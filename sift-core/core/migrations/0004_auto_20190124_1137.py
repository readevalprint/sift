# Generated by Django 2.1.5 on 2019-01-24 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='response',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='core.Response'),
        ),
    ]
