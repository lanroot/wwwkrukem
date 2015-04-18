#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.db.models import Q
from haystack.query import SearchQuerySet
from userdir.models import Person, City, Div

import json
import logging

logr = logging.getLogger(__name__)

def persons(request):

    args = {}
    args.update(csrf(request))

    args['persons'] = Person.objects.filter(visible=1)

    return render_to_response('persons.html',
            RequestContext(request, args)
            )

def person(request, person_id=1):
    div_id = Person.objects.get(pers_id=person_id).div_id
    city_id = Div.objects.get(id=div_id).city_id

    return render_to_response('person.html',
            RequestContext(request, ({ 'person': Person.objects.get(pers_id=person_id),
                'div': Div.objects.get(id=div_id),
                'city': City.objects.get(id=city_id) 
                                    })
                            )
            )

def search_persons(request):
#    if request.method == "POST":
#        search_text = request.POST['search_text']
#    else:
#        search_text = ''
    search_text = request.GET['sh']

    args = {}
    args.update(csrf(request))

#    args['persons'] = Person.objects.filter(visible=1, email__icontains=search_text)
    args['persons'] = Person.objects.filter(Q(visible=1), Q(email__icontains=search_text) | Q(name__icontains=search_text) | Q(mtel__icontains=search_text)| Q(office__contains=search_text) | Q(post__icontains=search_text) | Q(subdiv__icontains=search_text))
#    args['persons'] = SearchQuerySet().autocomplete(content_auto=request.GET.get('sh', '')).order_by('-pri')[:100]
#    args['persons'] = SearchQuerySet().autocomplete(content_auto=search_text).order_by('-pri')[:100]
#    args['persons'] = SearchQuerySet().autocomplete(content_auto=request.GET.get('sh', '')).order_by('div')[:100]
#    args['persons'] = SearchQuerySet().autocomplete(content_auto=request.GET.get('sh', ''))[:100]
#    args['persons'] = SearchQuerySet().filter(content=search_text).order_by('-pri')[:100]
#    args['persons'] = SearchQuerySet().auto_query(search_text)
#    args['person'] = SearchQuerySet().models(Person).order_by('-pri').filter(content=search_text)[:100]
    logr.debug(persons)

    return render_to_response('persons.html', RequestContext(request, args))

def autocomplete(request):
#    if request.method == "POST":
#        return HttpResponseRedirect('/userdir/get/%s' % request.POST['q'])

    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:15]
    suggestions = [{'label': (result.name, result.email), 'value': result.pers_id} for result in sqs]
# Make sure you return a JSON object, not a base list.
# Otherwise, you could be vulnerable to an XSS attack.
#    the_data = json.dumps({
#        'results': suggestions
#    })

    return HttpResponse(json.dumps(suggestions), content_type='application/json')
