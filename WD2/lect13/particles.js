let canvas;
let context;

let fpsInterval = 100 / 30;
let now;
let then = Date.now();
let request_id

let asteroids = [];

let player = {
    x : 0,
    y : 150,
    size : 10
};

let moveLeft = false;
let moveUp = false;
let moveRight = false;
let moveDown = false;

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    window.addEventListener("keydown", activate, false)
    window.addEventListener("keyup", deactivate, false)

    draw();
}


function draw() {
    request_id = window.requestAnimationFrame(draw);
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
        return;
    }
    then = now - (elapsed % fpsInterval)

    if (asteroids.length < 10) {
        let a = {
            x : canvas.width,
            y : randint(0, canvas.height),
            size : randint(5, 15),
            xChange : randint(-3, -1),
            yChange : randint(-1, 1)
        };
        asteroids.push(a);
    }



    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "yellow";
    for (let a of asteroids) {
        context.fillRect(a.x, a.y, a.size, a.size);
    }

    context.fillStyle = "cyan";
    context.fillRect(player.x, player.y, player.size, player.size);
    if (player.x + player.size >= canvas.width) {
        stop("You Win!");
        return;
    }
    for (let a of asteroids) {
        if (player_collides(a)) {
            stop("You Lose!");
            return;
        }
    }


    for (let a of asteroids) {
        if (a.x + a.size < 0) {
            a.x = canvas.width;
            a.y = randint(0, canvas.height);
        }
        else {
            a.x = a.x + a.xChange; 
            a.y = a.y + a.yChange;  
        }
    }
    if (moveRight) {
        player.x = player.x + player.size
    }
    if (moveUp) {
        player.y = player.y - player.size
    }
    if (moveDown) {
        player.y = player.y + player.size
    }
}







function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}


function activate(event) {
    let key = event.key;
    if (key === "ArrowLeft") {
        moveLeft = true;
    } else if (key === "ArrowUp") {
        moveUp = true;
    } else if (key === "ArrowRight") {
        moveRight = true;
    } else if (key === "ArrowDown") {
        moveDown = true;
    }
}

function deactivate(event) {
    let key = event.key;
    if (key === "ArrowLeft") {
        moveLeft = false;
    } else if (key === "ArrowUp") {
        moveUp = false;
    } else if (key === "ArrowRight") {
        moveRight = false;
    } else if (key === "ArrowDown") {
        moveDown = false;
    }
}

function player_collides(a) {
    if (player.x + player.size < a.x ||
        a.x + a.size < player.x ||
        player.y > a.y + a.size ||
        a.y > player.y + player.size) {
        return false;
    } else {
        return true;
    }
}


function stop(outcome) {
    window.removeEventListener("keydown", activate, false);
    window.removeEventListener("keyup", deactivate, false);
    window.cancelAnimationFrame(request_id);
    let outcome_element = document.querySelector("#outcome");
    outcome_element.innerHTML = outcome;

}

