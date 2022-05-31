const searchBlock = document.querySelectorAll('.search__block');

function createSearchBlock(){
    fetch('https://starline.pythonanywhere.com/starline/category_search/')
    .then(responce => responce.json())
    .then(categorySearch => {
        
        categorySearch.forEach(item => {
            const searchTitle = document.createElement('h3');
                searchTitle.className = 'search__block-title';
                searchTitle.innerHTML = item.title;
            searchBlock[0].append(searchTitle);

            const searchLableWrap = document.createElement('div');
                searchLableWrap.className = 'search__label-wrap';
            
                item.categores.forEach(element => {
                    const searchLabel = document.createElement('label');
                        searchLabel.className = 'search__label';
                        searchLabel.setAttribute('data-search', `${element}`)

                    const inputSearch = document.createElement('input');
                        inputSearch.type = 'checkbox';
                        inputSearch.value = element;
                        inputSearch.className = 'seach__checkbox';
                    searchLabel.append(inputSearch);

                    const spanFake = document.createElement('span');
                        spanFake.className = 'search__fake';
                    searchLabel.append(spanFake);

                    const searchText = document.createElement('span');
                        searchText.className = 'search__text';
                        searchText.innerHTML = element;
                    searchLabel.append(searchText);

                    searchLableWrap.append(searchLabel);
                })

                searchBlock[0].append(searchLableWrap);
        })
    })
}
createSearchBlock()