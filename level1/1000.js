const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");
console.log(parseInt(input[0]) + parseInt(input[1]));
