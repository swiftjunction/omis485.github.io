"use strict";
var $ = function(id) { return document.getElementById(id); };



var toggle = function() {
    var h2 = this;                        
    var div = h2.nextElementSibling;  

  	if(h2.className){  
        h2.className = '';
    } else { 
        h2.className = 'minus';
    }

   
      if (div.className){
        div.className = '';
    } else { 
        div.className = 'open';
    } 
       
     
};

window.onload = function() {
    var faqs = $("faqs");
    var h2Elements = faqs.getElementsByTagName("h2");
    var next = h2Elements.nextElementSibling;
    
    
       
    for (var i = 0; i < h2Elements.length; i++ ) {
    	h2Elements[i].onclick = toggle;
    }
    
    h2Elements[0].firstChild.focus();    
  
};
