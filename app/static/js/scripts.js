const observer = new IntersectionObserver(entries => {
    entries.forEach(entry =>{
        if(entry.isIntersecting){
            document.querySelector(".animated").add("fadeInBottom");
        }
    })

})

observer.observe(document.querySelector(".infoblock"));

function pageScroll() {
    window.scrollBy(0,1);
    scrolldelay = setTimeout(pageScroll,10);
}   