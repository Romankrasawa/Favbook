document.getElementById('search_input').addEventListener("focus", function(){
    this.style.borderRadius = '15px 15px 0 0'
    document.getElementById('search_autocomplete').style.display = 'flex'
})
document.getElementById('search_input').addEventListener("blur", function(){
        console.log("focuse out")
        setTimeout(() => {
        this.style.borderRadius = '15px 15px 15px 15px'
        document.getElementById('search_autocomplete').style.display = 'none'
        }, 150)

})
// document.getElementById('search_autocomplete').addEventListener("blur", function(){
//     if(document.getElementsByClassName('search_area')[0] != document.activeElement){
//         this.style.borderRadius = '15px 0 0 15px'
//         document.getElementById('search_autocomplete').style.display = 'none'
//     }
// })