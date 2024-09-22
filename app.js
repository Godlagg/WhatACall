
window.addEventListener("DOMContentLoaded", () => {
var miningtextID =document.getElementById('miningtext')
var buttonminID =document.getElementById('buttonmin') 
if(sessionStorage.getItem('scor')){
    var score = parseInt(sessionStorage.getItem('scor'));
    miningtextID.textContent='Your mining:' + score;
}
else {
    var score = 0
}
var score2 = 1;
buttonminID.addEventListener('click', function(){
    score = score + score2;
    sessionStorage.setItem('scor',score);
    miningtextID.textContent='Your mining:'+score;});
document.addEventListener('keydown', function(event){
     if(event.keyCode=13){
        buttonminID.blur();
     }
});
});


