import json

from rest_framework import serializers

from a_shop.models import *
from f_system_log.models import AuditLog
from f_schedule_job.models import SyncTask


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
        customer_name = validated_data.get('customer_name')

        # Create System Log
        log = AuditLog(message=validated_data.get('customer_name') + ' is created')
        log.save()

        # Create Application
        ap = Application(customer_name=customer_name)
        ap.save()

        # Get Application's id, customer, created at
        print('Application Customer Name: ', ap.customer_name)
        print('Application ID:', ap.application_id)
        print('Application Create At: ', ap.created_at)
        # create a api request to schedule job
        x = {
            'application_id': str(ap.application_id),
            'customer': ap.customer_name,
            'timestamp': str(ap.created_at)
        }
        sj = SyncTask(category=0, action=1, parameters=json.dumps(x))
        sj.save()

        return ap
