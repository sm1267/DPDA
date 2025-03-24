def dpda_accepts(dpda, cuvant):
    # stiva initiala conține simbolul initial al stivei
    stack = [dpda['simbol_stiva']]
    current_state = dpda['stare_initiala']

    # citim fiecare simbol din cuvânt
    for simbol in cuvant:
        if not stack:
            return False  # daca stiva este goala cuvantul nu este acceptat
        top_stack = stack.pop()  # scoatem simbolul de pe varful stivei
        # verificam daca exista o tranzitie pentru combinatia (current_state, symbol, top_stack)
        if (current_state, simbol, top_stack) in dpda['tranzitii']:
            new_state, new_stack_symbols = dpda['tranzitii'][(current_state, simbol, top_stack)]
            current_state = new_state
            stack.extend(reversed(new_stack_symbols))  # adaugam noile simboluri pe stiva
        else:
            return False  # daca nu exista tranzitie cuvantul nu este acceptat

    # citim simboluri (tranziții fără citire de simboluri de intrare)
    while stack and (current_state, '', stack[-1]) in dpda['tranzitii']::
        top_stack = stack.pop()
        new_state, new_stack_symbols = dpda['tranzitii'][(current_state, '', top_stack)]
        current_state = new_state
        stack.extend(reversed(new_stack_symbols))

    # verificam daca am ajuns intr-o stare de acceptare
    return current_state in dpda['stari_finale']



dpda = {
    'tranzitii': {
        ('1', 'a', 'A'): ('1', ('A', 'A')),
        ('1', 'a', 'Z'): ('1', ('A', 'Z')),
        ('1', 'b', 'A'): ('2', ()),
	('2', 'b', 'A'): ('2', ()),
	('2', '', 'Z'): ('3', ('Z',)),
    },
    'stare_initiala': '1',
    'simbol_stiva': 'Z',
    'stari_finale': {'3'}
}


if dpda_accepts(dpda,"aaabbb"):
    print("DA")
else:
    print("NU")

