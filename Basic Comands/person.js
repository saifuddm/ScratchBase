// exporting an object aswell
// const person = {
//     name: "John",
//     age: 30
// }

// exporting a class
class Person {
    constructor(name,age){
        this.name = name
        this.age = age

    }


    greeting(){
        console.log(`My name is ${this.name} and I am ${this.age}`)

    }
}

module.exports = Person