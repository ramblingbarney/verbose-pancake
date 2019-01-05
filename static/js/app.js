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

// ajax product vote button add one vote
function plusOneVote(element){
    var voteId = $(element).attr("data-id");
    var csrftoken = getCookie('csrftoken');

    $.ajax({
        url : '', // the endpoint
        type : 'POST', // http method
        data : { vote_id : voteId, 'csrfmiddlewaretoken': csrftoken }, // data sent with the post request

        // handle a successful response
        success : function(data) {

          var originalVoteNumber = Number($("span[data-id=" + data +"]").text());
          // change the vote number red
          $("span[data-id=" + data +"]").css('color', 'red');
          // increment text by 1 to match database record value
          $("span[data-id=" + data +"]").text(originalVoteNumber + 1);

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });

}

// get the user logged in cookie for the ajax product vote add one vote
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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

// remove spaces in the credit card number on checkout charge page
$(document).ready(function(){
    $('#creditcard-number').on('change', function(){
       $(this).val($(this).val().replace(/\s+/g, ''));
     });
});
