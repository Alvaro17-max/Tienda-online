//Animacion de escritura
const texto="aqui!!";
const nombre=document.getElementById("titulo_registro");
const apellido=document.getElementById("titulo_registro");
const dni=document.getElementById("titulo_registro");

let i=0;
function escribir(){
    if( i < texto.length){
        document.getElementById("titulo_registro").textContent+=texto.charAt(i);
        i++;
        setTimeout(escribir,100);
    }
}
escribir();