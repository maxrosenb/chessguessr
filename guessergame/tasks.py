from bs4 import BeautifulSoup
import requests
import re
import lichess.api
from lichess.format import SINGLE_PGN, PYCHESS
from .models import ChessGame

# def chess_test():
#     r = requests.get(
#     'https://www.chess.com/game/live/16389952395')
#     # if r.status_code == 200:
#     soup = BeautifulSoup(r.content, "html.parser")
#     elo_line = str(soup.findAll('meta', {'name' : 'twitter:description'}))
#     pattern = re.compile(r"\((\d+)\)")
#     print("elo line: ", elo_line, "type: ", type(elo_line))
#     elos = pattern.findall(elo_line)
#     white_elo = elos[0]
#     black_elo = elos[1]
#     print(soup)

def add_game_to_db(game_link, white_elo, black_elo, pgn):
    new_game = ChessGame(game_link=game_link, white_elo=white_elo, black_elo=black_elo, pgn=pgn, average_elo=((white_elo+black_elo)/2))
    new_game.save()
    
def lichess_test():
    # from guessergame.tasks import lichess_test
    game_ids = ['Qa7FJNk2']
    for game_id in game_ids:
        game_pgn = lichess.api.game(game_id, evals=False, format=SINGLE_PGN, tags=False).rstrip()
        game = lichess.api.game(game_id, evals=False, format=PYCHESS)
        black_elo = int(game.headers._others['BlackElo'])
        white_elo = int(game.headers._others['WhiteElo'])
        game_link = game.headers._tag_roster['Site']
        print(game_pgn)
        print(black_elo)
        print(white_elo)
        print(game_link)
        add_game_to_db(game_link, white_elo, black_elo, game_pgn)