from django.shortcuts import render_to_response, RequestContext


def index_page(request):
    return render_to_response('index.html',
                              RequestContext(request,
                                             {'title': 'Home',
                                             'description': 'Connecting people with what matters.'}))