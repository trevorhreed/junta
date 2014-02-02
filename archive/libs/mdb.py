from google.appengine.ext import db, ndb

def to_blob(file):
	return db.Blob(file)

def delete_by_id(urlsafe_id):
	ndb.Key(urlsafe=urlsafe_id).delete()

def key_from_id(urlsafe_id):
	return ndb.Key(urlsafe=urlsafe_id)

def entity_from_id(urlsafe_id):
	return ndb.Key(urlsafe=urlsafe_id).get()

class BaseModel(ndb.Model):

	def id(self):
		return self.key.urlsafe()

	@staticmethod
	def get(urlsafe_key):
		return ndb.Key(urlsafe=urlsafe_key).get()
