from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated

from api.filter import FilterWork
from api.mixins import ProModelViewSet
from api.paginations import Pagination
from api.permissions import IsOwnerOrReadOnly, IsOwner, IsSuperuser
from api.serializer import WorkListSerializer, WorkCreatSerializer, WorkDetailSerializer, WorkUpdateSerializer, \
    CategorySerializer, SkillSerializer, CountrySerializer, CitySerializer, AddressSerializer
from headhunter.models import Work, Category, Skills, Country, City, Address


class WorkViewSet(ProModelViewSet):
    queryset = Work.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'id'
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    filterset_class = FilterWork
    search_filter = ['name', 'category', 'city']
    ordering_fields = ['category', 'from_price', 'to_price', 'city']

    serializer_classes = {
        'list': WorkListSerializer,
        'create': WorkCreatSerializer,
        'retrieve': WorkDetailSerializer,
        'update': WorkUpdateSerializer,
    }

    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [IsAuthenticated],
        'update': [IsAuthenticated, IsOwner],
        'destroy': [IsAuthenticated, IsOwner],
    }

    pagination_class = Pagination


class CategoryViewSet(ProModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'id'
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    search_filter = ['name',]
    ordering_fields = ['name', 'created_at']

    pagination_class = Pagination
    serializer_class = CategorySerializer

    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [IsAuthenticated, IsSuperuser],
        'update': [IsAuthenticated, IsSuperuser],
        'destroy': [IsAuthenticated, IsSuperuser],
    }


class SkillsViewSet(ProModelViewSet):
    queryset = Skills.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'id'
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    search_filter = ['name',]
    ordering_fields = ['name', 'created_at']

    pagination_class = Pagination
    serializer_class = SkillSerializer

    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [IsAuthenticated, IsSuperuser],
        'update': [IsAuthenticated, IsSuperuser],
        'destroy': [IsAuthenticated, IsSuperuser],
    }

class CountryViewSet(ProModelViewSet):
    queryset = Country.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'id'
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    search_filter = ['name',]
    ordering_fields = ['name', 'created_at']

    pagination_class = Pagination
    serializer_class = CountrySerializer

    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [IsAuthenticated, IsSuperuser],
        'update': [IsAuthenticated, IsSuperuser],
        'destroy': [IsAuthenticated, IsSuperuser],
    }


class CityViewSet(ProModelViewSet):
    queryset = City.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'id'
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    search_filter = ['name',]
    ordering_fields = ['name', 'created_at']

    pagination_class = Pagination
    serializer_class = CitySerializer

    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [IsAuthenticated, IsSuperuser],
        'update': [IsAuthenticated, IsSuperuser],
        'destroy': [IsAuthenticated, IsSuperuser],
    }


class AddressViewSet(ProModelViewSet):
    queryset = Address.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    lookup_field = 'id'
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]

    search_filter = ['name',]
    ordering_fields = ['name', 'created_at']

    pagination_class = Pagination
    serializer_class = AddressSerializer

    permission_classes_by_action = {
        'list': [AllowAny],
        'retrieve': [AllowAny],
        'create': [IsAuthenticated, IsSuperuser],
        'update': [IsAuthenticated, IsSuperuser],
        'destroy': [IsAuthenticated, IsSuperuser],
    }