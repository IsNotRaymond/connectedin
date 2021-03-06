# Generated by Django 3.1 on 2020-10-30 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('nome_empresa', models.CharField(max_length=255)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('contatos', models.ManyToManyField(related_name='_perfil_contatos_+', to='perfis.Perfil')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfis',
                'db_table': 'PERFIL',
            },
        ),
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convidado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_recebidos', to='perfis.perfil')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_feitos', to='perfis.perfil')),
            ],
            options={
                'verbose_name': 'convite',
                'verbose_name_plural': 'convites',
                'db_table': 'CONVITE',
            },
        ),
    ]
