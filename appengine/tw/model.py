from google.appengine.ext import ndb

DEFAULT_MSG_KEY=ndb.Key("msg", "public")

class Message(ndb.Model):
  text = ndb.StringProperty(required=True)
  timestamp = ndb.DateTimeProperty(auto_now_add=True)
  user_email = ndb.StringProperty(default=None)

  @classmethod
  def query_message(cls, ancestor_key=DEFAULT_MSG_KEY):
      return cls.query(ancestor=ancestor_key).order(-cls.timestamp)

  def to_d(self):
    d = self.to_dict()
    d['timestamp'] = str(d['timestamp'])
    d['key_id'] = self.key.id()
    return d
