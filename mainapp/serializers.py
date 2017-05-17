from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import User, Candidate, Election, ElectionsCandidate, ElectionsPrivileged


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','id' , 'name')


class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ('url', 'id', 'name', 'surname', 'birth_date')


class ElectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Election
        fields = ('url', 'id', 'description', 'vote_limit',
                  'start_date,', 'end_date')


class ElectionsCandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ElectionsCandidate
        fields = ('url', 'id', 'election','candidate', 'votes')


class ElectionsPrivilegedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ElectionsPrivileged
        fields = ('url', 'id', 'election', 'elector', 'vote')