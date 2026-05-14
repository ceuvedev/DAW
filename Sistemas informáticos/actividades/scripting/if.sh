#!/bin/bash

# if.sh: Script para demostrar el uso de la estructura if en bash

# 1. 
echo "Ingrese un número:"
read NUMERO
if [ $NUMERO -gt 10 ]; then
    echo "Massa gran"
else 
    echo "Nah, es menor que 10"
fi

# 2.

echo "Ingresa un numero:"
read NUMERO2
par=(NUMERO2 % 2)

if [[ $par -eq 0 ]]; then 
    echo "Numero par"
else 
    echo "Numero impar"
fi

#3.Crea un programa COMPROVA que demane un nom i comprove si aquest es troba dins d’un arxiu anomenat LLESTA. {guió i demostració}

echo "Dime una paraula:" 
read paraula
grep $paraula llesta
if [[ $? -eq 0 ]]; then
    echo "Se ha encontrado la palabra $paraula en llesta"
    exit 0
else 
    echo "NO se ha encontrado res"
    exit 1
fi