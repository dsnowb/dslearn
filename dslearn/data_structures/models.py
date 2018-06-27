from django.db import models

class Method(models.Model):
    """
    Method typically found on a given data structure.

    Attributes:
        title: Common name for the method
        description: Purpose and methodology of method
        snippet: Code representation of method
        data_structure: Parent data structure

    """
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    snippet = models.TextField(blank=True, null=True)
    data_structure = models.ForeignKey(DataStructure, on_delete=models.CASCADE, related_name='methods')

class DataStructure(models.Model):
    """
    Data Structure Model.

    Attributes:
        title: Common name for the data structure
        description: Purpose and methodology of data structure
        snippet: Code representation of data structure
        image_url: location of image representation of data structure

    """
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    snippet = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
