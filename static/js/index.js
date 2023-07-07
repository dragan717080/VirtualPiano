const blackKeys = document.getElementsByClassName('black-key');
const whiteKeys = document.getElementsByClassName('white-key');
const distances = [28, 65, 139, 175, 212, 287, 324, 398, 434, 471, 546, 583, 657, 694, 732, 805, 842, 915, 953, 990, 1064, 1101, 1174, 1212, 1249];
const distancesMediaQuery =[-9, 17, 66, 91, 114, 167, 192, 241, 266, 291, 341, 366, 416, 441, 467, 517, 541, 593, 617, 642, 690, 717, 767, 791, 816];
const pianoMenuTopContent = document.getElementsByClassName('piano-menu-top__content')[0];
const pianoMenuTopContentKeys = document.getElementsByClassName('piano-menu-top__content_keys')[0];
const pianoMenuItem = document.getElementsByClassName('piano-menu-bottom_item');
const headerMenuImages = document.getElementsByClassName('menu_item_img');
const headerMenuTitles = document.getElementsByClassName('piano-menu-bottom_item_title');
const pianoMenuTop = document.getElementsByClassName('piano-menu-top')[0];
const pianoMenuBottom = document.getElementsByClassName('piano-menu-bottom')[0];
const pianoStartWrapper = document.getElementsByClassName('piano-start__wrapper')[0];

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
    const note = keyboardNotes[event.key];
    const sound = keyboardSounds[event.key];
    if (typeof(note) !== 'undefined') {
        var fileLocation = `../static/keys_mp3/${sound}.mp3`;
        new Audio(fileLocation).play();
    }

    // White key was pressed
    for (let i = 0; i < whiteKeys.length; i++) {
        if (whiteKeys[i].innerText == event.key) {
            whiteKeys[i].style.backgroundColor = 'lightgray';
        }
    }

    // Black key was pressed
    for (let i = 0; i < blackKeys.length; i++) {
        if (blackKeys[i].innerText == event.key) {
            blackKeys[i].childNodes[1].style.backgroundColor = '#000';
        }
    }
});

document.addEventListener('keyup', event => {
    // White key was released
    for (let i = 0; i < whiteKeys.length; i++) {
        if (whiteKeys[i].innerText == event.key) {
            whiteKeys[i].style.backgroundColor = '#fff';
        }
    }

    // Black key was released
    for (let i = 0; i < blackKeys.length; i++) {
        if (blackKeys[i].innerText == event.key) {
            blackKeys[i].childNodes[1].style.backgroundColor = '#313131';
        }
    }
});

function handleMediaQueryChange(x) {
    const toMove = x.matches ? ['2%', 'calc(95% + 7px)', 62] : ['15%', '1369px', 301];
    const arr = x.matches ? distancesMediaQuery : distances;

    [pianoMenuTop, pianoMenuBottom, pianoStartWrapper].forEach(element =>
        element.style.marginLeft = toMove[0]);

    [pianoMenuTop, pianoMenuBottom].forEach(element => 
        element.style.width = toMove[1]);

    for (let i = 0; i < blackKeys.length; i++) {
        blackKeys[i].style.left = `${arr[i] + toMove[2]}px`;
    }
}

const mediaQuery = window.matchMedia('(max-width: 1500px)');
handleMediaQueryChange(mediaQuery); // Call listener function at run time
mediaQuery.addEventListener('change', handleMediaQueryChange);
