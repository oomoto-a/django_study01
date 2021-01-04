from django.views import generic
from django.shortcuts import render
from .forms import UserForm
from .models import Kimetsu


CHOICE = {
    ('m','男'),
    ('f','女'),
    ('n','不明'),
}

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

def index_template(request):
    myapp_data = {
        'app': 'Django'
    }
    return render(request, 'side.html', myapp_data)

def get_sex(sex):
    for array in CHOICE:
        if array[0] == sex:
            return array[1]

    return CHOICE[2][1]

def insert_template(request):

    params = {'name': '', 'sex': '', 'feature': '', 'form': None}
    if request.method == 'POST':

        form = UserForm(request.POST)
        params['name'] = request.POST['name']
        params['sex'] = get_sex(request.POST['sex'])
        params['feature'] = request.POST['feature']
        params['form'] = form
        k = Kimetsu(name=params['name'], sex=params['sex'], feature=params['feature'])
        k.save()
        Kimetsu.objects.all()
    else:
        params['form'] = UserForm()

    return render(request, 'insert.html', params)

def table_template(request):
    all_data = Kimetsu.objects.all()

    myapp_data = {
        'app': 'Django',
        'data': all_data,
    }


    return render(request, 'table.html', myapp_data)
