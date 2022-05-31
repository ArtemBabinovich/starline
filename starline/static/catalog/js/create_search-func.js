function createSearchBlockFunc(){
    fetch('https://starline.pythonanywhere.com/starline/characteristic/')
    .then(responce => responce.json())
    .then(categorySearch => {

        categorySearch.forEach(item => {

            const searchLabel = document.createElement('label');
                searchLabel.className = 'search__label';
                searchLabel.setAttribute('data-search', `${item.title}`)

                const inputSearch = document.createElement('input');
                    inputSearch.type = 'checkbox';
                    inputSearch.value = item.title;
                    inputSearch.className = 'seach__checkbox';
                searchLabel.append(inputSearch);

                const spanFake = document.createElement('span');
                    spanFake.className = 'search__fake';
                searchLabel.append(spanFake);

                const searchText = document.createElement('span');
                    searchText.className = 'search__text';
                    searchText.innerHTML = item.title;
                searchLabel.append(searchText);

                searchBlock[1].append(searchLabel);
        })
    })
}
createSearchBlockFunc()