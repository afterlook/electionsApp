from django.contrib.auth.models import Group
from .models import User, Candidate, Election, ElectionsCandidate, ElectionsPrivileged
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, CandidateSerializer, ElectionSerializer, \
    ElectionsCandidateSerializer, ElectionsPrivilegedSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows candidates to be viewed or edited.
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class ElectionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows elections to be viewed or edited.
    """
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer


class ElectionsCandidateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows elections candidates to be viewed or edited.
    """
    queryset = ElectionsCandidate.objects.all()
    serializer_class = ElectionsCandidateSerializer


class ElectionsPrivilegedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows election privileges to be viewed or edited.
    """
    queryset = ElectionsPrivileged.objects.all()
    serializer_class = ElectionsPrivilegedSerializer






