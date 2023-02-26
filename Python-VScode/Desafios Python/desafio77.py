lista = ('Aprender','Programar','Linguagem','Python','Curso','Gratis','Estudar','Praticar','Trabalhar','Mercado','Programador','Futuro')
for c in lista:
    print(f'\nDentro da palavra {c.upper()} temos',end=' ')
    for p in c:
        if p.lower() in 'aeiou':
            print(p,end=' ')
            