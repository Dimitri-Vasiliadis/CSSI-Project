function disappear() {
  $("#disappear-div").toggleClass("hidden");
}


$(document).ready(function() {
    $("#disappear-btn").click(disappear);
  }
)
