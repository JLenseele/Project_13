import pytest
from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


class TestOCLettingsSiteView:

    @pytest.mark.django_db
    def test_index_view(self):
        client = Client()

        path = reverse('index')
        response = client.get(path)
        content = response.content.decode()
        title = "<title>Holiday Homes</title>"

        # test Title in HTML response
        assert title in content
        # test URL Path content
        assert path == '/'
        # test status_code
        assert response.status_code == 200
        # test view_name
        assert resolve(path).view_name == 'index'
        # test template name used
        assertTemplateUsed(response, "index.html")
