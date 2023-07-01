var keysToMove = document.getElementsByClassName("key_2");
var keys = document.getElementsByClassName("key_1");
var distances = [28, 65, 139, 175, 212, 287, 324, 398, 434, 471, 546, 583, 657, 694, 732, 805, 842, 915, 953, 990, 1064, 1101, 1174, 1212, 1249];
var distancesMediaQuery = [1, 10, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109, 119, 129, 139, 149, 159, 169, 179, 189, 199, 209];
var pianoMenuTopContent = document.getElementsByClassName("piano-menu-top__content")[0];
var pianoMenuTopContentKeys = document.getElementsByClassName("piano-menu-top__content_keys")[0];
var MostRecentKeyTop = document.getElementsByClassName("piano-menu-top__content_keys_most_recent_key_top")[0];
var MostRecentKeyBottom = document.getElementsByClassName("piano-menu-top__content_keys_most_recent_key_bottom")[0];
var allRecentKeys = document.getElementsByClassName("piano-menu-top__content_keys_all_keys")[0];
var pianoMenuItem = document.getElementsByClassName("piano-menu__bottom_item");
var loadedSheetContent = document.getElementsByClassName("loaded_sheet_content")[0];
var loadedSheetAutoplay = document.getElementsByClassName("autoplay_loaded_sheet_button")[0];
var headerMenuImages = document.getElementsByClassName("menu_item_img");
var headerMenuTitles = document.getElementsByClassName("piano-menu__bottom_item_title");
var pianoMenuTop = document.getElementsByClassName("piano-menu-top")[0];
var pianoMenuBottom = document.getElementsByClassName("piano-menu__bottom")[0];
var pianoStartWrapper = document.getElementsByClassName("piano-start__wrapper")[0];

for (let i = 0; i < keysToMove.length; i++) {
    moveDistance = distances[i] + 301 + "px";
    keysToMove[i].style.left = moveDistance;
}

for (let i = 0; i < pianoMenuItem.length; i++) {
    pianoMenuItem[i].addEventListener("mouseover", event => {
        headerMenuImages[i].style.display = "block";
        headerMenuTitles[i].style.color = "#fff";
    });

    pianoMenuItem[i].addEventListener("mouseout", event => {
        headerMenuImages[i].style.display = "none";
        headerMenuTitles[i].style.color = "#939393";
    });
}

document.addEventListener("keydown", event => {
    let note = keyboardNotes[event.key];
    let sound = keyboardSounds[event.key];
    if (!(typeof(note) === 'undefined')) {
        var fileLocation = "../static/keys_mp3/" + sound + ".mp3";
        var audio = new Audio(fileLocation);
        audio.play();
    }

    // White key was pressed
    for (let i = 0; i < keys.length; i++) {
        if (keys[i].innerText == event.key) {
            keys[i].style.backgroundColor = "lightgray";
        }
    }

    // Black key was pressed
    for (let i = 0; i < keysToMove.length; i++) {
        if (keysToMove[i].innerText == event.key) {
            keysToMove[i].childNodes[1].style.backgroundColor = "#000";
        }
    }
});

document.addEventListener("keyup", event => {
    // White key was released
    for (let i = 0; i < keys.length; i++) {
        if (keys[i].innerText == event.key) {
            keys[i].style.backgroundColor = "#fff";
        }
    }

    // Black key was released
    for (let i = 0; i < keysToMove.length; i++) {
        if (keysToMove[i].innerText == event.key) {
            keysToMove[i].childNodes[1].style.backgroundColor = "darkgray";
        }
    }
});

function mediaQuery(x) {
    if (x.matches) { // If media query matches
        pianoMenuTop.style.marginLeft = "3%";
        pianoMenuTop.style.width = "calc(94% + 3px)";
        pianoMenuBottom.style.marginLeft = "3%";
        pianoMenuBottom.style.width = "calc(94% + 3px)";
        pianoStartWrapper.style.marginLeft = "3%";

        for (let i = 0; i < keysToMove.length; i++) {
            moveDistance = distances[i] + 62 + "px";
            keysToMove[i].style.left = moveDistance;
        }
    }
}

var x = window.matchMedia("(max-width: 1500px)");
mediaQuery(x); // Call listener function at run time
x.addListener(mediaQuery);

const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms));

async function autoPlayMusicSheet(sheet) {
    allRecentKeys.innerHTML = sheet;
    for (let i = 0; i < sheet.length; i++) {
        let sound = keyboardSounds[sheet[i]];
        if (typeof(sound) != 'undefined') {
            var fileLocation = "../static/keys_mp3/" + sound + ".mp3";
            var audio = new Audio(fileLocation);
            audio.autoplay = true;
            audio.play();
            await wait(369);
            if (typeof(sheet[i]) != 'undefined') {
                pianoMenuTopContent.style.display = "none";
                pianoMenuTopContentKeys.style.display = "flex";
                MostRecentKeyTop.innerText = sheet[i];
                pianoMenuTopContent.style.display = "none";
                pianoMenuTopContentKeys.style.display = "flex";
            }
        } else {
            // Between notes
            if (sheet[i] == " ") await wait(700);
            // New line
            if (sheet[i] == "<") {
                if (sheet[i + 1] == "b") {
                    await wait(700);
                    i = i + 3;
                }
            }
        }
    }
}

function editMusicSheet(sheet) {
    let musicSheet = musicSheet.substr(2, musicSheet.length - 3);
    return musicSheet.replace(/\\r\\n/g, "<br>");
}

if (!(typeof(musicSheet) == 'undefined') && !(typeof(loadedSheetContent) == 'undefined')) {
    loadedSheetContent.innerHTML = editMusicSheet(musicSheet);

    loadedSheetAutoplay.addEventListener("click", event => {
        autoPlayMusicSheet(loadedSheetContent.innerHTML);
    });
}
