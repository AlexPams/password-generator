let ch1 = document.getElementById("checkbox1")
let ch2 = document.getElementById("checkbox2")
let ch3 = document.getElementById("checkbox3")

function chbox1(params) {
  if (ch1.checked) {
		document.getElementById("symbols").value = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	}
	else {
		document.getElementById("symbols").value = "Введите нежелательные символы"
	}
}
function chbox2(params) {
  if (ch2.checked) {
		alert('Выбран');
	}
	else {
		alert ('Не выбран');
	}
}
function chbox3() {
  if (ch3.checked) {
		alert('Выбран');
	}
	else {
		alert ('Не выбран');
	}
}


var textarea = document.querySelector('textarea');
textarea.addEventListener('keyup', function(){
  if(this.scrollTop > 0){
    this.style.height = this.scrollHeight + "px";
  }
});