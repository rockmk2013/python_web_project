$(document).ready(function(){
  
  $(".gotop").click(function(){
    $("html,body").animate({"scrollTop":"0"})
    n=1
  })
  $(".gotop").fadeOut(0)
  $(window).scroll(function(){
    if($(window).scrollTop()>=$(".header").offset().top+150){
      $(".gotop").fadeIn()
    }else{
      $(".gotop").fadeOut()
    }
  })
})