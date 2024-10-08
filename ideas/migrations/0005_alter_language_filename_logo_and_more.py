# Generated by Django 4.2.8 on 2024-07-20 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='filename_logo',
            field=models.ImageField(blank=True, default='defaultpic.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_deadline',
            field=models.DateField(verbose_name='Date deadline'),
        ),
        migrations.AlterField(
            model_name='project',
            name='lang_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ideas.language', verbose_name='Programming Language'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tech_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ideas.technology', verbose_name='Technology'),
        ),
    ]
