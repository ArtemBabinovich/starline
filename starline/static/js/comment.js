//! функция слайдера

function getTextComment(){
    fetch('https://starline.pythonanywhere.com/starline/comments/')
    .then(response => response.json())
    .then(commentsText => {

        const arrLeft = document.querySelector('.left');
            arrLeft.addEventListener('click', setPrevComment);
        const arrRight = document.querySelector('.right');
            arrRight.addEventListener('click', setNextComment);
        
        let count = 0;

        function setSliderText(count){
            const sliderTitle = document.querySelector('.slider__title');
                sliderTitle.innerHTML = commentsText[count].title;

            const sliderText = document.querySelector('.slider__text');
                sliderText.innerHTML = commentsText[count].body;

            const sliderNameText = document.querySelector('.slider__contact');
                sliderNameText.innerHTML = commentsText[count].name;

            let sliderFirstPage = document.querySelector('.comment__page-first');
                sliderFirstPage.innerHTML = count + 1;

            let sliderLastPage = document.querySelector('.comment__page-last');
                sliderLastPage.innerHTML = commentsText.length;
        }
        setSliderText(count);

        function setNextComment(){
            count++;
            if(count === commentsText.length - 1){
                setSliderText(count);
                arrRight.classList.add('disabled');
                count = commentsText.length - 2;
            } else{
                arrRight.classList.remove('disabled');
                arrLeft.classList.remove('disabled');
                setSliderText(count);
            }
        }

        function setPrevComment(){
            if(count <= 0){
                setSliderText(count);
                arrLeft.classList.add('disabled');
                count = 0
            } else{
                arrRight.classList.remove('disabled');
                arrLeft.classList.remove('disabled');
                setSliderText(count);
                count--;
            }
        }
    })
}
getTextComment()
