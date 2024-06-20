// main script
(function () {
  "use strict";

  // Dropdown Menu Toggler For Mobile
  // ----------------------------------------
  const dropdownMenuToggler = document.querySelectorAll(
    ".nav-dropdown > .nav-link",
  );

  dropdownMenuToggler.forEach((toggler) => {
    toggler?.addEventListener("click", (e) => {
      e.target.parentElement.classList.toggle("active");
    });
  });

  // Testimonial Slider
  // ----------------------------------------
  // new Swiper(".testimonial-slider", {
  //   spaceBetween: 24,
  //   loop: true,
  //   pagination: {
  //     el: ".testimonial-slider-pagination",
  //     type: "bullets",
  //     clickable: true,
  //   },
  //   breakpoints: {
  //     768: {
  //       slidesPerView: 2,
  //     },
  //     992: {
  //       slidesPerView: 3,
  //     },
  //   },
  // });

  // Audio Player Control
  // ----------------------------------------
  const audioPlayers = document.querySelectorAll('.audio-player');

  audioPlayers.forEach(player => {
    player.addEventListener('play', function() {
      audioPlayers.forEach(otherPlayer => {
        if (otherPlayer !== player && !otherPlayer.paused) {
          otherPlayer.pause();
        }
      });
    });
  });
})();
