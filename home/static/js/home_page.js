$(document).ready(function () {
  $(".owl-carousel").owlCarousel({
    //Basic Speeds
    slideSpeed : 200,
    paginationSpeed : 800,
 
    //Autoplay
    autoPlay : false,
    goToFirst : true,
    goToFirstSpeed : 1000,
 
    // Navigation
    navigation : false,
    navigationText : ["prev","next"],
    pagination : true,
 
    // Responsive
    responsive: true,
    items : 1,
    itemsDesktop : [1199,1],
    itemsDesktopSmall : [980,1],
    itemsTablet: [768,1],
    itemsMobile : [479,1]
  });
});
