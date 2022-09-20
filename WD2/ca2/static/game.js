let canvas;
let context;

let fpsInterval = 100 / 30;
let now;
let then = Date.now();
let request_id

let score = 0
let bullets = [];
let enemies = [];
let bosses = [];
let objects = [];


let xhttp;
let timer = 1


let backgroundImage = new Image();
let tilesPerRow = 16;
let tileSize = 16;

let ammo = 20;
let bullet_Count = 20;

let background = [
    [17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17],
    [17,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,112,113,114,115,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,128,129,130,131,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,144,145,146,147,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,17],
    [17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17]



]


let player = {
    x : 0,
    y : 0,
    width: 32,
    height : 48,
    frameX : 0,
    frameY : 0,
    xChange : 0,
    yChange : 0

};

let hp = 3


let enemyImage = new Image();
let spacebarPressed = false
let playerImage = new Image();
let bossImage = new Image();
let enemyImage1 = new Image();
let enemyImage2 = new Image();
let enemyImage3 = new Image();
let enemyImage4 = new Image();

let moveLeft = false;
let moveUp = false;
let moveRight = false;
let moveDown = false;
let spacebar = false;





document.addEventListener("DOMContentLoaded", init, false);

function init() {
    canvas = document.querySelector("canvas");
    context = canvas.getContext("2d");
    //tileset from https://0x72.itch.io/16x16-dungeon-tileset
    backgroundImage.src = "../static/dungeon1.png"

    window.addEventListener("keydown", activate, false)
    window.addEventListener("keyup", deactivate, false)
    //sprites taken from "Sithjester's RMXP Resources url="https://untamed.wild-refuge.net/rmxpresources.php?characters"
    playerImage.src = "../static/main.png";
    enemyImage1.src = "../static/enemy1.png";
    enemyImage2.src = "../static/enemy2.png";
    enemyImage3.src = "../static/enemy3.png";
    enemyImage4.src = "../static/enemy4.png";
    bossImage.src = "../static/boss.png";

    //creating enemies
    //creates enemies from the right
    for (let i = 0; i < 2; i++) {
        let enemyRight = {
            x : canvas.width - 48,
            y : randint(64, canvas.height - 64),
            width: 32,
            height : 48,
            frameX : 0,
            frameY : 0,
            xChange : -1,
            yChange : 0,
            img : randint(1, 4)
        };
        enemies.push(enemyRight);
    }
    //creates enemies from the left
    for (let i = 0; i < 2; i++) {
        let enemyLeft = {
            x : 48,
            y : randint(64, canvas.height - 64),
            width: 32,
            height : 48,
            frameX : 0,
            frameY : 0,
            xChange : 1,
            yChange : 0,
            img : randint(1, 4)
        };
        enemies.push(enemyLeft);
    }
    //creates enemies from the top
    for (let i = 0; i < 2; i++) {
        let enemyUp = {
            x : randint(64, canvas.width - 64),
            y : 80,
            width: 32,
            height : 48,
            frameX : 0,
            frameY : 0,
            xChange : 0,
            yChange : 1,
            img : randint(1, 4)
        };
        enemies.push(enemyUp);
    }
    //creates enemies from the bottom
    for (let i = 0; i < 2; i++) {
        let enemyDown = {
            x : randint(64, canvas.width - 64),
            y : canvas.height - 80,
            width: 32,
            height : 48,
            frameX : 0,
            frameY : 0,
            xChange : 0,
            yChange : -1,
            img : randint(1, 4)
        };
        enemies.push(enemyDown);
    }

    player.x = (canvas.width / 2) - player.width + 16;
    player.y = (canvas.height / 2) - player.height;

    for (let r = 0; r < 40; r += 1) {
        for (let c = 0; c < 64; c += 1) {
            let tile = background[r][c];
            if (tile === 17) {
                let object = {
                    x : c * tileSize,
                    y : r * tileSize,
                    size : tileSize
                }
                objects.push(object)
            }
        }
    }
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

    //clears canvas
    context.clearRect(0, 0, canvas.width, canvas.height);
    for (let r = 0; r < 40; r += 1) {
        for (let c = 0; c < 64; c += 1) {
            let tile = background[r][c];
            if (tile >= 0) {
                let tileRow = Math.floor(tile / tilesPerRow);
                let tileCol = Math.floor(tile % tilesPerRow);
                context.drawImage(backgroundImage,
                    tileCol * tileSize, tileRow * tileSize, tileSize, tileSize,
                    c * tileSize, r * tileSize, tileSize, tileSize)
            }
        }
    }

    timer = timer - 0.0001

    if (bullet_Count > -1) {
    bulletsCount(bullet_Count)
        if (bullet_Count < 0) {
            score = ScoreMulti(score, bullet_Count, hp, timer)
            stop("You Lose! You ran out of bullets!");
            return;
        }
    }
    hpCount(hp)
    ScoreCount(score)
    //draw enemies
    if (enemies.length !== 0) {
        for (let enemy of enemies) {
            if (enemy.img === 1) {
                enemyImage = enemyImage1
            } else if (enemy.img === 2) {
                enemyImage = enemyImage2
            } else if (enemy.img === 3) {
                enemyImage = enemyImage3
            } else if (enemy.img === 4) {
                enemyImage = enemyImage4
            }
            context.drawImage(enemyImage,
                enemy.width * enemy.frameX, enemy.height * enemy.frameY, enemy.width, enemy.height,
                enemy.x, enemy.y, enemy.width, enemy.height);
            if (enemy.xChange === 1) {
                enemy.frameY = 2;
                enemy.frameX = (enemy.frameX + 1) % 4;
            } else if (enemy.xChange === -1) {
                enemy.frameY = 1;
                enemy.frameX = (enemy.frameX + 1) % 4;
            } else if (enemy.yChange === -1) {
                enemy.frameY = 3;
                enemy.frameX = (enemy.frameX + 1) % 4;
            } else if (enemy.yChange === 1) {
                enemy.frameY = 0;
                enemy.frameX = (enemy.frameX + 1) % 4;
            }

        }
    }
    //draw player
    context.drawImage(playerImage,
        player.width * player.frameX, player.height * player.frameY, player.width, player.height,
        player.x, player.y, player.width, player.height);
    if ((moveLeft || moveRight || moveUp || moveDown) && ! (moveLeft && moveRight) && ! (moveUp && moveDown)) {
        player.frameX = (player.frameX + 1) % 4;
    }

    //draw bullets
    context.fillStyle = "red";
    for (let bullet of bullets) {
        context.fillRect(bullet.x, bullet.y, bullet.width, bullet.height);
    }

    //draw boss
    for (let boss of bosses) {
        context.drawImage(bossImage,
            boss.width * boss.frameX, boss.height * boss.frameY, boss.width, boss.height,
            boss.x, boss.y, boss.width, boss.height);
        if (boss.xChange > 0.5) {
                boss.frameY = 2;
                boss.frameX = (boss.frameX + 1) % 4;
            } else if (boss.xChange < -0.5) {
                boss.frameY = 1;
                boss.frameX = (boss.frameX + 1) % 4;
            } else if (boss.yChange < -0.5) {
                boss.frameY = 3;
                boss.frameX = (boss.frameX + 1) % 4;
            } else if (boss.yChange > 0.5) {
                boss.frameY = 0;
                boss.frameX = (boss.frameX + 1) % 4;
        }
    }




    let playerMovingLeft = true
    let playerMovingRight = true
    let playerMovingUp = true
    let playerMovingDown = true

    
    //player input
    if (moveLeft) {
        for (let object of objects) {
            if (playerObject_collides(object) && (player.x + player.width <= 40) || (player.x + player.width < 0)) {
                player.xChange = 0;
                player.frameY = 1;
                playerMovingLeft = false;
            }
        }
        if (playerMovingLeft) {
            player.xChange = player.xChange - 1
            player.frameY = 1;
        }
    }
    if (moveRight) {
        for (let object of objects) {
            if (playerObject_collides(object) && (player.x + player.width  >= (canvas.width - 10)) || (player.x + player.width > canvas.width)) {
                player.xChange = 0
                player.frameY = 2;
                playerMovingRight = false;
            }
        }
        if (playerMovingRight) {
        player.xChange = player.xChange + 1
        player.frameY = 2;
        }
    }
    if (moveUp) {
        for (let object of objects) {
            if (playerObject_collides(object) && (player.y + player.height <= 50) || (player.y + player.height < 0)) {
                player.yChange = 0;
                player.frameY = 3;
                playerMovingUp = false;
            }
        }
        if (playerMovingUp) {
        player.yChange = player.yChange - 1
        player.frameY = 3
        }
    }
    if (moveDown) {
        for (let object of objects) {
            if (playerObject_collides(object) && (player.y >= (canvas.height - 60)) || (player.y + player.height > canvas.height)) {
                player.yChange = 0
                player.frameY = 0;
                playerMovingDown = false;
            }
        } 
        if (playerMovingDown) {
        player.yChange = player.yChange + 1
        player.frameY = 0
        }
    }
    if (spacebar) {
        let bullet = {
            x : player.x + 6.5,
            y : player.y + (player.height / 2),
            width : 0,
            height : 0,
            xChange : 0,
            yChange : 0
        };
        if (player.frameY === 0){
            bullet.yChange = 6
            bullet.height = 20
            bullet.width = 20
        } else if (player.frameY === 3){
            bullet.yChange = -6
            bullet.height = 20
            bullet.width = 20
        } else if (player.frameY === 2){
            bullet.xChange = 6
            bullet.width = 20
            bullet.height = 20
        } else if (player.frameY === 1){
            bullet.xChange = -6
            bullet.width = 20
            bullet.height = 20
        }
        if (bullets.length <= ammo)  {
            if (spacebarPressed === false) {
                bullets.push(bullet)
                spacebarPressed = true;
                bullet_Count = bullet_Count - 1
                    if (bullet_Count < 0) {
                        score = ScoreMulti(score, bullet_Count, hp, timer)
                        stop("You Lose! You ran out of bullets!");
                        return;
                }
            }
        }
    }


    //updating bullets
    for (let bullet of bullets) {
        movement(bullet)
    };


    //updating player
    movement(player)

    //updating enemies
    for (let enemy of enemies) {
        movement(enemy)
    };

    for (let boss of bosses) {
        movement(boss)
    };

    //player friction (so he doesn't go zoom)
    player.xChange = player.xChange * 0.3
    player.yChange = player.yChange * 0.3

    //boss friction
    if (bosses.length !== 0) {
        for (let boss of bosses) {
            boss.xChange = boss.xChange * 0.5
            boss.yChange = boss.yChange * 0.5
        }
    }


    //collision of player
    for (let enemy of enemies) {
        if (player_collides(enemy)) {
            enemies = enemies.filter(item => item !== enemy)
            hp = hp - 1
            hpCount(hp)
            if (hp === 0) {
                score = ScoreMulti(score, bullet_Count, hp, timer)
                stop("You Lose!");
                return;
            }
            if (enemies.length === 0) {
                let boss = {
                    x : canvas.width,
                    y : canvas.height / 2,
                    width: 40,
                    height : 56,
                    frameX : 0,
                    frameY : 0,
                    xChange : 0,
                    yChange : 0,
                    hp : 5
                }
                boss.y = boss.y - boss.height
                boss.x = boss.x - 80
                bosses.push(boss)
            }
        }
    };
    for (let boss of bosses) {
        if (player_collides(boss)) {
            hp = hp - 3
            hpCount(hp)
            if (hp <= 0) {
                score = ScoreMulti(score, bullet_Count, hp, timer)
                stop("You Lose!");
                return;
            }
        }
    };



    //collision of bullets
    for (let enemy of enemies) {
        for (let bullet of bullets) {
            if (bullet_collides(enemy, bullet)) {
                enemies = enemies.filter(item => item !== enemy)
                bullets = bullets.filter(item => item !== bullet)
                score = score + 10
                if (enemies.length === 0) {
                    let boss = {
                        x : canvas.width,
                        y : canvas.height / 2,
                        width: 40,
                        height : 56,
                        frameX : 0,
                        frameY : 0,
                        xChange : 0,
                        yChange : 0,
                        hp : 5
                    }
                    boss.y = boss.y - boss.height
                    boss.x = boss.x - 80
                    bosses.push(boss)
                }
                if (bullet_Count < 0) {
                    score = ScoreMulti(score, bullet_Count, hp, timer)
                    stop("You Lose! You ran out of bullets!");
                    return;
                    }
                }
            }
        }
    for (let boss of bosses) {
        for (let bullet of bullets) {
            if (bullet_collides(boss, bullet)) {
                    boss.hp = boss.hp - 1
                    bullets = bullets.filter(item => item !== bullet)
                    if (boss.hp === 0) {
                        bosses = bosses.filter(item => item !== boss)
                        score = score + 100
                        score = ScoreMulti(score, bullet_Count, hp, timer)
                        stop("You Win!");
                        return;
                    }
                    if (bullet_Count < 0) {
                        score = ScoreMulti(score, bullet_Count, hp, timer)
                        stop("You Lose! You ran out of bullets!");
                        return;
                    }  
            }
        }
    }
        



        //boss homing in on player
    for (let boss of bosses) {
        if (player.x < boss.x) {
            boss.xChange = boss.xChange + -0.5
        } else if (player.x === boss.x) {
            boss.xChange = 0
        } else {
            boss.xChange = boss.xChange + 0.5
        }
        if (player.y - 8 < boss.y) {
            boss.yChange = boss.yChange + -0.5
        } else if (player.y + 8 === boss.y) {
            boss.yChange = 0
        } else {
            boss.yChange = boss.yChange + 0.5
        }
    }








    //enemies bouncing
    for (let enemy of enemies) {
        if (enemy.x + enemy.width < 0 + 42) {
            enemy.xChange = enemy.xChange * -1
            enemy.yChange = randint(-1, 1)
        } else if (enemy.x + enemy.width > canvas.width - 14) {
            enemy.xChange = enemy.xChange * -1
            enemy.yChange = randint(1, -1)
        } else if (enemy.y + enemy.height < 0 + 42) {
            enemy.yChange = enemy.yChange * -1
            enemy.xChange = randint(1, -1)
        } else if (enemy.y + enemy.width > canvas.height - 34) {
            enemy.yChange = enemy.yChange * -1
            enemy.xChange = randint(1, -1)
        }
    }

    //bullets disappear on impact
    for (let bullet of bullets) {
        if (bullet.x + bullet.width < 0 + 34) {
            bullets = bullets.filter(item => item !== bullet)
            if (bullet_Count <= 0) {
                score = ScoreMulti(score, bullet_Count, hp, timer)
                stop("You Lose! You ran out of bullets!");
                return;
            }
        } else if (bullet.x + bullet.width > canvas.width - 14) {
            bullets = bullets.filter(item => item !== bullet)
            if (bullet_Count <= 0) {
                score = ScoreMulti(score, bullet_Count, hp, timer)
                stop("You Lose! You ran out of bullets!");
                return;
            }
        } else if (bullet.y + bullet.height < 0 + 30) {
            bullets = bullets.filter(item => item !== bullet)
            if (bullet_Count <= 0) {
                score = ScoreMulti(score, bullet_Count, hp, timer)
                stop("You Lose! You ran out of bullets!");
                return;
            }
        } else if (bullet.y + bullet.width > canvas.height - 10) {
            bullets = bullets.filter(item => item !== bullet)
            if (bullet_Count <= 0) {
                score = ScoreMulti(score, bullet_Count, hp, timer)
                stop("You Lose! You ran out of bullets!");
                return;
            }
        }
    }

}










