from django.db import models

# Create your models here.

class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.country


class Match(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='team_matches')
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()

    def __str__(self):
        return self.team.country