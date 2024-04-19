    function toggleMenu() {
    var menu = document.getElementById("menu");
    menu.classList.toggle("open");

    var content = document.getElementById("content");
    content.classList.toggle("menu-open");
    }
    

    function toggleMenu() {
        var menu = document.getElementById("menu");
        var content = document.getElementById("content");
    
        menu.classList.toggle("open");
        content.classList.toggle("menu-open");
    
        if (menu.classList.contains("open")) {
            content.style.marginLeft = "250px";
        } else {
            content.style.marginLeft = "0";
        }
    }
    
    document.addEventListener("click", function(event) {
        var menu = document.getElementById("menu");
        var menuButton = document.getElementById("menuButton");
        var content = document.getElementById("content");

        if (menu.classList.contains("open") && event.target !== menu && event.target !== menuButton && !menu.contains(event.target)) {
            menu.classList.remove("open"); 
            content.classList.remove("menu-open"); 
            content.style.marginLeft = "0"; 
        }
    });

    document.addEventListener("DOMContentLoaded", function() {
        var floatingButton = document.getElementById("floatingBtn");
        
        floatingButton.addEventListener("click", function(event) {
            event.preventDefault();
            
            var start = window.pageYOffset;
            var end = 0;
            var duration = 500;
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

    revealElements();

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

    
