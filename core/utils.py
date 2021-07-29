from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Base
import requests
from datetime import datetime
import pytz


def pagination(request, bases):
    paginator = Paginator(bases, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return posts


def create_base_object(key, parent):
    if Base.objects.filter(hacker_id=key).exists():
        pass
    else:
        url = "https://hacker-news.firebaseio.com/v0/item/{}.json".format(key)
        new_object_response = requests.get(url)
        new_object_response = new_object_response.json()
        Base.objects.create(
            hacker_id=new_object_response.get('id'),
            type=new_object_response.get('type'),
            time=datetime.fromtimestamp(new_object_response.get('time'), pytz.utc),
            title=new_object_response.get('title'),
            url=new_object_response.get('url'),
            author=new_object_response.get('by'),
            hn_deleted=new_object_response.get('deleted'),
            text=new_object_response.get('text'),
            parent=parent
        )



