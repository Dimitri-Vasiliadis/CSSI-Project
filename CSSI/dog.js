function disappear() {
  $("#disappear_ul").toggleClass("hidden");
}
function hidetext() {
  $("#sub_photo").hide();
  $("#sub_about").hide();
  $("#sub_profile").hide();
}

/*
function moveTest() {
  var input_text = $('input').val();
  $('#result').text(input_text);
}
*/

function about() {
  $("#sub_about").show();
}
function photo() {
  $("#sub_photo").show();
}
function profile() {
  $("#sub_profile").show();
}

$(document).ready(function() {
  $("#popdown").click(disappear);
  $("#about").hover(about,hidetext);
  $("#photo").hover(photo,hidetext);
  $("#profile").hover(profile,hidetext);
  hidetext();
  }
)
