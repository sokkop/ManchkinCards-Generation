const valueElement1 = document.querySelector('.counter1');
const add1 = document.querySelector('.plus1');
const sub1 = document.querySelector('.minus1');
const valueElement2 = document.querySelector('.counter2');
const add2 = document.querySelector('.plus2');
const sub2 = document.querySelector('.minus2');

let value1 = 0;
let value2 = 0;

function UpdateValue1() {
    valueElement1.textContent = value1;
}

function UpdateValue2() {
    valueElement2.textContent = value2;
}

add1.addEventListener('click', () => {
    value1++;
    UpdateValue1();
})

sub1.addEventListener('click', () => {
    value1--;
    UpdateValue1();
})

add2.addEventListener('click', () => {
    value2++;
    UpdateValue2();
})

sub2.addEventListener('click', () => {
    value2--;
    UpdateValue2();
})

UpdateValue1();
UpdateValue2();
