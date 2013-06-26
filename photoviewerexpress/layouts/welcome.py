from pyramid_layout.layout import layout_config

@layout_config(name='welcome', 
               template='layouts/welcome.mako')
class WelcomeLayout(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.home_url = request.application_url

    @property
    def project_title(self):
        return 'Photo Viewer Express'
