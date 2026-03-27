// selectionnena n element html 
const fenetre = document.getElementById("fenetre")

// message d'info 
const info = document.querySelector(".info")

// tous le sbutton 
const button = document.querySelectorAll("button")

const egal = document.getElementById("egal")

const reset = document.getElementById("reset")
// boucle @naz aby 
button.forEach(
    button => {
        button.addEventListener("click",() =>{
            // maka text buttn 
            const value = button.textContent
            if(value !== "=" && button !== reset)
            {
                // ajouter la valeur dans la zone d'affiche 
                fenetre.value += value
                // mamafa 
                info.innerText = ""
            }
        })
    }
)
egal.addEventListener("click",() => {
    // SI RIEN N ES ENTRE 
    if(fenetre.value === "") {
        // SOLON MESS ERREUR 
        info.innerText = "MAMPIDIRA ISA"
return
    }
    try{
        fenetre.value = eval(fenetre.value)
    } catch (error) {
        info.innerText = "Erreur de calcul"
        fenetre.value = ""
    }
})
reset.addEventListener("click", () => {
    // vide la zone debugger'affiche 
    fenetre.value =""
// mamafa ny eo 
    info.innerText = ""

}
)