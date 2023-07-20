from django import forms
from Travelling.models import Authentication
class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = Authentication
        fields = "__all__"

# from django import forms
# # from registrationapp.models import Member
# from Travelling.models import User
# # class MemberForm(forms.ModelForm):
# #     class Meta:
# #         model = Member
# #         fields = "_all_"


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = "__all__"