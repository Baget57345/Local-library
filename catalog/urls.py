from django.urls import path
#from django.conf.urls import url
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path(r'^books/$', views.book_l, name='books'),
    path(r'^books/(?P<pk>\d+)$',views.BookDetailView.as_view(),name='book-detail'),
    path(r'authors/', views.author_l, name='authors'),

]
