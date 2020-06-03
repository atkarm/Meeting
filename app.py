from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myblog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkeysecretkeysecretkey'
db = SQLAlchemy(app)


class Meet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mroom = db.Column(db.String(100), nullable=False)
    employee = db.Column(db.String(100), nullable=False)
    stime = db.Column(db.DateTime, default=datetime.utcnow)
    etime = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, mroom, employee, stime, etime):
        self.mroom = mroom
        self.employee = employee
        self.stime = stime
        self.etime = etime

    def __repr__(self):
        return '<Meet %r>' % self.id


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        mroom = request.form['mroom']
        employee = request.form['employee']
        stime = request.form['stime']
        etime = request.form['etime']

        meeting = Meet(mroom=mroom, employee=employee, stime=stime, etime=etime)

        if request.form['mroom'] and request.form['employee'] and request.form['stime'] and request.form['stime'] :
            flash(f"Thank you for reserving meeting. Your meeting is start at {stime[11:16]} in {stime[0:10]}")
        else:
            return render_template('404.html'), 404

        try:
            db.session.add(meeting)
            db.session.commit()
            return redirect(url_for('all_meeting'))
        except:
            return "Something wrong"
    else:
        return render_template('create.html')






@app.route('/meetings')
def all_meeting():
    meeting = Meet.query.order_by(Meet.id)

    return render_template('meetings.html', meeting=meeting)


@app.route('/meetings/delete/<int:id>')
def delete(id):
    meeting = Meet.query.get_or_404(id)

    try:
        db.session.delete(meeting)
        db.session.commit()
        return redirect(url_for('all_meeting'))
    except:
        return "Something wrong"


@app.route('/meetings/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    meeting = Meet.query.get_or_404(id)

    if request.method == 'POST':
        meeting.mroom = request.form['mroom']
        meeting.employee = request.form['employee']
        meeting.stime = request.form['stime']
        meeting.etime = request.form['etime']

        if request.form['mroom'] and request.form['employee'] and request.form['stime'] and request.form['stime'] :
            flash("Thank you. Your meeting has been updated. ")
        else:
            flash("something wrong")

        try:
            db.session.commit()
            return redirect('/meetings')
        except:
            return "Something wrong"
    else:
        meeting = Meet.query.get(id)
        return render_template('update.html', meeting=meeting)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