function randint(min, max) {
    return Math.round(Math.random() * (max - min)) + min;
}


function activate(event) {
    let key = event.key;
    let space = event.code
    if (key === "ArrowLeft") {
        moveLeft = true;
    } else if (key === "ArrowUp") {
        moveUp = true;
    } else if (key === "ArrowRight") {
        moveRight = true;
    } else if (key === "ArrowDown" ) {
        moveDown = true;
    } else if (space === "Space") {
        spacebar = true;
    }
}

function deactivate(event) {
    let key = event.key;
    let space = event.code
    if (key === "ArrowLeft") {
        moveLeft = false;
    } else if (key === "ArrowUp") {
        moveUp = false;
    } else if (key === "ArrowRight") {
        moveRight = false;
    } else if (key === "ArrowDown") {
        moveDown = false;
    } else if (space === "Space") {
        spacebar = false
        spacebarPressed = false
    }
}



function player_collides(enemy) {
    if (player.x + player.width < enemy.x ||
        enemy.x + enemy.width < player.x ||
        player.y > enemy.y + enemy.height ||
        enemy.y > player.y + player.height) {
        return false;
    } else {
        return true;
    }
}







function bullet_collides(enemy, bullet) {
    if (bullet.x + bullet.width < enemy.x ||
        enemy.x + enemy.width < bullet.x ||
        bullet.y > enemy.y + enemy.height ||
        enemy.y > bullet.y + bullet.height) {
        return false;
    } else {
        return true;
    }
}


