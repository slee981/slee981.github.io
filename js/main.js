/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function toggleTopNav() {
  var x = document.getElementById("menu");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
  var r = document.getElementById("linksmenu");
  if (r.className === "links") {
    r.className += " responsive";
  } else {
    r.className = "links";
  }
}

// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function () { scrollFunction() };

// media match 
var x = window.matchMedia("(max-width: 1200px)")

function scrollFunction() {

  // if you are scrolling
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    document.getElementById("menu").style.borderBottom = "2px solid rgb(65, 65, 65)";
    // mobile
    if (x.matches) {
      document.getElementById("menu").style.padding = "60px 10px 10px";
      // desktop
    } else {
      document.getElementById("menu").style.padding = "20px 10px 5px";
    }

    // if you are not scrolling
  } else {
    document.getElementById("menu").style.borderBottom = "0.5px solid rgb(65, 65, 65)";
    // mobile
    if (x.matches) {
      document.getElementById("menu").style.padding = "60px 10px 20px";
      // desktop
    } else {
      document.getElementById("menu").style.padding = "20px 10px";
    }
  }
}