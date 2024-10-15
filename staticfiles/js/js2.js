mainMenuItems.forEach(item => {
    const submenu = item.querySelector("ul"); // Get the submenu (if any)
    const link = item.querySelector("a"); // Get the link

    if (submenu) {
        // Listen for a click on the main menu item
        item.addEventListener("click", function (e) {
            // Check if the link has data-new-tab attribute (you can set this in HTML)
            if (link && link.getAttribute("data-new-tab") === "true") {
                // Open link in a new tab using window.open()
                window.open(link.href, "_blank");
                return; // Exit to avoid further actions
            }

            // Prevent the link from navigating if it has a submenu
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
            window.location = link.href;
        });
    }
});
