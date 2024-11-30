document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.querySelector(".hamburger");
    const nav = document.querySelector("nav");
    const mainMenuItems = document.querySelectorAll("nav ul li");

    // Toggle the navigation menu when the hamburger is clicked
    hamburger.addEventListener("click", function () {
        nav.classList.toggle("active"); // Toggle the 'active' class on the nav
    });

    // Handle submenu and link clicks
    mainMenuItems.forEach(item => {
        const submenu = item.querySelector("ul"); // Get the submenu (if any)
        const link = item.querySelector("a"); // Get the main link

        if (submenu) {
            // Listen for a click on the main menu item
            link.addEventListener("click", function (e) {
                // Prevent navigation for menu items with submenus
                e.preventDefault();

                // Toggle active class on the parent menu item
                item.classList.toggle("active");

                // Close other submenus
                mainMenuItems.forEach(otherItem => {
                    if (otherItem !== item) {
                        otherItem.classList.remove("active");
                    }
                });
            });
        } else if (link && link.getAttribute("target") === "_blank") {
            // Handle external links with target="_blank"
            link.addEventListener("click", function (e) {
                e.preventDefault(); // Prevent default behavior
                window.open(link.href, "_blank"); // Open the link in a new tab
            });
        }
    });
});
