# coding: utf-8
from crogull_sync.db import db

class User(db.Model):

    user_id = db.Column(db.Integer, nullable=True)

    class Meta:
        table_name = 'zzz'
