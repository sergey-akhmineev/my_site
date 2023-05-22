from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category, Type, Subcategory, Medicine


class CategoryModelTest(TestCase):

    def setUp(self):
        self.image = SimpleUploadedFile('test_img.png', content=b'', content_type='image/png')
        self.category = Category.objects.create(name='Test Category', img=self.image)

    def tearDown(self):
        self.category.delete()

    def test_category_name(self):
        self.assertEqual(self.category.name, 'Test Category')


class TypeModelTest(TestCase):

    def setUp(self):
        self.type = Type.objects.create(name='Test Type')

    def tearDown(self):
        self.type.delete()

    def test_type_name(self):
        self.assertEqual(self.type.name, 'Test Type')


class SubcategoryModelTest(TestCase):

    def setUp(self):
        self.subcategory = Subcategory.objects.create(name='Test Subcategory')

    def tearDown(self):
        self.subcategory.delete()

    def test_subcategory_name(self):
        self.assertEqual(self.subcategory.name, 'Test Subcategory')


class MedicineModelTest(TestCase):

    def setUp(self):
        self.type = Type.objects.create(name='Test Type')
        self.category = Category.objects.create(name='Test Category')
        self.subcategory = Subcategory.objects.create(name='Test Subcategory')
        self.image = SimpleUploadedFile('test_img.png', content=b'', content_type='image/png')
        self.medicine = Medicine.objects.create(
            name='Test Medicine',
            description='Test description',
            dosage=5,
            quantity=10,
            price=10.0,
            availability=True,
            img=self.image
        )
        self.medicine.type.add(self.type)
        self.medicine.category.add(self.category)
        self.medicine.subcategory.add(self.subcategory)

    def tearDown(self):
        self.type.delete()
        self.category.delete()
        self.subcategory.delete()
        self.medicine.delete()

    def test_medicine_name(self):
        self.assertEqual(self.medicine.name, 'Test Medicine')

    def test_medicine_description(self):
        self.assertEqual(self.medicine.description, 'Test description')

    def test_medicine_dosage(self):
        self.assertEqual(self.medicine.dosage, 5)

    def test_medicine_quantity(self):
        self.assertEqual(self.medicine.quantity, 10)

    def test_medicine_price(self):
        self.assertEqual(self.medicine.price, 10.0)

    def test_medicine_availability(self):
        self.assertEqual(self.medicine.availability, True)

    def test_medicine_foreign_keys(self):
        self.assertIn(self.type, self.medicine.type.all())
        self.assertIn(self.category, self.medicine.category.all())
        self.assertIn(self.subcategory, self.medicine.subcategory.all())