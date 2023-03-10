from . import db


class Texts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    group_id = db.Column(
        db.Integer, db.ForeignKey("group.id", ondelete="CASCADE", onupdate="CASCADE")
    )


class Recomendations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    extra = db.Column(db.String)
    group_id = db.Column(
        db.Integer, db.ForeignKey("group.id", ondelete="CASCADE", onupdate="CASCADE")
    )


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(
        db.Integer,
        db.ForeignKey("question.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    text = db.Column(db.String, nullable=False)
    sex = db.Column(db.String, nullable=False, default="all")
    point = db.Column(db.Integer, default=None)
    type = db.Column(db.String, default=None)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    correct_answer_id = db.Column(
        db.Integer, db.ForeignKey("answer.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    notion = db.Column(db.String, default=None)
    group_id = db.Column(
        db.Integer, db.ForeignKey("group.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    type = db.Column(db.String, nullable=False, default="radio")
    answers = db.relationship("Answer", foreign_keys=[Answer.question_id])


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    questions = db.relationship("Question")
    recomendations = db.relationship("Recomendations")


class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String, nullable=False)
