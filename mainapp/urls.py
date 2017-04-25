from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ElectionsCandidatesList,  UserList

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    # url(r'^$', UserList.as_view(), name='user-list'),
    url(r'^election-candidates/(?P<pk>\d+)/$', ElectionsCandidatesList.as_view(), name='index'),
    url(r'^user-list/$', UserList.as_view(), name='user-list')
]