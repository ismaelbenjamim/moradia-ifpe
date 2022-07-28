from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from moradia_ifpe.spreadsheet.api.serializers import SpreadsheetSerializer
from moradia_ifpe.spreadsheet.models import SpreadSheet


class SpreadsheetViewSet(viewsets.ModelViewSet):
    queryset = SpreadSheet.objects.all()
    serializer_class = SpreadsheetSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    #permission_classes = [IsAuthenticated]
    #authentication_classes = [TokenAuthentication]
