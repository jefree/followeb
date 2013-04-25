
function init(){

	$('#preview-button').click(getPreview);
	$('#save-button').hide();

	$('#url-text').keyup(function(e){

		if (e.keyCode == 13){
			getPreview();
		}
	});
}

function getPreview(){
	
	if ( ! $('#save-button').is(':visible') ){
		$('#save-button').show();
	}

	request_url = $('#url-text').val();

	alert(request_url);

	$.get("/followeb/tasks/preview/"+request_url+"/", function(data){

		var info = eval(data);

		if( ! info["error"]){

			$('#title-text').text(info["title"]);
			$('#description-text').text(info["description"]);
			$('#image-preview').attr('src', info["image"]);

		}else{

			alert("Invalid URL");

		}
	});
}