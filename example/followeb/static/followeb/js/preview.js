
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
	request_url = "http://"+ $('#url-text').val();

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

			$('#title-text').text('');
			$('#description-text').text('');
			$('#image-preview').attr('src', '');
			$('#save-button').hide();

			$('#error-message-p').text(info['error-message']);
			$('#error-message-div').show();
		}
	});
}


function sendSubscribe(){

	if( $('#title').val() == '' ){

		$('#error-message-p-modal').text('Please set title for this subscription');
		$('#error-message-div-modal').show();
		return;
	}

	$.get("/followeb/tasks/checktitle/"+$('#title').val()+"/", function(data){

		var info = eval(data);


		if (info['error']) {
			$('#error-message-p-modal').text('This title is already in use');
			$('#error-message-div-modal').show();			
		}else{
			$('#formSubscribe').submit();
		}	
	});
}

function hideAlert(alert){

	$('#'+alert).hide()
}
