/** init
* This function clear the all fields of the site web 
*/
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

/** getPreview
* This function send the search and write the reponse of the insertion
*/
function getPreview(){
	request_url = "http://"+ $('#url-text').val();
	//Clear the image
	$('#image-preview').attr('src','');
	//Clear the text
	$('#description-text').text('');
	//Clear the title
	$('#title-text').text('');
	//Clear message-error
	hideAlert("error-message-div");
	//Concatenated
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

/** sendSubscribe
* This fuction assigned the personal values the web site joined
*/
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
/**hideAlert
* This function showing errors that ocurring in the execution.
*@param: id_alert: This variable is the id of the div showing error-message
*/
function hideAlert(id_alert){

	$('#'+id_alert).hide()
}
