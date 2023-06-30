$('.like-comment .reaction_icon').click( function(){
    let url = window.location.href+'like'
    fetch(url)
    $('.dislike-comment .reaction_icon').removeClass('reaction_icon_active')
    $('.like-comment .reaction_icon').addClass('reaction_icon_active')
})
$('.dislike-comment .reaction_icon').click( function(){
    let url = window.location.href+'dislike'
    fetch(url)
    $('.like-comment .reaction_icon').removeClass('reaction_icon_active')
    $('.dislike-comment .reaction_icon').addClass('reaction_icon_active')
})
