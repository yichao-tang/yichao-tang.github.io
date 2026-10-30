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

  // Publication topic links use native anchors to clear the sticky masthead.
  $("a").not(".publication-list__topics a").smoothScroll({offset: -20});

  // add lightbox class to all image links
  $("a[href$='.jpg'],a[href$='.jpeg'],a[href$='.JPG'],a[href$='.png'],a[href$='.gif']").addClass("image-popup");

  // Keep Magnific's single-image dialog, but animate only after the full image
  // has loaded. Its built-in zoom skips opening when hasSize is not ready yet.
  var figureZoomDuration = 300;

  var figureImageRect = function(image) {
    var rect = image.getBoundingClientRect();
    var style = window.getComputedStyle(image);
    var left = parseFloat(style.paddingLeft) || 0;
    var right = parseFloat(style.paddingRight) || 0;
    var top = parseFloat(style.paddingTop) || 0;
    var bottom = parseFloat(style.paddingBottom) || 0;
    return {
      left: rect.left + left,
      top: rect.top + top,
      width: rect.width - left - right,
      height: rect.height - top - bottom
    };
  };

  var clearFigureZoom = function(popup, revealContent) {
    var state = popup.figureZoomState;
    if (state) {
      window.cancelAnimationFrame(state.frame);
      window.cancelAnimationFrame(state.nextFrame);
      window.clearTimeout(state.timer);
      if (state.onTransitionEnd) {
        state.image.removeEventListener('transitionend', state.onTransitionEnd);
      }
      if (state.image.parentNode) state.image.parentNode.removeChild(state.image);
      popup.figureZoomState = null;
    }
    if (revealContent !== false) {
      if (popup.content) popup.content.css('visibility', 'visible');
      if (popup.currItem && popup.currItem.img) popup.currItem.img.css('visibility', '');
    }
  };

  var animateFigureZoom = function(popup, closing) {
    var item = popup.currItem;
    if (!popup.figureZoomMotion || !item || item.type !== 'image' ||
        !item.hasSize || item.loadError || !item.el || !item.img) return;
    if (!closing && popup.figureZoomStarted) return;

    var thumbnail = item.el.find('img')[0];
    if (!thumbnail) return;
    var small = figureImageRect(thumbnail);
    var large = figureImageRect(item.img[0]);
    if (!small.width || !small.height || !large.width || !large.height) return;

    var state = popup.figureZoomState;
    var isNewState = !state;
    if (isNewState) {
      var image = item.img[0].cloneNode(false);
      image.removeAttribute('style');
      image.className = 'mfp-animated-image';
      image.setAttribute('aria-hidden', 'true');
      $(image).css({
        position: 'fixed', zIndex: 9999, left: 0, top: 0,
        width: large.width, height: large.height,
        maxWidth: 'none', maxHeight: 'none', margin: 0, padding: 0,
        border: 0, transformOrigin: '0 0', willChange: 'transform',
        transition: 'none'
      });
      state = { image: image, width: large.width, height: large.height };
      popup.figureZoomState = state;
      popup.wrap.append(image);
    } else {
      window.cancelAnimationFrame(state.frame);
      window.cancelAnimationFrame(state.nextFrame);
      window.clearTimeout(state.timer);
      if (state.onTransitionEnd) {
        state.image.removeEventListener('transitionend', state.onTransitionEnd);
      }
    }

    var transform = function(rect) {
      return 'translate3d(' + rect.left + 'px,' + rect.top + 'px,0) scale(' +
        (rect.width / state.width) + ',' + (rect.height / state.height) + ')';
    };

    popup.content.css('visibility', 'hidden');
    item.img.css('visibility', 'hidden');
    if (!closing || isNewState) {
      state.image.style.transform = transform(closing ? large : small);
    }
    popup.figureZoomStarted = true;
    state.onTransitionEnd = function(event) {
      if (event.target === state.image && event.propertyName === 'transform') {
        clearFigureZoom(popup, !closing);
      }
    };
    state.image.addEventListener('transitionend', state.onTransitionEnd);
    // Flush the starting geometry and paint it before changing the transform.
    state.image.getBoundingClientRect();
    state.frame = window.requestAnimationFrame(function() {
      state.nextFrame = window.requestAnimationFrame(function() {
        state.image.style.transition = 'transform ' + figureZoomDuration +
          'ms cubic-bezier(0.22, 0.61, 0.36, 1)' +
          (closing ? ', opacity 100ms ease ' + (figureZoomDuration - 100) + 'ms' : '');
        state.image.style.transform = transform(closing ? small : large);
        // Blend the returning copy into the original thumbnail at the end.
        // The full-size image stays hidden until Magnific removes its layer.
        if (closing) state.image.style.opacity = '0';
        state.timer = window.setTimeout(function() {
          clearFigureZoom(popup, !closing);
        }, figureZoomDuration + 64);
      });
    });
    if (closing) popup.st.removalDelay = figureZoomDuration + 64;
    return true;
  };

  // Each figure opens on its own, then returns to its thumbnail on click.
  $(".image-popup").magnificPopup({
    type: 'image',
    mainClass: 'paper-figure-popup',
    tLoading: document.documentElement.lang === 'zh-CN' ? '正在载入图片…' : 'Loading image…',
    gallery: {
      enabled: false,
      navigateByImgClick: false,
      arrows: false
    },
    image: {
      verticalFit: false,
      tError: document.documentElement.lang === 'zh-CN' ? '<a href="%url%">图片</a>无法载入。' : '<a href="%url%">The image</a> could not be loaded.'
    },
    zoom: {
      enabled: false
    },
    removalDelay: 0,
    closeOnContentClick: true,
    closeOnBgClick: true,
    midClick: false,
    callbacks: {
      beforeOpen: function() {
        clearFigureZoom(this);
        this.figureZoomStarted = false;
        // The requested figure interaction uses this gentle transition even
        // when the browser's broader reduced-motion preference is enabled.
        this.figureZoomMotion = this.supportsTransition;
        this.st.removalDelay = 0;
      },
      open: function() {
        var item = this.currItem;
        if (this.figureZoomMotion && item.type === 'image' && item.el &&
            item.el.find('img').length) {
          this.content.css('visibility', 'hidden');
          if (item.img[0].complete && !animateFigureZoom(this, false)) {
            clearFigureZoom(this);
          }
        }
      },
      imageLoadComplete: function() {
        if (this.isOpen && !this.figureZoomStarted &&
            !animateFigureZoom(this, false)) clearFigureZoom(this);
      },
      updateStatus: function(status) {
        if (status.status === 'error') clearFigureZoom(this);
      },
      beforeClose: function() {
        animateFigureZoom(this, true);
      },
      close: function() {
        clearFigureZoom(this, false);
      }
    }
  });

});
