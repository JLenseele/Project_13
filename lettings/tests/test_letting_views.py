import pytest
from django.urls import reverse, resolve
from django.test import Client
from lettings.models import Address, Letting
from pytest_django.asserts import assertTemplateUsed
from django.core.exceptions import ObjectDoesNotExist


class TestLettingView:

    @pytest.mark.django_db
    def test_index_view(self):
        client = Client()

        path = reverse('lettings_index')
        response = client.get(path)
        content = response.content.decode()
        title = "<title>Lettings</title>"

        # test Title in HTML response
        assert title in content
        # test URL Path content
        assert path == '/letting/'
        # test status_code
        assert response.status_code == 200
        # test view_name
        assert resolve(path).view_name == 'lettings_index'
        # test template name used
        assertTemplateUsed(response, "lettings_index.html")


class TestIndexView:

    @pytest.mark.django_db
    def test_lettings_view(self):
        client = Client()

        address = Address.objects.create(
            number="10",
            street="street",
            city="Paris",
            state="France",
            zip_code="10000")

        Letting.objects.create(
            title='test_letting',
            address=address
        )

        path = reverse('letting', kwargs={'letting_id': 1})
        response = client.get(path)
        content = response.content.decode()
        title = '<title>test_letting</title>'

        # test Title in HTML response
        assert title in content
        # test status_code
        assert response.status_code == 200
        # test URL Path content
        assert path == '/letting/1/'
        # test view_name
        assert resolve(path).view_name == 'letting'
        # test template name used
        assertTemplateUsed(response, "letting.html")

    @pytest.mark.django_db
    def test_lettings_view_data_no_exist(self):
        client = Client()

        address = Address.objects.create(
            number="10",
            street="street",
            city="Paris",
            state="France",
            zip_code="10000")

        Letting.objects.create(
            title='test_letting',
            address=address
        )
        try:
            path = reverse('letting', kwargs={'letting_id': 2})
            response = client.get(path)
        except ObjectDoesNotExist:
            path = None
            response = None

        assert path is None
        assert response is None
