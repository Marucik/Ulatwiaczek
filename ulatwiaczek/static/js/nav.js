var menuButton = document.querySelector('.menuButton');
var navigation = document.querySelector('nav.main');
var icon = document.querySelector('.menuButton > i')

menuButton.addEventListener('click', () => {
    icon.classList.toggle('fa-bars');    
    icon.classList.toggle('fa-times');
    navigation.classList.toggle('revealNav')
})