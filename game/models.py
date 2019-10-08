from game import db

#FIGURE OUT HOW TO SET DEFAULTS

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, unique=True)
    table_id = db.Column(db.Integer, db.ForeignKey("table.id"))
    partner_name = db.Column(db.String(80), unique=True)
    cards = db.relationship("Card", backref="player", lazy="dynamic")

    def __repr__(self):
        return "<Player: {}>".format(self.username)
    
    def play(self, card):
        self.table.cards.append(card)
        card.set_state_in_play()

    def join_table(self, table):
        self.table = table

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suit = db.Column(db.String(80), index=True,)
    number = db.Column(db.Integer, index=True)
    state = db.Column(db.String(80))
    player_name = db.Column(db.String(80), db.ForeignKey("player.username"))
    table_id = db.Column(db.Integer, db.ForeignKey("table.id"))

    def __repr__(self):
        return "<{}'s Card: {} of {} - State: {}>".format(self.player_name, self.number, self.suit, self.state)
    
    def set_state_unplayed(self):
        self.state = "unplayed"

    def set_state_in_play(self):
        self.state = "in_play"

    def set_state_played(self):
        self.state = "played"

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    players = db.relationship("Player", backref="table", lazy="dynamic")
    cards = db.relationship("Card", backref="table", lazy="dynamic")

    def __repr__(self):
        return "<Table: {}>".format(self.id)
  
    def roundClear(self):
        for c in self.cards.all():
            #give card to player who won
            c.set_state_played()
        self.cards.delete()

