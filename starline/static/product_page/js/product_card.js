const productPerfomance = document.querySelector('.product__perfomance');
let outerProductPerfomance = productPerfomance.outerHTML;

const tabsBlock = document.querySelector('.product__tabs');
    tabsBlock.addEventListener('click', (event) => {
        if(event.target.getAttribute('data-tabs') === 'instructions'){
            setClassTab();
                productPerfomance.innerHTML = '';

            const productPerfomanceTitle = document.createElement('h3');
                productPerfomanceTitle.className = 'perfomance__title';
                productPerfomanceTitle.innerHTML = `Инструкции ${document.querySelector('.pagintaion__page').innerHTML}`;
                productPerfomance.append(productPerfomanceTitle);


                const linkInstruction = document.createElement('a');
                    linkInstruction.setAttribute('href', '#');
                    linkInstruction.innerHTML = `
                                            ${document.querySelector('.pagintaion__page').innerHTML}, 
                                            инструкции по эксплуатации и установке`;
                    productPerfomance.insertAdjacentElement('beforeend', linkInstruction);
        } else{
            setClassTab();
            productPerfomance.innerHTML = outerProductPerfomance;
        }
    });

    function setClassTab(){
        const tabsText = document.querySelectorAll('.tabs__text');
            tabsText.forEach(elem => elem.classList.contains('tab-choice') ? 
                                elem.classList.remove('tab-choice') : 
                                elem.classList.add('tab-choice'));
    }
