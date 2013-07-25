<div>
  <table class="table table-hover">
    <thead>
      <tr>
	<th>${_(u"URL")}</th>
      </tr>
      % for url in urls:
	<tr>
	  <td><a href="/shared/${url.token}">${url.path}</a></td>
	  <td>
	    <a href="#delete_${url.token}" role="button" data-toggle="modal" data-toggle="tooltip" title="${_(u"Delete")}">
	      <i class="icon-trash"></i>
	    </a>
	  </td>
	</tr>
      % endfor
    </thead>
  </table>
  <!-- Confirm -->
  % for url in urls:
  <div id="delete_${url.token}" class="modal hide fake">
    <div class="modal-header">
    </div>
    <div class="modal-body">
      <p>${_(u"Really delete url")} ${url.path}?</p>
    </div>
    <div class="modal-footer">
      <a class="btn" data-dismiss="modal" aria-hidden="true">${_(u"Cancel")}</a>
      <a class="btn btn-primary" href="/shared/delete/${url.token}">${_(u"Delete")}</a>
    </div>    
  </div>
  % endfor
</div>
