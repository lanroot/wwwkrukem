#from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.db.models import Q
from haystack.query import SearchQuerySet
from userdir.models import Person, City, Div

import json

#def persons(request):
#
#    args = {}
#    args.update(csrf(request))
#
#    args['persons'] = Person.objects.filter(visible=1)
#
#    return render_to_response('persons.html',
#            RequestContext(request, args)
#            )

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

def autocomplete(request):
    if request.method == "POST":
        return HttpResponseRedirect('/userdir/get/%s' % request.POST['q'])

    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:15]
    suggestions = [{'label': (result.name, result.email), 'value': result.pers_id} for result in sqs]
# Make sure you return a JSON object, not a base list.
# Otherwise, you could be vulnerable to an XSS attack.
#    the_data = json.dumps({
#        'results': suggestions
#    })

    return HttpResponse(json.dumps(suggestions), content_type='application/json')
