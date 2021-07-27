import requests
from celery import task
from .models import Base


@task(name='sync_news')
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

            Base.objects.create(
                hacker_id=new_object_response.get('id'),
                time=new_object_response.get('time'),
                type=new_object_response.get('type'),
                title=new_object_response.get('title'),
                url=new_object_response.get('url'),
                author=new_object_response.get('by'),
                hn_deleted=new_object_response.get('deleted'),
                text=new_object_response.get('text'),
            )
