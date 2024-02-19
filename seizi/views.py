from django.shortcuts import render
from django.http import HttpResponse

from seizi.models import People, Sns, HouseOfCouncillors, Representatives

# Create your views here.
SNS_COLUMN = [
        "順位", "名前", "follower", "会派", "衆議院or参議院", "比例or選挙区", "選挙区", "follow", "第n回選挙", "Twitter名", "twitter_id"
    ]
DATA_OBJ_TEMPLATE = {
    "index": "",
    "name_ja": "",
    "group_name": "",
    "twitter_id": "",
    "twitter_name": "",
    "twitter_follow": "",
    "twitter_follower": "",
    "is_proportional": True,
    "block": "",
    "nd": "",
    "is_rep": True, # 衆議院かどうか
}

def SnsOrderList(request):
    """
    "0": なし
    "1": 選挙区と比例
    "2": 選挙区のみ
    "3": 比例のみ
    """
    check_rep_value = "1"
    check_cou_value = "1"
    if 'search' in request.GET:
        check_cou_value = request.GET.get("cou_name")
        check_rep_value = request.GET.get("rep_name")
    
    if check_rep_value == "0" and check_cou_value == "0":
        data = {
            "sns_data": [],
            "sns_column": []
        }
        return render(request, 'indexList.html', data)

    print("データ作成開始")
    # 参議院, 衆議院のpeople.idを取得
    cou_obj = []
    if check_cou_value == "1":
        cou_obj = HouseOfCouncillors.objects.select_related("people_id").all()
    elif check_cou_value == "2":
        cou_obj = HouseOfCouncillors.objects.select_related("people_id").filter(is_proportional=False)
    elif check_cou_value == "3":
        cou_obj = HouseOfCouncillors.objects.select_related("people_id").filter(is_proportional=True)
    else:
        pass

    rep_obj = []
    if check_rep_value == "1":
        rep_obj = Representatives.objects.select_related("people_id").all()
    elif check_rep_value == "2":
        rep_obj = Representatives.objects.select_related("people_id").filter(is_proportional=False)
    elif check_rep_value == "3":
        rep_obj = Representatives.objects.select_related("people_id").filter(is_proportional=True)
    else:
        pass
    print("cou_obj, rep_obj get done")

    people_id_list = []
    cou_people_id_list = [cou.people_id.id for cou in cou_obj]
    rep_people_id_list = [rep.people_id.id for rep in rep_obj]
    people_id_list = cou_people_id_list + rep_people_id_list

    print("people_id_list get done")

    cou_rep_data = {}
    for cou in cou_obj:
        cou_rep_data.setdefault(cou.people_id.id, {})
        cou_rep_data[cou.people_id.id] = {
            "people_id": cou.people_id.id,
            "is_proportional": cou.is_proportional,
            "block": cou.block,
            "nd": cou.nd,
            "expire": cou.expire
        }
    for rep in rep_obj:
        cou_rep_data.setdefault(rep.people_id.id, {})
        cou_rep_data[rep.people_id.id] = {
            "people_id": rep.people_id.id,
            "is_proportional": rep.is_proportional,
            "block": rep.block,
            "nd": rep.nd,
            "expire": rep.expire
        }
    print("cou_rep_data get done")

    # snsテーブルからデータを取得
    sns_obj = Sns.objects.filter(people_id__id__in=people_id_list).select_related("people_id").order_by("twitter_follower").reverse()
    print("sns_obj get done")

    # view用データの作成
    sns_data = []
    for index, sns in enumerate(sns_obj):
        group_name = sns.people_id.group_name if sns.people_id.group_name != None else "-"
        twitter_id = sns.twitter_id if sns.twitter_id != None else "-"
        twitter_name = sns.twitter_name if sns.twitter_name != None else "-"
        twitter_follower = str(sns.twitter_follower) if sns.twitter_follower != None else "-"
        twitter_follow = str(sns.twitter_follow) if sns.twitter_follow != None else "-"

        sns_data_tmp = DATA_OBJ_TEMPLATE.copy()
        sns_data_tmp["index"] = str(index+1)
        sns_data_tmp["name_ja"] = sns.people_id.name_ja
        sns_data_tmp["group_name"] = group_name
        sns_data_tmp["twitter_id"] = twitter_id
        sns_data_tmp["twitter_name"] = twitter_name
        sns_data_tmp["twitter_follow"] = twitter_follow
        sns_data_tmp["twitter_follower"] = twitter_follower
        sns_data_tmp["is_proportional"] = cou_rep_data[sns.people_id.id]["is_proportional"]
        sns_data_tmp["block"] = cou_rep_data[sns.people_id.id]["block"]
        sns_data_tmp["nd"] = str(cou_rep_data[sns.people_id.id]["nd"])
        sns_data_tmp["is_rep"] = True if sns.people_id.id in rep_people_id_list else False

        sns_data.append(sns_data_tmp)
    
    print("data format done")

    data = {
        "sns_data": sns_data,
        "sns_column": SNS_COLUMN
    }

    return render(request, 'indexList.html', data)
