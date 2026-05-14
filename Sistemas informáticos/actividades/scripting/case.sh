#!/bin/bash

read -p "Tria una opció: (a, b, c)" opcio

case $opcio in
    a)
    echo "Primera";;
    b)
    echo "Segunda";;      
    c)
    echo "Tercera";;
    *)
    echo "Elecció incorrecta" ;;
esac