// On récupère le fichiers fonctions.fr
const fonctions = require("./fonctions.js");
function askUser() {
  let choice = prompt("Choisissez un nombre entre 5, 7, 9 ou 11");
  return choice;
}

// On entre taille_du_tableau  dans taille du tableau la taille souhaiter par l'utilisateur
let taille_du_tableau = askUser();

// On affiche la taille du tableau
console.log(taille_du_tableau);
