
function  timer2start() {
  // Set the date we're counting down to
  //var countDownDate = new Date("Aug 6, 2023 16:15:00").getTime();
  var countDownDate = new Date("Aug 5, 2023 23:29:00").getTime();

  // Update the count down every 1 second
  var x = setInterval(function() {

    // Get today's date and time
    var now = new Date().getTime();
      
    // Find the distance between now and the count down date
    var distance = countDownDate - now;
      
    // Time calculations for days, hours, minutes and seconds
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
      
    // Output the result in an element with id="demo"
    document.getElementById("hrs2").innerHTML = hours + "h ";
    document.getElementById("min2").innerHTML = minutes + "m ";
    document.getElementById("sec2").innerHTML = seconds   + "s ";

    if (distance < 0) {
      clearInterval(x);
      document.getElementById('web').style.display='none'
      document.getElementById('releasedweb').style.display='block'
      document.getElementById('timerweb').style.display='none'
    }else{
      document.getElementById('web').style.display='none'
      document.getElementById('releasedweb').style.display='none'
      document.getElementById('timerweb').style.display='block'
    }
  }, 1000);
}
