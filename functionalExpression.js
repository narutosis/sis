"use srtict"

let cnst = function (cnst) {
    return function () {
        return cnst;
    };
}

variable = function (variable) {
    return function (x, y, z) {
        if (variable === "x") {
            return x
        } else if (variable === "y") {
            return y
        } else {
            return z
        }
    }
}

let multiply =  function (first, second){
    return function(x, y, z) {
        return first(x, y, z) * second(x, y, z);
    }
}

let add = function (first, second) {
    return function(x, y, z) {
        return first(x, y, z) + second(x, y, z);
    }
}

let divide = function (first, second) {
    return function(x, y, z) {
        return first(x, y, z) / second(x, y, z);
    }
}

let negate = function (first) {
    return function(x, y, z) {
        return -first(x, y, z);
    }
}

let subtract = function (first, second) {
    return function(x, y, z) {
        return first(x, y, z) - second(x, y, z);
    }
}


for(i=0; i<=10; i++) {
    let expr = add(
        subtract(multiply(
        variable("x"),
            variable("x")), multiply(
            cnst(2),
                variable("x"))),
        cnst(1))
    console.log(expr(i, 0, 0));
}