from django.test import TestCase
from .modles import Name
# Create your tests here.
class NameTestCase(TestCase):
	name1
	name2
	name3

	def setup(self):
		self.name1 = Name.objects.create(
			Fname = 'Travis',
			Lname = 'Deschenes'
			)

		self.name2 = Name.objects.create(
			Fname = 'Jon',
			Lname = 'Snow'
			)

		self.name3 = Name.objects.create(
			Fname = 'Optimus',
			Lname = 'Prime'
			)

	 def test_starting_conditions(self):
        '''
        Check if Name exists
        '''

        self.assertIsInstance(self.name1, Name)
        self.assertIsInstance(self.name2, Name)
        self.assertIsInstance(self.name3, Name)
        self.assertEqual(self.name1,name1.Fname = 'Travis' )
        self.assertEqual(self.name1,name1.Lname = 'Deschenes' )
        self.assertEqual(self.name2,name2.Fname = 'Jon' )
        self.assertEqual(self.name2,name2.Lname = 'Snow' )
        self.assertEqual(self.name3,name3.Fname = 'Optimus' )
        self.assertEqual(self.name3,name3.Lname = 'Prime' )
       

    