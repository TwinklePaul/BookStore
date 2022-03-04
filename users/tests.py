from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

# from .forms import CustomUserCreationForm
# from .views import SignUpView


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email="test@test.com",
            password="testpass123"
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='testuser',
            email="test@test.com",
            password="testpass123"
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignUpPageTests(TestCase):

    username = "testuser"
    email = "testuser@test.com"

    def setUp(self):
        # self.response = self.client.get(reverse("signup"))
        self.response = self.client.get(reverse("account_signup"))

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(self.response, "signup.html")
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up!")
        self.assertNotContains(self.response, "Log In!")

    def test_signup_form(self):
        #         form = self.response.context.get("form")
        #         self.assertIsInstance(form, CustomUserCreationForm)
        #         self.assertContains(self.response, 'csrfmiddlewaretoken')

        #     def test_signup_view(self):
        #         view = resolve("/accounts/signup/")
        #         self.assertEqual(
        #             view.func.__name__,
        #             SignUpView.as_view().__name__
        #         )
        newuser = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
