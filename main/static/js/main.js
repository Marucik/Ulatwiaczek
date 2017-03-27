

  function usunTest(url) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (xhttp.readyState == 4 && xhttp.status == 200) {
        
        console.log('zrobilem se zapytanie');
        var info = JSON.parse(xhttp.responseText);
        console.log(info);
        console.log(info.deleted);
        if(info.deleted === false){
          document.querySelector('#alert').innerHTML = '<div class="alert alert-danger" role="alert"><strong>Oh water chicken!</strong> Nie udało się!</div>' + xhttp.getResponse;
        } else {
          document.querySelector('#alert').innerHTML = '<div class="alert alert-success" role="alert"><strong>Udało się!</strong> Prawidłowo usunięto test o nazwie ' + info.temat + '.</div>';
        }
      } else {
        //document.querySelector('#alert').innerHTML = '<div class="alert alert-danger" role="alert"><strong>Błąd!</strong> Komunikacja z serwerem zasysa!</div>' + xhttp.getResponse;
        console.log("błąd komunikacji");
      }
    };
    xhttp.open("GET", url + "", true);
    xhttp.send();
  }
