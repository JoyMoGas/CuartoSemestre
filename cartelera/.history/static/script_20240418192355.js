function toggleMenu() {
    var menu = document.getElementById('menu');
    menu.classList.toggle('open');

    var content = document.getElementById('content');
    content.classList.toggle('menu-open');
}

window.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    var floatingButton = document.getElementById('floatingBtn');

    if (scrollPosition > 100) {
        floatingButton.classList.add('show');
    } else {
        floatingButton.classList.remove('show');
    }
    });

    document.addEventListener("DOMContentLoaded", function() {
        var cardMovies = document.querySelectorAll(".card-movie");

        function revealElements() {
            cardMovies.forEach(function(cardMovie) {
                if (isElementInViewport(cardMovie)) {
                    cardMovie.classList.add("visible");
                }
            });
        }


        function isElementInViewport(el) {
            var rect = el.getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        }

        document.addEventListener("DOMContentLoaded", function () {
            var cardMovies = document.querySelectorAll(".card-movie-page");
      
            function revealElements() {
              cardMovies.forEach(function (cardMovie) {
                if (isElementInViewport(cardMovie)) {
                  cardMovie.classList.add("visible");
                }
              });
            }
      
            function isElementInViewport(el) {
              var rect = el.getBoundingClientRect();
              return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <=
                  (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <=
                  (window.innerWidth || document.documentElement.clientWidth)
              );
            }

        // Revelar elementos al cargar la página
        revealElements();

        // Revelar elementos al hacer scroll
        window.addEventListener("scroll", revealElements);
    });

    document.addEventListener("DOMContentLoaded", function() {
    var cardMovies = document.querySelectorAll(".card-movie-page");

    function revealElements() {
        cardMovies.forEach(function(cardMovie) {
            if (isElementInViewport(cardMovie)) {
                cardMovie.classList.add("visible");
            }
        });
    }

    function isElementInViewport(el) {
        var rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    revealElements();

    window.addEventListener("scroll", revealElements);
    });