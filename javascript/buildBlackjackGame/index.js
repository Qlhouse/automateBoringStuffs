let firstCard = 10
let secondCard = 7
let sum = firstCard + secondCard
let hasBlackJack = false
let isAlive = true
let message = ''
let messageEl = document.getElementById("message-el")
// let sumEl = document.getElementById("sum-el")
let sumEl = document.querySelector("#sum-el")
let cardEl = document.querySelector("#card-el")

function startGame() {
    sumEl.textContent = "Sum: " + sum
    cardEl.textContent = "Cards: " + firstCard + ' ' + secondCard
    if (sum <= 20) {
        message = "Do you want to draw a new card?"
    } else if (sum === 21) {
        message = "Wohoo! You've got Blackjack!"
        hasBlackJack = true
    } else {
        message = "You're out of the game!"
        isAlive = false
    }

    messageEl.textContent = message;
    // console.log(hasBlackJack)
    // console.log(isAlive)
}

function newCard() {
    console.log("New card!")
}

// 02:22:54.679