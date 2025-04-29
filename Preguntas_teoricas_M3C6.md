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
&#128204; **Ejemplo de sintaxis de una clase** en Python:
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
# ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
&#128204; Cuando creas una instancia de una clase en el lenguaje de programación Python (es decir, un objeto basado en esa clase), hay un método especial que se llama automáticamente. Este método se llama *\_\_init\_\_*.

**El método \_\_init\_\_** es una función constructora especial y reservada en Python que inicializa (es decir, configura) un nuevo objeto cuando se crea. En otras palabras, cuando creas un objeto, Python llama automáticamente a *\_\_init\_\_*, y puedes usarlo para preparar el objeto para su funcionamiento.
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
# ¿Cuáles son los tres verbos de API?
&#128204; Cuando los desarrolladores trabajan con una API (ver la pregunta 5: [¿Qué es una API?](#qué-es-una-api)), a menudo interactúan con los datos mediante solicitudes HTTP. Estas solicitudes utilizan "verbos" especiales (métodos) para indicarle al servidor qué se debe hacer con los datos.

Los verbos de API más utilizados son:
- **POST** – crea / escribe nuevos datos. Envía datos al servidor para crear un nuevo objeto.
- **GET** – solicita / obtiene datos. Obtiene información del servidor. No modifica los datos, solo los lee.
- **PUT** – actualiza / sobrescribe datos. Actualiza completamente un objeto existente.

También existen otros métodos HTTP, como **DELETE**, que elimina el objeto especificado del servidor.
![](images/api_metods.jpeg)
Comprender estos verbos es fundamental al trabajar con cualquier API. Es como el “lenguaje” de comunicación entre el cliente (tu aplicación) y el servidor.
#
# ¿Es MongoDB una base de datos SQL o NoSQL?
&#128204; Cuando comienzas a estudiar bases de datos, te encuentras con dos términos principales:
- SQL - lenguaje estructurado de consultas, utilizado en bases de datos relacionales tradicionales para trabajar con tablas que contienen filas y columnas (Ejemplos: MySQL, PostgreSQL, Oracle, SQL Server).
- NoSQL - un enfoque más flexible para almacenar datos. Las bases de datos NoSQL no utilizan tablas. Los datos se almacenan en forma de documentos o colecciones (Ejemplos: MongoDB, Cassandra, Redis, CouchDB).
#
&#128204; **MongoDB es una base de datos NoSQL** orientada a documentos. En lugar de tablas y filas, MongoDB utiliza datos flexibles y no estructurados.
**Estructura de MongoDB:**
- Base de datos → contiene una o varias colecciones
- Colección → contiene muchos documentos
- Documento → es un registro individual en formato JSON
**Ejemplo de un documento en MongoDB:**
```
{
  "name": "Tiana",
  "age": 35,
  "email": "tiana@example.com"
}
```
Para trabajar con MongoDB en Python, necesitaremos la biblioteca ***pymongo***.
Instala la biblioteca ejecutando el comando:
```
pip install pymongo
```
- [Documentación de MongoDB](https://www.mongodb.com/docs/)

















# ¿Qué es una API?

# ¿Qué es Postman?

# ¿Qué es el polimorfismo?

# ¿Qué es un método dunder?

# ¿Qué es un decorador de Python?
