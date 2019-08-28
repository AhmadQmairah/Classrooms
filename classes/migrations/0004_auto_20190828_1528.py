# Generated by Django 2.1.5 on 2019-08-28 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0003_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='teacher',
        ),
        migrations.AddField(
            model_name='classroom',
            name='Teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Classroom'),
        ),
    ]