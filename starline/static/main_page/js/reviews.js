function getReviewText(){
    fetch('https://starline.pythonanywhere.com/starline/our_work/')
    .then(response => response.json())
    .then(reviewItems => {

        const lengthReviewItems = document.querySelector('.review__lengh');
            lengthReviewItems.innerHTML = reviewItems.length;

        const reviewsBlock = document.querySelector('.review-card__column');

        reviewItems.forEach((item, index) => {
            const reviewCard = document.createElement('div');
                reviewCard.className = 'review-card';
            
            reviewsBlock.append(reviewCard);
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
                    reviewCardLink.href = `https://starline.pythonanywhere.com/ourwork/`${item.slug};
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
getReviewText()