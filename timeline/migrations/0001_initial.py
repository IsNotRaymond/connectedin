# Generated by Django 3.1 on 2020-10-30 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfis', '0002_auto_20201030_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_postagem', models.CharField(max_length=255)),
                ('texto', models.TextField()),
                ('data_de_criacao', models.DateTimeField(auto_now_add=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfis.perfil')),
            ],
            options={
                'verbose_name': 'postagem',
                'verbose_name_plural': 'postagens',
                'db_table': 'POSTAGEM',
            },
        ),
    ]
