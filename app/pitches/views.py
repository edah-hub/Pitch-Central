from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import current_user, login_required
from app import db
from app.models import Pitch, Comment, Upvote, Downvote
from app.pitches.forms import PitchForm,  CommentForm

pitches = Blueprint('pitches', __name__)