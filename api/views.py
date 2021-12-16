from django.shortcuts import render, HttpResponseRedirect
from .models import Data
from .forms import UserForm
from django.http.response import JsonResponse
from django.urls import reverse_lazy


def form(request):
    response_data = {}
    if request.method == 'POST':
        forms = UserForm(request.POST)
        if forms.is_valid():
            user = Data(
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                email=request.POST['email'],
                subject=request.POST['subject'],
            )

            user.save()
            response_data['result'] = 'Success'
            response_data['link'] = reverse_lazy('form')

        else:
            response_data['result'] = 'failed'
            response_data['message'] = forms.errors
        return JsonResponse(response_data)
    return render(request, 'Form.html')
