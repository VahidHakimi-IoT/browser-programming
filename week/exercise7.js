const output = document.getElementById("output")

function log(text){
    output.textContent += text + "\n"
}

function clearOutput(){
    output.textContent = ""
}

document.getElementById("btnLoadUsers").onclick = loadUsers

async function loadUsers(){

    clearOutput()

    // TODO: fetch users from API

}