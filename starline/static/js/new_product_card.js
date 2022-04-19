    //!  функция построения популярных товаров getPopularCard

    function getPopularCard(){
        const newProductCardBlock = document.querySelector('.new-product-wrap .card');

        fetch('https://starline.pythonanywhere.com/starline/novelties/')
        .then(response => response.json())
        .then(newProductCards => {
            newProductCards.forEach((card, index) => {
                if((index < 8 && window.innerWidth > 768) || (index < 4 && window.innerWidth < 768)){

                //! создаем карточку товара
                const cardItem = document.createElement('a');
                    cardItem.className = 'card__item';

                    //! функция создания текста о выборе
                    function createTextChoice(){
                        const cardTextChoice = document.createElement('div');
                            cardTextChoice.className = 'item__choice';
                            cardTextChoice.innerHTML = 'Выбор большинства';
                        
                        return cardTextChoice;
                    }
                    //? вставляем в карточку выбор большинства
                    cardItem.append(createTextChoice());

                    //! функция создания обертки для img!
                    function createCardImg(){
                        const cardImgWrap = document.createElement('div');
                            cardImgWrap.className = 'item__img-wrap';

                        const cardImg = document.createElement('img');
                            cardImg.className = 'item__img';
                            cardImg.src = card.image;

                            cardImgWrap.append(cardImg);
                        
                        return cardImgWrap;
                    }
                    //? вставляем в каточку обертку с img
                    cardItem.append(createCardImg());

                    //! функция создания заголовков
                    function createCardTitle(){
                        const cardTitle = document.createElement('p');
                            cardTitle.className = 'item__title';
                            cardTitle.innerHTML = card.title;
                        
                        return cardTitle;
                    }
                    //? вставляем в каточку заголовки
                    cardItem.append(createCardTitle());

                    //! функция создания категорий товаров
                    function createCardCategory(){
                        const cardCategory = document.createElement('p');
                            cardCategory.className = 'item__subtitle';
                            cardCategory.innerHTML = card.category.title;

                        return cardCategory;
                    };
                    //? вставляем в карточку категорию
                    cardItem.append(createCardCategory());

                    //! функция создания наличия товара
                    function createCardPresence(){
                        const cardPresence = document.createElement('p');
                            if(card.presence === 'Под заказ'){
                                cardPresence.className = 'item__presence presence-orange';
                            }
                            if(card.presence === 'Есть в наличии'){
                                cardPresence.className = 'item__presence presence-green';
                            }
                            if(card.presence === 'Нет в наличии'){
                                cardPresence.className = 'item__presence presence-red';
                            }
                            cardPresence.innerHTML = card.presence;

                        return cardPresence;
                    }
                    //? вставляем в карточку наличие товара
                    cardItem.append(createCardPresence());

                    //! функция создания стоимости оборудования
                    function createCardEquipment(){
                        const cardEquipmentWrap = document.createElement('div');
                            cardEquipmentWrap.className = 'item__equipment';

                        const cardEquipmentText = document.createElement('p');
                            cardEquipmentText.className = 'item__equipment-text';
                            cardEquipmentText.innerHTML = 'Оборудование:';
                        cardEquipmentWrap.append(cardEquipmentText);

                        const cardEquipmentPrice = document.createElement('p');
                            cardEquipmentPrice.className = 'item__equipment-price';
                            cardEquipmentPrice.innerHTML = card.price + ' BYN';
                        cardEquipmentWrap.append(cardEquipmentPrice);

                        return cardEquipmentWrap;
                    }
                    //? вставляем в карточку стоимость оборудования
                    cardItem.append(createCardEquipment());

                    //! функция создания стоимости установки
                    function createCardPlant(){
                        const cardPlantWrap = document.createElement('div');
                            cardPlantWrap.className = 'item__plant';

                        const cardPlantText = document.createElement('p');
                            cardPlantText.className = 'item__plant-text';
                            cardPlantText.innerHTML = 'Установка:';
                        cardPlantWrap.append(cardPlantText);

                        const cardPlantPrice = document.createElement('p');
                            cardPlantPrice.className = 'item__plant-price';
                            cardPlantPrice.innerHTML = card.price_install + ' BYN';
                        cardPlantWrap.append(cardPlantPrice);

                        return cardPlantWrap;
                    }
                    //? вставляем в карточку стоимость установки
                    cardItem.append(createCardPlant());

                    newProductCardBlock.append(cardItem);
                }
            })
        })

    }
    getPopularCard()