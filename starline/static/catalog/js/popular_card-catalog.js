//!  функция построения популярных товаров getPopularCard

let allCards = []
let visibleCards = []
let visibleCardsAmount = 12
let categoryFilters = []
let functionFilters = []
let sortOrder = 'all'
const popularCardBlock = document.querySelector('.card')
const button = document.querySelector('.card__link')

function getPopularCard() {
  return fetch('https://starline.pythonanywhere.com/starline/product/')
    .then((response) => response.json())
    .then((popularCards) => {
      allCards = popularCards
      visibleCards = popularCards
    })
}

function drawCards() {
  visibleCards = allCards
    .filter((card) => (categoryFilters.length
      ? categoryFilters.includes(card.category.title)
      : true
    ))
    .filter((card) => (functionFilters.length
      ? card.characteristics.some((characteristic) => functionFilters.includes(characteristic))
      : true
    ))
    .sort((a, b) => {
      switch (sortOrder) {
        case 'all':
          return 0
        case 'low':
          return a.price - b.price
        case 'high':
          return b.price - a.price
        default:
          return 0
      }
    })

  if (visibleCards.length) {
    popularCardBlock.innerHTML = ''

    visibleCards
      .slice(0, visibleCardsAmount)
      .forEach((card) => {
        // if((index < 9 && window.innerWidth > 768) || (index < 5 && window.innerWidth < 768)){

        //! создаем карточку товара
        const cardItem = document.createElement('a')
        cardItem.setAttribute('href', `https://starline.pythonanywhere.com/catalog/product/${card.slug}`)
        cardItem.className = 'card__item'

        //! функция создания обертки для img!
        function createCardImg() {
          const cardImgWrap = document.createElement('div')
          cardImgWrap.className = 'item__img-wrap'

          const cardImg = document.createElement('img')
          cardImg.className = 'item__img'
          cardImg.src = card.image

          cardImgWrap.append(cardImg)

          return cardImgWrap
        }
        // ? вставляем в каточку обертку с img
        cardItem.append(createCardImg())

        //! функция создания заголовков
        function createCardTitle() {
          const cardTitle = document.createElement('p')
          cardTitle.className = 'item__title'
          cardTitle.innerHTML = card.title

          return cardTitle
        }
        // ? вставляем в каточку заголовки
        cardItem.append(createCardTitle())

        //! функция создания категорий товаров
        function createCardCategory() {
          const cardCategory = document.createElement('p')
          cardCategory.className = 'item__subtitle'
          cardCategory.innerHTML = card.category.title

          return cardCategory
        }
        // ? вставляем в карточку категорию
        cardItem.append(createCardCategory())

        //! функция создания наличия товара
        function createCardPresence() {
          const cardPresence = document.createElement('p')
          if (card.presence === 'Под заказ') {
            cardPresence.className = 'item__presence presence-orange'
          }
          if (card.presence === 'Есть в наличии') {
            cardPresence.className = 'item__presence presence-green'
          }
          if (card.presence === 'Нет в наличии') {
            cardPresence.className = 'item__presence presence-red'
          }
          cardPresence.innerHTML = card.presence

          return cardPresence
        }
        // ? вставляем в карточку наличие товара
        cardItem.append(createCardPresence())

        //! функция создания стоимости оборудования
        function createCardEquipment() {
          const cardEquipmentWrap = document.createElement('div')
          cardEquipmentWrap.className = 'item__equipment'

          const cardEquipmentText = document.createElement('p')
          cardEquipmentText.className = 'item__equipment-text'
          cardEquipmentText.innerHTML = 'Оборудование:'
          cardEquipmentWrap.append(cardEquipmentText)

          const cardEquipmentPrice = document.createElement('p')
          cardEquipmentPrice.className = 'item__equipment-price'
          cardEquipmentPrice.innerHTML = `${card.price} BYN`
          cardEquipmentWrap.append(cardEquipmentPrice)

          return cardEquipmentWrap
        }
        // ? вставляем в карточку стоимость оборудования
        cardItem.append(createCardEquipment())

        //! функция создания стоимости установки
        function createCardPlant() {
          const cardPlantWrap = document.createElement('div')
          cardPlantWrap.className = 'item__plant'

          const cardPlantText = document.createElement('p')
          cardPlantText.className = 'item__plant-text'
          cardPlantText.innerHTML = 'Установка:'
          cardPlantWrap.append(cardPlantText)

          const cardPlantPrice = document.createElement('p')
          cardPlantPrice.className = 'item__plant-price'
          cardPlantPrice.innerHTML = `${card.price_install} BYN`
          cardPlantWrap.append(cardPlantPrice)

          return cardPlantWrap
        }
        // ? вставляем в карточку стоимость установки
        cardItem.append(createCardPlant())

        popularCardBlock.append(cardItem)
        // }
      })
  } else {
    popularCardBlock.innerHTML = 'Не найдено товаров'
  }
}

function updateCardsAmount() {
  document.querySelector('.amount__text').innerHTML = visibleCards.length
}

function updateButton() {
  if (categoryFilters.length || functionFilters.length) {
    button.innerHTML = 'Сбросить фильтр'

    if (button.classList.contains('btn-hidden')) {
      button.classList.remove('btn-hidden')
    }
  } else {
    button.innerHTML = 'Показать ещё товары'

    if (visibleCards.length <= visibleCardsAmount) {
      button.classList.add('btn-hidden')
    }
  }
}

function updateCardsList() {
  drawCards()
  updateCardsAmount()
  updateButton()
}

function filterByCategory(event) {
  const filter = event.target.parentElement.getAttribute('data-search')

  categoryFilters = categoryFilters.includes(filter)
    ? categoryFilters.filter((item) => item !== filter)
    : [...categoryFilters, filter]

  updateCardsList()
}

function filterByFilter(event) {
  const filter = event.target.parentElement.getAttribute('data-search')

  functionFilters = functionFilters.includes(filter)
    ? functionFilters.filter((item) => item !== filter)
    : [...functionFilters, filter]

  updateCardsList()
}

function cleanFilters() {
  const checkboxes = document.querySelectorAll('.search__block .seach__checkbox')
  // eslint-disable-next-line no-param-reassign
  checkboxes.forEach((checkbox) => { checkbox.checked = false })

  visibleCardsAmount = 12
}

async function run() {
  await getPopularCard()

  updateCardsList()
}

run()

// Filters
const filterBlocks = document.querySelectorAll('.search__block')

filterBlocks[0].addEventListener('change', filterByCategory)
filterBlocks[1].addEventListener('change', filterByFilter)

// Dropdown
function selectDropdownValue(event) {
  document.getElementById('dropdown-text').innerHTML = event.target.innerText
  sortOrder = event.target.getAttribute('data-price')

  updateCardsList()
}

const dropDownItems = document.querySelectorAll('.dropdown__subitem')

dropDownItems.forEach((dropDownItem) => {
  dropDownItem.addEventListener('click', selectDropdownValue)
})

// Button
button.addEventListener('click', () => {
  if (categoryFilters.length || functionFilters.length) {
    categoryFilters = []
    functionFilters = []

    cleanFilters()
    updateCardsList()
  } else if (visibleCards.length > visibleCardsAmount) {
    visibleCardsAmount += 6

    updateCardsList()
  }
})