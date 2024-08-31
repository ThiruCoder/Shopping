
// Optional JavaScript to toggle menu on mobile view
document.querySelector('.hamburger').addEventListener('click', function() {
    document.getElementById('menu').classList.toggle('active')
});

$('.buy').click(function(){
    $('.bottom').addClass("clicked");
  });
  
  $('.remove').click(function(){
    $('.bottom').removeClass("clicked");
  });