<%inherit file="${context['main_template'].uri}"/>

<style type="text/css">
  .span3 {
  padding-top: 10px;
  padding-bottom: 10px;
  }
</style>

<div class="row-fluid">
  <% row = 0 %>
  % for d in dirs:
  <% row = row + 1 %>
  <div class="span3">
    <a href="${d['url']}" class="btn btn-large"> 
      <img width="100" height="100" src="${request.static_url('photoviewerexpress:static/img/folder-icon.png')}" alt="${d['name']}">
	  <p class="text-center">${d['name']}</p>
    </a>
  </div>
  % if (row % 4) == 0:
  <% row = 0 %>
  </div>
  <div class="row-fluid">
  % endif
  % endfor

  % for p in photos:
  % if (row % 4) == 0:
  <% row = 0 %>
  </div>
  <div class="row-fluid">
  % endif

  <div class="span3">
    <a href="${p['url']}" rel="lightbox"><img src="${p['thumb']}" alt="${p['name']}" class="img-polaroid"></a>
  </div>
  <% row = row + 1 %>
  % endfor
</div>

<script src="${request.static_url('photoviewerexpress:static/js/jquery-1.7.2.min.js')}"></script>
<script src="${request.static_url('photoviewerexpress:static/js/jquery-ui-1.8.18.custom.min.js')}"></script>
<script src="${request.static_url('photoviewerexpress:static/js/jquery.smooth-scroll.min.js')}"></script>    
<script src="${request.static_url('photoviewerexpress:static/js/lightbox.js')}"></script>    
