// foundation initialisation
$(document).foundation();

// message fade out

$(document).ready(function(){
    $('.messages').delay(3000).fadeOut();
});

// product image toggle full size to reduced
function toggleFullSize(element){
  element.classList.toggle('image-detail-full-size');
}

// product vote button add one vote
function plusOneVote(element){
  alert('adding vote');
}

// Toggle Desktop Menu bar
function showDesktopMenu(){
  document.getElementById("desktopNav").style.visibility = 'visible';
}

function hideDesktopMenu(){
  document.getElementById("desktopNav").style.visibility = 'hidden';
}

// Toggle Mobile Menu bar
function showMobileMenu() {
    document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function hideMobileMenu() {
    document.getElementById("mySidenav").style.width = "0";
}
