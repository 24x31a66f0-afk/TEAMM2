const symbols = ["♫","♪","♬","♩","♭","♯"];

const bg = document.querySelector(".background");

/* create floating symbols */

for(let i=0;i<20;i++){

let span = document.createElement("span");

span.classList.add("symbol");

span.innerHTML = symbols[Math.floor(Math.random()*symbols.length)];

span.style.left = Math.random()*100 + "vw";

span.style.animationDuration = (10 + Math.random()*10) + "s";

span.style.fontSize = (25 + Math.random()*40) + "px";

bg.appendChild(span);

}

/* generate music */

function generateMusic(){

let visualizer = document.getElementById("visualizer");

visualizer.classList.add("play");

/* backend connection */

let audio = document.getElementById("audio");

audio.src="sample.mp3";

audio.play();

}