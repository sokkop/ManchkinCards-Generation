const BooleanSwitch = document.getElementById("bool_switch")
const BooleanValue = document.getElementById('booleanValue')
let isActive = false;

BooleanSwitch.addEventListener('click', function () {
    isActive = !isActive;
    if (isActive) {
        this.classList.add('active');
        BooleanValue.value = true;
    }
    else {
        this.classList.remove('active');
        BooleanValue.value = false;
    }
})