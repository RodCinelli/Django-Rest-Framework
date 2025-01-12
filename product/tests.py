from django.test import TestCase
from product.models.category import Category

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title='Literatura',
            slug='literatura',
            description='Livros de literatura em geral',
            active=True
        )

    def test_category_creation(self):
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.title, 'Literatura')
        self.assertEqual(self.category.slug, 'literatura')
        self.assertEqual(self.category.description, 'Livros de literatura em geral')
        self.assertTrue(self.category.active)
