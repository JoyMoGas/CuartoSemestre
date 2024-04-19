    function toggleMenu() {
    var menu = document.getElementById("menu");
    menu.classList.toggle("open");

    var content = document.getElementById("content");
    content.classList.toggle("menu-open");
    }

    document.addEventListener("DOMContentLoaded", function() {
        var floatingButton = document.querySelectorAll("#floatingBtn, #list-button");
        
        floatingButton.addEventListener("click", function(event) {
            event.preventDefault();
            
            var start = window.pageYOffset;
            var end = 0;
            var duration = 500; // Duración total de la animación en milisegundos
            var startTime = null;
            
            function easeInOutQuad(t, b, c, d) {
                t /= d / 2;
                if (t < 1) return c / 2 * t * t + b;
                t--;
                return -c / 2 * (t * (t - 2) - 1) + b;
            }
            
            function scrollAnimation(currentTime) {
                if (startTime === null) startTime = currentTime;
                var timeElapsed = currentTime - startTime;
                var scrollY = easeInOutQuad(timeElapsed, start, end - start, duration);
                window.scrollTo(0, scrollY);
                if (timeElapsed < duration) requestAnimationFrame(scrollAnimation);
            }
            
            requestAnimationFrame(scrollAnimation);
        });
        
        window.addEventListener("scroll", function () {
            var scrollPosition = window.scrollY;
    
            if (scrollPosition > 100) {
                floatingButton.classList.add("show");
            } else {
                floatingButton.classList.remove("show");
            }
        });
    });

    document.addEventListener("DOMContentLoaded", function () {
    var cardMovies = document.querySelectorAll(".card-movie");

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
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    // Revelar elementos al cargar la página
    revealElements();

    // Revelar elementos al hacer scroll
    window.addEventListener("scroll", revealElements);
    });

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
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    revealElements();

    window.addEventListener("scroll", revealElements);
    });

    
