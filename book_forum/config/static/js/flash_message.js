document.getElementById('account_image').addEventListener('click', function() { 
    $('.flash_area').css('display', 'flex')
    $('.flash_area').slideDown(500)
    console.log('ok')
    setTimeout(() => {
        $('.flash_area').slideUp(500)
    }, 5000)

 })
