document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.querySelector(".hamburger");
    const nav = document.querySelector("nav");
    const mainMenuItems = document.querySelectorAll("nav ul li");
    const scrollToTopBtn = document.getElementById("scrollToTop");

    // Hamburger menu toggle
    hamburger?.addEventListener("click", function () {
        nav.classList.toggle("active");
    });

    // Menu item handling for submenus and links
    mainMenuItems.forEach(item => {
        const submenu = item.querySelector("ul");
        const link = item.querySelector("a");

        if (submenu) {
            // For items with submenus
            link.addEventListener("click", function (e) {
                e.preventDefault(); // Prevent navigation for parent links
                submenu.classList.toggle("visible"); // Toggle visibility

                // Close other submenus
                mainMenuItems.forEach(otherItem => {
                    if (otherItem !== item) {
                        const otherSubmenu = otherItem.querySelector("ul");
                        if (otherSubmenu) {
                            otherSubmenu.classList.remove("visible");
                        }
                    }
                });
            });
        }
    });

    // Scroll to Top Button logic
    window.addEventListener("scroll", function () {
        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            scrollToTopBtn.style.display = "block"; // Show button
        } else {
            scrollToTopBtn.style.display = "none"; // Hide button
        }
    });

    scrollToTopBtn?.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: "smooth" }); // Smooth scroll to top
    });
});
