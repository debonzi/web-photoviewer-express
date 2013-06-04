from pyramid_layout.layout import layout_config


@layout_config(template='layouts/home.mako')
class AppLayout(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.home_url = request.application_url
        self.headings = []

    @property
    def project_title(self):
        return 'Photo Viewer Express'

    def add_heading(self, name, *args, **kw):
        self.headings.append((name, args, kw))
