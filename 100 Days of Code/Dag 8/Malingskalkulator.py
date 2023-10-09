
#Funksjon som regner ut hvor mange spann med maling som er nødvendig for å male et visst areal

høyde_vegg = float(input("Hvor høyt er det under taket? "))
bredde_vegg = float(input("Hvor bredt er rommet? "))
dekkningsgrad = float(input("Hvor mange kvadratmeter dekkes av et malingspann? "))

#Funksjon med tre parametere som tar imot tre argumenter
def maling_kvm(høyde, bredde, dekkning):
    antall_spann = (høyde * bredde) / dekkning
    opprundet = round(antall_spann)
    print(f"Du vil trenge {opprundet} antall spann for å male veggen din :)")

#Test av funksjon ved bruk av keyword arguments
maling_kvm(høyde=høyde_vegg, bredde=bredde_vegg, dekkning=dekkningsgrad)

#Test av funksjon med ren input
maling_kvm(2,4,5)