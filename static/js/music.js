const artistsElementButton = document.getElementsByClassName('artists_element_button');
const musicSheetsElementButton = document.getElementsByClassName('music-sheets__element_button');
const artistsLink = document.getElementsByClassName('artists_link');
const musicSheetsLink = document.getElementsByClassName('music-sheets__link');
var genreNames = document.getElementsByClassName('genre-name');
const genreLinks = document.getElementsByClassName('genre_link');
const themeNames = document.getElementsByClassName('genre-name');
const artistNames = document.getElementsByClassName('genre-name');
genreNames = [...Array.from(genreNames), ...Array.from(themeNames), ...Array.from(artistNames)];

document.getElementsByClassName('active')[0].classList.remove('active');
document.getElementsByClassName('header-menu__item')[1].classList.add('active');

for (let i = 0; i < artistsElementButton.length; i++) {
    artistsLink[i].setAttribute('href', `/music/artists?letter=${artistsElementButton[i].innerText}`);
    // To be rewritten using AJAX
    artistsElementButton[i].addEventListener('click', event => {
        console.log('1');
    })
}

for (let i = 0; i < musicSheetsElementButton.length; i++) {
    musicSheetsLink[i].setAttribute('href', `/music/sheets?letter=${musicSheetsElementButton[i].innerText}`);
    musicSheetsElementButton[i].addEventListener('click', event => {
        console.log('1');
    })
}

for (let i = 0; i < genreLinks.length; i++) {
    genreLinks[i].href = `/music/genres/${genreNames[i].innerText}`;
}
