function read_more(element) {
    if (element.dataset.mode == "More"){
        console.log(element.previousElementSibling)
        element.previousElementSibling.style.maxHeight='fit-content'
        element.dataset.mode = "Less"
        element.innerText = "Меньше"
    }else{
        console.log(element.previousElementSibling)
        element.previousElementSibling.style.maxHeight='200px'
        element.dataset.mode = "More"
        element.innerText = "Більше"
    }
} 

function renderCommentReadMore(){
readMore = document.querySelectorAll(".comment-content")
readMore.forEach(element => {
    console.log("readmore work")
    if (element.firstElementChild.scrollHeight > 200){
        console.log("overflow")
        element.lastElementChild.style.display = "flex"
    }
    else{
        element.lastElementChild.style.display = "none"
    }
})
}

function renderBookDescriptionReadMore(){
    readMore = document.querySelectorAll(".book_page_description")
    readMore.forEach(element => {
        console.log("readmore work")
        if (element.firstElementChild.scrollHeight > 200){
            console.log("overflow")
            element.lastElementChild.style.display = "flex"
        }
        else{
            element.lastElementChild.style.display = "none"
        }
    })
    }

function renderDiscussionDescriptionReadMore(){
    readMore = document.querySelectorAll(".discussion_page_description")
        readMore.forEach(element => {
        console.log("readmore work")
        if (element.firstElementChild.scrollHeight > 200){
            console.log("overflow")
            element.lastElementChild.style.display = "flex"
        }
        else{
            element.lastElementChild.style.display = "none"
        }
    })
    }
window.addEventListener("resize", renderCommentReadMore)
window.addEventListener("resize", renderBookDescriptionReadMore)
window.addEventListener("resize", renderDiscussionDescriptionReadMore)
renderBookDescriptionReadMore()
renderDiscussionDescriptionReadMore()
renderCommentReadMore()