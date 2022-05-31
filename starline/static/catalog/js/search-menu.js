const catalogSearch = document.querySelector('.catalog__search');

const searchBtn = document.querySelector('.search-mob__btn');
    searchBtn.addEventListener('click', () => {
        catalogSearch.classList.add('search-active');
        document.body.classList.add('body-h');
    })

catalogSearch.addEventListener('click', closeSearchMenu);

function closeSearchMenu(event){
    let target = event.target;

    if(target === document.querySelector('.search__cross') || target === document.querySelector('.search__btn')){
        catalogSearch.classList.remove('search-active');
        document.body.classList.remove('body-h');
    }
}

window.addEventListener('scroll', () => {
    if(window.scrollY > document.querySelector('.card').scrollHeight){
        searchBtn.style.opacity = '0';
    }
    if(window.scrollY < document.querySelector('.card').scrollHeight){
        searchBtn.style.opacity = '1';
    }
});
