from django.urls import path
from . import views

urlpatterns = [
    # api endpoints
    path('api/stories/', views.story_list, name="api_latest_stories"),
    path('api/story/<int:story_id>/', views.get_story, name="get_story"),
    path('api/create/story/', views.create_story, name='create_story'),

    # pages with templates
    path('', views.latest_news, name='latest_stories'),
    path('search/', views.search_results, name='search_results'),
    path('story/<int:story_id>/', views.story_detail, name='story_detail')
]
