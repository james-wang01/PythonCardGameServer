from game import myGame, db
from game.models import Player, Card, Table

@myGame.shell_context_processor
def make_shell_context():
    return {"db": db, "Player": Player, "Card": Card, "Table": Table}

