//! input main!!!
const mainInput = document.querySelector('.main__input');
    mainInput.addEventListener('input', () => {
        if(mainInput.value.slice(-1) === '0'){
            mainInput.value = mainInput.value;
        } else if(!Number(mainInput.value.slice(-1))){
            mainInput.value = mainInput.value.slice(0, -1);
        }
    });
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
            mainInput.classList.remove('m-input-error');
            document.body.classList.remove('body-h');
    }
});


const mainBtn = document.querySelector('.main__btn');
    mainBtn.addEventListener('click', (e) => {
        e.preventDefault();
        let re = /^((80|\+375)?)(25|33|44|29)(\d{7})$/;
        let valid = re.test(mainInput.value);

        const mainText = document.querySelector('.main__text');

        if(valid){
            confirmModalTitle.innerHTML = 'Мы получили вашу заявку';
            confirmModalText.innerHTML = 'Наш технический специалист перезвонит вам в течение 8 минут';
            confirmModal.classList.add('m-confirm-show');
            mainText.classList.remove('not-valid-text');
            mainText.innerHTML = 'Перезвоним в течении 8 минут и наш технический эксперт ответит на все ваши вопросы.';
            mainInput.value = '';
            document.body.classList.add('body-h');
        } else if(mainInput.value != ''){
            mainText.innerHTML = 'Введите номер в формате +375__';
            mainText.classList.add('not-valid-text');
            mainInput.classList.add('m-input-error');
        } 
        else{
            mainText.innerHTML = 'Перезвоним в течении 8 минут и наш технический эксперт ответит на все ваши вопросы.';
            mainInput.classList.remove('m-input-error');
            mainText.classList.remove('not-valid-text');
        }
    })



