
function getDataForm(e) {
    e.preventDefault();
    const formData = new FormData(form[0]);
    const loadMSG = document.querySelector(".txt");

      


    let responseArray = [];

    let twitterState = ["healthy", "careful", "read the newspaper"];
    let buttonColours = ["green", "orange", "red"];
    const ws = new WebSocket('ws://localhost:8080');
    const trackWord = formData.get('keyWord');

    const r = document.querySelector(':root');
    r.style.setProperty("--analyse-op", "100");


    ws.onopen = function (eve)  {
        console.log("Connected");
        ws.send(trackWord.toString());
    };

    console.log("data sent");

    ws.onmessage = (evt) => {

        const data = evt.data.toString();
        responseArray.push(data);

        if (responseArray.length === 10){
            loadMSG.innerHTML= twitterState[parseInt(responseArray[responseArray.length - 1])]
            r.style.setProperty("--color-two", buttonColours[parseInt(responseArray[responseArray.length - 1])]);
            submitInput.classList.remove("button--loading")
            ws.close();
        }
    };
}

const form = document.querySelectorAll(".form"),
    submitInput = form[0].querySelector(".button");


document.addEventListener("DOMContentLoaded", function (){
    submitInput.addEventListener("click", getDataForm, false);
}, false);