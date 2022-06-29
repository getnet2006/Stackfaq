from crypt import methods
from bs4 import Tag
from app.main import bp
from flask import jsonify, render_template, request, url_for, current_app
from app.main import util
from app import models
from app import db

@bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    questions = models.Questions.query.order_by(models.Questions.question).paginate(page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=questions.next_num) if questions.has_next else None
    prev_url = url_for('main.index', page=questions.prev_num) if questions.has_prev else None
    return render_template('main/index.html', questions = questions.items, next_url = next_url, prev_url = prev_url)

@bp.route('/<tag>')
def show_question(tag):
    page = request.args.get('page', 1, type=int)
    questions=models.Questions.query.filter_by(tag=tag).paginate(page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=questions.next_num) if questions.has_next else None
    prev_url = url_for('main.index', page=questions.prev_num) if questions.has_prev else None
    return render_template('main/index.html', questions = questions.items, next_url = next_url, prev_url = prev_url)

@bp.route('/show/questions/<id>/<question>')
@bp.route('/questions/<id>/<question>')
def show_answer(question, id):
    link = f'https://stackoverflow.com/questions/{id}/{question}'
    answer = util.answer(link)
    return render_template('main/show.html', answer=answer)

@bp.post('/questions')
def add():
    if request.is_json:
        tag = request.get_json()['tag']
        questions = util.freq_questions(tag)
        if questions:
            for question in questions:
                q1 = models.Questions(question = question['title'], link = question['link'], tag = tag)
                db.session.add(q1)
                db.session.commit()
            return jsonify({'message': 'New Question added Successfully!'}), 201
    return jsonify({'message': 'Question not added'}), 415

@bp.get('/questions')
def question():
    if request.is_json:
        tag = request.get_json()['tag']
        questions = models.Questions.query.filter_by(tag=tag).all()
        if questions:
            questions = [{'question': question.question, 'url': f"https://stackoverflow.com/questions{question.link.replace('*','/')}"} for question in questions]
            return jsonify(questions)
    return jsonify({
                        "message": "There is no question related with this tag"
                   }), 415