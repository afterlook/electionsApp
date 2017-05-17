from django.contrib.auth.models import Group
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp.permissions import PublicEndpoint
from .models import User, Candidate, Election, ElectionsCandidate, ElectionsPrivileged
from rest_framework import viewsets, generics
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


class ElectionsCandidatesList(generics.ListAPIView):
    """
    API endpoint list of candidates for specific elections.
    """
    queryset = Candidate.objects.all()
    serializer_class = ElectionsCandidateSerializer

    def get_queryset(self):
        id = self.kwargs['pk']
        return ElectionsCandidate.objects.filter(election_id=id)


class UserElectionList(viewsets.ModelViewSet):
    """
    API endpoint list of elections which user can vote on.
    """
    # queryset = Election.objects.all()
    # serializer_class = ElectionSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated, )
    #
    # def get_queryset(self):
    #     id = self.kwargs['pk']
    #     return ElectionsPrivileged.objects.filter(elector_id=id)
    queryset = ElectionsPrivileged.objects.all()
    serializer_class = ElectionsPrivilegedSerializer

    def retrieve(self, request, pk=None):
        if pk == 'i':
            user_id = request.user.id
            user_elections = ElectionsPrivileged.objects.filter(elector_id=user_id)
            serialized_elections = ElectionsPrivilegedSerializer(
                user_elections,
                context={'request': request},
                many=True
            )
            return Response(serialized_elections.data)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return Response(UserSerializer(request.user,
                context={'request':request}).data)
        return super(UserViewSet, self).retrieve(request, pk)


class ExampleView(APIView):
    def get(self, request, format=None):
        content = {
            'user': request.user,  # `django.contrib.auth.User` instance.
            'auth': request.auth,  # None
        }
        return Response(content)


class UserList(generics.ListAPIView):
    # permission_classes = (PublicEndpoint,)

    queryset = User.objects.all()
    serializer_class = UserSerializer
