from name_function import get_formatted_name
import unittest

class NameTestCase(unittest.TestCase):

	def test_first_last_name(self):
		formatted_name = get_formatted_name('a', 'i')

		self.assertEqual(formatted_name, 'A I')

	def test_f_l_m_name(self):
		formatted_name = get_formatted_name('a', 'i', 'middle')

		self.assertEqual(formatted_name, "A Middle I")

unittest.main()
