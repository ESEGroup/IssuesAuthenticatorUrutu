from datetime import datetime
from .usuario import Usuario
from . import db

class Delegate():
  def __init__():
    pass

  def log_presence(ev):
    values = (ev.user_id, ev.lab_id, ev.data, ev.chegada)
    db.execute("""
      INSERT INTO Auth_Presenca
      (user_id, lab_id, data, chegada)
      VALUES (?, ?, ?, ?);""", values)

  def presence_history(user):
    data = db.fetchall("""
      SELECT * 
      FROM Auth_Presenca
      WHERE user_id = ?
      ORDER BY ID DESC
      """,(user.id,))
    return data    

  def check_presence(user):
    data = db.fetchone("""
      SELECT chegada, lab_id 
      FROM Auth_Presenca 
      ORDER BY ID DESC LIMIT 1;""")
    return data

  def check_preferences(user, lab_id):
    data = db.fetchall("""
      SELECT temperatura, umidade, iluminacao
      FROM Auth_Preferencias
      WHERE user_id = ? AND lab_id = ?;""", (user.id,lab_id))
    return data

  def add_preferences(user, preferences):
    values = (user.id, preferences['lab_id'], preferences['temperatura'], preferences['umidade'], preferences['iluminacao'])
    db.execute("""
      INSERT INTO Auth_Preferencias
      (user_id, lab_id, temperatura, umidade, iluminacao)
      VALUES (?, ?, ?, ?, ?);""", values)

  def update_preferences(user, preferences):
    db.execute("""
      UPDATE Auth_Preferencias
      SET temperatura = ?,
          umidade = ?, 
          iluminacao = ?
      WHERE user_id = ? 
        AND lab_id = ?;""",
        (preferences['temperatura'], 
        preferences['umidade'], 
        preferences['iluminacao'], 
        user.id, 
        preferences['lab_id']))