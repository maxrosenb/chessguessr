from django.db import models

class ChessGame(models.Model):
    white_elo = models.IntegerField()
    black_elo = models.IntegerField()
    average_elo = models.IntegerField()
    pgn = models.CharField(max_length=10000)
    game_link = models.CharField(max_length=10000)