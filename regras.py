header = 'config firewall address'
final = 'end'
with open("subnet.txt","w") as s, open("origem.txt", "r") as g:
    s.write(f'{header}\n')
    for i in g:
        k = i.strip("\n")
        s.write(f'edit adress host_{k}\n')
        s.write(f'set subnet {k} 255.255.255.255\n')
        s.write("next\n")
    s.write(f'{final}')