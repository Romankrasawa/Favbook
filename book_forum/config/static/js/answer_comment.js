
function answerComment(element){
    id = element.dataset.id
    comment_text = $('.comment-content[data-id=\"'+id+'\"] p').text()
    console.log(comment_text, id, '.comment-content[data-id=\"'+id+'\"] p')
    $('.answer_comment').text(comment_text)
    $('#id_answer').val(id)
}