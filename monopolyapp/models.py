from django.db import models

# Create your models here.


class Room(models.Model):
    # 状態のセット
    STATE_SET = (
        ('starting', '開始待ち'),
        ('playing', 'プレイ中'),
        ('closed', '終了'),
    )

    room_id = models.CharField(max_length=128, primary_key=True)
    state = models.CharField(max_length=16, choices=STATE_SET, default='starting')
    parent = models.CharField(max_length=64)


class Player(models.Model):
    line_id = models.CharField(max_length=64)
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)
    position = models.CharField(max_length=8, choices=(('parent', '親'), ('child', '子')), default='child')
    money = models.IntegerField(default=2000000)
    deal = models.CharField(max_length=8, choices=(('free', 'なし'), ('gain', '受け取り'), ('pay', '支払い')), default='free')
