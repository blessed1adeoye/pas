$(document).ready(function(){
	$('#basicuse').jflickrfeed({
		limit: 15,
		qstrings: {id: '42983924@N00'},
		itemTemplate: '<li><a href="http://www.flickr.com/photos/42983924@N00"><img src="{{image_s}}" alt="{{title}}" /></a></li>'
	});
	
	$('#sidebarflickr').jflickrfeed({
		limit: 15,
		qstrings: {id: '42983924@N00'},
		itemTemplate: '<li><a href="http://www.flickr.com/photos/42983924@N00"><img src="{{image_s}}" alt="{{title}}" /></a></li>'
	});
});