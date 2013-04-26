
function init(){

	//clean forms
	$('#url-text').val('');
	$('#title').val('');
	$('#description').val('');
	$('#save-button').hide();

	$('#url-text').keyup(function(e){

		if (e.keyCode == 13){
			getPreview();
		}
	});
}

function getPreview(){

	request_url = $('#url-text').val();

	$.get("/followeb/tasks/preview/"+request_url+"/", function(data){

		var info = eval(data);

		if( ! info["error"]){

			$('#title-text').text(info["title"]);
			$('#description-text').text(info["description"]);
			$('#image-preview').attr('src', info["image"]);

			$('#url').val(request_url);

			//show subscribe button
			if ( ! $('#save-button').is(':visible') ){
				$('#save-button').show();
			}		

		}else{

			alert("Invalid URL");

		}
	});
}

function sendSubscribe(){

	if( $('#title').val() == '' ){

		alert('Please set a title for your subscription');
		return;
	}

	$('#formSubscribe').submit();
}
