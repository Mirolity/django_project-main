import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Load data from fixtures into the database'

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Чтение данных из фикстур
        with open('fixtures/catalog_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for item in data:
            if item['model'] == 'catalog.category':
                category_for_create.append(
                    Category(
                        id=item['pk'],
                        name=item['fields']['name'],
                        description=item['fields']['description']
                    )
                )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фикстуры для получения информации об одном объекте
        for item in data:
            if item['model'] == 'catalog.product':
                product_for_create.append(
                    Product(
                        id=item['pk'],
                        name=item['fields']['name'],
                        description=item['fields']['description'],
                        price=item['fields']['price'],
                        category_id=item['fields']['category'],
                        created_at=item['fields']['created_at'],
                        updated_at=item['fields']['updated_at']
                    )
                )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
