from django.shortcuts import render
from .models import Data
from .forms import UserForm
from django.http.response import JsonResponse, HttpResponse
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
        action = '<button class="btn btn-default btn-rounded mb-4" data-toggle="modal" ' \
                 'data-target="#mymodal" data-fname="' + info.fname + '" data-lname="' + info.lname + '" data-email="' + info.email + '" data-subject="' + info.subject + '" data-id="'+str(info.id) + '"><i class="fas fa-edit"></i></button> ' \
                 '<a href="../delete/'+ str(info.id) + '"class="btn btn-default btn-rounded mb-4 delete"><i class="fas fa-trash"></i></a>'

        data_dict = {
            'first_name': info.fname,
            'last_name': info.lname,
            'email': info.email,
            'subject': info.subject,
            'action': action,
        }
        data_list.append(data_dict)
        response_Data["data"] = data_list

    return JsonResponse(response_Data)


def edit(request):
    response_data = {}
    if request.method == 'POST':
        uid = request.POST['uid']
        tab_data = Data.objects.get(id=uid)
        tab_data.fname = request.POST.get('fname')
        tab_data.lname = request.POST.get('lname')
        tab_data.subject = request.POST.get('subject')
        tab_data.email = request.POST.get('email')
        tab_data.save()
        response_data['result'] = 'Success'
        response_data['link'] = reverse_lazy('table_data')
        return JsonResponse(response_data)


def delete(request, user_id):
    data_del = Data.objects.get(id=user_id)
    data_del.delete()
    return JsonResponse({'message': 'This user has been deleted successfully'})


def withajaxdata(request):
    # response_Data = {}
    Infos = Data.objects.all()
    datalist = []
    for info in Infos:
        list = "<tr>" \
               "<th scope="">" + info.fname + "</th>" \
                                              "<td>" + info.lname + "</td>" \
                                                                    "<td>" + info.email + "</td>" \
                                                                                          "<td>" + info.subject + "</td>" \
                                                                                                                  "</tr>"
        datalist.append(list)
        # response_Data = datalist

    return JsonResponse({'data': datalist})
