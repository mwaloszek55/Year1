let canvas;
let context;

let x = 250;
let y = 150;
let size = 10;
let xChange = randint(-10, 10);
let yChange = randint(-10, 10);
let fpsInterval = 100 / 30;
let now;
let then = Date.now();



document.addEventListener("DOMContentLoaded", init, false);

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");

    draw();
}


function draw() {
    window.requestAnimationFrame(draw);
    let now = Date.now();
    let elapsed = now - then;
    if (elapsed <= fpsInterval) {
        return;
    }
    then = now - (elapsed % fpsInterval)

    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "yellow";
    context.fillRect(x, y, size, size);
    if (x < 0) {
        xChange = xChange * -1;
    } else if ( x + size > canvas.width) {
        xChange = xChange * -1;
    }
    if (y < 0) {
        yChange = yChange * -1;
    } else if ( y + size > canvas.height) {
        yChange = yChange * -1;
    }


    x = x + xChange; 
    y = y + yChange;


}


function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}









