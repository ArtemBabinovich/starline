//! input main!!!
const footerInputTel = document.querySelector('.footer-tel');
    footerInputTel.addEventListener('input', () => {
        if(footerInputTel.value.slice(-1) === '0'){
            footerInputTel.value = footerInputTel.value;
        } else if(!Number(footerInputTel.value.slice(-1))){
            footerInputTel.value = footerInputTel.value.slice(0, -1);
        }
    });

const formBtn = document.querySelector('.form__btn');
    formBtn.addEventListener('click', validationFormComment)


//! функция валидации футера, оставить отзыв
//* валидация с показанием окна, если все ок
function validationFormComment(event){
    event.preventDefault();

    let re = /^((80|\+375)?)(25|33|44|29)(\d{7})$/;
    let userPhone = document.querySelector('.footer__form [type="tel"]');
    let userName =  document.querySelector('.footer__form [type="text"');
    let userTextArea = document.querySelector('.footer__form textarea');

    let valid = re.test(userPhone.value);

    if (valid && userName != '' && userPhone != '' && userTextArea.value != ''){
        const confirmModal = document.querySelector('.m-confirm__wrapper');
            userName.classList.remove('m-input-error');
            userName.classList.remove('m-input-valid');
            userPhone.classList.remove('m-input-error');
            userPhone.classList.remove('m-input-valid');
            userTextArea.classList.remove('m-input-valid');
            userTextArea.classList.remove('m-input-error');
            userName.value = '';
            userPhone.value = '';
            userTextArea.value = '';
            confirmModal.classList.add('m-confirm-show');
            document.body.classList.add('body-h');
    } else{
        if(userName.value != ''){
            userName.classList.add('m-input-valid');
        } else{
            userName.classList.add('m-input-error');
        }
        if(userPhone.value != '' && userPhone.value != '+375' && valid){
            userPhone.classList.add('m-input-valid');
        } else{
            userPhone.classList.add('m-input-error');
        }
        if(userTextArea.value != ''){
            userTextArea.classList.add('m-input-valid');
        } else{
            userTextArea.classList.add('m-input-error');
        }
    }
}


