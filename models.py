from app import db
from datetime import datetime

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    speaker = db.Column(db.String(100))
    speaker_bio = db.Column(db.Text)
    is_featured = db.Column(db.Boolean, default=False)
    registration_link = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Event {self.title}>'

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    college = db.Column(db.String(200))
    year = db.Column(db.String(20))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    event = db.relationship('Event', backref=db.backref('registrations', lazy=True))
    
    def __repr__(self):
        return f'<Registration {self.name}>'

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ContactMessage {self.subject}>'
