
from django.db import models

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

CREATE TABLE Elections_Priviliged
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
class Electors(models.Model):
	name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	birth_date = models.DateField()
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)

	def __str__(self):
		return name + surname


class Candidates(models.Model):
	name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	birth_date = models.DateField()

	def __str__(self):
		return self.name + self.surname	


class Elections(models.Model):
	description = models.CharField(max_length=50)
	vote_limit = models.IntegerField(default=1)
	start_date = models.DateField()
	end_date = models.DateField()
	candidates = models.ManyToManyField(Candidates, through='ElectionsCandidates')
	voters = models.ManyToManyField(Electors, through='ElectionsPriviliged')

	def __str__(self):
		return self.description


class ElectionsCandidates(models.Model):
	election = models.ForeignKey(Elections, on_delete=models.CASCADE)
	candidate = models.ForeignKey(Candidates, on_delete=models.CASCADE)
	votes = models.IntegerField(default=0)


class ElectionsPriviliged(models.Model):
	election = models.ForeignKey(Elections, on_delete=models.CASCADE)
	elector = models.ForeignKey(Electors, on_delete=models.CASCADE)
	vote = models.BooleanField(default=False)
