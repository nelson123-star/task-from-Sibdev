from rest_framework import serializers
from.models import deal

class DealSerializer(serializers.Serializer):
    customers = serializers.CharField(max_length=120)
    item = serializers.CharField(max_length=120)
    total = serializers.IntegerField()
    quantity = serializers.IntegerField()
    date = serializers.DateField()

    def create(self, validated_data):
        return deal.objects.create(**validated_data)