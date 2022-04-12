const inputTel = document.querySelectorAll('[type="tel"]');
    inputTel.forEach(elem => elem.addEventListener('input', inputTelValue))

function inputTelValue(){
    this.value = '+375' + this.value.slice(4);
}
//! input main!!!
const mainInput = document.querySelector('.main__input');
//! модальное окно подтверждения
const confirmModal = document.querySelector('.m-confirm__wrapper');
//! текст модального окна подтверждения
const confirmModalTitle = document.querySelector('.m-confirm__title'),
        confirmModalText = document.querySelector('.m-confirm__subtitle');

confirmModal.addEventListener('click', (event) => {
    if(event.target === document.querySelector('.m-confirm__cross') 
        || event.target === document.querySelector('.m-confirm__wrapper')
        || event.target === document.querySelector('.m-confirm__btn')){
            confirmModal.classList.remove('m-confirm-show');
            mainInput.classList.remove('m-input-error')
    }
});


const mainBtn = document.querySelector('.main__btn');
    mainBtn.addEventListener('click', (e) => {
        e.preventDefault();
        let re = /^((80|\+375)?)(25|33|44|29)(\d{7})$/;
        let valid = re.test(mainInput.value);

        if(valid){
            confirmModalTitle.innerHTML = 'Мы получили вашу заявку';
            confirmModalText.innerHTML = 'Наш технический специалист перезвонит вам в течение 8 минут';
            confirmModal.classList.add('m-confirm-show');
            mainInput.value = '';
        } else if(mainInput.value != ''){
            mainInput.classList.add('m-input-error');
        } 
        else{
            mainInput.classList.remove('m-input-error');
        }
    })


// const wrapper = document.querySelector('.wrapper');
//     wrapper.addEventListener('click', validPhone);

// function validPhone(event) {
//     if(event.target.tagName === 'BUTTON')
//     event.preventDefault();
//     let re = /^((80|\+375)?)(25|33|44|29)(\d{7})$/;
//     let myPhone = event.target.previousElementSibling.value; 
//     let valid = re.test(myPhone); 
//     if (valid){
//         console.log(111)
//     }
// }


