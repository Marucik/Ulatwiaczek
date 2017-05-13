var drop = document.querySelectorAll('nav > ul > li > a.dropdownButton');
for (let i = 0; i < drop.length; i++) {
  drop[i].addEventListener('click', () => {
    drop[i].nextElementSibling.classList.toggle("showDropdown");
  });
}
