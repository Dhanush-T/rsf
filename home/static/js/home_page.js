//News Carousel
let newsCarouselItems = document.querySelectorAll(
    "#newsCarousel .carousel-item"
);

const minPerSlide = 4;

newsCarouselItems.forEach((el) => {
    let next = el.nextElementSibling;
    for (let i = 1; i < minPerSlide; i++) {
        if (!next) {
            next = newsCarouselItems[0];
        }
        let cloneChild = next.cloneNode(true);
        el.appendChild(cloneChild.children[0]);
        next = next.nextElementSibling;
    }
});

let newsCI = document.querySelectorAll('#newsCarousel .carousel-indicators > button')
let previousWindowWidth = -1
const fixCarouselIndicators = () => {
    if(window.innerWidth > 768 && previousWindowWidth < 768) {
        previousWindowWidth = window.innerWidth
        let newsFirstCItem = document.querySelector('#newsCarousel .carousel-item')
        let newsActiveCItem = document.querySelector('#newsCarousel .carousel-item.active')
        if(newsActiveCItem !== newsFirstCItem) {
            newsActiveCItem?.classList.remove('active')
            newsFirstCItem?.classList.add('active')
        }

        let newsFirstCI = document.querySelector('#newsCarousel .carousel-indicators > button')
        let newsActiveCI = document.querySelector('#newsCarousel .carousel-indicators > button.active')

        if(newsFirstCI !== newsActiveCI) {
            newsFirstCI?.classList.add('active')
            newsActiveCI?.classList.remove('active')
        }

        newsCI.forEach((ele, index) => {
            if(index > newsCI.length-4) ele.remove();
        })
    } else if(window.innerWidth < 768 && previousWindowWidth > 768) {
        previousWindowWidth = window.innerWidth
        let newsCIContainer = document.querySelector('#newsCarousel .carousel-indicators')
        while (newsCIContainer.firstChild) {
            newsCIContainer.removeChild(newsCIContainer.firstChild);
        }
        newsCI.forEach((ele, index) => {
            newsCIContainer.appendChild(ele)
        })
    }
}
fixCarouselIndicators();
window.addEventListener("resize", fixCarouselIndicators);

const newsCarousel = document.getElementById('newsCarousel');

const carousel = new bootstrap.Carousel(newsCarousel, {pause:true})

newsCarousel.addEventListener('wheel', (e)=>{
    const currentActive = document.querySelector('#newsCarousel .carousel-indicators > button.active').getAttribute('data-bs-slide-to') - '0';
    if(e.deltaX>4 && currentActive < newsCI.length - minPerSlide ){
        carousel.next()
    }

    if(e.deltaX<-4 && currentActive > 0){
        carousel.prev();

    }
    setTimeout(()=>{}, 2000)
})
