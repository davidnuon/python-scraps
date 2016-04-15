import unittest


def add_two_lists(list1, list2):
	if type(list1) is not list or type(list2) is not list:
		raise ValueError('list1 and list2 must be lists')

	return list1 + list2


def say_string(string):
	return str(string)

class TestAddTwoLists(unittest.TestCase):
	def test_strings_return_error(self):
		with self.assertRaises(ValueError):
			add_two_lists('foo', 'bar')

	def test_say_string_always_returns_string(self):
		print(dir(self))
		self.assertEquals(type(say_string(9)), str)

	def test_div_zero(self):
		1/0


unittest.main(exit=False)
