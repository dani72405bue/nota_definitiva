# prgrama para calcular la nota definiva 
print ("------------")
print ("--INGRESE LAS  NOTAS--")
print ("------------")

Nc=input ("DIGITE NOTA COGNITIVA ")
Nc=int(Nc)

Np=input ("DIGITE LA NOTA PROCEDIMENTAL ")
Np=int(Np)

Na=input ("DIGITE LA NOTA ACTITUDINAL ")
Na=int(Na)

Aut=input ("DIGITE LA NOTA DE AUTOEVALUACION ")
Aut=int(Aut)

Bi=input ("DIGITE LA NOTA BIMESTRAL ")
Bi=int(Bi)

print("----------")
print("LA NOTA DEFINITIVA ES ")
print("-----------")

ND=input(0.3*Nc+0.3*Np+0.1*Na+0.1*Aut+0.2*Bi)
ND=int(ND)