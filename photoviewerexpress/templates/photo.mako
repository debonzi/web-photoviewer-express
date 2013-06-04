<%inherit file="${context['main_template'].uri}"/>

<ul>
% for d in dirs:
<li><a href="${d['url']}"> ${d['name']}</a></li>
% endfor
</ul>

<ul>
% for p in photos:
<li><a href="${p['url']}"> ${p['name']}</a></li>
% endfor
</ul>
