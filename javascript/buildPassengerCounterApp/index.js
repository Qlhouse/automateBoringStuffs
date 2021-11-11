// document.getElementById("count-el").innerText = 7;

// let bonusPoints = 50

// bonusPoints = bonusPoints + 50
// console.log(bonusPoints)

let countEl = document.getElementById("count-el")
let saveEl = document.getElementById('save-el')
// console.log(countEl)
let count = 0

function increment() {
    count += 1
    countEl.textContent = count
}

function save() {
    let countStr = count + ' - '
    saveEl.textContent += countStr   // defference innerText vs. textContent
    count = 0
    countEl.textContent = count   
}

// let name = 'John'
// let greeting = "Welcome back "
// welcome = document.getElementById('welcome-el');
// welcome.innerText = greeting + name
// welcome.innerText += '👏'



// ################ function #####################
let myPoints = 3

function add3Points() {
    myPoints += 3
}

function remove1Points() {
    myPoints -= 1
}

add3Points()
add3Points()
add3Points()
remove1Points()
remove1Points()

// console.log(myPoints)



// ################ render error #####################
let errorTag = document.getElementById("error")

function purchase() {
    errorTag.textContent = "Something wront! Please try again."
}



// ################ calculator #####################
let num1 = 8
let num2 = 2
document.getElementById('num1-el').textContent = num1
document.getElementById('num2-el').textContent = num2
let resultEl = document.getElementById('result-el')

function add() {
    let result = num1 + num2
    resultEl.textContent = "Sum: " + result
}

function subtract() {
    let result = num1 - num2
    resultEl.textContent = "Subtract: " + result
}

function divide() {
    let result = num1 / num2
    resultEl.textContent = "Divide: " + result
}

function multiply() {
    let result = num1 * num2
    resultEl.textContent = "Multiply: " + result
}