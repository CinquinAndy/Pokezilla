let cards


window.onload = function () {

    window.scrollTo(0, 300);

    cards = document.querySelectorAll(".card")
    console.log(cards)


}


function search(input) {
    console.log("text : " + input)
    const title = document.querySelector("#title")

    if (input !== "") {
        title.classList.add('hidden');
    } else {
        title.classList.remove('hidden');

    }


    var i;
    for (i = 0; i < cards.length; i++) {

        cards[i].classList.remove('hidden');


        if (!cards[i].innerHTML.includes(input)) {
            cards[i].classList.add('hidden');
        }


    }


}