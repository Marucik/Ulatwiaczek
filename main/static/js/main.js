var przyciski = document.getElementsByClassName('button'),
    drops = document.getElementsByClassName('drop_down'),
    visible = [false, false];

function clicker(x) {
  if (visible[x] === false){
    drops[x].style.display = "flex";
    visible[x] = true;
  }else {
    drops[x].style.display = "none";
    visible[x] = false;
  }
}

przyciski[0].addEventListener("click", function(){
  if(visible[1] === true){
    clicker(0);
    clicker(1);
  }else {
    clicker(0);
  }
});

przyciski[1].addEventListener("click", function(){
  if(visible[0] === true){
    clicker(1);
    clicker(0);
  }else {
    clicker(1);
  }
});
