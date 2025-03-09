# Generated by Django 5.1.6 on 2025-03-05 17:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('dta_atualizacao', models.DateTimeField(auto_now=True)),
                ('conteudo', models.TextField()),
                ('dta_criacao', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'rascunho'), (1, 'publicar')], default=0)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-dta_criacao'],
            },
        ),
    ]
