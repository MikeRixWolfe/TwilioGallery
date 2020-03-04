from flask import render_template
from app import app, db
from app.persist.models import Message, Phonebook


@app.route('/image/<sid>', strict_slashes=False, methods=['GET'])
def image(sid):
    messages = db.session.query(Message, Phonebook) \
        .outerjoin(Phonebook, Phonebook.Number==Message.From) \
        .filter(Message.AccountSid==app.config['TWILIO_ACCOUNT_SIDS_CSV']) \
        .filter(Message.To==app.config['PHONE_NUMBER']) \
        .filter(Message.MediaUrl!=None) \
        .filter(Phonebook.Name!=None) \
        .filter(Message.MessageSid==sid) \
        .all()

    phonebook = db.session.query(Phonebook) \
        .outerjoin(Message, Phonebook.Number==Message.From) \
        .filter(Message.AccountSid==app.config['TWILIO_ACCOUNT_SIDS_CSV']) \
        .filter(Message.To==app.config['PHONE_NUMBER']) \
        .filter(Message.MediaUrl!=None) \
        .filter(Phonebook.Name!=None) \
        .order_by(Phonebook.Name.asc()) \
        .distinct(Phonebook.Name)

    return render_template('image.html', msgs=messages, pb=phonebook)


