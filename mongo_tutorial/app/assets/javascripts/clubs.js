$(document).ready(function() {  

	$(".grandchild").hide();
	$("#Attack").show();

  	$(".grandparent").click(function() {
		console.log("activated");
		$(".grandchild").removeClass("active").hide();
	});
})


