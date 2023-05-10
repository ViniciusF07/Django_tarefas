# Generated by Django 4.2.1 on 2023-05-10 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField()),
                ('responsavel', models.CharField()),
                ('nivel', models.PositiveIntegerField()),
                ('prioridade', models.PositiveIntegerField()),
                ('situacao', models.CharField()),
            ],
        ),
    ]
