from django.test import TestCase
from .models import Medicine

# Create your tests here.


class TestMedicine(TestCase):
    def test_init(self):
        medicine = Medicine.objects.create(name='Ципрофлоксацин', price=100)
        self.assertEqual(medicine.name, 'Ципрофлоксацин')

    def test_str(self):
        medicine = Medicine.objects.create(name='Ципрофлоксацин', price=100)
        self.assertEqual(str(medicine), 'Ципрофлоксацин')