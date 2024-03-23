from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_requried
def home():
  if requested.method == 'POST':
    note = request.form.get('note')
    new_note = Note(data=note, user_id=current_user.id)
    db.session.add(new_note)
    db.session.commit()
  return render_template("mainpage.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
  note = json.loads(request.data)
  noteId = note['noteID']
  note = Note.query.get(noteID)
  if note:
    if note.user_id == current_user.id:
      db.session.delete(note)
      db.session.commit()
  return jsonify({})
