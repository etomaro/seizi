import csv
import sys
import os
import datetime
from zoneinfo import ZoneInfo


from seizi.models import People, Sns, HouseOfCouncillors, Representatives


# データ全削除
Sns.objects.all().delete()
HouseOfCouncillors.objects.all().delete()
Representatives.objects.all().delete()
People.objects.all().delete()