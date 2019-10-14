# main class for generating data related to the module
class Generator:
	def generateHTMLStart(this):
		return """
		<!doctype html>
		<html lang="en">
		"""

	def generateHeadStartEnd(this,title):
	  return """
	  <head>
	  <meta charset="utf-8">
	  <meta http-equiv="X-UA-Compatible" content="IE=edge">
	  <meta name="viewport" content="width=device-width, initial-scale=1">
	  <meta name="description" content="">
	  <meta name="author" content="">
	  <link rel="icon" href="../../favicon.ico">
	  <link rel="canonical" href="https://getbootstrap.com/docs/3.4/examples/navbar-fixed-top/">
	  <title>"""+title+"""</title>
	  <link href="css/style.css" rel="stylesheet">
	  <link href="css/bootstrap.min.css" rel="stylesheet">
	  <link href="css/components.min.css" rel="stylesheet">
	  <script src="https://code.jquery.com/jquery-1.12.0.min.js"></script>
	  <script src="https://code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
	  <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
	  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
	  <link href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap.min.css" rel="stylesheet">
	  <link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
	  <!-- datepicker -->
	  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
	  <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.0/js/bootstrap-datepicker.js"></script>
	  <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet"
	      type="text/css" />
	  <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.0/css/datepicker.css" rel="stylesheet"
	      type="text/css" />
	  <!-- enddatepicker -->
	  <link href="navbar-fixed-top.css" rel="stylesheet">
	  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.3/angular.min.js"></script>
	  <script src="hello.js"></script>
	  <style>
	      .loadingbar {
	          /* background-color: black; */
	          /* opacity: 0.5; */
	          width: 100%;
	          height: 100%;
	          z-index: 100;
	          position: fixed;
	          /* margin-left: 45%;
	          margin-top: 15%; */
	      }
	  </style>
	  <script>
	$(function(){
	  #nav-placeholder").load("NavigationBar");
	});
	</script>
	</head>"""
	def generateTableRecords(this):
		return """
		<div class="row m0">
	    <div class="col-md-12 tableBG">
	        <table id="example1" class="table table-striped table-bordered" style="width:100%">
	            <thead>
	                <tr>
	                    <th>Order ID</th>
	                    <th>Source Location</th>
	                    <th>Destination Location</th>
	                    <th>Early Pickup Date</th>
	                    <th>Late Pickup Date</th>
	                    <th>Early Delivery Date</th>
	                    <th>Late Delivery Date</th>
	                </tr>
	            </thead>
	            <tbody ng-controller="ordermanagementController">
	                <tr ng-repeat="x in ordermanagementList">
	                    <th>{{ x.ordermanagement_pf_orderid }}</th>
	                    <th>{{ x.ordermanagement_pf_sourcelocationname }}</th>
	                    <th>{{ x.ordermanagement_pf_destinationlocationname }}</th>
	                    <th>{{ x.ordermanagement_pf_earlypickupdate }}</th>
	                    <th>{{ x.ordermanagement_pf_latepickupdate }}</th>
	                    <th>{{ x.ordermanagement_pf_earlydeliverydate }}</th>
	                    <th>{{ x.ordermanagement_pf_latedeliverydate }}</th>
	                </tr>
	            </tbody>
	        </table>
	    </div>
	</div>
  """
	def generateLeftFrontend(this):
		return """ 
<div class="col-md-6 pr0">
                    <div class="portlet light portlet panel panel-primary">
                        <div class="panel-heading portlet-title">
                            <h4 class="panel-title">Shipment Details</h4>
                            <span class="pull-right"><span class="clickable mt0"><i class="fa fa-chevron-circle-down"></i></span> <i class="fa fa-expand cP fullscreen"></i> <i class="fa fa-compress cP fullscreen" style="display:none;"></i></span>
                        </div>
                        <div class="panel-body">
                            <table class="table table-striped smooth-scroll list-unstyled">
                                <tbody>
                                    <tr>
                                        <td colspan="1">
                                            <form class="form-horizontal">
                                                <fieldset>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Shipment Id</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_shipmentid' ng-model='claimsmanagement_shipmentid' name='claimsmanagement_shipmentid' placeholder='Shipment Id' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Shipment Mode</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <select class="form-control claimsmanagement_shipmentmode" ng-model='claimsmanagement_shipmentmode'>
                                                                <option>Select </option>
                                                            </select>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Shipment Quantity</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_shipmentquantity' ng-model='claimsmanagement_shipmentquantity' name='claimsmanagement_shipmentquantity' placeholder='Shipment Quantity' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Shipment Comment</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_shipmentcomment' ng-model='claimsmanagement_shipmentcomment' name='claimsmanagement_shipmentcomment' placeholder='Shipment Comment' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                </fieldset>
                                            </form>
                                        </td>
                                        <td colspan="1">
                                            <form class="form-horizontal">
                                                <fieldset>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Shipment Type</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <select class="form-control claimsmanagement_shipmenttype" ng-model='claimsmanagement_shipmenttype'>
                                                                <option>Select </option>
                                                            </select>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Shipment Weight</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_shipmentweight' ng-model='claimsmanagement_shipmentweight' name='claimsmanagement_shipmentweight' placeholder='Shipment Weight' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Charges</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_charges' ng-model='claimsmanagement_charges' name='claimsmanagement_charges' placeholder='Charges' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                </fieldset>
                                            </form>
                                        </td>
                                    </tr>
                                    <tr class="trBG">
                                        <td>
                                        </td>
                                        <td>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div></div>
  	"""
	def generateRightFrontend(this):
		return """
  	<div class="col-md-6">
                    <div class="portlet light portlet panel panel-primary">
                        <div class="panel-heading portlet-title">
                            <h4 class="panel-title">Claims Details</h4>
                            <span class="pull-right"><span class="clickable mt0"><i class="fa fa-chevron-circle-down"></i></span> <i class="fa fa-expand cP fullscreen"></i> <i class="fa fa-compress cP fullscreen" style="display:none;"></i></span>
                        </div>
                        <div class="panel-body">
                            <table class="table table-striped">
                                <tbody>
                                    <tr>
                                        <td colspan="1">
                                            <form class="form-horizontal">
                                                <fieldset>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Claims Id</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_claimsid' ng-model='claimsmanagement_claimsid' name='claimsmanagement_claimsid' placeholder='Claims Id' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Affected Shipment Weight</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_affectedshipmentweight' ng-model='claimsmanagement_affectedshipmentweight' name='claimsmanagement_affectedshipmentweight' placeholder='Affected Shipment Weight' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Loss Date</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_lossdate' ng-model='claimsmanagement_lossdate' name='claimsmanagement_lossdate' placeholder='Loss Date' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Claim Comments</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_claimcomments' ng-model='claimsmanagement_claimcomments' name='claimsmanagement_claimcomments' placeholder='Claim Comments' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                </fieldset>
                                            </form>
                                        </td>
                                        <td colspan="1">
                                            <form class="form-horizontal">
                                                <fieldset>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Claims Type</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <select class="form-control claimsmanagement_claimstype" ng-model='claimsmanagement_claimstype'>
                                                                <option>Select </option>
                                                            </select>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Affected Shipment Quantity</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_affectedshipmentquantity' ng-model='claimsmanagement_affectedshipmentquantity' name='claimsmanagement_affectedshipmentquantity' placeholder='Affected Shipment Quantity' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Claims Amount</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_claimsamount' ng-model='claimsmanagement_claimsamount' name='claimsmanagement_claimsamount' placeholder='Claims Amount' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                    <div class="form-group">
                                                        <label class="col-md-4 p0 control-label">Reference Number</label>
                                                        <div class="col-md-8 inputGroupContainer">
                                                            <div class="input-group"><input id='claimsmanagement_referencenumber' ng-model='claimsmanagement_referencenumber' name='claimsmanagement_referencenumber' placeholder='Reference Number' class="form-control" value="" type="text"></div>
                                                        </div>
                                                    </div>
                                                </fieldset>
                                            </form>
                                        </td>
                                    </tr>
                                    <tr class="trBG">
                                        <td>
                                        </td>
                                        <td>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                     </div>
                
  	"""
	def generateButtons(this):
		return """
  	<div class="col-md-offset-9">
                <div class="pull-left">
                    #contact" data-original-title>Email Claim</a>
                </div>
                <div class="pull-right">
                    <a ng-click="buildShipment('Hello')" class="btn btn-sm btn-default">Save Claim</a>
                </div>
            </div>
            <div class="clearfix mb15">
            </div>
  	"""
	def generateTermsAndCondition(this):
		return """
  	<div class="alert alert-success mt15" role="alert">
                <h4 class="alert-heading">Terms and conditions</h4>
                <p>Help protect your website and its users with clear and fair website terms and conditions. These terms
                    and conditions for a website set out key issues such as acceptable use, privacy, cookies,
                    registration and passwords, intellectual property, links to other sites, termination and disclaimers
                    of responsibility. Terms and conditions are used and necessary to protect a website owner from
                    liability of a user relying on the information or the goods provided from the site then suffering a
                    loss.</p>
                <hr>
                <p class="mb-0">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
                    has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a
                    galley of type and scrambled it to make a type specimen book. </p>
            </div>
  	"""
	def generateScriptInsideBody(this):
		return """<script type="text/javascript">    $(document).ready(function() {        var panels = $('.vote-results');        var panelsButton = $('.dropdown-results');        panels.hide();        //Click dropdown        panelsButton.click(function() {            //get data-for attribute            var dataFor = $(this).attr('data-for');            var idFor = $(dataFor);            //current button            var currentButton = $(this);            idFor.slideToggle(400, function() {                //Completed slidetoggle                if (idFor.is(':visible')) {                    currentButton.html('Hide Results');                } else {                    currentButton.html('View Results');                }            })        });    });    </script>    <script src="js/bootstrap.min.js"></script>    <script src="js/app.min.js"></script>    <script>    $(document).on('click', '.panel-heading span.clickable', function(e) {        var $this = $(this);        if (!$this.hasClass('panel-collapsed')) {            $this.parents('.panel').find('.panel-body').slideUp();            $this.addClass('panel-collapsed');            $this.find('i').removeClass('fa fa-chevron-circle-down').addClass('fa fa-chevron-circle-up');        } else {            $this.parents('.panel').find('.panel-body').slideDown();            $this.removeClass('panel-collapsed');            $this.find('i').removeClass('fa fa-chevron-circle-up').addClass('fa fa-chevron-circle-down');        }    })    </script>    """

#object creation
generator = Generator()

#method calling for generating the script
print generator.generateHTMLStart()

# #Add title for the Head Section (if required)
print generator.generateHeadStartEnd(title = "")

# print generator.generateTableRecords()

# print generator.generateLeftFrontend()

# print generator.generateRightFrontend()

# print generator.generateScriptInsideBody()

# print generator.generateBody()


print "</html>"
# body
# 	mainDiv
# 		container
# 			rowBg
# 				row
# 					generateLeftFrontend
# 					generateRightFrontend
# 				generateButtons
# 				generateTermsAndCondition
