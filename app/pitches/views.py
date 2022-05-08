from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import current_user, login_required
from app import db
from app.models import Pitch, Comment, Upvote, Downvote
from app.pitches.forms import PitchForm,  CommentForm

pitches = Blueprint('pitches', __name__)

@pitches.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def new_pitch():
  form = PitchForm()
  if form.validate_on_submit():
    pitch = Pitch(title=form.title.data, content=form.content.data, category=form.category.data, author=current_user)
    db.session.add(pitch)
    db.session.commit()
    flash('Your pitch has been posted!', 'success')
    return redirect(url_for('main.index'))
  return render_template('create_pitch.html', title='New Pitch', form=form, legend='New Post')

@pitches.route('/pitch/<int:pitch_id>', methods=['GET', 'POST'])
@login_required
def new_comment(pitch_id):
  pitch = Pitch.query.get_or_404(pitch_id)
  form =  CommentForm()

  if form.validate_on_submit():
    comment = Comment(content=form.content.data, author=current_user, pitch_id = pitch_id)
    db.session.add(comment)
    db.session.commit()
    flash('Your comment has been posted!', 'success')
    return redirect(url_for('pitches.new_comment', pitch_id= pitch_id))
    
  all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()

  return render_template('pitch.html', form=form, legend='Leave a Comment', pitch=pitch, comments=all_comments, title=pitch.title)