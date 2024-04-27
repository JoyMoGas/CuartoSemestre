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