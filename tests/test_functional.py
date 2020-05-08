
import pytest

from urlshort.models import Link
from urlshort.shorten import URLOperations
from urlshort.strings import Strings


class TestFunctional:
    """
    Functional tests using WebTest.
    See: http://webtest.readthedocs.org/
    """

    url = 'https://example.com'
    notaurl = 'notaurl'
    short = '3'

    def test_inject_strings(self, testapp):
        """
        Tests if the inject_strings() context processor works as expected
        and jinja2 can use the strings in the templates
        if TestURLForm's test_invalid_link fails this should fail
        """
        response = testapp.post('/', dict(
            url=TestFunctional.notaurl
        ))
        assert Strings.strings['URLValidationError'].encode() in response.body

    def test_inject_strings_2(self, testapp):
        """
        Tests if the string is not found when it should not be found in the template.
        """
        response = testapp.post('/', dict(
            url=TestFunctional.url
        ))
        assert Strings.strings['URLValidationError'].encode() not in response.body

    def test_database_indexing(self, db, testapp):
        """
        Tests if the shortened url created by the index route matches the expectation of the unshortening algorithm.
        """
        response = testapp.post('/', dict(
            url=TestFunctional.url
        ))

        match = db.session.query(Link).first()
        print(match)
        assert URLOperations.lengthen(match.short) == match.id

    def test_unshorten_find(self, db, testapp, app):
        """
        Tests the unshorten route.
        """
        link = Link(long=TestFunctional.url, short=TestFunctional.short)
        response = testapp.post('/unshorten', dict(
            url=TestFunctional.short
        ))
        assert bytes(app.config['URL'].join('/').join(TestFunctional.short), 'utf-8') in response.body

