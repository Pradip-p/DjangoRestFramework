from products.models import product
from rest_framework import serializers



class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'