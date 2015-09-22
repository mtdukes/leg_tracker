from rest_framework import serializers
from billcatcher.models import Bill, Lawmaker

class LawmakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lawmaker

class BillSerializer(serializers.HyperlinkedModelSerializer):
    sponsors = LawmakerSerializer(many=True)
    class Meta:
        model = Bill
