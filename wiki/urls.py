from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreateView

app_name = 'wiki'
urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('newpage', PageCreateView.as_view(), name = 'page-create-view'),
    path('<str:slug>', PageDetailView.as_view(), name='wiki-details-page'),
]
