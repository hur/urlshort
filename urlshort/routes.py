from flask import render_template, flash, redirect
from urlshort import app, db
from urlshort.forms import URLForm
from urlshort.models import Link
from urlshort.shorten import URLOperations
from urllib.parse import urlparse

@app.route('/', methods=['GET','POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        search = Link.query.filter_by(long=form.url.data).first()
        # Check if url already in database.
        if search:
            print("Exists in db: " + search.short)
            flash(app.config["URL"] + "/" + search.short)
            return render_template('index.html', form=form)
        # If not, add to database.
        link = Link(long=form.url.data)
        db.session.add(link)
        # Now get the id of the link that was just added to the db and use it
        # to create shortened link
        link = Link.query.filter_by(long=form.url.data).first()
        link.short=URLOperations.shorten(int(link.id))
        db.session.add(link)
        db.session.commit()
        flash(app.config["URL"] + "/" + link.short)
        print("Added to database: " + link.short)
    else:
        flash('Invalid URL.')
    return render_template('index.html', form=form)

@app.route('/<string:short>')
def redirectShort(short):
    # id = URLOperations.lengthen(short)
    search = Link.query.filter_by(short=short).first()
    if not search:
        print("Cannot redirect. Invalid URL.")
        return redirect('/')
    return redirect(search.long)

