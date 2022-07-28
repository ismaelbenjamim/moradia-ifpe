from rest_framework import serializers

from moradia_ifpe.spreadsheet.models import SpreadSheet, Campi


class CampiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campi
        fields = '__all__'


class SpreadsheetSerializer(serializers.ModelSerializer):
    campi = CampiSerializer()
    class Meta:
        model = SpreadSheet
        fields = '__all__'
