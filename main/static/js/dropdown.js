var drop = document.querySelectorAll('nav > ul > li > a.dropdownButton'),
  dropElements = document.querySelectorAll('nav > ul > li > ol > li'),
  eventy = ['click'];
for (let i = 0; i < drop.length; i++) {
  for (event of eventy) {
    drop[i].addEventListener(event, function(){
      drop[i].nextElementSibling.classList.toggle("showDropdown");
    });
  }
}
/*
console.log(dropElements);
for (let i = 0; i < dropElements.length; i++) {
  dropElements[i].addEventListener('blur', function(){

  });
}
*/