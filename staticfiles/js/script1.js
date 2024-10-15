document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.querySelector(".hamburger");
    const nav = document.querySelector("nav");
    const mainMenuItems = document.querySelectorAll("nav ul li");

    // Toggle the navigation menu when hamburger is clicked
    hamburger.addEventListener("click", function () {
        nav.classList.toggle("active"); // Toggle the 'active' class on the nav
    });

    // Handle submenu click on small screens
    mainMenuItems.forEach(item => {
        const submenu = item.querySelector("ul"); // Get the submenu (if any)

        if (submenu) {
            // Listen for a click on the main menu item
            item.addEventListener("click", function (e) {
                // Prevent the link from navigating only if there is a submenu
                e.preventDefault();

                // Toggle active class on the parent menu item
                item.classList.toggle("active");

                // Close other submenus if one is opened
                mainMenuItems.forEach(otherItem => {
                    if (otherItem !== item) {
                        otherItem.classList.remove("active");
                    }
                });
            });
        } else {
            // If there's no submenu, allow the link to work normally
            item.addEventListener("click", function () {
                window.location = item.querySelector("a").href;
            });
        }
    });
});
