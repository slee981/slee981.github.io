/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
  var x = document.getElementById("menu");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }

  var r = document.getElementsByClassName("right-nav");
  r.className += " responsive";
}

// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("menu").style.padding = "5px 30px";
    document.getElementById("menu").style.borderBottom = "2px solid rgb(65, 65, 65)";
  } else {
    document.getElementById("menu").style.padding = "10px 30px";
    document.getElementById("menu").style.borderBottom = "none";
  }
}