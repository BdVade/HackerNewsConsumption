from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import redirect
from .models import Base
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BaseSerializer
from .utils import pagination


# Create your views here.

def latest_news(request):
    if request.method == 'GET':
        story_type = request.GET.get('type')
        if story_type:
            bases = Base.objects.filter(type=story_type)[:100]
        else:
            bases = Base.objects.all()[:100]
        posts = pagination(request, bases=bases)
        return render(request, template_name='latest_news.html', context={'bases': bases, 'posts': posts})


def search_results(request):
    if request.method == 'POST':
        text = request.POST.get('search_box')
        bases = Base.objects.filter(Q(text__icontains=text) | Q(title__icontains=text))[:100]
        posts = pagination(request, bases=bases)
        return render(request, template_name='search.html', context={'bases': bases, 'posts': posts})
    return redirect('latest_stories')


@api_view(['GET', 'PUT', 'DELETE'])
def get_story(request, story_id):
    try:
        base = Base.objects.get(id=story_id)
    except Base.DoesNotExist:
        return Response({'message': 'This story does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = BaseSerializer(instance=base)
        return Response(serializer.data)

    if base.local:

        if request.method == "PUT":
            serializer = BaseSerializer(instance=base, data=request.data)
            serializer.is_valid(raise_exception=True)
            new_base = serializer.save()
            return Response(BaseSerializer(instance=new_base).data, status=status.HTTP_206_PARTIAL_CONTENT)

        if request.method == 'DELETE':
            base.delete()
            return Response({'message': 'deleted successfully'})
    else:
        return Response({"message": "This story is from hacker news hence it can't be modified"})


@api_view(['GET'])
def story_list(request):
    story_type = request.GET.get('type')
    if story_type:
        base = Base.objects.filter(type=story_type)[:100]
    else:
        base = Base.objects.all()[:100]
    serializer = BaseSerializer(instance=base, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_story(request):
    serializer = BaseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
