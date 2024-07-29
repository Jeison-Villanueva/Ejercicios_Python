mensaje="hola, estoy aprendiendo python"
nombre="Jeison"
Formacion="ADSO"
edad="17"
estatura="1.78"
peso="76"
#forma de imprimir1
print(mensaje, "mi nombre es:",nombre, "soy de la formación:", Formacion, "Tengo:",edad, "Años", "mido",estatura,"y peso:",peso,"kg")
#forma de imprimir2
print(f"{mensaje}.Mi nombre es:{nombre}, soy de la formacion: {Formacion}, tengo: {edad} años, mido: {estatura}, y peso: {peso} kg")

a=int(input("Ingrese el primer digito: "))
b=int(input("ingrese el segundo digito: "))
Suma= a + b
Resta= a - b
Multiplicacion= a + b
Division_Cociente= a / b
Division_Residuo= a % b
print("el resultado de la suma es: ",Suma,"El resultado de la resta es: ",Resta,"El resultado de la Multiplicacion es: ",Multiplicacion,"El resultado de la Division_cociente es: ",Division_Cociente, "El resultado de la division con residuo es: ",Division_Residuo)

print(f"suma, {Suma}, Resta {Resta}, Multiplicacion {Multiplicacion}, Division_cociente{Division_Cociente}, Division Residuo{Division_Residuo}")