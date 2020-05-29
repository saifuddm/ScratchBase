const url = require('url')

const myUrl = new URL('http://mywebsite.com/hello.html?id=100&status=active')


// Sericalized 
console.log(myUrl.href)
console.log(myUrl.toString())

// Host (Root Domain)
console.log(myUrl.host)

// HostName
// Does not get port
console.log(myUrl.hostname)

// Pathname
console.log(myUrl.pathname)

// Serialized Query
console.log(myUrl.search)

// Params Object
console.log(myUrl.searchParams)

// Add Params
myUrl.searchParams.append('abc','123')
console.log(myUrl.searchParams)

// Loop through Param
myUrl.searchParams.forEach((value,name)=> console.log(`${name} and ${value}`))