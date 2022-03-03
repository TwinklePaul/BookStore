from urllib import response
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


class HomePageTests(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get(reverse("home"))

    def test_homepage_status_code(self):
        # response = self.client.get("/")
        self.assertEqual(self.response.status_code, 200)

    # def test_homepage_url_name(self):
    #     response = self.client.get(reverse("home"))
    #     self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        # response = self.client.get(reverse("home"))
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        # response = self.client.get("/")
        self.assertContains(self.response, "Home Page")

    def test_homepage_does_not_contain_incorrect_html(self):
        # response = self.client.get("/")
        self.assertNotContains(self.response, "Some Dummy Text.")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get(reverse("about"))

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "About")

    def test_aboutpage_contains_incorrect_html(self):
        self.assertNotContains(self.response, "Home")

    def test_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
