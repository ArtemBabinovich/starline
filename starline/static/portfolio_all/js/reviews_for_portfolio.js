function getReviewText(){
    fetch('https://starline.pythonanywhere.com/starline/our_work/')
    .then(response => response.json())
    .then(reviewItems => {

        const reviewsBlock = document.querySelector('.review-card__column');

        reviewItems.forEach((item, index) => {
            if(index < 6){
                const reviewCard = document.createElement('div');
                reviewCard.className = 'review-card';
            
            reviewsBlock.append(reviewCard);
            } else{
                const reviewCard = document.createElement('div');
                reviewCard.className = 'review-card';
                reviewCard.classList.add('show');
            
            reviewsBlock.append(reviewCard);
            }
        });

        reviewCard = document.querySelectorAll('.review-card');
            
            reviewCard.forEach(element => {
                const reviewCardInfo = document.createElement('div');
                    reviewCardInfo.className = 'review-card__info';
                
                element.append(reviewCardInfo);

                const reviewCardImg = document.createElement('div');
                    reviewCardImg.className = 'review-card__img';

                element.append(reviewCardImg);
            });

        reviewCardInfo = document.querySelectorAll('.review-card__info');

            reviewCardInfo.forEach((item, index) => {
                const reviewCardMeta = document.createElement('div');
                    reviewCardMeta.className = 'review-card__meta';

                item.append(reviewCardMeta);

                const reviewCardTitle = document.createElement('h3');
                    reviewCardTitle.className = 'review-card__title';

                item.append(reviewCardTitle);

                const reviewCardTextTime = document.createElement('div');
                    reviewCardTextTime.className = 'review-first__text';
                    reviewCardTextTime.classList.add('card__text');

                item.append(reviewCardTextTime);

                const reviewCardTextCost = document.createElement('div');
                    reviewCardTextCost.className = 'review-second__text';
                    reviewCardTextCost.classList.add('text-margin');
                    reviewCardTextCost.classList.add('card__text');

                item.append(reviewCardTextCost);

                const reviewCardLink = document.createElement('a');
                    reviewCardLink.className = 'review-card__link';
                    reviewCardLink.innerHTML = 'Подробнее';
                    reviewCardLink.href = `https://starline.pythonanywhere.com/our_work/${reviewItems[index].slug}`;
                    //! тут надо добавить ссылку на карточку!!!
                    
                item.append(reviewCardLink);
            });

        reviewCardTitle = document.querySelectorAll('.review-card__title');
            reviewCardTitle.forEach((el, index) => {
                el.innerHTML = reviewItems[index].title;
            });

        reviewCardMeta = document.querySelectorAll('.review-card__meta');
            reviewCardMeta.forEach((el, index) => {
                for(let text of reviewItems[index].category_work){
                    const reviewMetaText = document.createElement('p');
                        reviewMetaText.setAttribute('data-work', `${text}`)
                        reviewMetaText.innerHTML = text;
                    
                    el.append(reviewMetaText);
                }
            });

        reviewCardTextTime = document.querySelectorAll('.review-first__text');
            reviewCardTextTime.forEach((el, index) => {
                const textStaticTime = document.createElement('p');
                    textStaticTime.innerHTML = 'Срок установки:';

                el.append(textStaticTime);

                const textTime = document.createElement('p');
                    textTime.innerHTML = reviewItems[index].installation_price;

                el.append(textTime);
            });

        reviewCardTextCost = document.querySelectorAll('.review-second__text');
            reviewCardTextCost.forEach((el, index) => {
                const textStaticCost = document.createElement('p');
                    textStaticCost.innerHTML = 'Стоимость установки:';

                el.append(textStaticCost);

                const textCost = document.createElement('p');
                    textCost.innerHTML = reviewItems[index].installation_time;

                el.append(textCost);
            });

        reviewCardImg = document.querySelectorAll('.review-card__img');
            reviewCardImg.forEach((el, index) => {
                const reviewImg = document.createElement('img');
                    reviewImg.src = reviewItems[index].image1;
                    reviewImg.alt = 'image';
                
                el.append(reviewImg);
            });
    });
}
getReviewText();

function getCategory(){
    fetch('https://starline.pythonanywhere.com/starline/all_category/')
    .then(response => response.json())
    .then(allCategory => {
        
        const blockCategory = document.querySelector('.review__search-btn');

        allCategory.forEach(item => {
            const itemCategory = document.createElement('button');
                itemCategory.className = 'search-btn';
                itemCategory.setAttribute('data-work', `${item.title}`);
                itemCategory.innerHTML = item.title;

            blockCategory.append(itemCategory);
        })
    })
};
getCategory();

let indexCard = 9;

const searchBtnWork = document.querySelector('.review__link');
searchBtnWork.addEventListener('click', showCard);

function showCard(event){
    event.preventDefault();

    const reviewCard = document.querySelectorAll('.review-card');
        reviewCard.forEach((item, index) => {
            if(index < indexCard){
                if(item.classList.contains('show')){
                    item.classList.remove('show');
                }
                if(indexCard === reviewCard.length){
                    searchBtnWork.classList.add('disable-btn');
                    searchBtnWork.removeEventListener('click', showCard);
                }
            }
        })

    indexCard += 3;
}

const searchWork = document.querySelector('.review__search-btn');
    searchWork.addEventListener('click', (event) => {
        const reviewCard = document.querySelectorAll('.review-card');

        let targetAttribute = event.target.getAttribute('data-work');

        reviewCard.forEach(item => {
            const dataCard = item.querySelectorAll('.review-card__meta p');
                
            for(let i = 0; i < dataCard.length; i++){
                if(dataCard[i].getAttribute('data-work') === targetAttribute){
                    item.classList.remove('show');
                    break
                } else{
                    item.classList.add('show');
                    searchBtnWork.classList.add('show');
                }
            }
        });
    });
