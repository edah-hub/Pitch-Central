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


@pitches.route('/pitch/<int:pitch_id>/update', methods=['GET', 'POST'])
@login_required
def update_pitch(pitch_id):
  pitch = Pitch.query.get_or_404(pitch_id)
  if pitch.author != current_user:
    abort(403)
  form = PitchForm()
  if form.validate_on_submit():
    pitch.title = form.title.data
    pitch.content = form.content.data
    db.session.commit()
    flash('Your pitch has been updated', 'success')
    return redirect(url_for('pitches.new_comment', pitch_id=pitch_id))
  elif request.method == 'GET':
    form.title.data = pitch.title
    form.content.data = pitch.content
  return render_template('create_pitch.html', title='Update Pitch', form=form, legend='Update Pitch')

@pitches.route('/pitch/<int:pitch_id>/delete', methods=['POST'])
@login_required
def delete_pitch(pitch_id):
  pitch = Pitch.query.get_or_404(pitch_id)
  if pitch.author != current_user:
    abort(403)
  db.session.delete(pitch)
  db.session.commit()
  flash('Your pitch has been deleted', 'success')
  return redirect(url_for('main.index'))


@pitches.route('/pitch/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
@login_required
def upvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Upvote.query.filter_by(pitch_id= pitch_id)
    if Upvote.query.filter(Upvote.user_id==user.id, Upvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))

    new_upvote = Upvote(pitch_id=pitch_id, author=current_user)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))

@pitches.route('/pitch/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Downvote.query.filter_by(pitch_id= pitch_id)
    if Downvote.query.filter(Downvote.user_id==user.id, Downvote.pitch_id==pitch_id).first():
      return  redirect(url_for('main.index'))

    new_downvote = Downvote(pitch_id=pitch_id, author=current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index'))

@pitches.route('/categories/<string:cat_name>')
def category(cat_name):
    '''
    function to return the pitches by category
    '''
    category = Pitch.get_pitches(cat_name)

    return render_template('categories.html', category = category, title=cat_name)





