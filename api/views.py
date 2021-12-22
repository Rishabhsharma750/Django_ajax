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


def table_data(request):
    return render(request, 'table.html')


def datalist(request):
    response_Data = {'data': []}
    data_list = []
    Infos = Data.objects.all()

    for info in Infos:
        data_dict = {'first_name': info.fname,
                     'last_name': info.lname,
                     'email': info.email,
                     'subject': info.subject}
        data_list.append(data_dict)
        response_Data["data"] = data_list

    return JsonResponse(response_Data)


def withajaxdata(request):
    # response_Data = {}
    Infos = Data.objects.all()
    datalist = []
    for info in Infos:
        list = "<tr>"\
                  "<th scope="">"+info.fname+"</th>"\
                  "<td>"+info.fname+"</td>"\
                  "<td>"+info.fname+"</td>"\
                  "<td>"+info.fname+"</td>"\
                "</tr>"
        datalist.append(list)
        # response_Data = datalist

    return JsonResponse({'data': datalist})
