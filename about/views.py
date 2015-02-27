from django.shortcuts import render_to_response, RequestContext


def privacy_policy(request):
    return render_to_response('about/privacy_policy.html', RequestContext(request, {
        'title': 'Privacy Policy'
    }))


def terms_of_service(request):
    return render_to_response('about/terms_of_service.html', RequestContext(request, {
        'title': 'Terms of Service'
    }))