let cards
let team


window.onload = function () {
    window.scrollTo(0, 300);

    cards = document.querySelectorAll(".card")
    console.log(cards)

    let popup = document.getElementById("popup");
    popup.addEventListener("click", displayPopup);

    let value = localStorage.getItem("team")
    console.log(value);
    if (value != null) {
        team = JSON.parse(value);
    } else {
        team = []
    }
    console.log(team);

    checkTeam()
    generateModal()

}

function addTeam(url, name, id) {
    team.push({url, name, id});
    localStorage.setItem("team", JSON.stringify(team));
    console.log(team);

    checkTeam()
    generateModal()
    displayPopup()
}

function delTeam(index) {
    team.splice(index, 1);
    localStorage.setItem("team", JSON.stringify(team));
    console.log(team);
    checkTeam()
    generateModal()

}

function delAllTeam() {
    team = [];
    localStorage.setItem("team", JSON.stringify(team));

    console.log(team);

    checkTeam()
    generateModal()

}

function checkTeam() {
    document.querySelectorAll('.team-add').forEach((i) => {
        i.classList.remove('opacity-20', 'pointer-events-none');
    })

    if (team.length >= 5) {
        document.querySelectorAll('.team-add').forEach((i) => {
            i.classList.add('opacity-20', 'pointer-events-none');
        })
    }
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


function generateModal() {
    let genemodal = document.getElementById("genemodal");
    genemodal.addEventListener("click", hideModal);
    let elem = document.getElementById("team");
    elem.innerHTML = '';

    console.log("team");
    console.log(team);
    let lengthTeam = team.length >= 5 ? 5 : team.length;
    for (let i = 0; i < lengthTeam; i++) {
        let t = team[i];
        console.log(t);
        elem.innerHTML += '<div class="flex py-4 justify-start w-full">' +
            '<a href="' + t.id + '" class="flex flex-col items-center justify-center my-2 mr-4 hover:scale-105">' +
            '<img src=' + t.url + ' alt="image" class="h-16 w-16" alt="Pokemon">' +
            '<div class="flex flex-col justify-center items-center">' +
            '<p class="font-semibold text-sm opacity-80">' +
            t.name +
            '</p>' +
            '</div>' +
            '</a>' +
            '<div class="flex flex-col justify-center items-center">' +
            '<button class="hover:scale-105" onclick="delTeam(' + i + ')" >' +
            '<img src="../static/pokedex/Ressources/del-poke.svg" alt="del-poke" class="w-8 h-8">' +
            '</button>' +
            '</div>' +
            '</div>';
    }
}


function showModal() {
    document.querySelectorAll(".modal").forEach((i) => {
        i.classList.remove("hidden")
    })
}


function hideModal() {
    document.querySelectorAll(".modal").forEach((i) => {
        i.classList.add("hidden")
    })
}

function hidePopup(){
    let popup = document.getElementById("popup");
    popup.classList.add("opacity-0","z-0");
}

function displayPopup(){
    let popup = document.getElementById("popup");
    popup.classList.remove("opacity-0","z-0");
    setTimeout(hidePopup, 1000);
}