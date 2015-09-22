from rest_framework import viewsets
from rest_framework import filters, generics
from billcatcher.models import Bill, Lawmaker
from billcatcher.serializers import BillSerializer, LawmakerSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    #setup for filters
    #NOTE: True/False must be in sentence case
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('watch','bill_id','bill_number','sponsors')

class LawmakerViewSet(viewsets.ModelViewSet):
    queryset = Lawmaker.objects.all()
    serializer_class = LawmakerSerializer
