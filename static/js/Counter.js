const valueElement = document.querySelector('.counter');
const add = document.querySelector('.plus');
const sub = document.querySelector('.minus');

let value = 0;

function UpdateValue() {
    valueElement.textContent = value;
}

add.addEventListener('click', () => {
    value++;
    UpdateValue();
})

sub.addEventListener('click', () => {
    value--;
    UpdateValue();
})

UpdateValue();
