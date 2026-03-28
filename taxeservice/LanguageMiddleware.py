from django.utils.translation import activate


class Language:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'language' in request.session:
            language = request.session['language']
            activate(language)
        else:
            language = activate('ne')
            request.session['language'] = language

        response = self.get_response(request)
        return response
