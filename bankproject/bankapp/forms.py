from django import forms
from .models import Customer, District, SubArea, AccountType, Materials

class CustomerForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select District")
    sub_area = forms.ModelChoiceField(queryset=SubArea.objects.none(), empty_label="Select Sub Area")
    account_type = forms.ModelChoiceField(queryset=AccountType.objects.all(), empty_label="Select Account Type")
    materials_provide = forms.ModelMultipleChoiceField(queryset=Materials.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Customer
        fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'district', 'sub_area', 'account_type', 'materials_provide']
        widgets = {
            'materials_provide': forms.CheckboxSelectMultiple,
            'gender': forms.RadioSelect,
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_area'].queryset = SubArea.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['sub_area'].queryset = SubArea.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass