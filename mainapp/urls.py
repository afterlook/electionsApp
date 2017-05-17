from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import ElectionsCandidatesList, UserList, UserViewSet, UserElectionList, ExampleView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-elections', UserElectionList)
# router.register(r'user-elections', UserElectionList)

urlpatterns = router.urls

urlpatterns += [
    url(r'^home/$', TemplateView.as_view(template_name='home.html')),
    # url(r'^$', UserList.as_view(), name='user-list'),
    url(r'^election-candidates/(?P<pk>\d+)/$', ElectionsCandidatesList.as_view(), name='index'),
    url(r'^user-list/$', UserList.as_view(), name='user-list'),
    url(r'^example/$', ExampleView.as_view(), name='example'),
    url(r'^api-token-auth/', views.obtain_auth_token)
]