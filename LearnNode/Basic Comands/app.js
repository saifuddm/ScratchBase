// This import is using bable (Common JS)
const mymodule = require('./tutorial')
const Person = require('./person')

// This import is ES6 (Not in Node yet)
// import Person form './Person'


console.log(mymodule(1,1))
const Person1 = new Person('John Doe',30)
Person1.greeting()