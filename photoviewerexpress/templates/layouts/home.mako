<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>${layout.project_title}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <link href="${request.static_url('collabportal:static/css/bootstrap.min.css')}" rel="stylesheet">
    <link href="${request.static_url('collabportal:static/css/bootstrap-responsive.min.css')}" rel="stylesheet">
    <style type="text/css">
      .container {
      width: 90%;
      }
    </style>
  </head>

  <body>
    <!-- ${panel('navbar')} -->
    <div class="container">
      <div class="row-fluid">
	<div class="span12">
	  <div class="row-fluid">
	    <div class="span2">
	      <div class="hero-unit">Left Panel</div>
	    </div>
	    <div class="span8">
	      ${next.body()}
	    </div>
	    <div class="span2">
	      <div class="hero-unit">Right Panel</div>
	    </div>
	  </div>
	</div>
      </div>

      <hr>
    </div>
    ${panel('footer')}

    <script src="${request.static_url('collabportal:static/js/jquery-1.10.0.min.js')}"></script>
    <script src="${request.static_url('collabportal:static/js/bootstrap.min.js')}"></script>
  </body>
</html>

