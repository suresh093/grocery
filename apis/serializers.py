from rest_framework import serializers
from products import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Product