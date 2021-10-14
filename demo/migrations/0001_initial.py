# Generated by Django 3.2.7 on 2021-09-20 02:52

import core.subtable
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log202003',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202003',
                'verbose_name_plural': 'Log202003',
                'db_table': 'demo_log_202003',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202004',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202004',
                'verbose_name_plural': 'Log202004',
                'db_table': 'demo_log_202004',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202005',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202005',
                'verbose_name_plural': 'Log202005',
                'db_table': 'demo_log_202005',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202006',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202006',
                'verbose_name_plural': 'Log202006',
                'db_table': 'demo_log_202006',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202007',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202007',
                'verbose_name_plural': 'Log202007',
                'db_table': 'demo_log_202007',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202008',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202008',
                'verbose_name_plural': 'Log202008',
                'db_table': 'demo_log_202008',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202009',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202009',
                'verbose_name_plural': 'Log202009',
                'db_table': 'demo_log_202009',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202010',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202010',
                'verbose_name_plural': 'Log202010',
                'db_table': 'demo_log_202010',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202011',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202011',
                'verbose_name_plural': 'Log202011',
                'db_table': 'demo_log_202011',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202012',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202012',
                'verbose_name_plural': 'Log202012',
                'db_table': 'demo_log_202012',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202101',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202101',
                'verbose_name_plural': 'Log202101',
                'db_table': 'demo_log_202101',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202102',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202102',
                'verbose_name_plural': 'Log202102',
                'db_table': 'demo_log_202102',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202103',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202103',
                'verbose_name_plural': 'Log202103',
                'db_table': 'demo_log_202103',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202104',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202104',
                'verbose_name_plural': 'Log202104',
                'db_table': 'demo_log_202104',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202105',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202105',
                'verbose_name_plural': 'Log202105',
                'db_table': 'demo_log_202105',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202106',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202106',
                'verbose_name_plural': 'Log202106',
                'db_table': 'demo_log_202106',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202107',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202107',
                'verbose_name_plural': 'Log202107',
                'db_table': 'demo_log_202107',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202108',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202108',
                'verbose_name_plural': 'Log202108',
                'db_table': 'demo_log_202108',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='Log202109',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Log202109',
                'verbose_name_plural': 'Log202109',
                'db_table': 'demo_log_202109',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='User0',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User0',
                'verbose_name_plural': 'User0',
                'db_table': 'demo_user_0',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User1',
                'verbose_name_plural': 'User1',
                'db_table': 'demo_user_1',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User2',
                'verbose_name_plural': 'User2',
                'db_table': 'demo_user_2',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='User3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User3',
                'verbose_name_plural': 'User3',
                'db_table': 'demo_user_3',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='User4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User4',
                'verbose_name_plural': 'User4',
                'db_table': 'demo_user_4',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='User5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User5',
                'verbose_name_plural': 'User5',
                'db_table': 'demo_user_5',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='User6',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User6',
                'verbose_name_plural': 'User6',
                'db_table': 'demo_user_6',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='User7',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User7',
                'verbose_name_plural': 'User7',
                'db_table': 'demo_user_7',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='User8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User8',
                'verbose_name_plural': 'User8',
                'db_table': 'demo_user_8',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
        migrations.CreateModel(
            name='User9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User9',
                'verbose_name_plural': 'User9',
                'db_table': 'demo_user_9',
            },
            bases=(models.Model, core.subtable.ShardingMixin),
        ),
    ]