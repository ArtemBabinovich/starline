const btnModal = document.querySelectorAll('[data-modal]');
    btnModal.forEach(btn => btn.addEventListener('click', showModalWindow));

const modal = document.querySelector('.modal');
    modal.addEventListener('click', closeModalWindow);

let userPhone = document.querySelector('.modal [type="tel"]');
    userPhone.addEventListener('input', () => {
        if(userPhone.value.slice(-1) === '0'){
            userPhone.value = userPhone.value;
        } else if(!Number(userPhone.value.slice(-1))){
            userPhone.value = userPhone.value.slice(0, -1);
        }
    });
let modalTextArea = document.querySelector('.modal__textarea');
let userName =  document.querySelector('.modal [type="text"');

function showModalWindow(e){
    const modalTitle = document.querySelector('.modal__title'),
        modalSubTitle = document.querySelector('.modal__subtitle'),
        modalBtn = document.querySelector('.modal__btn');
        modalBtn.addEventListener('click', validationModalWindow);
    let modalShowEl = document.querySelectorAll('.m-display');

        userName.value = '';
        userPhone.value = '';
        modalTextArea.value = '';
        userName.classList.remove('m-input-valid');
        userName.classList.remove('m-input-error');
        userPhone.classList.remove('m-input-valid');
        userPhone.classList.remove('m-input-error');
        document.body.classList.toggle('body-h');

    if(e.target.getAttribute('data-modal') === 'advice'){
        modalTitle.innerHTML = 'Заявка на бесплатную консультацию';
        modalSubTitle.innerHTML = 'Технический специалист перезвонит Вам в течение 10 минут и ответит на все вопросы';
        modalBtn.value = 'Отправить';
        modalShowEl.forEach(elem => elem.style.display = 'none');
        modal.classList.add('m-show');
    } 
    if(e.target.getAttribute('data-modal') === 'review'){
        modalTitle.innerHTML = 'Оставить отзыв';
        modalSubTitle.innerHTML = 'Через несколько дней Ваш отзыв отобразится на сайте в блоке «Отзывы»';
        modalBtn.value = 'Оставить отзыв';
        modalShowEl.forEach(elem => elem.style.display = 'block');
        modal.setAttribute('data-comment', 'comment');
        modal.classList.add('m-show');
    }
}

function closeModalWindow(e){
    if(e.target === modal || e.target === document.querySelector('.modal__cross') && modal.classList.contains('m-show')){
        modal.classList.remove('m-show');
        document.body.classList.remove('body-h');
    }
}

confirmModal = document.querySelector('.m-confirm__wrapper');
    confirmModal.addEventListener('click', (event) => {
        if(event.target === document.querySelector('.m-confirm__cross') 
            || event.target === document.querySelector('.m-confirm__wrapper')
            || event.target === document.querySelector('.m-confirm__btn')){
                confirmModal.classList.remove('m-confirm-show');
                document.body.classList.remove('body-h');
                userPhone.value = '';
                userName.value = '';
        }
    });

function validationModalWindow(event){
    event.preventDefault();

    const confirmModalTitle = document.querySelector('.m-confirm__title'),
        confirmModalText = document.querySelector('.m-confirm__subtitle');

    let re = /^((80|\+375)?)(25|33|44|29)(\d{7})$/;
    let userPhone = document.querySelector('.modal [type="tel"]');
    let userName =  document.querySelector('.modal [type="text"');

    let valid = re.test(userPhone.value);

    if (valid && userName != ''){
        if(modal.hasAttribute('data-comment')){
            modal.classList.remove('m-show');
            confirmModalTitle.innerHTML = 'Отзыв успешно отправлен';
            confirmModalText.innerHTML = 'Спасибо, отзыв появится на сайте в течение нескольких дней.';
            confirmModal.classList.add('m-confirm-show');
        } else{
            modal.classList.remove('m-show');
            confirmModalTitle.innerHTML = 'Мы получили вашу заявку';
            confirmModalText.innerHTML = 'Наш технический специалист перезвонит вам в течение 8 минут';
            confirmModal.classList.add('m-confirm-show');
        }
    } else{
        if(userName.value != ''){
            userName.classList.add('m-input-valid');
        } else{
            userName.classList.add('m-input-error');
        }
        if(userPhone.value != ''){
            userPhone.classList.add('m-input-valid');
        } else{
            userPhone.classList.add('m-input-error');
        }
    }
}

