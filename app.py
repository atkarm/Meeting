from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from validators import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myblog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkeysecretkeysecretkey'

db = SQLAlchemy(app)


class Meet(db.Model):
    __searchable__ = []

    id = db.Column(db.Integer, primary_key=True)

    mroom = db.Column(db.String(100), nullable=False)
    employee = db.Column(db.String(100), nullable=False)
    stime = db.Column(db.DateTime, default = datetime.datetime.utcnow())
    etime = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, mroom, employee, stime, etime ):

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

        # Validate employee name
        if validator_name(request.form['employee']):
            employee = request.form['employee']
        else:
            flash('Invalid employee name', 'error')
            return redirect(request.url)

        # validate and set the start time value
        if validator_stime(request.form['stime']):
            stime = request.form['stime']
        else:
            flash('Invalid start time', 'error')
            return redirect(request.url)

        # # validate and set the end time value
        if validator_etime(stime=request.form['stime'], etime=request.form['etime']):
            etime = request.form['etime']
        else:
            flash('Invalid end time', 'error')
            return redirect(request.url)


        meeting = Meet(mroom=mroom, employee=employee, stime=stime, etime=etime)

        if request.form['mroom'] and request.form['employee'] and request.form['stime'] and request.form['stime']:
            flash(f"Thank you for reserving meeting. Your meeting is start at {stime[11:16]} in {stime[0:10]}")
        else:
            return render_template('errors/404.html'), 404
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


@app.route('/meetings/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    meeting = Meet.query.get_or_404(id)

    try:
        db.session.delete(meeting)
        db.session.commit()
        flash(f"You deleted the meeting for {meeting.employee} ")
        return redirect(url_for('all_meeting'))

    except:
        return "Something wrong"


@app.route('/meetings/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    meeting = Meet.query.get_or_404(id)

    # Validate  employee name for update page
    if request.method == 'POST':
        meeting.mroom = request.form['mroom']

        if validator_name(request.form['employee']):
            meeting.employee = request.form['employee']
        else:
            flash('Invalid employee name', 'error')
            return redirect(request.url)

    # validate start time for update page
        if validator_stime(request.form['stime']):
            meeting.stime = request.form['stime']
        else:
            flash('Invalid Start Time', 'error')
            return redirect(request.url)

     # validate End time for update page
        if validator_etime(stime=request.form['stime'],etime=request.form['etime']):
            meeting.etime = request.form['etime']
        else:
            flash('Invalid End Time', 'error')
            return redirect(request.url)

        if request.form['mroom'] and request.form['employee'] and request.form['stime'] and request.form['stime']:
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


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        form = request.form
        search_value = form['search_string']
        search = "%{0}%".format(search_value)
        results = Meet.query.filter(Meet.employee.like(search)).all()
        return render_template('search.html', meeting=results, legend="Search results")
    else:
        return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
