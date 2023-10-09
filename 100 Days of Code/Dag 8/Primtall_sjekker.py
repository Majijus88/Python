
#Funksjon som undersøker om argumentet til parameteret er et primtall

def primetall_sjekker(tall):
    er_primtall = True
    for i in range (2, tall):
        if tall % i == 0:
            er_primtall = False

    if er_primtall:
        print(f"Tallet {tall} ER et primtall")
    else:
        print(f"tallet {tall} ER IKKE et primtall")

#Test av funksjon
primetall_sjekker(16)
primetall_sjekker(23)