window.onscroll = function() {
    var nav = document.getElementsByTagName('nav')[0];
    nav.classList.toggle('sticky', window.scrollY > 0);
}

window.onload = function() {
    window.scrollTo(0, 0);
}