document.addEventListener("DOMContentLoaded", function() {
    // Función para alternar la visibilidad del menú
    function toggleMenu() {
        var menu = document.getElementById("menu");
        menu.classList.toggle("open");

        var content = document.getElementById("content");
        content.classList.toggle("menu-open");
    }

    // Función para animación de desplazamiento suave
    function scrollToTarget(targetId) {
        var start = window.pageYOffset;
        var targetElement = document.getElementById(targetId);
        var end = targetElement.getBoundingClientRect().top + window.pageYOffset;
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
    }

    // Botón flotante
    var floatingButton = document.getElementById("floatingBtn");

    floatingButton.addEventListener("click", function(event) {
        event.preventDefault();
        scrollToTarget("top"); // Desplazarse suavemente hacia arriba
    });

    // Mostrar u ocultar el botón flotante según el desplazamiento
    window.addEventListener("scroll", function () {
        var scrollPosition = window.scrollY;

        if (scrollPosition > 100) {
            floatingButton.classList.add("show");
        } else {
            floatingButton.classList.remove("show");
        }
    });

    // Agregar evento de clic para abrir la lista desplegable
    var menuButton = document.getElementById("menuButton");

    menuButton.addEventListener("click", function() {
        toggleMenu();
    });

    // Agregar evento de clic a los enlaces del menú desplegable
    var menuLinks = document.querySelectorAll(".menu a");

    menuLinks.forEach(function (link) {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            var targetId = this.getAttribute("href").substring(1);
            scrollToTarget(targetId); // Desplazarse suavemente al objetivo del enlace
            toggleMenu(); // Ocultar el menú desplegable después de hacer clic
        });
    });

    // Revelar elementos al cargar la página
    function revealElements(selector) {
        var elements = document.querySelectorAll(selector);

        elements.forEach(function (element) {
            if (isElementInViewport(element)) {
                element.classList.add("visible");
            }
        });
    }

    // Verificar si un elemento está en la vista del usuario
    function isElementInViewport(el) {
        var rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    // Revelar elementos al cargar la página
    revealElements(".card-movie");

    // Revelar elementos al hacer scroll
    window.addEventListener("scroll", function () {
        revealElements(".card-movie");
    });

    // Revelar elementos al cargar la página
    revealElements(".card-movie-page");

    // Revelar elementos al hacer scroll
    window.addEventListener("scroll", function () {
        revealElements(".card-movie-page");
    });

});
