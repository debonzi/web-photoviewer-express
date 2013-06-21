<div>
  <table class="table table-hover">
    <thead>
      <tr>
	<th>${_(u"Login")}</th>
	<th>${_(u"First Name")}</th>
	<th>${_(u"Last Name")}</th>
	<th>${_(u"Email")}</th>
	<th>${_(u"Group")}</th>
	<th>${_(u"Actions")}</th>
      </tr>
      % for user in users:
	<tr>
	  <td>${user.login}</td>
	  <td>${user.firstname}</td>
	  <td>${user.lastname}</td>
	  <td>${user.emails.email}</td>
	  <td>${user.group.name}</td>
	  <td>
	    <a href="#delete_${user.login}" role="button" data-toggle="modal" data-toggle="tooltip" title="${_(u"Delete")}">
	      <i class="icon-trash"></i>
	    </a>
	  </td>
	</tr>
      % endfor
    </thead>
  </table>
  <!-- Confirm -->
  % for user in users:
  <div id="delete_${user.login}" class="modal hide fake">
    <div class="modal-header">
    </div>
    <div class="modal-body">
      <p>${_(u"Really delete user")} ${user.login}?</p>
    </div>
    <div class="modal-footer">
      <a class="btn" data-dismiss="modal" aria-hidden="true">${_(u"Cancel")}</a>
      <a class="btn btn-primary" href="/admin/delete/${user.login}">${_(u"Delete")}</a>
    </div>    
  </div>
  % endfor
</div>
