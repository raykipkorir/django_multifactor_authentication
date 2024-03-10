from django.shortcuts import render
from django_otp.decorators import otp_required


@otp_required()
def my_view(request):
    return render(request, "accounts/index.html")
