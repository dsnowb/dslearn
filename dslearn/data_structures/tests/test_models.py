from django.test import TestCase
from ..models import Method, DataStructure
import factory


class MethodFactory(factory.django.DjangoModelFactory):
    """
    Factory for Method model.

    """
    class Meta:
        model = Method


    title = factory.Faker('text', max_nb_chars=255)
    description = factory.Faker('text')
    snippet = """
        def fakefunction(fakeparam):
            fake=0
            return fake
    """
    data_structure = factory.Faker('text', max_nb_chars=255)


class DataStructureFactory(factory.django.DjangoModelFactory):
    """
    Factory for DataStructure model.

    """
    class Meta:
        model = DataStructure
    title = factory.Faker('text', max_nb_chars=255)
    description = factory.Faker('text')
    snippet = """
        def fakefunction(fakeparam):
            fake=0
            return fake
    """
    image_url = factory.Faker('url')
