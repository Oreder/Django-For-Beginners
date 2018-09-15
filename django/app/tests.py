from django.test import TestCase
from django.test import Client

# Create your tests here.

class ViewTest(TestCase):
	def testAppView(self):
		resp = self.client.get('/app/')
		self.assertEqual(resp.status_code, 200)
		
	def testAppProfile(self):
		resp = self.client.get('/app/profile/')
		self.assertEqual(resp.status_code, 200)
	
	def testProfile(self):
		resp = self.client.post('/app/profile/', {'user': 'mike'} )
		self.assertEqual(resp.status_code, 200)

	def testProfileContent(self):
		resp = self.client.post('/app/profile/', {'user': 'mike'} )
		self.assertNotEqual(resp.content, '')