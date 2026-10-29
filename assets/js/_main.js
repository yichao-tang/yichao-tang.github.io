/* ==========================================================================
   jQuery plugin settings and other scripts
   ========================================================================== */

$(document).ready(function(){
   // Sticky footer
  var bumpIt = function() {
      $("body").css("margin-bottom", $(".page__footer").outerHeight(true));
    },
    didResize = false;

  bumpIt();

  $(window).resize(function() {
    didResize = true;
  });
  setInterval(function() {
    if (didResize) {
      didResize = false;
      bumpIt();
    }
  }, 250);
  // FitVids init
  $("#main").fitVids();

  // init sticky sidebar
  $(".sticky").Stickyfill();

  var stickySideBar = function(){
    var show = $(".author__urls-wrapper button").length === 0 ? window.matchMedia("(min-width: 925px)").matches : !$(".author__urls-wrapper button").is(":visible");
    // console.log("has button: " + $(".author__urls-wrapper button").length === 0);
    // console.log("Window Width: " + windowWidth);
    // console.log("show: " + show);
    //old code was if($(window).width() > 1024)
    if (show) {
      // fix
      Stickyfill.rebuild();
      Stickyfill.init();
      $(".author__urls").show();
    } else {
      // unfix
      Stickyfill.stop();
      $(".author__urls").hide();
    }
  };

  stickySideBar();

  $(window).resize(function(){
    stickySideBar();
  });

  // Follow menu drop down

  $(".author__urls-wrapper button").on("click", function() {
    $(".author__urls").fadeToggle("fast", function() {});
    $(".author__urls-wrapper button").toggleClass("open");
  });

  // init smooth scroll
  $("a").smoothScroll({offset: -20});

  // add lightbox class to all image links
  $("a[href$='.jpg'],a[href$='.jpeg'],a[href$='.JPG'],a[href$='.png'],a[href$='.gif']").addClass("image-popup");

  // Each paper figure opens on its own and closes when clicked again.
  $(".image-popup").magnificPopup({
    type: 'image',
    tLoading: document.documentElement.lang === 'zh-CN' ? '正在载入图片…' : 'Loading image…',
    gallery: {
      enabled: false,
      navigateByImgClick: false,
      arrows: false
    },
    image: {
      verticalFit: true,
      tError: document.documentElement.lang === 'zh-CN' ? '<a href="%url%">图片</a>无法载入。' : '<a href="%url%">The image</a> could not be loaded.'
    },
    zoom: {
      enabled: !window.matchMedia('(prefers-reduced-motion: reduce)').matches,
      duration: 200,
      easing: 'ease-in-out'
    },
    removalDelay: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 200,
    closeOnContentClick: true,
    closeOnBgClick: true,
    midClick: false
  });

});
