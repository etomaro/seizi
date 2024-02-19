"""
調査用に作成した参議院選挙区のデータをdbに登録する
"""
import sys
import os

"""
おそらくアプリ外からのアクセスのためデーターベース設定を呼ばないといけない
※ 現状、本番環境のみ必要
"""
# pwd = os.path.dirname(os.path.realpath(__file__))
# x = sys.path.append(pwd + "../")
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wecandoit_back.settings')
# import django
# django.setup()

import csv
import sys
import os
import datetime
from zoneinfo import ZoneInfo


from seizi.models import People, Sns, HouseOfCouncillors, Representatives


# データ全削除
People.objects.all().delete()
Sns.objects.all().delete()
HouseOfCouncillors.objects.all().delete()
Representatives.objects.all().delete()

# -------- 衆議員[比例]---------
file_path_rep_pro = "seizi/data_files/representatives/25_26_people_proportional.csv"
with open(file_path_rep_pro, 'r') as f:
    csvreader = csv.DictReader(f)
    
    data_list = [row for row in csvreader]

count = 1
column_list = list(data_list[0].keys())
print("---衆議院[比例]---\n")
for data in data_list:
    # 先頭の空白を削除する
    for column in column_list:
        data[column] = data[column].strip(" ")
        data[column] = data[column].strip("　")
        data[column] = data[column].lstrip(" ")
        data[column] = data[column].lstrip("　")
    
    birthday = data["生年月日"]
    birthday_naive = datetime.datetime.strptime(birthday, "%Y年%m月%d日")
    JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    birthday_jst = birthday_naive.replace(tzinfo=JST)  # jstのdatetimeとしてawareに変換


    people = People.objects.create(
        name_ja=data["議員氏名"],
        name_ja_hiragana=data["読み方"],
        group_name=data["会派"],
        count_rep=int(data["当選回数"]),
        sex=int(data["性別"]),
        birthday=birthday_jst,
    )

    # snsテーブル
    twitter_follow = None if data["twitter_follow"] == "" else int(data["twitter_follow"])
    twitter_follower = None if data["twitter_follower"] == "" else int(data["twitter_follower"])
    youtube_follower = None if data["youtube_follower"] == "" else int(data["youtube_follower"])
    youtube_video_num = None if data["youtube_video_num"] == "" else int(data["youtube_video_num"])

    twitter_id = None if data["twitter_id"] == "" else data["twitter_id"]

    sns = Sns.objects.create(
        people_id=people,
        twitter_id=twitter_id,
        twitter_name=data["twitter_name"],
        twitter_follow=twitter_follow,
        twitter_follower=twitter_follower,
        youtube_id=data["youtube_id"],
        youtube_name=data["youtube_name"],
        youtube_follower=youtube_follower,
        youtube_video_num=youtube_video_num,
        homepage=data["home_page_url"]
    )

    # Representativesテーブル
    Representatives.objects.create(
        people_id=people,
        is_proportional=True,
        block=data["選挙区名"],
    )
    
    print(f"{count}: {data['議員氏名']}.ok")
    count+=1

# -------- 衆議員[選挙区]---------
file_path_rep_block = "seizi/data_files/representatives/25_26_people_block.csv"
with open(file_path_rep_block, 'r') as f:
    csvreader = csv.DictReader(f)
    
    data_list = [row for row in csvreader]

count = 1
column_list = list(data_list[0].keys())
print("---衆議院[選挙区]---\n")
for data in data_list:
    # 先頭の空白を削除する
    for column in column_list:
        data[column] = data[column].strip(" ")
        data[column] = data[column].strip("　")
        data[column] = data[column].lstrip(" ")
        data[column] = data[column].lstrip("　")
    
    birthday = data["生年月日"]
    birthday_naive = datetime.datetime.strptime(birthday, "%Y年%m月%d日")
    JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    birthday_jst = birthday_naive.replace(tzinfo=JST)  # jstのdatetimeとしてawareに変換


    people = People.objects.create(
        name_ja=data["議員氏名"],
        name_ja_hiragana=data["読み方"],
        group_name=data["会派"],
        count_rep=int(data["当選回数"]),
        sex=int(data["性別"]),
        birthday=birthday_jst,
    )

    # snsテーブル
    twitter_follow = None if data["twitter_follow"] == "" else int(data["twitter_follow"])
    twitter_follower = None if data["twitter_follower"] == "" else int(data["twitter_follower"])
    youtube_follower = None if data["youtube_follower"] == "" else int(data["youtube_follower"])
    youtube_video_num = None if data["youtube_video_num"] == "" else int(data["youtube_video_num"])

    twitter_id = None if data["twitter_id"] == "" else data["twitter_id"]

    sns = Sns.objects.create(
        people_id=people,
        twitter_id=twitter_id,
        twitter_name=data["twitter_name"],
        twitter_follow=twitter_follow,
        twitter_follower=twitter_follower,
        youtube_id=data["youtube_id"],
        youtube_name=data["youtube_name"],
        youtube_follower=youtube_follower,
        youtube_video_num=youtube_video_num,
        homepage=data["home_page_url"]
    )

    # Representativesテーブル
    Representatives.objects.create(
        people_id=people,
        is_proportional=False,
        block=data["選挙区名"],
    )
    
    print(f"{count}: {data['議員氏名']}.ok")
    count+=1


