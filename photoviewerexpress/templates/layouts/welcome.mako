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
      body {
      padding-top: 20px;
      padding-bottom: 60px;
      }
    </style>
  </head>

  <body>
    <div class="container">

      <div class="row">
	<div class="span12">
	  <div class="row">
	    <div class="span6"><h1>Logo</h1></div>
	    <div class="span6"><div class="pull-right">${panel('loginbar')}</div></div>
	  </div>
	</div>
      </div>

      <hr>
      <div class="row">
	<div class="span8">
	  <div class="hero-unit">
	    <h3>${_(u"Welcome to Beer Labs Bar!!")}</h3>
	    <p>
	      Donec id elit non mi porta gravida at eget metus. Fusce dapibus,
	      tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum 
	      massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. 
	      Donec sed odio dui.
	    </p>
	  </div>
	</div>
	<div class="span4 pull-right">
	  <div class="hero-unit">${panel('register')}</div>
	</div>
      </div>
      <hr>
      
      <footer>
        ${panel('footer')}
      </footer>
    </div>

    <script src="${request.static_url('collabportal:static/js/jquery-1.10.0.min.js')}"></script>
    <script src="${request.static_url('collabportal:static/js/bootstrap.min.js')}"></script>
  </body>
</html>
