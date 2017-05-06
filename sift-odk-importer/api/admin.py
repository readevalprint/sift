# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from .models import XForm
from pyxform import xls2json, builder
from pyxform.xls2json_backends import xls_to_dict


class XFormForm(forms.ModelForm):
    xlsform = forms.FileField(required=False)

    def parse_xlsform(self, fp):
        warnings = []
        json_survey = xls2json.workbook_to_json(
            xls_to_dict(fp), None, 'default', warnings)
        survey = builder.create_survey_element_from_dict(json_survey)
        return survey.xml().toprettyxml(indent='  ')

    class Meta:
        model = XForm
        fields = ['id', 'username', 'description',
                  'xml_data', 'xlsform', 'sift_core_url']

    def clean_xml_data(self):
        print('cleaning xform')
        if 'xlsform' in self.files:
            return self.parse_xlsform(self.files['xlsform'].file)
        return self.cleaned_data['xml_data']

    def clean(self):
        cleaned_data = super(XFormForm, self).clean()
        xlsform = cleaned_data.get("xlsform")
        xml_data = cleaned_data.get("xml_data")

        if not (xlsform or xml_data):
            raise forms.ValidationError("please specify XForm data or upload an XLSForm")


class XFormAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'title',
        'description',
        'created_at',
    )
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('title',)
    form = XFormForm


admin.site.register(XForm, XFormAdmin)
