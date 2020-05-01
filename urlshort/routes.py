from flask import render_template, flash, redirect, url_for, current_app

from urlshort.forms import URLForm, UnshortenForm
from urlshort.models import Link, db
from urlshort.shorten import URLOperations


@current_app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()

    if form.validate_on_submit():
        search = Link.query.filter_by(long=form.url.data).first()

        # Check if url already in database.
        if search:
            print("Exists in db: " + search.short)
            flash(current_app.config["URL"] + "/" + search.short)
            return redirect(url_for('index'))

        # If not, add to database.
        link = Link(long=form.url.data)
        db.session.add(link)
        link = Link.query.filter_by(long=form.url.data).first()
        link.short = URLOperations.shorten(link.id)
        db.session.add(link)
        db.session.commit()
        flash(current_app.config["URL"] + "/" + link.short)
        print("Added to database: " + link.short)

        return redirect(url_for('index'))
    return render_template('index.html', form=form)


@current_app.route('/unshorten', methods=['GET', 'POST'])
def unshortenRoute():
    form = UnshortenForm()
    if form.validate_on_submit():
        search = Link.query.filter_by(short=form.url.data).first()
        if search:
            print("Exists in db: " + search.short)
            flash(search.long)
        else:
            flash('Not found')
        return redirect(url_for('unshortenRoute'))
    return render_template('unshorten.html', form=form)


@current_app.route('/<string:short>')
def redirectShort(short):
    # id = URLOperations.lengthen(short)
    search = Link.query.filter_by(short=short).first()
    if not search:
        flash("Cannot redirect. Invalid URL.")
        return redirect('/')
    return redirect(search.long)
