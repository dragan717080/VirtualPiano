const keysToMove = document.getElementsByClassName('key_2');
const keys = document.getElementsByClassName('key_1');
const distances = [28, 65, 139, 175, 212, 287, 324, 398, 434, 471, 546, 583, 657, 694, 732, 805, 842, 915, 953, 990, 1064, 1101, 1174, 1212, 1249];
const distancesMediaQuery = [1, 10, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109, 119, 129, 139, 149, 159, 169, 179, 189, 199, 209];
const pianoMenuTopContent = document.getElementsByClassName('piano-menu-top__content')[0];
const pianoMenuTopContentKeys = document.getElementsByClassName('piano-menu-top__content_keys')[0];
const MostRecentKeyTop = document.getElementsByClassName('piano-menu-top__content_keys_most_recent_key_top')[0];
const MostRecentKeyBottom = document.getElementsByClassName('piano-menu-top__content_keys_most_recent_key_bottom')[0];
const allRecentKeys = document.getElementsByClassName('piano-menu-top__content_keys_all_keys')[0];
const pianoMenuItem = document.getElementsByClassName('piano-menu__bottom_item');
const loadedSheetContent = document.getElementById('loaded-sheet__content');
const loadedSheetAutoplayBtn = document.getElementById('autoplay-loaded-sheet-btn');
const headerMenuImages = document.getElementsByClassName('menu_item_img');
const headerMenuTitles = document.getElementsByClassName('piano-menu__bottom_item_title');
const pianoMenuTop = document.getElementsByClassName('piano-menu-top')[0];
const pianoMenuBottom = document.getElementsByClassName('piano-menu__bottom')[0];
const pianoStartWrapper = document.getElementsByClassName('piano-start__wrapper')[0];

function moveKeys() {
    for (let i = 0; i < keysToMove.length; i++) {
        keysToMove[i].style.left = `${distances[i] + 301}px`;
    }
}

moveKeys();

for (let i = 0; i < pianoMenuItem.length; i++) {
    pianoMenuItem[i].addEventListener('mouseover', event => {
        headerMenuImages[i].style.display = 'block';
        headerMenuTitles[i].style.color = '#fff';
    });

    pianoMenuItem[i].addEventListener('mouseout', event => {
        headerMenuImages[i].style.display = 'none';
        headerMenuTitles[i].style.color = '#939393';
    });
}

document.addEventListener('keydown', event => {
    let note = keyboardNotes[event.key];
    let sound = keyboardSounds[event.key];
    if (typeof(note) !== 'undefined') {
        var fileLocation = `../static/keys_mp3/${sound}.mp3`;
        new Audio(fileLocation).play();
    }

    // White key was pressed
    for (let i = 0; i < keys.length; i++) {
        if (keys[i].innerText == event.key) {
            keys[i].style.backgroundColor = 'lightgray';
        }
    }

    // Black key was pressed
    for (let i = 0; i < keysToMove.length; i++) {
        if (keysToMove[i].innerText == event.key) {
            keysToMove[i].childNodes[1].style.backgroundColor = '#000';
        }
    }
});

document.addEventListener('keyup', event => {
    // White key was released
    for (let i = 0; i < keys.length; i++) {
        if (keys[i].innerText == event.key) {
            keys[i].style.backgroundColor = '#fff';
        }
    }

    // Black key was released
    for (let i = 0; i < keysToMove.length; i++) {
        if (keysToMove[i].innerText == event.key) {
            keysToMove[i].childNodes[1].style.backgroundColor = 'darkgray';
        }
    }
});

function mediaQuery(x) {
    if (x.matches) { // If media query matches
        [pianoMenuTop, pianoMenuBottom, pianoStartWrapper].forEach((element) =>
            element.style.marginLeft = '3%');
        [pianoMenuTop, pianoMenuBottom].forEach((element) =>
            element.style.width = 'calc(94% + 3px)');

        for (let i = 0; i < keysToMove.length; i++) {
            keysToMove[i].style.left = `${distances[i] + 62}px`;
        }
    }
}

var x = window.matchMedia('(max-width: 1500px)');
mediaQuery(x); // Call listener function at run time

const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));
