!/bin/bash

#5.

read -p "Escribe un numerito negativo, nunca positivo!" numero

while [ $numero -gt 0 ]; do
    echo "Sigue esforzandote!"
    read -p "Escribe un numerito!" numero
done
echo "Saliste del bucle, Adios!"

6. while

read -p "Escribe un numerito y te saco la tabla de multiplicar" numero2

i=0
echo "Tabla del $numero2"
while [[ $i -le 10 ]]; do

    echo "$numero2 x $i = $((numero2 * i))"
    ((i++));
done

7. for

read -p "Escribe un numerito y te saco la tabla de multiplicar" numero3

for ((i=0; i<=10; i++))
do 
echo "$numero3 x $i = $((numero3 * i))"
done

8. estaono está

read -p "Dime el usuari que vols buscar: " usuari

who | grep $usuari
if [[ $? -eq 0 ]]; then
    echo "Se ha encontrado l'usuari $usuari en el sistema"
    exit 0
else 
    echo "NO se ha trobat res"
    exit 1
fi