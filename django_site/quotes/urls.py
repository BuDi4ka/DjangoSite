from django.urls import path

from . import views

app_name = 'quotes'
urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page>/', views.main, name='main_paginate'),
    path('author/', views.author, name='author'),
    path('tag/', views.tag, name='tag'),
    path('quote/', views.quote, name='quote'),
    path('detail_quote/<int:quote_id>', views.detail_quote, name='detail_quote'),
    path('detail_author/<int:author_id>', views.detail_author, name='detail_author'),
    path('tag/<str:tag_name>/', views.quotes_by_tag, name='quotes_by_tag')
]
