# Create your views here.
from records.models import Record
from records.serializers import RecordSerializer
from rest_framework import generics

from django_filters import rest_framework as filters
from django.shortcuts import render
import sys
from pathlib import Path
_PROJECTPATH = str(Path(__file__).resolve().parents[2])
sys.path.append(_PROJECTPATH)


class RecordFilter(filters.FilterSet):
    start_time_gte = filters.IsoDateTimeFilter(field_name="start_time", lookup_expr='gte')

    class Meta:
        model = Record
        fields = ['id']


class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all().order_by('-start_time')
    serializer_class = RecordSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RecordFilter


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer



# from django.contrib.sites.models import Site

# def index(request):
#     post_list = Post.objects.all().order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})

def main(request):
    return render(request, 'index.html')

