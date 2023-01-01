document.oncontextmenu=function(){return false};
document.onselectstart=function(){return false};
document.ondragstart=function(){return false};
function CreateBookmarkLink(){var b="Winners Chapel , Total Garden Ibadan";
var a=document.location.href;
if(window.sidebar){window.sidebar.addPanel(b,a,"")
}
else{if(window.external){window.external.AddFavorite(a,b)
}else {
	if(window.opera&&window.print){alert("Press Control + D to bookmark");
	return true}else{alert("Press Control + D to bookmark")
	 }
   }

 }

}  