from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

'''
Tables creation.

CREATE TABLE Elections
(
    id INT NOT NULL AUTO_INCREMENT,
    description VARCHAR(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    PRIMARY KEY(id)
);

CREATE TABLE Candidates
(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Elector
(
    id INT NOT NULL AUTO_INCREMENT,
    login VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE Elections_Privileged
(
    id INT NOT NULL AUTO_INCREMENT,
    elections_id MEDIUMINT NOT NULL,
    elector_id MEDIUMINT NOT NULL,
    did_vote TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY(id),
    FOREIGN KEY(elections_id) REFERENCES Elections(id),
    FOREIGN KEY(elector_id) REFERENCES Elector(id)
);

CREATE TABLE Elections_Candidates
(
    id INT NOT NULL AUTO_INCREMENT,
    elections_id MEDIUMINT NOT NULL,
    candidates_id MEDIUMINT NOT NULL,
    votes INT NOT NULL DEFAULT 0,
    PRIMARY KEY(id),
    FOREIGN KEY(elections_id) REFERENCES Elections(id),
    FOREIGN KEY(candidates_id) REFERENCES Candidates(id)
);
'''


class User(AbstractUser):
    birth_date = models.DateField(null=True)


class Candidate(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return self.name + self.surname


class Election(models.Model):
    description = models.CharField(max_length=50)
    vote_limit = models.IntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    candidates = models.ManyToManyField(Candidate, through='ElectionsCandidate')
    voters = models.ManyToManyField(User, through='ElectionsPrivileged')

    def __str__(self):
        return self.description


class ElectionsCandidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)


class ElectionsPrivileged(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    elector = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.BooleanField(default=False)
