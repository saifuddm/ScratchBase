var show = 0;
function showDiv() {
    if (show%2 == 0){
        document.getElementById('courses').style.display = "block";
    }
    if(show%2 == 1){
        document.getElementById('courses').style.display = "none";
        window.scrollTo({top:0, behavior: 'smooth'});
    }
    show++;
}
var i = 0;
var y = 0;
$(document).ready(function(){
  $("#courseButton").click(function(){
//    $("#courses").slideToggle(1000);
//    $('html, body').animate({
//        scrollTop: 1000
//    }, 5);
      
//      $("#courses").slideToggle("slow");
//      });
      if(i%2 == 0){
        $("#courses").show();
      }
      if(i%2 == 1){
          $("#courses").slideUp("slow");
          window.scrollTo({top: 0, behavior: 'smooth'});
      }
      i++;
  });
    
    $("#projectButton").click(function(){
//    $("#courses").slideToggle(1000);
//    $('html, body').animate({
//        scrollTop: 1000
//    }, 5);
      
//      $("#courses").slideToggle("slow");
//      });
      if(y%2 == 0){
        $("#projects").show();
      }
      if(y%2 == 1){
          $("#projects").slideUp("slow");
      }
      y++;
  });
});