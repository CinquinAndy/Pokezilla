let cards


window.onload = function () {

    window.scrollTo(0, 300);

    cards = document.querySelectorAll(".card")
    console.log(cards)


}


function search(input) {
    console.log("text : " + input)

    var i;
    for (i = 0; i < cards.length; i++) {

        if (cards[i].innerHTML.includes(input)) {
            console.log(cards[i]);


        }
        else {
            cards[i].classList.add('hidden');
        }



    }


}