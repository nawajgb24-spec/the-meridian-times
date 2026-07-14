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

/* ===========================
   SCROLL TO TOP BUTTON
=========================== */

.scroll-top{

    position:fixed;

    right:24px;

    bottom:24px;

    width:50px;

    height:50px;

    border:none;

    border-radius:50%;

    background:#c40000;

    color:#fff;

    font-size:22px;

    cursor:pointer;

    display:none;

    box-shadow:0 8px 18px rgba(0,0,0,.25);

    transition:.3s;

    z-index:9999;

}

.scroll-top:hover{

    transform:translateY(-4px);

}

/* ===========================
   DARK MODE
=========================== */

body.dark-mode{

    background:#121212;

    color:#eeeeee;

}

body.dark-mode .site-header{

    background:#1c1c1c;

    border-bottom:1px solid #333;

}

body.dark-mode .news-card{

    background:#1f1f1f;

}

body.dark-mode .news-summary{

    color:#bdbdbd;

}

body.dark-mode .site-footer{

    background:#000;

}

body.dark-mode .search-box input{

    background:#222;

    color:#fff;

    border-color:#444;

}
