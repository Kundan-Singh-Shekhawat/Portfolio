/**
 * Main client-side interactivity for the portfolio website:
 * - Light and dark mode theme toggle with localStorage & system preference support
 * - Mobile hamburger menu toggle
 */

document.addEventListener("DOMContentLoaded", () => {
  const THEME_STORAGE_KEY = "portfolio-theme";
  const themeToggleButtons = document.querySelectorAll("[data-theme-toggle]");
  const themeLabels = document.querySelectorAll("[data-theme-label]");

  const getActiveTheme = () => {
    const attrTheme = document.documentElement.getAttribute("data-theme");
    if (attrTheme === "dark" || attrTheme === "light") {
      return attrTheme;
    }
    return document.documentElement.classList.contains("dark") ? "dark" : "light";
  };

  const applyTheme = (theme, persist = false) => {
    const isDark = theme === "dark";
    document.documentElement.setAttribute("data-theme", theme);
    document.documentElement.classList.toggle("dark", isDark);

    themeToggleButtons.forEach((btn) => {
      btn.setAttribute("aria-pressed", String(isDark));
      btn.setAttribute(
        "aria-label",
        isDark ? "Switch to light mode" : "Switch to dark mode"
      );
      btn.setAttribute(
        "title",
        isDark ? "Switch to light mode" : "Switch to dark mode"
      );
    });

    themeLabels.forEach((label) => {
      label.textContent = isDark ? "Light Mode" : "Dark Mode";
    });

    if (persist) {
      try {
        localStorage.setItem(THEME_STORAGE_KEY, theme);
      } catch (e) {}
    }
  };

  // Sync initial button states with active theme
  applyTheme(getActiveTheme(), false);

  themeToggleButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const nextTheme = getActiveTheme() === "dark" ? "light" : "dark";
      applyTheme(nextTheme, true);
    });
  });

  // Listen for OS theme changes when user hasn't explicitly saved a preference
  if (window.matchMedia) {
    const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
    const handleSystemThemeChange = (e) => {
      try {
        if (!localStorage.getItem(THEME_STORAGE_KEY)) {
          applyTheme(e.matches ? "dark" : "light", false);
        }
      } catch (err) {}
    };
    if (typeof mediaQuery.addEventListener === "function") {
      mediaQuery.addEventListener("change", handleSystemThemeChange);
    }
  }

  // Mobile hamburger menu toggle
  const menuToggleBtn = document.getElementById("mobile-menu-toggle");
  const mobileMenu = document.getElementById("mobile-menu");
  const iconOpen = document.getElementById("menu-icon-open");
  const iconClose = document.getElementById("menu-icon-close");

  if (menuToggleBtn && mobileMenu) {
    menuToggleBtn.addEventListener("click", () => {
      const isExpanded = menuToggleBtn.getAttribute("aria-expanded") === "true";
      menuToggleBtn.setAttribute("aria-expanded", String(!isExpanded));
      mobileMenu.classList.toggle("hidden");
      if (iconOpen && iconClose) {
        iconOpen.classList.toggle("hidden");
        iconClose.classList.toggle("hidden");
      }
    });
  }
});
