from flask import render_template
from app import app
from app.persist.models import Message


@app.route('/gallery', strict_slashes=False, methods=['GET'])
def index():
    messages = [dict({"MediaUrl": m.MediaUrl, "DateReceived": str(m.DateReceived), "Body": m.Body, "From": m.From}) for m in
            Message.query.filter(Message.AccountSid==app.config['TWILIO_ACCOUNT_SIDS_CSV']).filter(Message.To==app.config['PHONE_NUMBER']).filter(Message.MediaUrl!=None).all()]
    return render_template('index.html', msgs=messages)

