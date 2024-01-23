from django.http import HttpResponse
from django.template import Template, Context

def home(request):
    request.session['visits'] = int(request.session.get('visits', 0)) + 1
    t = Template('<h1>visits: {{ visits }}</h1>')
    c = Context({'visits': request.session['visits']})
    return HttpResponse(t.render(c))
    
