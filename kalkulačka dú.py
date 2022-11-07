Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Vítejte v kalkulačce\n")
Vítejte v kalkulačce

>>> prvni_cislo=float(input("Zadejte prvni cislo:"))
Zadejte prvni cislo:6
>>> druhe_cislo=float(input("Zadejte druhé číslo:"))
Zadejte druhé číslo:9
>>> print("Součet",prvni_cislo + druhe_cislo)
Součet 15.0
>>> print(rozdíl",prvni_cislo - druhe_cislo)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print(rozdíl" ,prvni_cislo - druhe_cislo)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("Rozdíl",prvni_cislo - druhe_cislo)
...       
Rozdíl -3.0
>>> print("Součin", prvni_cislo * druhe_cislo)
...       
Součin 54.0
>>> print("Podíl",prvni_cislo / druhe_cislo)
...       
Podíl 0.6666666666666666
>>> input("\nDěkuji za použití kalkulačky, aplikaci ukončíte libovolnou klávesou.")
...       

