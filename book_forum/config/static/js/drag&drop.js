    function updatePreview(input, target) {
    let file = input.files[0];
    let reader = new FileReader();

    reader.readAsDataURL(file);
    reader.onload = function () {
        let img = document.getElementById(target);
        // can also use "this.result"
        img.src = reader.result;
    }
}
let file = document.getElementsByClassName('file')[0];
file.addEventListener('change', function() {
    if(file && file.value) {
        let val = file.files[0].name;
        console.log(document.getElementById('value').innerHTML, "Вибрано" + val)
        document.getElementById('value').innerHTML = "Вибрано: " + val;
    }
});