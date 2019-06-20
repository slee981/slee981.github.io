/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
  var x = document.getElementById("menu");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
  console.log("changed topnav")
  var r = document.getElementById("linksmenu");
  console.log("found linksmenu")
  if (r.className === "links") {
    r.className += " responsive";
  } else {
    r.className = "links";
  }
}

// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("menu").style.padding = "15px 10px";
    document.getElementById("menu").style.borderBottom = "2px solid rgb(65, 65, 65)";
  } else {
    document.getElementById("menu").style.padding = "20px 10px";
    document.getElementById("menu").style.borderBottom = "0.5px solid rgb(65, 65, 65)";
  }
}