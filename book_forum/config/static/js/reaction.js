let like_num = $('.like-comment span')
let dislike_num = $('.dislike-comment span')
let like_img = $('.like-comment img')
let dislike_img = $('.dislike-comment img')
like_img.click(function () {
    if (dislike_img.hasClass("reaction_icon_active")) {
        dislike_img.removeClass("reaction_icon_active")
        dislike_num.text(parseInt(dislike_num.text()) - 1)
        like_img.addClass("reaction_icon_active")
        like_num.text(parseInt(like_num.text()) + 1)
    } else if (like_img.hasClass("reaction_icon_active")) {
        like_img.removeClass("reaction_icon_active")
        like_num.text(parseInt(like_num.text()) - 1)
    } else {
        like_img.addClass("reaction_icon_active")
        like_num.text(parseInt(like_num.text()) + 1)
    }
    let url = window.location.href + 'like'
    fetch(url)

})
dislike_img.click(function () {
    if (like_img.hasClass("reaction_icon_active")) {
        like_img.removeClass("reaction_icon_active")
        like_num.text(parseInt(like_num.text()) - 1)
        dislike_img.addClass("reaction_icon_active")
        dislike_num.text(parseInt(dislike_num.text()) + 1)
    } else if (dislike_img.hasClass("reaction_icon_active")) {
        dislike_img.removeClass("reaction_icon_active")
        dislike_num.text(parseInt(dislike_num.text()) - 1)
    } else {
        dislike_img.addClass("reaction_icon_active")
        dislike_num.text(parseInt(dislike_num.text()) + 1)
    }
    let url = window.location.href + 'dislike'
    fetch(url)

})
