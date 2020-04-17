from rest_framework import serializers

from a_shop.models import *
from f_system_log.models import SystemLog


class MayorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mayor
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    # # Object Level Validation - "validate()"
    # def validate(self, data):
    #     if 'Jack' not in data['customer_name']:
    #         raise serializers.ValidationError("User name is not 'Jack'")
    #
    #     # if data['status'] is 0:
    #     #     raise serializers.ValidationError("Status should not be 0")
    #
    #     return data
    #
    # # Field Level Validation - validate_<field_name>
    # def validate_customer_user(self, value):
    #     if 'Jack' not in value:
    #         raise serializers.ValidationError("User name is not 'Jack'")
    #     return value

    def create(self, validated_data):
        log = SystemLog(log='Create User', message=validated_data.get('customer_name') + ' is created')
        log.save()

        ap = Application(customer_name=validated_data.get('customer_name'))
        ap.save()

        return ap
