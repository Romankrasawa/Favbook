$(function() {  
    $( "#tabs-list" ).tabs();  

    console.log('okeeey') 
   }); 
   $(".outside-link").click(function() {
    $(".nav li").removeClass("active");
	$($(this).attr("data-toggle-tab")).parent("li").addClass("active");

});
