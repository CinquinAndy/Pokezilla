let cards


window.onload = function () {

    window.scrollTo(0, 300);

    cards = document.querySelectorAll(".card")
    console.log(cards)

}


function search(input) {
    console.log("text : " + input)

    for (e in cards) {

        if (e.  includes(input)) {
            console.log(e)


        }
    }

}