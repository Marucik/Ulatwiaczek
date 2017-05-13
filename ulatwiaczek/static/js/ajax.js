
(function(){
  var deleteTestButtons = document.querySelectorAll('a[role="button"][data-ajax-role="deleteTest"]'),
    alertElement = document.querySelector('#alert');
  var deleteTest = function (element) {
    var xhttp = new XMLHttpRequest(),
        href = element.getAttribute('href'),
        ajaxResponse = '';
    xhttp.onreadystatechange = function() {
      console.log('Startuje ajaxa');
      if(xhttp.readyState == 4) {
        if(xhttp.status == 200) {
          console.log('zrobilem se zapytanie');
          ajaxResponse = JSON.parse(xhttp.responseText);
          console.log(ajaxResponse);
          if(ajaxResponse.deleted === false) {
            alertElement.innerHTML = '<div class="alert alert-danger" role="alert"><strong>Oh water chicken!</strong> Nie udało się!</div>' + xhttp.getResponse;
            setTimeout(clearAlertBox, 5000);
          } else {
            element.parentElement.parentElement.style.display = "none";
            alertElement.innerHTML = '<div class="alert alert-success" role="alert"><strong>Udało się!</strong> Prawidłowo usunięto test o nazwie ' + ajaxResponse.temat + '.</div>';
            setTimeout(clearAlertBox, 5000);
          }
        } else {
          alertElement.innerHTML = '<div class="alert alert-danger" role="alert"><strong>Błąd!</strong> Komunikacja z serwerem nie teges!</div>' + xhttp.getResponse;
          console.log('Błąd podczas zapytania');
          return;
        }
      }
    }
    xhttp.open("GET", href, true);
    xhttp.send();
  }
  var clearAlertBox = function() {
    alertElement.innerHTML = '';
  }
  for(let i = 0; i < deleteTestButtons.length; i++) {
    deleteTestButtons[i].addEventListener('click', function(ev) {
      ev.preventDefault();
      return deleteTest(ev.target);
    }, false);
  }
})();
