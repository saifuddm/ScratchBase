const EventEmitter = require('events')

// Create emitter class
class MyEmitter extends EventEmitter {}

// Init object
const myemitter = new MyEmitter()

// Event Listener
myemitter.on('event',()=>console.log('Event Fired'))

// Init event
myemitter.emit('event')