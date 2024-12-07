//////////////////////////////////////////////////////
// set current year
const yearEl = document.querySelector(".year");
const currentYear = new Date().getFullYear();
console.log(currentYear)
yearEl.textContent = currentYear;

//////////////////////////////////////////////////////
// make mobile navigation work

const btnNavEl = document.querySelector(".btn-mobile-nav");
const headerEl = document.querySelector(".header");

btnNavEl.addEventListener('click', function () {
    headerEl.classList.toggle("nav-open");
});

//////////////////////////////////////////////////////
// sticky navigation
const sectionHeroEl = document.querySelector(".section-hero");
const obs = new IntersectionObserver(
    function (entries) {
        const ent = entries[0];
        console.log(ent);

        if (ent.isIntersecting === false) {
            document.body.classList.add('sticky');
        }

        if (ent.isIntersecting) {
            document.body.classList.remove('sticky');
        }
    },
    {
    // in the viewport
    root: null,
    threshold: 0,
    rootMargin: "-80px",
});
obs.observe(sectionHeroEl);

//////////////////////////////////////////////////////
// fixing flexbox gap property missing in some Safari versions
function checkFlexGap() {
    var flex = document.createElement("div");
    flex.style.display = "flex";
    flex.style.flexDirection = "column";
    flex.style.rowGap = "1px";

    flex.appendChild(document.createElement("div"));
    flex.appendChild(document.createElement("div"));

    document.body.appendChild(flex);
    var isSupported = flex.scrollHeight === 1;
    flex.parentNode.removeChild(flex);
    console.log(isSupported);

    if (!isSupported) document.body.classList.add("no-flexbox-gap");
}

checkFlexGap();

// https://unpkg.com/smoothscroll-polyfill@0.4.4/dist/smoothscroll.min.js


//////////////////////////////////////////////////////

// Check if cookies are already accepted
document.addEventListener('DOMContentLoaded', function () {
    if (!getCookie("cookieConsent")) {
        document.getElementById("cookieConsentBanner").style.display = "block";
    }
});

// Function to manage cookies (shows additional preferences)
function manageCookies() {
    // Logic for showing preferences (essential, analytics, marketing)
    alert("Implement preferences here, like allowing only essential cookies.");
}

// Function to hide the banner
function hideBanner() {
    document.getElementById("cookieConsentBanner").style.display = "none";
}

// Helper function to set a cookie
function setCookie(name, value, days) {
    const d = new Date();
    d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));)
    const expires = "expires=" + d.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

// Helper function to get a cookie
function getCookie(name) {
    const value = "; " + document.cookie;
    const parts = value.split("; " + name + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

// Graphics for neonButton ~ UCSB / Forex
// place the .MP3 recording into the JS folder!
const neonButton = document.querySelector('.neon-button');

neonButton.addEventListener('click', () => {
    const audio = new Audio('CashRegister.mp3');

    audio.play();
});