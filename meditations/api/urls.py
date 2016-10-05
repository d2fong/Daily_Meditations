from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^authors/$',
        views.AuthorListView.as_view(),
        name='subject_list'),
    url(r'^authors/(?P<pk>\d+)/$', 
        views.AuthorDetailView.as_view(),
        name='subject_detail'),
    url(r'^meditations/$',
        views.MeditationListView.as_view(),
        name='meditation_list'),
    url(r'^meditations/(?P<pk>\d+)/$', 
        views.MeditationDetailView.as_view(),
        name='meditation_detail'),
]