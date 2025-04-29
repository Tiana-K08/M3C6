1. [¿Para qué usamos Clases en Python?](#para-qué-usamos-clases-en-python)
2. [¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?](#qué-método-se-ejecuta-automáticamente-cuando-se-crea-una-instancia-de-una-clase)
3. [¿Cuáles son los tres verbos de API?](#cuáles-son-los-tres-verbos-de-api)
4. [¿Es MongoDB una base de datos SQL o NoSQL?](#es-mongodb-una-base-de-datos-sql-o-nosql)
5. [¿Qué es una API?](#qué-es-una-api)
6. [¿Qué es Postman?](#qué-es-postman)
7. [¿Qué es el polimorfismo?](#qué-es-el-polimorfismo)
8. [¿Qué es un método dunder?](#qué-es-un-método-dunder)
9. [¿Qué es un decorador de Python?](#qué-es-un-decorador-de-python)

# ¿Para qué usamos Clases en Python?
&#128204; **Clase** es una plantilla (esquema) para crear objetos que combinan datos (variables) y comportamiento (funciones). Se puede decir que una clase es una forma de describir qué es un objeto y cómo debe comportarse.

Imaginemos que estás creando un juego y tienes personajes. Cada personaje tiene un nombre, salud y la capacidad de atacar. En lugar de describir estos datos una y otra vez, creas una clase llamada *"Personaje"* y luego creas diferentes personajes a partir de ella.
# 
&#128204; **Principales razones por las que usamos clases:**
- *Organización del código*. Las clases ayudan a estructurar el código, haciéndolo más legible y lógico.
- *Reutilización*. Una clase se puede usar muchas veces, creando múltiples objetos con la misma estructura pero con datos diferentes.
- *Encapsulación*. Ocultar la lógica interna de un objeto. Por ejemplo, podemos hacer que otras partes del programa no puedan modificar directamente las variables internas del objeto.
- *Simplificación de sistemas complejos*. Las clases permiten combinar datos y comportamiento en un solo objeto, lo que facilita el diseño de programas complejos.
# 
&#128204; Ejemplo de **sintaxis de una clase** en Python:
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'¡Hola! Mi nombre es {self.name}, tengo {self.age} años.')
```
*class* - palabra clave para crear una clase.
*\_\_init\_\_()* - método especial que se llama al crear un objeto. Sirve para inicializar (asignar valores iniciales) al objeto y se ejecuta automáticamente cuando se crea.
*self* - referencia al propio objeto. Se usa para acceder a las propiedades y métodos dentro de la clase.
*def()* - métodos (funciones) dentro de la clase. Describen lo que el objeto puede hacer.

Ahora podemos crear un objeto (una instancia de la clase):
```
person1 = Person('Tiana', 35)
person2 = Person('Kira', 10)

person1.say_hello()  # ¡Hola! Mi nombre es Tiana, tengo 35 años.
person2.say_hello()  # ¡Hola! Mi nombre es Kira, tengo 10 años.
```
# 
:white_check_mark: **Conclusión**  
Las clases en Python son necesarias para:
- Describir y utilizar fácilmente objetos con propiedades y comportamientos comunes.
- Estructurar, simplificar y reutilizar el código.
- Trabajar en el estilo de programación orientada a objetos.
#
# ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
&#128204; Cuando creas una instancia de una clase en el lenguaje de programación Python (es decir, un objeto basado en esa clase), hay un método especial que se llama automáticamente. Este método se llama **\_\_init\_\_**.

**El método \_\_init\_\_** es una función constructora especial y reservada en Python que inicializa (es decir, configura) un nuevo objeto cuando se crea. En otras palabras, cuando creas un objeto, Python llama automáticamente a \_\_init\_\_, y puedes usarlo para preparar el objeto para su funcionamiento.
#
&#128204; **Un ejemplo**:
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
Ahora podemos crear un objeto:
```
person1 = Person('Tiana', 35)  # creando un objeto

print(person1.name)  # Tiana
print(person1.age)  # 35
```
¿Qué ocurre aquí paso a paso?:
Se declara la clase Person.
Dentro de la clase, se define el método *\_\_init\_\_*, que acepta los parámetros(argumentos) name y age.
Cuando se crea el objeto person1, Python llama automáticamente al método *\_\_init\_\_*, pasándole los valores "Tiana" y 35.
Dentro de *\_\_init\_\_*, estos valores se almacenan en el objeto usando self.name y self.age.
#
:white_check_mark: **Conclusión**  
¿Para qué sirve *\_\_init\_\_*?
- Facilita la creación de objetos con los datos iniciales necesarios.
- Permite configurar el objeto directamente en el momento de su creación.
- Hace que el código sea más legible y predecible.








# ¿Cuáles son los tres verbos de API?

# ¿Es MongoDB una base de datos SQL o NoSQL?

# ¿Qué es una API?

# ¿Qué es Postman?

# ¿Qué es el polimorfismo?

# ¿Qué es un método dunder?

# ¿Qué es un decorador de Python?
