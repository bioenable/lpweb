(() => {
  const toggle = document.querySelector("[data-nav-toggle]");
  const mobile = document.querySelector("[data-nav-mobile]");
  if (toggle && mobile) {
    toggle.addEventListener("click", () => {
      const open = mobile.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  const reveals = document.querySelectorAll(".reveal");
  if (reveals.length && "IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("in"));
  }

  document.querySelectorAll("[data-inquiry]").forEach((form) => {
    form.addEventListener("submit", (ev) => {
      ev.preventDefault();
      const data = new FormData(form);
      const name = String(data.get("name") || "").trim();
      const phone = String(data.get("phone") || "").trim();
      const interest = String(data.get("interest") || "").trim();
      const destination = String(data.get("destination") || "").trim();
      const message = String(data.get("message") || "").trim();
      if (!name || !phone) {
        alert("Please share your name and WhatsApp number so we can reach you.");
        return;
      }
      const text = [
        "Hi LAUNCHPAD, I want admission guidance.",
        `Name: ${name}`,
        `Phone: ${phone}`,
        interest ? `Interest: ${interest}` : "",
        destination ? `Destination: ${destination}` : "",
        message ? `Message: ${message}` : "",
        `Page: ${location.href}`,
      ]
        .filter(Boolean)
        .join("\n");
      const url = `https://wa.me/918855833244?text=${encodeURIComponent(text)}`;
      window.open(url, "_blank", "noopener");
      const status = form.querySelector("[data-form-status]");
      if (status) {
        status.textContent = "Opening WhatsApp with your inquiry… our counsellor will reply shortly.";
      }
      form.reset();
    });
  });

  document.querySelectorAll("[data-quick-go]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const root = btn.closest("[data-quick-search]");
      if (!root) return;
      const dest = root.querySelector('[name="destination"]')?.value || "";
      const course = root.querySelector('[name="course"]')?.value || "";
      if (dest) location.href = dest;
      else if (course) location.href = course;
      else location.href = "admissions-marketplace.htm";
    });
  });
})();
