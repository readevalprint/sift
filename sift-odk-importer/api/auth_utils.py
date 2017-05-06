from django.contrib.sites.models import Site
from django.http import HttpResponse


def authorise(username=None, password=None):
    # TODO this is a stubbed method but eventually needs to call into sift
    # core
    return True


class HttpResponseNotAuthorized(HttpResponse):
    status_code = 401

    def __init__(self):
        HttpResponse.__init__(self)
        self['WWW-Authenticate'] =\
            'Basic realm="%s"' % Site.objects.get_current().name
