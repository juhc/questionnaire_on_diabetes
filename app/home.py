from flask import Blueprint, render_template, request, jsonify
from .models import Question, Answer, Group
from . import db


home = Blueprint("home", __name__)


@home.route("/")
def index():
    tests = [group.name for group in Group.query.all()]
    return render_template("index.html", tests=tests)


@home.route("/get-question")
def get_question_by_id():
    group_id = int(request.args.get("group"))
    response = {}

    if group_id:
        questions = Question.query.filter_by(group_id=group_id).all()

        for q in questions:
            question = dict.fromkeys(("text", "type", "notion", "answers"))
            question["text"] = q.text
            question["notion"] = q.notion
            question["type"] = q.type

            answers = Answer.query.filter_by(question_id=q.id).all()
            question["answers"] = [
                {"text": answer.text, "type": answer.type} for answer in answers
            ]

            response[len(response)+1] = question

    return jsonify(response)


@home.route("/get-questions-count")
def get_questions_count():
    group_id = request.args.get("group")
    response = {"count": None}

    if group_id:
        count = len(Question.query.filter_by(group_id=group_id).all())
        response["count"] = count if count else None

    return jsonify(response)