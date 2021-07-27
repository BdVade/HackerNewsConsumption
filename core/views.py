from django.shortcuts import render
from .models import Base
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BaseSerializer


# Create your views here.

def latest_news(request):
    base = Base.objects.all()[:100]
    paginator = Paginator(base, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, template_name='latest_news.html', context={'base': base, })


@api_view(['GET', 'PUT', 'DELETE'])
def get_story(request, story_id):
    try:
        base = Base.objects.get(id=story_id)
    except Base.DoesNotExist:
        return Response({'message': 'This story does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = BaseSerializer(instance=base)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BaseSerializer(instance=base, data=request.data)
        new_base = serializer.save()
        return Response(BaseSerializer(instance=new_base).data, status=status.HTTP_206_PARTIAL_CONTENT)

    if request.method == 'DELETE':
        base.delete()
        return Response({'message': 'deleted successfully'})


@api_view(['GET'])
def story_list(request):
    story_type = request.GET.get('type')
    if story_type:
        base = Base.objects.filter(type=story_type)[:100]
    else:
        base = Base.objects.all()[:100]
    serializer = BaseSerializer(instance=base, many=True)
    return Response(serializer.data)
