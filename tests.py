from flask import Flask
from flask_testing import TestCase
import unittest
from urlshort import db, create_test_app
from urlshort.strings import Strings


class TestURLShort(TestCase):

    def create_app(self):
        return create_test_app()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


class TestShortenForm(TestURLShort):

    def testInvalidURL1(self):
        response = self.client.post('/', data=dict(
            url='notaurl'
        ), follow_redirects=True)
        self.assertIn(Strings.strings['URLValidationError'].encode(), response.data)


if __name__ == '__main__':
    unittest.main()
