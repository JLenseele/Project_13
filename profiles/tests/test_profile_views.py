import pytest
from django.urls import reverse, resolve
from django.test import Client
from profiles.models import Profile
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed


class TestProfileIndexView:

    @pytest.mark.django_db
    def test_profile_index_view(self):
        client = Client()

        path = reverse('profiles_index')
        response = client.get(path)
        content = response.content.decode()
        title = "<title>Profiles</title>"

        # test Title in HTML response
        assert title in content
        # test URL Path content
        assert path == '/profile/'
        # test status_code
        assert response.status_code == 200
        # test view_name
        assert resolve(path).view_name == 'profiles_index'
        # test template name used
        assertTemplateUsed(response, "profiles_index.html")


class TestProfileView:

    @pytest.mark.django_db
    def test_profile_view(self):
        client = Client()

        user = User.objects.create(
            username="JDupont",
            first_name="jean",
            last_name="dupont",
            email="jean@a.com")
        Profile.objects.create(
            user=user,
            favorite_city="Paris"
        )

        path = reverse('profile', kwargs={'username': "JDupont"})
        response = client.get(path)
        content = response.content.decode()
        title = '<title>JDupont</title>'

        # test Title in HTML response
        assert title in content
        # test status_code
        assert response.status_code == 200
        # test URL Path content
        assert path == '/profile/JDupont/'
        # test view_name
        assert resolve(path).view_name == 'profile'
        # test template name used
        assertTemplateUsed(response, "profile.html")

    @pytest.mark.django_db
    def test_lettings_view_data_no_exist(self):
        client = Client()

        user = User.objects.create(
            username="JDupont",
            first_name="jean",
            last_name="dupont",
            email="jean@a.com")
        Profile.objects.create(
            user=user,
            favorite_city="Paris"
        )

        try:
            path = reverse('profile', kwargs={'username': user['username']})
            response = client.get(path)
            content = response.content.decode()
        except:
            path = None

        assert path is None
