<div class="container">
  <div class="navbar navbar-inverse">
  <!-- <div class="navbar"> -->
    <div class="navbar-inner">
      <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </a>
      <a class="brand" href="${homeurl}">${layout.project_title}</a>
      <div class="nav-collapse collapse navbar-responsive-collapse">
        % if nav:
        <ul class="nav">
          % for item in nav:
          <li class="${'active' if item['active'] else ''}">
            <a href="${item['url']}">${item['name']}</a>
          </li>
          % endfor
        </ul>
        % endif
	<ul class="nav pull-right">
	  <li class="divider-vertical"></li>
	  <li class="dropdown">
	    <a href="#" class="dropdown-toggle" data-toggle="dropdown">${request.user.firstname}<b class="caret"></b></a>
	    <ul class="dropdown-menu">
	      % for item in user_dropdown:
	      <li><a href="${item['url']}">${item['name']}</a></li>
	      % endfor
	      <li class="divider"></li>
	      <li><a href="${logouturl}"> ${_(u"Logout")} </a></li>
	    </ul>
	  </li>
	</ul>
      </div>
    </div>
  </div>
</div>
