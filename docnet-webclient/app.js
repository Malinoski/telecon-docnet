var express = require("express");
var app = express();
var router = express.Router();

var path = __dirname + '/app/';
const PORT = 8002;
const HOST = '0.0.0.0';

router.use(function (req,res,next) {
  console.log("/" + req.method);
  next();
});

router.get("/",function(req,res){
  res.sendFile(path + "index.html");
});

app.use(express.static(path));
app.use("/", router);

app.listen(8002, function () {
  console.log('Web app listening on port '+PORT+'!')  
})
