function disappear() {
  $("#disappear_ul").toggleClass("hidden");
}
function hidetext() {
  $("#sub").hide();
}
function moveTest() {
  var input_text = $('input').val();
  $('#result').text(input_text);
}

function about() {
  $("#info").text("I love programming!");
  $("#sub").show();
}
function photo() {
  $("#info").text("photo");
  $("#sub").show();
}
function profile() {
  $("#info").text("Hello I am Dimitri!");
  $("#sub").show();
}

$(document).ready(function() {
  $("#popdown").click(disappear);
  $("#disappear_ul div#about").hover(about,hidetext);
  $("#disappear_ul div#photo").hover(photo,hidetext);
  $("#disappear_ul div#profile").hover(profile,hidetext);
  $("#sub").hide();
  }
)
