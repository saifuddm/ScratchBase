const mymodule = require('./tutorial')
const Person = require('./person')
console.log(mymodule(1,1))
const Person1 = new Person('John Doe',30)
Person1.greeting()