# Generated by Django 4.2.8 on 2024-08-26 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0006_alter_technology_filename_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='filename_logo',
        ),
        migrations.RemoveField(
            model_name='technology',
            name='filename_logo',
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='filename',
            field=models.ImageField(upload_to='screenshots/', verbose_name='Screenshot image'),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to='ideas.project'),
        ),
    ]
