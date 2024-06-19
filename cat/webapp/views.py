from django.http import HttpResponseRedirect
from django.shortcuts import render

from webapp.cat import Cat


def index(request):
    if request.method == 'POST':
        name = request.POST.get('usr_cat_name')

        if name:
            cat = Cat(name=name)
            request.session['cat'] = cat.to_dict()
            return HttpResponseRedirect('/cat_info/')

    return render(request, 'index.html')


def cat_info(request):
    cat_data = request.session.get('cat')
    if not cat_data:
        return HttpResponseRedirect('index')

    cat = Cat.from_dict(cat_data)

    action = request.GET.get('action')

    if action == 'feed':
        cat.feed()
    elif action == 'play':
        cat.play()
    elif action == 'sleep':
        cat.sleep()
    request.session['cat'] = cat.to_dict()

    return render(request, 'cat_info.html', {'cat': cat})
