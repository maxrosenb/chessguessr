import random
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import ChessGame

def index(request):
    
    games = ChessGame.objects.all()
    game = random.choice(games)
    print("GAME: ", game.pgn)
    context = {"game": game}
    return render(request, 'guessergame/index.html', context)