let canvas;
let context;

let fpsInterval = 100 / 30;
let now;
let then = Date.now();


let particles = [];



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


    let p = {
        x : 250,
        y : 150,
        size : 10,
        xChange : randint(-10, 10),
        yChange : randint(-10, 10)
    };
    particles.push(p);



    context.clearRect(0, 0, canvas.width, canvas.height);
    context.fillStyle = "yellow";
    for (let p of particles) {
        context.fillRect(p.x, p.y, p.size, p.size);
    }
    for (let p of particles) {
    p.x = p.x + p.xChange; 
    p.y = p.y + p.yChange;
    p.yChange = p.yChange + 1.5
    }

}


function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}









