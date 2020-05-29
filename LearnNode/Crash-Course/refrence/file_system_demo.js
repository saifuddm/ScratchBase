const fs = require('fs')
const path = require('path')

// Create folder
fs.mkdir(path.join(__dirname,'test'),{},err => {
    if (err) throw err;
    console.log('Folder Created..')
})

// Create and write to file
// Overwrites files if it exists
fs.writeFile(path.join(__dirname,'./','hello.txt'),
'Hello World',
err => {
    if (err) throw err;
    console.log('Folder Created..')

    // File Append
    fs.appendFile(path.join(__dirname,'./','hello.txt'),
    'Love Node.js',
    err => {
        if (err) throw err;
        console.log('File Appended..')
    })
})

// Read File
fs.readFile(path.join(__dirname,'./','hello.txt'),'utf8', (err,data) => {
    if (err) throw err;
    console.log(data)
})

// File Rename
fs.rename(path.join(__dirname,'./','hello.txt'),path.join(__dirname,'./','helloWorld.txt'), (err,data) => {
    if (err) throw err;
    console.log('File Renamed')
})