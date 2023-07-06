const changeHover = document.getElementsByClassName('changetodoonhover');
const registerLoginLink = document.getElementById('register-login-link');
const darkOrange = '#ff8300';

for (let i = 0; i < changeHover.length; i++) {
    changeHover[i].addEventListener('mouseover', event => {
        toggleStyles(changeHover[i], darkOrange, '#000');
    });

    changeHover[i].addEventListener('mouseout', event => {
        toggleStyles(changeHover[i], '#000', darkOrange);
    });
}

function toggleStyles(element, backgroundColor, color) {
    element.style.backgroundColor = backgroundColor;
    element.style.color = color;
    if (element.innerText === 'Register / Login') {
        registerLoginLink.style.color = color;
    }
}

const linkSocials = document.getElementsByClassName('link_socials');
linkSocials[0].style.marginLeft = '0';
var imgOriginalSources = [];
var imgOriginalNames = [];
var imgOriginalExtensions = [];

Array.from(linkSocials).forEach((link, i) => {
    const src = link.getAttribute('src');
    const [name, extension] = src.split('.');

    imgOriginalSources.push(src);
    imgOriginalNames.push(name);
    imgOriginalExtensions.push('.' + extension);

    link.addEventListener('mouseover', () => {
        link.setAttribute('src', imgOriginalNames[i] + '-orange' + imgOriginalExtensions[i]);
    });

    link.addEventListener('mouseout', () => {
        link.setAttribute('src', imgOriginalSources[i]);
    });
});

const linkPlay = document.getElementById('link_play').childNodes[1];
const linkHow = document.getElementById('link_how').childNodes[1];
const linkAbout = document.getElementById('link_about').childNodes[1];
const isIndex = window.location.href.endsWith('/');
const prefix = isIndex ? '' : '/';
const socialLinks = ['#piano', '#piano__hints', '#piano-info__title'];

[linkPlay, linkHow, linkAbout].forEach((link, i) => {
    link.href = prefix + socialLinks[i];
});
