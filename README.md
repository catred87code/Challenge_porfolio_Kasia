# Zadanie 1: konfiguracja oprogramowania
## Podzadanie 1: Dlaczego zdecydowałam się

Zdecydowałam się na udział w wyzwaniu, gdyż chciałam zrozumieć na czym polega testowanie automatyczne, dostać przedsmak jak realnie wygląda ta praca i przekonać się robiąc praktyczne zadania, czy to jest ścieżka dla mnie. Aktualnie pracuję w firmie BI w suporcie technicznym i na co dzień też czasem muszę testować nasz produkt, jeśli zgłaszane są przez klientów jakieś problemy. 

Od stycznia robię kurs CS50x i odkryłam w sobie zamiłowanie do rozwiązywania problemów, główkowania i debuggowania. Pragnę się przebranżowić, a ponieważ "ponoć" testowanie ma niższy próg wejście do IT, chciałam się przekonać czy to mi się podoba i czy znajdę taką samą zajawkę jak w przypadku podstaw programowania z CS50x i zadecydować w naukę czego dalej inwestować czas i energię. 

# Zadanie 2: selektory 

###### Sign in button

//button\
//* [@id="__next"]/form/div/div[2]/button\
//* [@type="submit"]\
//* [@id="__next"]/form/div//child::button

###### Label for login 

//* [@id="login-label"]\
//form//div//div[1]/label\
//label[text()="Login"]


###### Input for login

//* [@id="login"]\
//input[@name="login"]\
//form//div//div[1]/div[1]/input

###### Label for password 

//* [@id="password-label"]\
//label[starts-with(@for, "pass")]\
//form//div//div[2]/label

###### Input for password

//* [@id="password"]\
//* [@name="password"]\
//form//div//div[1]/div[2]//child :: input

###### Input for changing language

//* [@id="__next"]/form/div/div[2]/div/input\
//input[contains(@class, "nativeInput")]\
//form/div/div[2]//input 