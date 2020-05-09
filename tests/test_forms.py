import pytest

from urlshort.forms import URLForm, UnshortenForm


class TestURLForm:
    """URLForm tests"""

    def test_invalid_link(self, app):
        """Invalid link"""
        form = URLForm(url='notaurl')
        assert form.validate() is False

    @pytest.mark.skip(reason="WIP")
    def test_valid_link(self, app):
        """Valid link"""
        form = URLForm(url='https://example.com')

        print(form.data)
        print(form.validate())
        print(form.errors)
        assert form.validate()


class TestUnshortenForm:
    """UnshortenForm tests"""

    @pytest.mark.skip(reason="WIP")
    def test_valid_input(self, app):
        form = UnshortenForm(url='3')
        assert form.validate()

    def test_invalid_input(self, app):
        form = UnshortenForm(url='')

        assert form.validate() is False
