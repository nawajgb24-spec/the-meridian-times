"use strict";

/* ===========================
   THE MERIDIAN TIMES
   MAIN JAVASCRIPT
=========================== */

document.addEventListener("DOMContentLoaded", () => {

    initSearch();

    initScrollTop();

    initDarkMode();

});


/* ===========================
   SEARCH
=========================== */

function initSearch() {

    const input = document.querySelector(
        ".search-box input"
    );

    if (!input) return;

    input.addEventListener(
        "keyup",
        function () {

            const value =
                this.value.toLowerCase();

            document
                .querySelectorAll(
                    ".news-card"
                )
                .forEach(card => {

                    const text =
                        card.innerText.toLowerCase();

                    card.style.display =
                        text.includes(value)
                            ? ""
                            : "none";

                });

        }
    );

}


/* ===========================
   SCROLL TO TOP
=========================== */

function initScrollTop() {

    const button =
        document.createElement("button");

    button.innerHTML = "↑";

    button.className = "scroll-top";

    document.body.appendChild(button);

    button.onclick = () => {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    };

    window.addEventListener(
        "scroll",
        () => {

            button.style.display =
                window.scrollY > 400
                    ? "block"
                    : "none";

        }
    );

}


/* ===========================
   DARK MODE
=========================== */

function initDarkMode() {

    const saved =
        localStorage.getItem(
            "theme"
        );

    if (saved === "dark") {

        document.body.classList.add(
            "dark-mode"
        );

    }

}
