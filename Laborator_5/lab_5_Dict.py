user_dict = {"Tema": "Programarea C++",
             "Linie cu #": "directive preprocesor",
             "Functia main()": "punctul de unde incepe programul, se apeleaza cind lansam programul",
             "Constanta": "are un tip şi o valoare fixă pe toată durata execuţiei programului",
             "Variabile": "valoarea păstrată în locaţiile memoriei se poate modifica în cursul execuţiei programului",
             "Expresii aritmetice": "sunt cele care efectuează operaţii aritmetice având ca rezultat un număr",
             "Expresii logice": "valoarea unei expresii logice reprezintă valoarea de adevăr a expresiei aferente",
             "cin": "flux de date de intrare",
             "cout": "flux de date de ieşire",
             "if": "instructiune decizionala (conditionala)"}

# printam dictionarul
# for key, value in user_dict.items():
#     print("'", key, "' -", value)

# intoarce o copie a dictionarului
# user_dict_2 = user_dict.copy()
# for key, value in user_dict_2.items():
#     print("'", key, "' -", value)

# - intoarce valoarea cheii , daca nu gaseste nu da exceptie dar intoarce valoarea None
# print(user_dict.get("cout"))

# intoarce valorile perechilor
# print(user_dict.items())

# intoarce cheile din dictionar
# print(user_dict.keys())

# sterge cheia si intoarce valoarea
# print(user_dict.pop("if"))
# print(user_dict)

# sterge si intoarce perechea. Daca dictionarul e gol intoarce exceptia KeyError
# print(user_dict.popitem())
# print(user_dict)

# intoarce valoarea cheii dar daca nu o gaseste, nu da exceptie, dar creeaza cheie cu valoarea none
# print(user_dict.setdefault("Temaa"))

# actualizeaza dictionarul,adaugand perechea (cheie, valoare) din other. Cheile existente se suprascriu.
# intoarce None (nu este dictionar nou!).
# print(user_dict.update())

# intoarce valorile din dictionar
# print(user_dict.values())

# curata dictionarul
# user_dict.clear()
# print(user_dict)
