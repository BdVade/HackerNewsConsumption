import requests
from QuickCheckProject.celery import app
from .models import Base
from datetime import datetime
import concurrent.futures
from .utils import create_base_object


@app.task(name='sync_news')
def sync_news():
    response = requests.get("https://hacker-news.firebaseio.com/v0/newstories.json")
    response = response.json()[:100]
    for hacker_news_id in response:
        if Base.objects.get(hacker_id=hacker_news_id).exists():
            pass
        else:
            url = "https://hacker-news.firebaseio.com/v0/item/{}.json".format(hacker_news_id)
            new_object_response = requests.get(url)
            new_object_response = new_object_response.json()
            kids = new_object_response.get('kids')
            # if kids:
            #     kids_objects_list = []
            #     for kid in kids:
            #         if Base.objects.get(hacker_id=kid).exists():
            #             kids_objects_list.append(kid)
            #         else:
            #
            #
            #     kid_objects = Base.objects.filter(hacker_id__in=kids)
            # else:
            #     kid_objects = None

            base = Base.objects.create(
                hacker_id=new_object_response.get('id'),
                time=datetime.timestamp(new_object_response.get('time')),
                type=new_object_response.get('type'),
                title=new_object_response.get('title'),
                url=new_object_response.get('url'),
                author=new_object_response.get('by'),
                hn_deleted=new_object_response.get('deleted'),
                text=new_object_response.get('text'),

            )

            if kids:
                base_list = (base for kid in kids)
                with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
                    executor.map(create_base_object, kids, base_list)



