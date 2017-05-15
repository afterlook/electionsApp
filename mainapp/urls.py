from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import ElectionsCandidatesList, UserList, UserViewSet, UserElectionList

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^index/$', TemplateView.as_view(template_name='home.html')),
    # url(r'^$', UserList.as_view(), name='user-list'),
    url(r'^election-candidates/(?P<pk>\d+)/$', ElectionsCandidatesList.as_view(), name='index'),
    url(r'^user-list/$', UserList.as_view(), name='user-list'),
    url(r'^user-election-list/$', UserElectionList.as_view(), name='user-election-list'),
    url(r'auth/', include('knox.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token)
]