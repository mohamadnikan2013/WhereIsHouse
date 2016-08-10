from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

# Create your tests here.
from House.models import Home, Comment


class Helper:
    @staticmethod
    def create_post(client, data):
        response = client.post(reverse('house:new-advertise'), data)
        return response

    @staticmethod
    def create_comment(client, token, data):
        response = client.post(reverse('house:ajax', kwargs={'token': token}), data)
        return response

    @staticmethod
    def log_in(client):
        params = {
            'username': 'nikan',
            'password': 'nikki2013',
            'first_name ': 'nikan',
            'last_name': 'ghorbani',
            'email': 'mohamadnikan2013@gmail.com',
            're_password': 'nikki2013',
        }
        client.post(reverse('account:join'), params)
        params = {'username': 'nikan', 'password': 'nikki2013'}
        response = client.post(reverse('account:login'), params)
        return response


class TestPost(TestCase):
    def setUp(self):
        self.client = Client()
        self.phone = "09365835479"
        self.email = 'ali@gmail.com'
        self.title = 'hello i want to sell my house'
        self.price1 = 86
        self.price2 = 85
        self.square = 45
        self.city = 'British'
        self.description = 'hello how are you'

    def generate_info(self, **kwargs):
        params = {
            'phone': kwargs.get('phone', self.phone),
            'email': kwargs.get('email', self.email),
            'title': kwargs.get('title', self.title),
            'price1': kwargs.get('price1', self.price1),
            'price2': kwargs.get('price2', self.price2),
            'square': kwargs.get('square', self.square),
            'city': kwargs.get('city', self.city),
            'description': kwargs.get('description', self.description),
        }
        return params

    def test_new_post(self):
        Helper.log_in(self.client)
        response = Helper.create_post(self.client, data=self.generate_info())
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("FirstPage"))
        self.assertTrue(Home.objects.last())
        self.assertEqual(Home.objects.last().title , self.title)

    def test_edit_Post(self):
        Helper.log_in(self.client)
        Helper.create_post(client=self.client, data=self.generate_info())
        token = Home.objects.last().token
        params = self.generate_info()
        params.update({'room_num': 4, 'region': 'shiraz', 'title': 'edited'})
        response = self.client.post(reverse('house:edit-my-post', kwargs={'token': token}), params)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("house:my-post"))
        self.assertEqual(Home.objects.last().room_num, 4)

    def test_delete_post(self):
        Helper.log_in(self.client)
        Helper.create_post(client=self.client, data=self.generate_info())
        token = Home.objects.last().token
        response = self.client.post(reverse('house:delete-my-post', kwargs={'token': token}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("house:my-post"))
        self.assertFalse(Home.objects.last())

    def test_comment(self):
        Helper.log_in(self.client)
        Helper.create_post(client=self.client, data=self.generate_info())
        token = Home.objects.last().token
        params = {'text': 'hello this is my new comment'}
        response = Helper.create_comment(self.client, token, params)
        self.assertEqual(Home.objects.get(token=token).comment.all()[0].text, 'hello this is my new comment')

    def test_reply(self):
        Helper.log_in(self.client)
        Helper.create_post(client=self.client, data=self.generate_info())
        house_pk = Home.objects.last().pk
        house_token = Home.objects.last().token
        params = {'text': 'hello this is my new comment'}
        Helper.create_comment(self.client, house_token, params)
        comment_pk = Comment.objects.last().pk
        params['text'] = "this is my new comment reply"
        response = self.client.post(reverse('house:reply', kwargs={'house_pk': house_pk, 'comment_pk': comment_pk}),
                                    params)
        self.assertEqual(Home.objects.get(token=house_token).comment.all()[0].replies.all()[0].text,
                         'this is my new comment reply')

    def test_like(self):
        Helper.log_in(self.client)
        Helper.create_post(client=self.client, data=self.generate_info())
        house_pk = Home.objects.last().pk
        response = self.client.get(reverse('house:reply', kwargs={'house_pk': house_pk, 'comment_pk': 1}))
        self.assertEqual(Home.objects.last().like, 1)



