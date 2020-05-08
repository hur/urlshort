"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp
from urlshort import create_app
from urlshort.models import Link
from urlshort.models import db as _db
from urlshort.shorten import URLOperations


@pytest.fixture
def app():
    """Create application for the tests."""
    _app = create_app(testing=True)

    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.fixture
def testapp(app):
    """Create Webtest app."""
    return TestApp(app)


@pytest.fixture
def client(app, db):
    """Flask test client"""
    return app.test_client()


@pytest.fixture
def db(app):
    """Create database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def link(db):
    """Create a link for the tests."""
    link = Link(long='https://example.com/', short='3')
    db.session.add(link)
    return link
