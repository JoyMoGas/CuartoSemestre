    function toggleMenu() {
    var menu = document.getElementById("menu");
    menu.classList.toggle("open");

    var content = document.getElementById("content");
    content.classList.toggle("menu-open");
    }

    document.addEventListener("click", function(event) {
        var menu = document.getElementById("menu");
        var menuButton = document.getElementById("menuButton");
        var content = document.getElementById("content");
    
        // Verificamos si el clic fue dentro del menú o en el botón de apertura del menú
        var isClickInsideMenu = menu.contains(event.target);
        var isClickOnMenuButton = event.target === menuButton;
    
        // Si el clic no fue dentro del menú ni en el botón de apertura del menú, entonces cerramos el menú
        if (!isClickInsideMenu && !isClickOnMenuButton) {
            menu.classList.remove("open");
            content.classList.remove("menu-open");
        }
    });

    function toggleMenu() {
        var menu = document.getElementById("menu");
        var content = document.getElementById("content");
    
        menu.classList.toggle("open");
        content.classList.toggle("menu-open");
    
        // Si el menú se abre, desplazar el contenido hacia la derecha; si se cierra, regresar el contenido a su posición original
        if (menu.classList.contains("open")) {
            content.style.marginLeft = "250px"; // Ajusta el valor según el ancho del menú
        } else {
            content.style.marginLeft = "0";
        }
    }
    
    document.addEventListener("click", function(event) {
        var menu = document.getElementById("menu");
        var menuButton = document.getElementById("menuButton");
        var content = document.getElementById("content");
    
        // Verificar si el menú está abierto y si el clic no es dentro del menú o en el botón de apertura del menú
        if (menu.classList.contains("open") && event.target !== menu && event.target !== menuButton && !menu.contains(event.target)) {
            menu.classList.remove("open"); // Cerrar el menú
            content.classList.remove("menu-open"); // Eliminar la clase de desplazamiento del contenido
            content.style.marginLeft = "0"; // Regresar el contenido a su posición original
        }
    });

    document.addEventListener("DOMContentLoaded", function() {
        var floatingButton = document.getElementById("floatingBtn");
        
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

    
