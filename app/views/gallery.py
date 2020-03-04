from flask import render_template
from app import app, db
from app.persist.models import Message, Phonebook


@app.route('/gallery', defaults={'name': None}, strict_slashes=False, methods=['GET'])
@app.route('/gallery/<name>', strict_slashes=False, methods=['GET'])
def gallery(name):
    if name:
        messages = db.session.query(Message, Phonebook) \
            .outerjoin(Phonebook, Phonebook.Number==Message.From) \
            .filter(Message.AccountSid==app.config['TWILIO_ACCOUNT_SIDS_CSV']) \
            .filter(Message.To==app.config['PHONE_NUMBER']) \
            .filter(Message.MediaUrl!=None) \
            .filter(Phonebook.Name==name) \
            .order_by(Message.DateReceived.desc()) \
            .all()
    else:
        messages = db.session.query(Message, Phonebook) \
            .outerjoin(Phonebook, Phonebook.Number==Message.From) \
            .filter(Message.AccountSid==app.config['TWILIO_ACCOUNT_SIDS_CSV']) \
            .filter(Message.To==app.config['PHONE_NUMBER']) \
            .filter(Message.MediaUrl!=None) \
            .filter(Phonebook.Name!=None) \
            .order_by(Message.DateReceived.desc()) \
            .all()

    phonebook = db.session.query(Phonebook) \
        .outerjoin(Message, Phonebook.Number==Message.From) \
        .filter(Message.AccountSid==app.config['TWILIO_ACCOUNT_SIDS_CSV']) \
        .filter(Message.To==app.config['PHONE_NUMBER']) \
        .filter(Message.MediaUrl!=None) \
        .filter(Phonebook.Name!=None) \
        .order_by(Phonebook.Name.asc()) \
        .distinct(Phonebook.Name)

    return render_template('gallery.html', msgs=messages, pb=phonebook)

