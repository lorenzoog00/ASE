# ASE
Carpeta de GASES 2022 hay: archivos tipo txt que son usados en ONEMINUTE
Carpeta de ONEMINUTE: trabajo de limpieza y manipulación de bases de datos con los datos de diferentes meses investigando temperatura y radiación máxima en diferentes formatos. 
    Dentro de ONEMINUTE hay una carpeta llamada promedios que es donde se juntan gráficas de meses, con histogramas entre otras.
Carpeta redN: Hay 5 carpetas, 4 de estas son para limpiar y acomodar los datos para usarlos en la red neuronal. 
    Dentro de redN está RedNeuronal1, que consta de varios archivos//
        - normalizado, primer intento de normalizar la red
        - normalizado2, segundo intento de normalizar la red
        - excel que se llama param que es la base de datos enorme, fue exportada para ver los datos en excel
        - Red, archivo donde se programó la primera red, con los intentos fallidos del resto de redes. 
        - red_neuronal: red donde está la primera red en limpio
        -redconmax: red neuronal funcional que recibe de input fracvol, radio y espesor. Output coeficiente de absorción y longitud de onda.
        - redmaxinversa: red neuronal casi los errores están muy altos funcional que recibe de input coeficiente de absorción y longitud de onda. Output fracvol, radio y espesor.
        -recreacion_de_graficas que toma fracvol, espesor, longitud de onda y radio para darnos un índice de absorción bastante atinado
