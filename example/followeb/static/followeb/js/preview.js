
function init(){

	button = document.getElementById('preview-button');
	button.onclick = getPreview;
}

function getPreview(){
	
	request_url = document.getElementById('url-text').value;

	$.get("/followeb/tasks/preview/"+request_url+"/", function(data){
		alert(data);	
	});
}