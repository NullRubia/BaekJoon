const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");
let a = parseInt(input[0]);
let b = parseInt(input[1]);
let b1 = b % 10;
let b2 = parseInt((b % 100) / 10);
let b3 = parseInt(b / 100);

console.log(a * b1);
console.log(a * b2);
console.log(a * b3);
console.log(a * b);
