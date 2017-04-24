from django.conf.urls import url

from .views import ElectionsCandidatesList

urlpatterns = [
    url(r'^election-candidates/(?P<pk>\d+)/$', ElectionsCandidatesList.as_view(), name='election-candidates'),
]