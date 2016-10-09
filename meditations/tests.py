from django.test import TestCase
from meditations.utils.book_slicer import * 
# Create your tests here.

class BookSlicerTestCase(TestCase):
	def test_string_begins_with_numeric(self):
		test_input = ['1.', '.34', 'dksff', '', '12324234324.']
		expected = [True, False, False, False, True]

		for i in range(len(test_input)):
			self.assertEqual(string_begins_with_numeric(test_input[i]), expected[i])