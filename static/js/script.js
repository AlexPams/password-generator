const ch1 = document.getElementById("checkbox1");
const ch2 = document.getElementById("checkbox2");
const ch3 = document.getElementById("checkbox3");
const symbols = document.getElementById("symbols");
let letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ";
let digits = "1 2 3 4 5 6 7 8 9 0 ";
let specialSymbols = "!  # $ % & ' ( ) * + , - _ [ ] / . ^ '\\' `  : ; < = > ? @ { | } ~ ";
let startStr = "Введите нежелательные символы";


$(window).on('load', function() {
  $('.preloader').fadeOut().end().delay(400).fadeOut('slow');
});


function chbox1(params) {
  if (ch1.checked) {
    if(symbols.value == startStr){
      symbols.value = letters;
    }else{
      symbols.value += letters;
    }
		
	}
	else {
		symbols.value = symbols.value.replace(letters, "");
	}
}


function chbox2(params) {
  if (ch2.checked) {
    if(symbols.value == startStr){
      symbols.value = specialSymbols;
    }else{
      symbols.value += specialSymbols;
    }
		
	}
	else {
		symbols.value = symbols.value.replace(specialSymbols, "");
	}
}


function chbox3() {
  if (ch3.checked) {
    if(symbols.value == startStr){
      symbols.value = digits;
    }else{
      symbols.value += digits;
    }
		
	}
	else {
		symbols.value = symbols.value.replace(digits, "");
	}
}


var textarea = document.querySelector('textarea');
textarea.addEventListener('keyup', function(){
  if(this.scrollTop > 0){
    this.style.height = this.scrollHeight + "px";
  }
});

function generate() {
            $.ajax({
                type: "POST",
                url: "/generate",
                data: $('form').serialize(),
                type: 'POST',
                success: function(response) {
                    var json = jQuery.parseJSON(response)
                    $('#passw').html(json.passw)
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }