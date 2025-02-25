from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
import datetime
from models.models import db, Game

games_bp = Blueprint('games', __name__)

UPLOAD_FOLDER = 'static/covers'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

games_bp = Blueprint('games', __name__)

@games_bp.route('/games/add', methods=['GET', 'POST'])
@login_required
def add_game():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        rating = request.form.get('rating')
        review = request.form.get('review')

        if not name or not description:
            flash("Game name and description are required!", "error")
            return redirect(url_for('games.add_game'))

        new_game = Game(
            name=name,
            description=description,
            rating=int(rating) if rating else 0,
            review=review if review else "",
            image_url="",
            user_id=current_user.id
        )

        db.session.add(new_game)
        db.session.flush()

        image_file = request.files.get('image')
        image_filename = None

        if image_file and allowed_file(image_file.filename):
            timestamp = datetime.datetime.now().strftime("%H%M%S")
            file_ext = image_file.filename.rsplit('.', 1)[1].lower()
            image_filename = f"{new_game.id}_{timestamp}.{file_ext}"
            
            image_path = os.path.join(UPLOAD_FOLDER, image_filename)

            try:
                image_file.save(image_path)
                new_game.image_url = image_filename
            except Exception as e:
                flash(f"Erro ao salvar imagem: {str(e)}", "error")
                return redirect(url_for('games.add_game'))

        try:
            db.session.commit()
            flash("Game added successfully!", "success")
            return redirect(url_for('games.list_games'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding game: {str(e)}", "error")

    return render_template('add_game.html')

@games_bp.route('/games', methods=['GET'])
@login_required
def list_games():
    """Lista os jogos do usuário logado"""
    try:
        games = Game.query.filter_by(user_id=current_user.id).all()
        return render_template('games_collection.html', games=games)
    except Exception as e:
        return f"Erro ao listar jogos: {str(e)}", 500

@games_bp.route('/games/<int:game_id>', methods=['GET'])
@login_required
def game_review(game_id):
    game = Game.query.filter_by(id=game_id, user_id=current_user.id).first()
    if not game:
        flash("Game not found!", "error")
        return redirect(url_for('games.list_games'))

    return render_template('game_review.html', game=game)

@games_bp.route('/games/ranking', methods=['GET'])
@login_required
def ranking():
    filter_by = request.args.get('filter', 'recents')

    if filter_by == 'score':
        games = Game.query.filter_by(user_id=current_user.id).order_by(Game.rating.desc()).all()
    else:
        games = Game.query.filter_by(user_id=current_user.id).order_by(Game.id.desc()).all()

    return render_template('ranking.html', games=games, filter_by=filter_by)