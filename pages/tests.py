from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    def test_home_page_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_reverse_url(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
