const ATJAUNOT = 3000;
async function lasiChatu(){
    const atbilde = await fetch('/chats/lasi');
    const datuObjekts = await atbilde.json();
    raadiChatuVienkaarshi(datuObjekts);
    await new Promise(resolve => setTimeout(resolve, ATJAUNOT));
    await lasiChatu();
}
function raadiChatuVienkaarshi(dati){
    const jaunaRinda="<br />";
    let chats = "";
    let chataDiv = document.getElementById("chats");
    for(let rinda of dati['chats']){
        chats = chats + rinda + jaunaRinda;
    }
    chataDiv.innerHTML = chats;
}
async function suutiZinju(){
    let zinjasElements = document.getElementById("zinja");
    let zinja = zinjasElements.value;
    zinjasElements.value = "";
    const atbilde = await fetch('/chats/suuti', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"chats": zinja})
    });
    const datuObjekts = await atbilde.json();
    raadiChatuVienkaarshi(datuObjekts);
}
function raadiChatu(){
}