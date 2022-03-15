from django.shortcuts import render
from filteringApp.models import Student
from filteringApp.serializers import StudentSerializer
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class StudentPagination(PageNumberPagination):
    page_size = 1

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LimitOffsetPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'exam_score']
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['id', 'name']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'exam_score']
    ordering = ['id']
