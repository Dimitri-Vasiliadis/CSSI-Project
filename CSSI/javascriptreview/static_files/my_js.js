function stuffToDoWhenFadeOutIsDone() {
  alert("done fading out");
}
// function stuffToDoWhenClicked() {
//   $("#button").fadeOut(1000)
// }

function stuffToDoWhenReady() {
  $("#hello").fadeOut(1000, stuffToDoWhenFadeOutIsDone);
  // $("#button").click(stuffToDoWhenClicked)
   $("#button").click(function() {
     $("#button").fadeOut(1000)
   })
}
$(document).ready(stuffToDoWhenReady)
