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
  let menu = document.getElementById("menu");

  // if you are scrolling
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
    menu.style.borderBottom = "2px solid rgb(65, 65, 65)";
    menu.style["boxShadow"] = "5px 10px 18px #888888";

    // mobile
    if (x.matches) {
      menu.style.padding = "40px 10px 10px";
      // desktop
    } else {
      menu.style.padding = "10px 10px 5px";
    }

    // if you are not scrolling
  } else {
    menu.style["boxShadow"] = "none";
    menu.style.borderBottom = "0.5px solid rgb(65, 65, 65)";
    // mobile
    if (x.matches) {
      menu.style.padding = "60px 10px 20px";
      // desktop
    } else {
      menu.style.padding = "20px 10px";
    }
  }
}