const app = require('express')
const {mongoose } = require('mongoose')
const http = require('http').Server(app)


mongoose.connect('url')

const user = require('./models/userModel')


async function insert(){
    await user.create({
        name:'parth',
        email: 'parthrudy@gamil.com',
  
    })
}

insert();

http.listen(3000, function(){
    console.log("server is running at 3000")
})