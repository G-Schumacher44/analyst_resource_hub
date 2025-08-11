(function () {
  function getHomeHref() {
    // Best: Material sets a <base> tag with the site root (works for GH Pages subpaths)
    const base = document.querySelector("base");
    if (base && base.href) {
      // Send to the built homepage from docs/index.md
      return new URL("index.html", base.href).href;
    }

    // Fallback: the logo link points at home
    const logo = document.querySelector(".md-header__button.md-logo");
    if (logo && logo.href) return logo.href;

    // Last resort: absolute root homepage
    return new URL("index.html", window.location.origin + "/").href;
  }

  function addHomeButton() {
    // Header actions container can vary by version:
    const header = document.querySelector("header .md-header__inner");
    if (!header) return;

    // Avoid duplicates if hot-reloading
    if (header.querySelector(".home-button")) return;

    // Build the Home button
    const button = document.createElement("a");
    button.className = "md-header__button md-icon home-button";
    button.href = getHomeHref();
    button.title = "Home";
    button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8h5z"/></svg>';

    // Insert before the search button to place it next to the palette toggle
    const search = header.querySelector('[for="__search"]');
    if (search) {
      search.parentNode.insertBefore(button, search);
    } else {
      // Fallback if search is disabled, append to header
      header.appendChild(button);
    }
  }

  // Run on initial load and after instant navigation
  const observer = new MutationObserver(addHomeButton);
  observer.observe(document.body, { childList: true, subtree: true });

  // Initial call
  document.addEventListener("DOMContentLoaded", addHomeButton);
})();