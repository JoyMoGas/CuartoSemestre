    function toggleMenu() {
    var menu = document.getElementById("menu");
    menu.classList.toggle("open");

    var content = document.getElementById("content");
    content.classList.toggle("menu-open");
    }

    document.addEventListener("DOMContentLoaded", function() {
        var floatingButton = document.getElementById("floatingBtn");
        
        floatingButton.addEventListener("click", function(event) {
            event.preventDefault();
            
            var scrollToTop = window.setInterval(function() {
                var position = window.pageYOffset;
                
                if (position > 0) {
                    window.scrollTo(0, position - 50); // Controla la velocidad del desplazamiento cambiando este valor
                } else {
                    window.clearInterval(scrollToTop);
                }
            }, 16); // Controla la velocidad del desplazamiento cambiando este valor
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
