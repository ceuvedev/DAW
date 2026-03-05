

# 1. Realitza un script que demane a l’usuari números sencers fins que l’usuari indrodueixca el número 0.

$num1 = Read-Host "Escriu un num: "
Write-Host "Tu num es: $num1"
while ($num1 -eq 0) {
Write-Host "Tu num es: $num1"
}
Write-Host "Saliste del bucle, adios!"

# 2. Realitza un script que demane a l’usuari números reals fins que l’usuari indrodueixca el caràcter “q”. Una vegada acabe ha de mostrar el nombre de valors, la suma total i la mitja.

$contador = 0
$suma = 0

do {

$num1 = Read-Host "Escriu un num: (o q per a eixir)"

if ($num1 -eq "q") {
        break  # Salimos del do
    }
$suma = $suma + $num1
$contador++

} while ($num1 -ne "q")


$mitja = ($suma/$contador)
Write-Host "Resultado final:"
Write-Host "Contador: $contador"
Write-Host "Suma: $suma"
Write-Host "Mitja: $mitja"

# 3. Fes un script demane a l’usuari un número sencer vàlid i a continuació mostre el factorial d’eixe número. El factorial de 3 és representa i es resol aixi: 3! = 3x2x1 = 6. Has de validar quin és el màxim valor a introduir per l’usuari.

$entrada = Read-Host "Escriu un num: (del 1 al 20)"

if ($entrada -match "^[0-9]+$") {
    # Convertir a número después de validar
    $num1 = [int]$entrada
    
    # Calcular factorial
    $factorial = 1
    for ($i = 1; $i -le $num1; $i++) {
        $factorial = $factorial * $i
    }
    Write-Host "Factorial de $num1 = $factorial"
} else {
    Write-Host "Num no validooo"
}

#4 Fes un script que donat un directori, recòrrega el llistat de fills, i determine quin és el fill que ocupa més espai.

$entrada = Read-Host "Posa un directori: "

$midaMaxima = 0

Get-ChildItem -Path $entrada -File | ForEach-Object {
    if ($entrada.Length -gt $midaMaxima) {
        $midaMaxima = $_.Length
        $mesGran = $entrada
    }
}

# Mostrar resultat
Write-Host "`n=== ELEMENT QUE OCUPA MÉS ESPAI ===" -ForegroundColor Green
if ($mesGran) {
    Write-Host "Nom: $($mesGran.Name)"
    Write-Host "Tipus: $(if ($mesGran.PSIsContainer) {'Directori'} else {'Fitxer'})"
    Write-Host "Ruta: $($mesGran.FullName)"
    Write-Host "Mida: $midaMaxima bytes"
    Write-Host "Mida: $([math]::Round($midaMaxima/1MB, 2)) MB"
    Write-Host "Mida: $([math]::Round($midaMaxima/1GB, 2)) GB"
} else {
    Write-Host "El directori està buit"
}

# 5 Menu gastaren la funcio do-while per a fer aquest exercici

$opcio = 0

do {
    Write-Host "`nMenu"
    Write-Host "1. Versió"
    Write-Host "2. Data"
    Write-Host "3. Ajuda"
    Write-Host "4. Notepad"
    Write-Host "5. Eixir"
    
    $opcio = Read-Host "Tria opció"

} while ($opcio -ne 5)


#6. reciclem el codi anterior i usarem un switch case per a fer interactiu el menu
$opcio = 0

do {
    Write-Host "`nMenu"
    Write-Host "1. Versió"
    Write-Host "2. Data"
    Write-Host "3. Ajuda"
    Write-Host "4. Notepad"
    Write-Host "5. Eixir"
    
    switch ($opcio) {
        "1" { versio }
        "2" { fecha }
        "3" { ajuda }
        "4" { notepad }
        default { Write-Host "Opció no vàlida" }
    }

    $opcio = Read-Host "Tria opció"

} while ($opcio -ne 5)


function versio{    
    Get-ComputerInfo | Select WindowsProductName
}
function fecha {  
    Get-Date  
}
function ajuda{    
    Get-Help
}
function notepad{    
    notepad
}

#7 

# Script per comptar serveis al fitxer services

$fitxer = "C:\Windows\System32\drivers\etc\services"

# Comprovar que el fitxer existeix
if (Test-Path $fitxer) {
    $linies = Get-Content $fitxer
    $comptador = 0
    
    foreach ($linia in $linies) {
        if ($linia -match "^\s*[^#]") {
            $comptador++
        }
    }
    
    Write-Host "Nombre total de serveis: $comptador" 
} else {
    Write-Host "Error: El fitxer no existeix" 
}

