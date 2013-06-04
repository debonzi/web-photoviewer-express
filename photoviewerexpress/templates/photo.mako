<%inherit file="${context['main_template'].uri}"/>

<ul>
% for d in dirs:
<li><a href="${d['url']}"> ${d['name']}</a></li>
% endfor
</ul>

<ul>
% for p in photos:
<li><a href="${p['url']}" rel="lightbox"><img src="${p['thumb']}" alt="${p['name']}" class="img-rounded"><a></li>
% endfor
</ul>

<script src="${request.static_url('photoviewerexpress:static/js/jquery-1.7.2.min.js')}"></script>
<script src="${request.static_url('photoviewerexpress:static/js/jquery-ui-1.8.18.custom.min.js')}"></script>
<script src="${request.static_url('photoviewerexpress:static/js/jquery.smooth-scroll.min.js')}"></script>    
<script src="${request.static_url('photoviewerexpress:static/js/lightbox.js')}"></script>    
