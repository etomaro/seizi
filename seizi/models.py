from django.db import models

# Create your models here.
class People(models.Model):

    name_en = models.CharField(max_length=255, null=True, blank=True)
    name_ja = models.CharField(max_length=255, null=True, blank=True)
    name_ja_hiragana = models.CharField(max_length=255, null=True, blank=True)
    another_name = models.CharField(max_length=255, null=True, blank=True)
    group_name = models.CharField(max_length=255, null=True, blank=True)
    background = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    count_rep = models.PositiveSmallIntegerField(null=True, blank=True)
    count_cou = models.PositiveSmallIntegerField(null=True, blank=True)

    created_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)  # 登録時に現在時間を設定
    update_time = models.DateTimeField(null=True, blank=True, auto_now =True)  # 登録時と更新時に現在時間を設定

class Sns(models.Model):

    people_id = models.ForeignKey(People, on_delete=models.CASCADE)
    twitter_id = models.CharField(unique=True, max_length=100, null=True)
    twitter_name = models.CharField(max_length=255, null=True, blank=True)
    twitter_follow = models.PositiveIntegerField(null=True, blank=True)
    twitter_follower = models.PositiveIntegerField(null=True, blank=True)
    homepage = models.CharField(max_length=255, null=True, blank=True)
    youtube_id = models.CharField(max_length=255, null=True, blank=True)
    youtube_name = models.CharField(max_length=255, null=True, blank=True)
    youtube_follower = models.PositiveIntegerField(null=True, blank=True)
    youtube_video_num = models.PositiveIntegerField(null=True, blank=True)

    created_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)  # 登録時に現在時間を設定
    update_time = models.DateTimeField(null=True, blank=True, auto_now =True)  # 登録時と更新時に現在時間を設定

class HouseOfCouncillors(models.Model):
#     # 参議院テーブル
    people_id = models.ForeignKey(People, on_delete=models.CASCADE)
    is_proportional = models.BooleanField()  # True: 比例, False: 選挙区
    block = models.CharField(max_length=50, null=True, blank=True)
    nd = models.PositiveSmallIntegerField(null=True, blank=True)
    expire = models.DateTimeField(null=True, blank=True) # 任期

    created_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)  # 登録時に現在時間を設定
    update_time = models.DateTimeField(null=True, blank=True, auto_now =True)  # 登録時と更新時に現在時間を設定

class Representatives(models.Model):
#     # 衆議院テーブル
    people_id = models.ForeignKey(People, on_delete=models.CASCADE)
    is_proportional = models.BooleanField()  # True: 比例, False: 選挙区
    block = models.CharField(max_length=50, null=True, blank=True)
    nd = models.PositiveSmallIntegerField(null=True, blank=True)
    expire = models.DateTimeField(null=True, blank=True) # 任期

    created_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)  # 登録時に現在時間を設定
    update_time = models.DateTimeField(null=True, blank=True, auto_now =True)  # 登録時と更新時に現在時間を設定