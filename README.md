# Ułatwiaczek </br>Bo ułatwia / jasne jak słońce! [ ͡° ͜ʖ ͡°]

### Uruchamianie aplikacji na komputerze lokalnym:

Żeby uruchomić Ułatwiaczka lokalnie, musimy wykonać następujące kroki:

1. Pobieranie potrzebnych materiałów:
    1. Klonujemy branch `master` z [repozytorium](https://github.com/Marucik/Ulatwiaczek/tree/master "Github/Ułatwiaczek/master");
    2. Pobieramy [Python](https://www.python.org/downloads/ "Pobierz Pythona")'a w wersji 3.6.0 dla naszego systemu;
    3. Pobieramy [Node.js](https://nodejs.org/en/download/ "Pobierz Node.js") w wersji 7.5.0;
2. Sprawdzenie poprawosci instalacji Python'a oraz Node.js:
    1. Otwieramy konsolę i wpisujemy `python --version`. Powinniśmy ujrzeć:</br>      
      ![wersja Python'a](http://i.imgur.com/TS7IDKs.png)    
    2. Otwieramy konsolę i wpisujemy `node --version`. Powinniśmy ujrzeć:</br>    
      ![wersja Node.js](http://i.imgur.com/lBObH1F.png)
3. Przygotowanie wirtualnego środowiska:
    1. Przechodzimy w konsoli do głównego folderu projektu (można go poznać po plikach `manage.py, requirements.txt, README.md`;

      ![System plików](http://i.imgur.com/aZC3dvA.png)
      
    2. Wpisujemy komendę `pip install virtualenv`. </br>Po zakończeniu instalacji sprawdzamy czy wszystko zainstalowało się poprawnie komendą `virtualenv --version`;</br>		
      ![Wersja virtualenv](http://i.imgur.com/2PFUcnL.png)
      
    3. Tworzymy wirtualne środowisko `virtualenv virtualenv`  i aktywujemy go:</br>
        W przypadku Linuxa: `source virtualenv/bin/activate`</br>
	W przypadku Windowsa: `virtualenv\Scripts\activate`</br>

    4. Możemy teraz uruchomić wirtualne środowisko przygotowane dla Ułatwiaczka.</br>
    Żeby "wejść" do tego środowiska wpisujemy w konsolę (będąc w głównym folderze projektu): `virtualenv\Scripts\activate`.</br>
		Po wykonaniu tej komendy nasza konsola powinna wyglądać następująco:</br>		
    	![Wejscie do virtualenv](http://i.imgur.com/6TiPhxi.png)

    	Należy pamiętać, że musimy wejść do naszego wirtualnego środowiska za każdym razem jeżeli chcemy uruchomić naszą aplikację lokalnie ( ͡^ ͜ʖ ͡^).

    5. Następnie instalujemy Python'ową paczkę, która zawiera między innymi [Django](https://www.djangoproject.com/ "Strona Django"), na którym oparty jest nasz projekt.</br>
    Paczkę instalujemy poleceniem `pip install -r requirements.txt`. Po skończeniu pobierania sprawdzamy czy Django zainstalował się poprawnie poleceniem `python -m django --version`</br></br>
		![Sprawdzanie wersji Django](http://i.imgur.com/yDD5C37.png)
    6. Teraz instalujemy [Gulp](http://gulpjs.com/ "Strana Gulp'a")'a i potrzebne do jego działania moduły.</br>
  	Będąc w głównym folderze projektu wpisujemy w konsolę: `npm install`. NodePackageManager automatycznie zainstaluje za nas potrzebne moduły które są zawarde w pliku `package.json`.
    7. Po instalacji modułów `npm` w konsolę wpisujemy komendę: `gulp compile_css`.</br>
  	Powinniśmy ujrzeć taki widok:</br>      
        ![Kompilowanie plików scss](http://i.imgur.com/dRAfQxz.png)
4. Uruchomienie serwera i dodawanie danych:</br>
Po wykonaniu poprzednich kroków, wreszcie możemy uruchomić naszą aplikację na lokalnym serwerze! Żeby to zrobić, wykonujemy następujące kroki:
  	1. W konsoli [w której mamy uruchomione wirtualne środowisko!] otwartej w głównym folderze projektu (poznamy go po pliku `manage.py`) wpisujemy komendę: `python manage.py runserver`</br>
  	Powinniśmy zobaczyć coś takiego:</br>
  		![Uruchomiony serwer](http://i.imgur.com/eZjIvZu.png)
  	2. Uruchamiamy przeglądarkę i wpisujemy adres: `127.0.0.1:8000`. Powinna nam się pokazać strona Ułatwiaczka.
