from urlshort.models import Link


class TestDatabase:

    def test_database_long_matches_input(self, db):
        """
        Test that database long field matches the actual input
        """
        link = Link(long='https://example.com')
        db.session.add(link)
        db.session.commit()
        assert Link.query.filter_by(long='https://example.com').first().long == 'https://example.com'
