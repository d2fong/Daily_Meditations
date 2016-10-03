from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^authors/$',
        views.AuthorListView.as_view(),
        name='subject_list'),
    url(r'^authors/(?P<pk>\d+)/$', 
        views.AuthorDetailView.as_view(),
        name='subject_detail'),
]