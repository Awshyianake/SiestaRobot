import threading

from sqlalchemy import Column, String
from SiestaRobot.modules.sql import BASE, SESSION

class NiskalaChats(BASE):
    __tablename__ = "niskala_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

NiskalaChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_niskala(chat_id):
    try:
        chat = SESSION.query(NiskalaChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()

def set_niskala(chat_id):
    with INSERTION_LOCK:
        niskalachat = SESSION.query(NiskalaChats).get(str(chat_id))
        if not niskalachat:
            niskalachat = NiskalaChats(str(chat_id))
        SESSION.add(niskalachat)
        SESSION.commit()

def rem_niskala(chat_id):
    with INSERTION_LOCK:
        niskalachat = SESSION.query(NiskalaChats).get(str(chat_id))
        if niskalachat:
            SESSION.delete(niskalachat)
        SESSION.commit()


def get_all_niskala_chats():
    try:
        return SESSION.query(NiskalaChats.chat_id).all()
    finally:
        SESSION.close()
