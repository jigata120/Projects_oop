// custom.js
let counter = 0;

function script() {
    counter++;
    document.querySelector('h1').innerHTML = counter;

    if (counter > 10) {
        alert(`You have reached ${counter}`);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = script;
});