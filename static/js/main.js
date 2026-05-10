/**
 * main.js — Small JavaScript helpers for the portfolio.
 * Purpose 1: Toggle the mobile navigation menu open/closed.
 * Purpose 2: Filter project cards by technology tag.
 */

// ── MOBILE NAV TOGGLE ────────────────────────────────────────────────────────
const navToggle = document.getElementById("navToggle");
const navLinks  = document.getElementById("navLinks");

if (navToggle && navLinks) {
  navToggle.addEventListener("click", () => {
    navLinks.classList.toggle("open");
  });

  // Close the menu if the user clicks a link (good UX on mobile)
  navLinks.querySelectorAll(".nav-link").forEach((link) => {
    link.addEventListener("click", () => navLinks.classList.remove("open"));
  });
}

// ── PROJECT FILTER ───────────────────────────────────────────────────────────
// On the Projects page there are filter buttons (All, Flask, CLI, etc.).
// When clicked, we hide cards that don't match the selected tag.
const filterBar     = document.getElementById("filterBar");
const projectsGrid  = document.getElementById("projectsGrid");

if (filterBar && projectsGrid) {
  const buttons = filterBar.querySelectorAll(".filter-btn");
  const cards   = projectsGrid.querySelectorAll(".project-card");

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      // 1. Mark the clicked button as active
      buttons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");

      const filter = btn.dataset.filter; // e.g. "Flask" or "all"

      // 2. Show/hide cards based on their data-tags attribute
      cards.forEach((card) => {
        const tags = card.dataset.tags || "";          // "Python,Flask,HTML/CSS"
        const show = filter === "all" || tags.includes(filter);
        card.style.display = show ? "flex" : "none";
      });
    });
  });
}

// ── FADE-IN ON SCROLL ────────────────────────────────────────────────────────
// Adds a gentle fade-in effect to elements with the class "fade-in"
// when they scroll into view. Progressive enhancement — no crash if missing.
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target); // only animate once
      }
    });
  },
  { threshold: 0.1 }
);

document.querySelectorAll(".project-card, .journey-card, .skill-group, .timeline-item")
  .forEach((el) => {
    el.style.opacity  = "0";
    el.style.transform = "translateY(20px)";
    el.style.transition = "opacity 0.5s ease, transform 0.5s ease";
    observer.observe(el);
  });

// Add CSS class to trigger the animation
document.head.insertAdjacentHTML("beforeend", `
  <style>
    .visible { opacity: 1 !important; transform: translateY(0) !important; }
  </style>
`);
