from django.test import TestCase, Client
from django.urls import reverse
from mainapp.models import Medicine, Type, Category, Subcategory
from userapp.models import MyUser
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class TestViews(TestCase):

    def test_status_code(self):
        response_home = self.client.get('/')
        response_list = self.client.get('/medicine-list/')
        self.assertEqual(response_home.status_code, 200)
        self.assertEqual(response_list.status_code, 302)


class MedicineViewTest(TestCase):
    def setUp(self):
        self.user = MyUser.objects.create_user(username="testuser", password="testpassword")
        self.user.is_superuser = True
        self.client.login(username="testuser", password="testpassword")
        self.type = Type.objects.create(name="Test Type")
        self.category = Category.objects.create(name="Test Category")
        self.subcategory = Subcategory.objects.create(name="Test Subcategory")
        image_file = BytesIO()
        image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        image.save(image_file, 'png')
        image_file.seek(0)
        img_name = 'my-test-image.png'
        uploaded_image = InMemoryUploadedFile(
            image_file,
            None,
            img_name,
            'image/png',
            None,
            None
        )
        self.medicine = Medicine.objects.create(
            name="Test Medicine",
            price=100,
            availability=True,
            img=uploaded_image,
        )
        self.medicine.type.add(self.type)
        self.medicine.category.add(self.category)
        self.medicine.subcategory.add(self.subcategory)


        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/index.html')

    def test_medicine_list_view(self):
        self.client.login(username="testuser", password="testpassword")
        self.user.is_superuser = True
        response = self.client.get(reverse('medicine_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('object_list' in response.context)
        self.assertIsInstance(response.context['object_list'][0], Medicine)

    def test_medicine_detail_view(self):
        self.client.login(username="testuser", password="testpassword")
        self.user.is_superuser = True
        response = self.client.get(reverse('medicine_detail', args=[self.medicine.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], self.medicine)

    def test_medicine_create_view(self):
        self.client.login(username="testuser", password="testpassword")
        self.user.is_superuser = True

        response = self.client.get(reverse('medicine_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/medicine_form.html')

    def test_medicine_update_view(self):
        self.client.login(username="testuser", password="testpassword")
        self.user.is_superuser = True
        response = self.client.get(reverse('medicine_update', args=[self.medicine.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], self.medicine)

