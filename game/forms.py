from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired

class EnterNameEven(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    partner = StringField("Partner")
    submit = SubmitField("Let's Go!")

class EnterNameOdd(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Let's Go!")

class CreateGame(FlaskForm):
    roomName = StringField("Room Name", validators=[DataRequired()])
    numberOfPlayers = RadioField("Number of Players", choices=[("4","4"),("5","5"),("6","6"),("7","7"),("8","8")])
    numberOfDecks = RadioField("Number of Decks", choices=[("2","2"),("3","3")])
    roomPassword = StringField("Room Password")
    submit = SubmitField("Create Room")

class JoinGame(FlaskForm):
    roomName = StringField("Room Name", validators=[DataRequired()])
    roomPassword = StringField("Room Password")
    submit = SubmitField("Join Room")


