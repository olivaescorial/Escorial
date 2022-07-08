# from django.urls import resolve
from urllib import response
from django.test import TestCase
from vtvsn.views import MainPage
from .models import Feedback

# from django.http import HttpRequest

class HomePageTest(TestCase):
# 	def test_root_url_resolves_to_mainpage_view(self): 
# 		found=resolve('/')
# 		self.assertEqual(found.func, MainPage)
		
# 	def test_mainpage_returns_correct_view(self):
# 		request = HttpRequest()
# 		response = MainPage(request)
# 		html = response.content.decode('utf8')
# 		self.assertTrue(html.startswith('<html>'))
# 		self.assertIn('<title>Vote Vision</title>', html)
# 		self.assertTrue(html.endswith(''))


	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')
	def test_save_POST_request(self):
		response = self.client.post('/', {'name' :'Oliva',
	 		'e-mail': 'olivaescorial3@gmail.com',
	 		'concerns': 'Other concerns about the website',
	 		'message': 'Helpful Website!'})
		self.assertEqual(Feedback.objects.count(),1)
		Data = Feedback.objects.first()
		self.assertEqual(Data.uname, 'Oliva')
		self.assertEqual(Data.uemail, 'olivaescorial3@gmail.com')
		self.assertEqual(Data.uchoices, 'Other concerns about the website')
		self.assertEqual(Data.umessage, 'Helpful Website!')

	def test_POST_redirect(self):
		response = self.client.post('/', {'name' :'Oliva',
	 		'e-mail': 'olivaescorial3@gmail.com',
	 		'concerns': 'Other concerns about the website',
	 		'message': 'Helpful Website!'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')


	def test_only_saves_items_uf_necessary(self):
		self.client.get('/')
		self.assertEqual(Feedback.objects.count(), 0)

class ORMTEST(TestCase):
	def test_saving_retrive(self):
		FeedbackC = Feedback()
		FeedbackC.uname = 'Oliva'
		FeedbackC.uemail = 'olivaescorial3@gmail.com'
		FeedbackC.uchoices = 'Other concerns about the website'
		FeedbackC.umessage = 'Helpful Website!'
		FeedbackC.save()

		FeedbackC = Feedback()
		FeedbackC.uname = 'Dimple'
		FeedbackC.uemail= 'asdfghjkl@gmail.com'
		FeedbackC.uchoices = 'Question/s aboutwhfggdhyo the website'
		FeedbackC.umessage = 'How long is the process when I register?'
		FeedbackC.save()

		Feedback_list = Feedback.objects.all()
		self.assertEqual(Feedback_list.count(), 2)

		first_info = Feedback_list[0]
		second_info = Feedback_list[1]

		self.assertEqual(first_info.uname, 'Oliva')
		self.assertEqual(first_info.uemail, 'olivaescorial3@gmail.com')
		self.assertEqual(first_info.uchoices, 'Other concerns about the website')
		self.assertEqual(first_info.umessage, 'Helpful Website!')

		self.assertEqual(second_info.uname, 'Dimple')
		self.assertEqual(second_info.uemail, 'asdfghjkl@gmail.com')
		self.assertEqual(second_info.uchoices, 'Question/s aboutwhfggdhyo the website')
		self.assertEqual(second_info.umessage, 'How long is the process when I register?')

	def test_template_display_list(self):
		Feedback.objects.create(
			uname = 'Dimple',
			uemail = 'asdfghjkl@gmail.com',
			uchoices = 'Question/s aboutwhfggdhyo the website',
			umessage = 'How long is the process when I register?')

		Feedback.objects.create(
			uname = 'Oliva',
			uemail = 'olivaescorial3@gmail.com',
			uchoices = 'Other concerns about the website',
			umessage = 'Helpful Website!')

		response = self.client.get('/')
		self.assertIn('Dimple, asdfghjkl@gmail.com, Question/s aboutwhfggdhyo the website, How long is the process when I register?', response.content.decode())
		self.assertIn('Oliva, olivaescorial3@gmail.com, Other concerns about the website, Helpful Website!', response.content.decode())


