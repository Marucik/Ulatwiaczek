var przyciski = document.getElementsByClassName('button'),
    drop1 = document.getElementsByClassName('drop_down1'),
    drop2 = document.getElementsByClassName('drop_down2'),
    drops = [drop1, drop2],
    checker = [true, true];

function clicker(x) {
  if (checker[x] === true){
    for (var i = 0; i < drops[x].length; i++) {
      drops[x][i].style.display = "none";
    }
    checker[x] = false;
  }else {
      for (var i = 0; i < drops[x].length; i++) {
        drops[x][i].style.display = "flex";
    }
    checker[x] = true;
  }
}

clicker(0);
clicker(1);

przyciski[0].addEventListener("click", function(){
  if(checker[1] === true){
    clicker(0);
    clicker(1);
  }else {
    clicker(0);
  }
});

przyciski[1].addEventListener("click", function(){
  if(checker[0] === true){
    clicker(1);
    clicker(0);
  }else {
    clicker(1);
  }
});