function playerObject_collides(object) {
    if (player.x + player.width < object.x ||
        object.x + object.size < player.x ||
        player.y > object.y + object.size ||
        object.y > player.y + player.height) {
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


    let data = new FormData();
    data.append("score", score);
    xhttp = new XMLHttpRequest();
    xhttp.addEventListener("readystatechange", handle_response, false);
    xhttp.open("POST", "/~mw17/cgi-bin/ca2/run.py/store_score", true);
    xhttp.send(data);

}

function bulletsCount(bulletCount) {
    let bullet_element = document.querySelector("#bullets");
    bullet_element.innerHTML = "Ammo: " + bulletCount;
}

function hpCount(hpCount) {
    let hp_element = document.querySelector("#hp");
    hp_element.innerHTML = "HP: " + hpCount;
}

function ScoreCount(scoreCount) {
    if (scoreCount < 0) {
        scoreCount = 0
    }
    scoreCount = Math.round(scoreCount)
    let score_element = document.querySelector("#score");
    score_element.innerHTML = "Score: " + scoreCount;
}


function movement(character) {
    character.x = character.x + character.xChange
    character.y = character.y + character.yChange
}



function ScoreMulti(scoreAmount, bulletAmount, hpAmount, timer) {
    scoreAmount = scoreAmount  + (hpAmount * 15)
    scoreAmount = scoreAmount * bulletAmount
    scoreAmount = scoreAmount * timer
    ScoreCount(scoreAmount)
    scoreAmount = Math.round(scoreAmount)
    return scoreAmount
}

function handle_response() {
    if (xhttp.readyState === 4) {
        if ( xhttp.status == 200){
            if ( xhttp.responseText === "success") {
            } else {

            }
        }
    }
}