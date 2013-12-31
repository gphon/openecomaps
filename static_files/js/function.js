$(document).ready(function(){
	var browserhoehe = $(document).height();
	$('.karte').css('height',browserhoehe-170);
	$('#tabs').height($('#main_content').height());
	
	// Link in iFrame anzeigen
	$('.openIframeLink').click(function() {
		if(!$('.overlay').length){
			$('body').append('<div class="overlay hidden"><div class="overlayContent"><iframe class="overlayIframe" src="' + $(this).attr('href') + '"></iframe><img src="/static/img/close.png" alt="Schließen" class="closeOverlay"></div></div>');
		}
		$('.overlay').fadeIn("fast");
		$('.overlay').height($(document).height());
		return false;
	});
	$(document.body).on("click",".overlay",function() {
		$(".overlay").fadeOut("fast");
	});
	
	// Stadtsuche Suchwert übernehmen
	if($(document).getUrlParam("search-text")) {
		$("#search-text").val($(document).getUrlParam("search-text"));
	}
	
	// Stadtsuche Text aus-/einblenden
	var defaultSuchVal = $("#search-text").val();
	$("#search-text").focus(function() {
		if($(this).val() == defaultSuchVal) {
			$(this).val("");
		}
	});
	$("#search-text").blur(function() {
		if($(this).val() == "") {
			$(this).val(defaultSuchVal);
		}
	});
});
