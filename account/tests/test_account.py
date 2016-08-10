from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

# Create your tests here.
REQUIRED_FIELD_ERROR = 'This field is required'


class Helper:
    @staticmethod
    def login(client, data):
        response = client.post(reverse('account:login'), data)
        return response

    @staticmethod
    def create_account(client, data, active=True):
        response = client.post(reverse('account:join'), data)
        if response.status_code == 302:  # successful signup
            user = User.objects.get(username=data['username'])
            user.is_active = active
            user.save()
        return response


class TestLogin(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_form(self):
        response = self.client.get(reverse('account:login'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)
        param = {'username': 'nikan', 'password': 'nikki2013'}
        response = Helper.login(self.client, param)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)


class TestSignUp(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'amir'
        self.first_name = 'ali'
        self.last_name = 'alavi'
        self.email = 'ali@ali.com'
        self.password = '123'

    def generate_signup_info(self, **kwargs):
        params = {
            'username': kwargs.get('username', self.username),
            'password': kwargs.get('password', self.password),
            'first_name ': kwargs.get('first_name', self.first_name),
            'last_name': kwargs.get('last_name', self.last_name),
            'email': kwargs.get('email', self.email),
            're_password': kwargs.get('re_password', self.password),
        }
        return params

    def test_signup_error(self):
        response = Helper.create_account(self.client,
                                         data=self.generate_signup_info(
                                             username=''))
        self.assertContains(response, REQUIRED_FIELD_ERROR)
        response = Helper.create_account(self.client,
                                         data=self.generate_signup_info(
                                             password=''))
        self.assertContains(response, REQUIRED_FIELD_ERROR)
        response = Helper.create_account(self.client,
                                         data=self.generate_signup_info(
                                             re_password='1234'))
        self.assertContains(response, 'doesnt')
        response = Helper.create_account(self.client,
                                         data=self.generate_signup_info(
                                             email='kdaadjlasd'))
        self.assertContains(response, 'Enter a valid email address')

    def test_signup_ok(self):
        response = Helper.create_account(self.client,
                                         data=self.generate_signup_info())
        self.assertRedirects(response, reverse("FirstPage"))

        response = Helper.login(self.client,
                                data=self.generate_signup_info())
        self.assertRedirects(response, reverse("FirstPage"))
        self.assertIn('_auth_user_id', self.client.session)
        response = Helper.login(self.client,
                                data={'username': self.username,
                                      'password': '1234'})
        self.assertContains(response, 'Invalid username or password')

    def test_signup_existing_username(self):
        response = Helper.create_account(self.client,
                                         data=self.generate_signup_info())
        self.assertRedirects(response, reverse('FirstPage'))
        response = Helper.create_account(self.client,
                                         data=self.generate_signup_info(
                                             email='ajsdlksdlka@jkldjad.com'
                                         ))
        self.assertContains(response, 'already')
        response = Helper.create_account(self.client,
                                         data=self.generate_signup_info(
                                             username='nikan'
                                         ))
        self.assertContains(response, 'already')

