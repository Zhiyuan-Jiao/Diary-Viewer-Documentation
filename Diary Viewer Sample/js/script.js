<script type="text/javascript" src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
 
 $(document).ready(function(){
     $("#input").keyup(function(event) {
        if (event.keyCode === 13) {
            $("#button").click();
        }
    });
     
     $('#button').click(function() {
         var inputvalue = $("#input").val();
         window.location.replace("../diary-47-desynchronized-scrolling/#a"+inputvalue);
         if (inputvalue < 1 || inputvalue > 392) {
          window.location.href="#modalWindow1";
         }
     });
 });