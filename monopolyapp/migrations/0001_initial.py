# Generated by Django 2.0.5 on 2018-12-14 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_id', models.CharField(max_length=64)),
                ('position', models.CharField(choices=[('parent', '親'), ('child', '子')], default='child', max_length=8)),
                ('money', models.IntegerField(default=2000000)),
                ('deal', models.CharField(choices=[('free', 'なし'), ('gain', '受け取り'), ('pay', '支払い')], default='free', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('state', models.CharField(choices=[('starting', '開始待ち'), ('playing', 'プレイ中'), ('closed', '終了')], default='starting', max_length=16)),
                ('parent', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monopolyapp.Room'),
        ),
    ]
