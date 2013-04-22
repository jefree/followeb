
function init(){

	button = document.getElementById('preview-button');
	button.onclick = getPreview;
}

function getPreview(){
	
	request_url = document.getElementById('url-text').value;

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