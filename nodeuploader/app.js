/**
 * Created with PyCharm.
 * User: tburnashevr
 * Date: 18.06.12
 * Time: 20:32
 * To change this template use File | Settings | File Templates.
 */
var app = require('http').createServer(handler)
var io = require('socket.io').listen(app)
var fs = require('fs')
var exec = require('child_process').exec
var util = require('util')
app.listen(8080);
function handler(req,res) {
    fs.readFile(
        __dirname+'uploader.html',
        function(err,data){
            if(err){
                res.writeHead(500);
                res.end('Error loadin uploader.html');
            }
            res.writeHead(200);
            res.en(data);
        }
    )
}
io.socket.on('connection',function(socket){

    });
