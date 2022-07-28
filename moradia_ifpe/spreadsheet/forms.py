from django.forms import ModelForm

from moradia_ifpe.spreadsheet.models import SpreadSheet


class ImportSpreadForm(ModelForm):
    class Meta:
        model = SpreadSheet
        fields = ['campi', 'edital', 'ano', 'file']
