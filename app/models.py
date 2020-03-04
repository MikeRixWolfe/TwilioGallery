from datetime import datetime
from app import db


class Message(db.Model):
    __tablename__ = 'Message'

    MessageSid = db.Column(db.String, primary_key=True)
    AccountSid = db.Column(db.String)
    ApiVersion = db.Column(db.String)
    Body = db.Column(db.String)
    From = db.Column(db.String)
    To = db.Column(db.String)
    MediaUrl = db.Column(db.String, nullable=True)
    DateReceived = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, MessageSid, AccountSid, ApiVersion,
                 Body, From, To, MediaUrl):
        self.MessageSid = MessageSid
        self.AccountSid = AccountSid
        self.ApiVersion = ApiVersion
        self.Body = Body
        self.From = From
        self.To = To
        self.MediaUrl = MediaUrl

class Phonebook(db.Model):
    __tablename__ = 'Phonebook'

    Name = db.Column(db.String, primary_key=True)
    Number = db.Column(db.String)

    def __init__(self, name, number):
        self.Name = name
        self.Number = number

