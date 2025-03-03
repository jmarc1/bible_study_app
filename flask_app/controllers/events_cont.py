from flask_app import app
from flask_app.models.events_model import bible_event
from flask import render_template,session,redirect,request,flash 

@app.route('/new_event',methods =["POST"])
def add_event():
    if request.form['action'] == 'cancel':
        return redirect('/dashboard')
    data = {
        'title': request.form['title'],
        'location':request.form['location'],
        'event_date': request.form['event_date'],
        'time':request.form['time'],
        'details':request.form['details'],
        'user_id': session['user_id']
    }
    
    bible_event.add_event(data)
    print(data)
    
    return redirect('/dashboard')

@app.route('/view_events/<int:id>')
def view_event(id):
    data={'id':id}
    get_event =  bible_event.event_by_id(data)
    print(get_event)
    return render_template('viewEvent.html', event = get_event)

@app.route("/delete_event/<int:id>")
def rm_event(id):
    if session['user'] == None:
        return redirect('/')
    data={"id":id}
    bible_event.remove_event(data)
    return redirect('/dashboard')


@app.route("/update_event/<int:id>")
def update(id):
    if session == None:
        return redirect("/")
    data={"id":id}
    event = bible_event.event_by_id(data)
    return render_template("edit_event.html", event =event)


@app.route("/update/<int:id>",methods=["POST"])
def edit(id):
    data = {
        'id': id,
        'title': request.form['title'],
        'location':request.form['location'],
        'event_date': request.form['event_date'],
        'time':request.form['time'],
        'details':request.form['details'],
        'user_id': session['user_id']
    }
    bible_event.update_events(data)
    return redirect("/dashboard")


