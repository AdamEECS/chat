from . import ModelMixin
from . import db
from . import timestamp


class Chat(db.Model, ModelMixin):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    created_time = db.Column(db.Integer)
    channel = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, form):
        print('chat init', form)
        self.content = form.get('content', '')
        self.channel = form.get('channel', '')
        self.user_id = form.get('user_id', '')
        self.created_time = timestamp()

    def valid(self):
        n = Chat.query.filter_by(user_id=self.user_id).order_by(Chat.id.desc()).first()
        print('last', n)
        if n is not None:
            delta = (self.created_time - n.created_time) > 2
        else:
            delta = True
        length = 0 < len(self.content) < 1000
        script = self.content.find('<script') == -1
        print(script)
        return length and delta and script
