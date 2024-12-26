
# Titulo

Como dijo Silvina, mi tésis consiste en la renovación de un espectrofluorímetro obsoleto para la caracterización de nanopartículas de upconversion.

# 1

Expongo la estructura de la charla

Para contarles lo que hice primero voy a 
Entonces, para contarles lo que hice durante mi tésis primero voy a introducir qué son los materiales fotoluminiscentes y las nanopartículas de upconversion.
Después, les voy a mostrar el espectrofluorímetro que renovamos y los cambios de hardware y software que les hicimos.
En la tercera sección les voy a comentar sobre los protocolos de medición y las verificaciones que hice para asegurarme que el fluorímetro funcionara correctamente.
Por último, antes de las conclusiones, les voy a mostrar una caracterización óptica que hicimos de un lote de UCNPs.

# 2 fotoluminiscencia

## Agregar espectro acá y tiempo de vida

Los materiales fotoluminiscentes son los que absorben luz para luego reemitirla.
El sistema más simple luminiscente es un sistema donde el electrón puede estar en dos niveles de energía, el fundamental con E1 y el excitado con E2. 
Al iluminar al material con una longitud de onda con energía equivalente a la diferencia de energía entre E1 y E2, el electrón pasa al estado excitado, se queda un tiempo en ese estado y luego vuelve a decaer al fundamental, reemitiendo un fotón de la misma longitud de onda.
Bajo la hipótesis de probabilidad de transición constante en el tiempo se puede describir la dinámica de este proceso: la probabilidad de encontrar al electrón en el estado excitado después de iluminar decae exponencialmente con el tiempo y tiene un tiempo característico tau.

# 3 - fotoluminiscencia

Alejándonos un poco del modelo ideal de dos niveles, tenemos un nivel fundamental con E1 y otro excitado con E2, con muchos sub niveles de energía similar por debajo, hasta llegar a E2'.
Lo que puede pasar en este caso es que excitamos al electrón al nivel más alto, luego decae sin emitir luz al nivel más bajo transfiriendo energía por vibraciones por ejemplo a la molécula o átomo, y luego cae al fundamental nuevamente re-emitiendo un fotón, pero esta vez con menor energía con el que se iluminó.
La energía faltante se disipó en las vibraciones de la molécula.
Estas vibraciones afectan también al tiempo de vida medio del material.

# 4 - UCNP

Las UCNP son un tipo de material luminiscente más complejo que los de los ejemplos anteriores.
Están compuestas por matrices cristalinas dopadas con iones lantánidos. 
Que son estos elementos de la tabla periódica y se caracterizan por tener los niveles F libres.
En esta tésis trabajé con UCNPs de fluoruro de ítrio dopadas con erbio e iterbio, acá se puede ver una imagen de ellas.
La particularidad que tienen las UCNP es que absorben luz en el espectro infrarrojo, en particular a 980 nm, y la re-emiten en el espectro visible, es decir convierten fotones de baja energía a fotones de alta energía.
Esta propiedad hace que las nanopartículas tengan potenciales aplicaciones en microscopía como trazadores ópticos y en celdas solares aumentando su eficiencia.

# 5 - UCNP

El principio de funcionamiento de las nanopartículas es el de sensibilizador (en este caso el iterbio) - activador (el erbio).
En este caso, el sensibilizador tiene un primer y único nivel de energía accesible a 980 nm y es el encargado de absorber a los fotones incidentes.
El erbio por otro lado tiene sucesivos valores separados a 980 nm. 
Dado que tanto el iterbio como el erbio son lantánidos, sus transiciones al estado fundamental están prohibidas y por lo tanto sus tiempos de vida son muy largos, del orden de los cientos de microsegundos.
Gracias a esta propiedad, los electrones del erbio se pueden excitar sucesivamente hasta decaer al fundamental desde un nivel más alto de energía, y emitir en el visible.
Hay múltiples mecanismos por los cuales pueden interactuar los iones.
El más común es upconversion por transferencia de energía (o ETU). 
En este mecanismo, un erbio y un iterbio excitados al primer nivel se transfieren energía a través de interacción dipolo-dipolo. 
Esto hace que el iterbio se desexcite y el erbio se excite a un nivel más alto.
Así se ven las ecuaciones dinámicas para un sistema como este.
Es un sistema de muchas ecuaciones diferenciales, una por cada nivel de energía, no lineales debido a las interacciones complejas entre los iones, y con muchos (del orden de 50) parámetros desconocidos, que determinan el tiempo de vida de la transición entre cada estado.

Poder caracterizar un lote de UCNPs implicaría ajustar este modelo para obtener el valor de sus parámetros.
Sin embargo, esto resulta imposible porque 


El sensibilizador se encarga de absorber los fotones de baja energía
Viendo el diagrama de Jablonski de las UCNP

Para caracterizar un material fotoluminiscente hay que medir su espectro de abs y em, y sus tiempos de vida. (todo: esta quizás la puedo mergear con la anterior)

# 6 - UCNP

Matrices cristalinas nanométricas.
Dopadas con lantánidos, Erbio e Iterbio.
Tienen la propiedad particular de absorber fotones de baja energía y emitir de mayor E.
Esto es útil para distintas aplicaciones.
Pero, ¿Cómo sucede esto?

# 7 - UCNP

Sistema sensibilizador - activador.
Interacción Er - Yb, ETU y absorción 