# ---------参議院議員[選挙区]---------
file_path_cou_block = "seizi/data_files/councillors/25_26_people_block.csv"
with open(file_path_cou_block, 'r') as f:
    csvreader = csv.DictReader(f)
    
    data_list = [row for row in csvreader]

count = 1
column_list = list(data_list[0].keys())
print("---参議院[選挙区]---\n")
for data in data_list:
    # 先頭の空白を削除する
    for column in column_list:
        data[column] = data[column].strip(" ")
        data[column] = data[column].strip("　")
        data[column] = data[column].lstrip(" ")
        data[column] = data[column].lstrip("　")
    
    people = People.objects.create(
        name_ja=data["議員氏名"],
        another_name=data["別名"],
        name_ja_hiragana=data["読み方"],
        group_name=data["会派"]
    )

    # snsテーブル
    twitter_follow = None if data["twitter_follow"] == "" else int(data["twitter_follow"])
    twitter_follower = None if data["twitter_follower"] == "" else int(data["twitter_follower"])
    youtube_follower = None if data["youtube_follower"] == "" else int(data["youtube_follower"])
    youtube_video_num = None if data["youtube_video_num"] == "" else int(data["youtube_video_num"])

    twitter_id = None if data["twitter_id"] == "" else data["twitter_id"]

    sns = Sns.objects.create(
        people_id=people,
        twitter_id=twitter_id,
        twitter_name=data["twitter_name"],
        twitter_follow=twitter_follow,
        twitter_follower=twitter_follower,
        youtube_id=data["youtube_id"],
        youtube_name=data["youtube_name"],
        youtube_follower=youtube_follower,
        youtube_video_num=youtube_video_num
    )

    # house_of_councillorsテーブル
    if data["任期満了"] == "令和7年7月28日":
        nd = 25
        expire = datetime.datetime(2025, 7, 28, 0, 0, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
    elif data["任期満了"] == "令和10年7月25日":
        nd = 26
        expire = datetime.datetime(2028, 7, 25, 0, 0, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
    else:
        raise Exception("任期満了 is invalid")

    HouseOfCouncillors.objects.create(
        people_id=people,
        is_proportional=False,
        block=data["選挙区名"],
        nd=nd,
        expire=expire
    )
    
    print(f"{count}: {data['議員氏名']}.ok")
    count+=1

# ---------参議院議員[比例]---------
file_path_cou_block = "seizi/data_files/councillors/25_26_people_proportional.csv"
with open(file_path_cou_block, 'r') as f:
    csvreader = csv.DictReader(f)
    
    data_list = [row for row in csvreader]

count = 1
column_list = list(data_list[0].keys())
print("---参議院[比例]---\n")
for data in data_list:
    # 先頭の空白を削除する
    for column in column_list:
        data[column] = data[column].strip(" ")
        data[column] = data[column].strip("　")
        data[column] = data[column].lstrip(" ")
        data[column] = data[column].lstrip("　")
    
    people = People.objects.create(
        name_ja=data["議員氏名"],
        another_name=data["別名"],
        name_ja_hiragana=data["読み方"],
        group_name=data["会派"]
    )

    # snsテーブル
    twitter_follow = None if data["twitter_follow"] == "" else int(data["twitter_follow"])
    twitter_follower = None if data["twitter_follower"] == "" else int(data["twitter_follower"])
    youtube_follower = None if data["youtube_follower"] == "" else int(data["youtube_follower"])
    youtube_video_num = None if data["youtube_video_num"] == "" else int(data["youtube_video_num"])

    twitter_id = None if data["twitter_id"] == "" else data["twitter_id"]

    sns = Sns.objects.create(
        people_id=people,
        twitter_id=twitter_id,
        twitter_name=data["twitter_name"],
        twitter_follow=twitter_follow,
        twitter_follower=twitter_follower,
        youtube_id=data["youtube_id"],
        youtube_name=data["youtube_name"],
        youtube_follower=youtube_follower,
        youtube_video_num=youtube_video_num
    )

    # house_of_councillorsテーブル
    if data["任期満了"] == "令和7年7月28日":
        nd = 25
        expire = datetime.datetime(2025, 7, 28, 0, 0, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
    elif data["任期満了"] == "令和10年7月25日":
        nd = 26
        expire = datetime.datetime(2028, 7, 25, 0, 0, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
    else:
        raise Exception("任期満了 is invalid")

    HouseOfCouncillors.objects.create(
        people_id=people,
        is_proportional=True,  # 比例
        block=None,  # 比例の場合は選挙区名はなし
        nd=nd,
        expire=expire
    )
    
    print(f"{count}: {data['議員氏名']}.ok")
    count+=1







