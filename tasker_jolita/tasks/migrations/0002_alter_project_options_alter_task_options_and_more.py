# Generated by Django 5.0 on 2024-02-15 16:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name'], 'verbose_name': 'projektas', 'verbose_name_plural': 'projektai'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_done', '-created_at'], 'verbose_name': 'užduotis', 'verbose_name_plural': 'užduotys'},
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='pavadinimas'),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='savininkas'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='sukurta'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='terminas'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=10000, verbose_name='aprašymas'),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(db_index=True, default=False, verbose_name='padaryta'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='pavadinimas'),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='savininkas'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.project', verbose_name='projektas'),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_index=True, verbose_name='atnaujinta'),
        ),
    ]
