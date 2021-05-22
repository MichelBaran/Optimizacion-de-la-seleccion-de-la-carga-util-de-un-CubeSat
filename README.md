# Optimizacion-de-la-seleccion-de-la-carga-util-de-un-CubeSat
Aquí se puede acceder a los datos de entrada y los resultados obtenidos en el proyecto de investigación: Optimización de la selección de la carga útil de un CubeSat.

El Excel Conjunto Pareto.xlsx contiene 8 hojas donde se listan los elementos que conforman el Conjunto Pareto.
  * Hoja 1: Conjunto Pareto del algoritmo de Búsqueda Exhaustiva.
  * Hoja 2: Conjunto Pareto del algoritmo NSGA II con 10 Generaciones.
  * Hoja 3: Conjunto Pareto del algoritmo NSGA II con 100 Generaciones.
  * Hoja 4: Conjunto Pareto del algoritmo NSGA II con 250 Generaciones.
  * Hoja 5: Conjunto Pareto del algoritmo NSGA II con 500 Generaciones.
  * Hoja 6: Conjunto Pareto del algoritmo NSGA II con 800 Generaciones.
  * Hoja 7: Conjunto Pareto del algoritmo NSGA II con 1.000 Generaciones.
  * Hoja 8: Conjunto Pareto del algoritmo NSGA II con 10.000 Generaciones.

El Excel Frente Pareto.xlsx contiene 10 hojas donde se listan los valores que conforman el Frente Pareto.
  * Hoja 1: Frente Pareto del algoritmo de Búsqueda Exhaustiva.
  * Hoja 2: Frente Pareto del algoritmo NSGA II con 10 Generaciones.
  * Hoja 3: Frente Pareto del algoritmo NSGA II con 100 Generaciones.
  * Hoja 4: Frente Pareto del algoritmo NSGA II con 250 Generaciones.
  * Hoja 5: Frente Pareto del algoritmo NSGA II con 500 Generaciones.
  * Hoja 6: Frente Pareto del algoritmo NSGA II con 800 Generaciones.
  * Hoja 7: Frente Pareto del algoritmo NSGA II con 1.000 Generaciones.
  * Hoja 8: Frente Pareto del algoritmo NSGA II con 10.000 Generaciones.
  * Hoja 9: Un cuadro comparativo entre la cantidad de soluciones se encontró en cada generación teniendo en cuenta solo las soluciones no dominadas.
  * Hoja 10: Un cuadro comparativo entre la cantidad de soluciones se encontró en cada generación teniendo en cuenta incluso las soluciones dominadas.

El Excel lista_de_componentes.xlsx contiene 11 hojas donde se listan los valores de los componentes con los cuales se trabajará en el presente proyecto.
  * Hoja 1: Listado de ADCS considerados en el trabajo. (id, nombre, costo, masa, volumen, confiabilidad, potencia, web de origen y factor de conversión Euro/Dólar)
  * Hoja 2: Listado de COM considerados en el trabajo. (id, nombre, costo, masa, volumen, confiabilidad, potencia, web de origen y factor de conversión Euro/Dólar)
  * Hoja 3: Listado de EPS considerados en el trabajo. (id, nombre, costo, masa, volumen, confiabilidad, potencia, web de origen y factor de conversión Euro/Dólar)
  * Hoja 4: Listado de OBC considerados en el trabajo. (id, nombre, costo, masa, volumen, confiabilidad, potencia, web de origen y factor de conversión Euro/Dólar)
  * Hoja 5: Listado de PL considerados en el trabajo. 
            (id, nombre, costo, masa, volumen, confiabilidad, potencia, gsd, tamaño de pixel, foco, Rango Espectrales (x1, x2,...,x7), web de origen y factor                      de conversión Euro/Dólar)
  * Hoja 6: Listado de Notaciones utilizadas en la tabla de PL donde hace una conversión de cada X_i a su Rango Espectral correspondiente; Desde x1 hasta x7.
  * Hoja 7: Listado de STR considerados en el trabajo. (id, Factor U, costo, confiabilidad, web de origen y factor de conversión Euro/Dólar)
  * Hoja 8: Listado de Notaciones utilizadas en la tabla de STR donde hace una conversión detallada de cada Factor U a sus rangos de masa y volumen máximos                       soportados.
  * Hoja 9: Un cuadro llamado rent, donde se puede convertir cualquier combinación de Rango Espectral y Resolución Espacial de cada cámara a un valor en unidades                   monetarias equivalente a la rentabilidad estimada de dicha cámara en el proyecto.
  * Hoja 10: Listado de Notaciones utilizadas en la tabla de rent donde hace una conversión directa de cada columna (1,2,...,7) a el Área de aplicación equivalente.
  * Hoja 11: Listado de proveedores y la confiabilidad que tiene cada uno.

 Data-py es la forma vectorial en la que se representaron los datos encontrados en lista_de_componentes.xlsx para su uso con los algoritmos de Búsqueda Exhaustiva y NSGA II. 

GLOSARIO
  * ADCS: Attitude Determination and Control System. - Una de las partes más importantes del CubeSat. En ella, mediante algoritmos y sensores se hará el control del             CubeSat, teniendo en cuenta que en su hábitat natural hay una ingravidez total.

  * EPS: Electrical Power System. - Esta parte de la estructura se encargará de suministrar, transferir y usar la energía.
  
  * OBC: On Board Computer. - Es considerado el cerebro del CubeSat. El OBC controla todos los subsistemas y monitorea el estado de cada subsistema.
  
  * COM: Subsistema de Comunicaciones. - Esta parte de la estructura se encargará de estar en constante comunicación con la Tierra para enviar y recibir información y          órdenes.
  
  * PL: PayLoad. - La carga útil consistirá en cámaras o sensores ópticos.
         * En este proyecto se define que un cubesat puede tener entre 1 y 3 cámaras se divide PL en 3.
              - PL1: La primer cámara elegida que no puede ser un espacio vacío.
              - PL2: La segunda cámara elegida que esta si ya puede ser un espacio vacío.
              - PL3: La tercer cámara elegida que esta también ya puede ser un espacio vacío.
  
  * STR: Estructura. - Es el esqueleto que contendrá los componentes del CubeSat. El tamaño de esta estructura depende del factor de forma necesario para contener los
    componentes: 1 [U], 1.5 [U], 2 [U], 3 [U], 4 [U], 6 [U] hasta incluso de 8 [U].
    El límite máximo se debe a que el enfoque del presente trabajo es en nanosatélites, cuya masa oscila entre 1 [kg] y 10 [kg].

  
