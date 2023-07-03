
function timer(ms) { return new Promise(res => setTimeout(res, ms)); }

async function show_flash_messages(){
flash_messages = document.getElementsByClassName("flash_area")
for (const element of flash_messages){
    element.style.display = "flex"

    await timer(3500)
    element.style.display = "none"
};}
show_flash_messages()

