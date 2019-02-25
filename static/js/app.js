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
        data : { vote_id : voteId,
                'csrfmiddlewaretoken': csrftoken,
                action_type: 'vote' }, // data sent with the post request

        // handle a successful response
        success : function(data) {

          if (data == 0){
            // User is only allowed to vote once
            $('input#vote_' + voteId).css('background-color','red');
            $('input#vote_' + voteId).val('Already Voted!');
          }else if(data == 1){
            // User has to purchase freature first
            $('input#vote_' + voteId).css('background-color','red');
            $('input#vote_' + voteId).val('Purchase Required');
          }

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

// ajax admin time spent button add 15 mins
function plus15Mins(element){
    var timeId = $(element).attr("time-id");
    var csrftoken = getCookie('csrftoken');

    $.ajax({
        url : '', // the endpoint
        type : 'POST', // http method
        data : { time_id : timeId,
                'csrfmiddlewaretoken': csrftoken,
                action_type: 'time' }, // data sent with the post request

        // handle a successful response
        success : function(data) {

          var originalTimeNumber = Number($("span[time-id=" + data +"]").text());
          // change the vote number red
          $("span[time-id=" + data +"]").css('color', 'red');
          // increment text by 1 to match database record value
          $("span[time-id=" + data +"]").text(originalTimeNumber + 15);

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

// issues are created and edited with zero price
function issueZeroPrice() {

  let productType = $('#id_product_type').val();

  if (productType == 'I') {
        $('input#id_price').val(0);
  }

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
    document.getElementById("mySidenav").style.width = "50%";
    document.getElementById("mySidenav").style.borderRightStyle = "solid";
    document.getElementById("mySidenav").style.borderColor = "#76503F";
}

/* Set the width of the side navigation to 0 */
function hideMobileMenu() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("mySidenav").style.borderRightStyle = "none";
    document.getElementById("mySidenav").style.borderColor = "#8B817F";
}

// remove spaces in the credit card number on checkout charge page
$(document).ready(function(){
    $('#creditcard-number').on('change', function(){
       $(this).val($(this).val().replace(/\s+/g, ''));
     });
});
