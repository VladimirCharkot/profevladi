// Método del colgadero
var mapa = {}

mapa['1a'] = {'0' : ['r'],
              '1' : ['t','d'],
              '2' : ['n'],
              '3' : ['m'],
              '4' : ['c', 'k', 'q'],
              '5' : ['l'],
              '6' : ['s','c'],
              '7' : ['f','j'],
              '8' : ['g','ch'],
              '9' : ['p','b','v']
            }

mapa['a1'] = {'b' : '9',
              'c' : '4',
              'd' : '1',
              'f' : '7',
              'g' : '8',
              'ch': '8',
              'j' : '7',
              'k' : '4',
              'l' : '5',
              'm' : '3',
              'n' : '2',
              'ñ' : '2',
              'p' : '9',
              'q' : '4',
              'r' : '0',
              's' : '6',
              't' : '1',
              'v' : '9',
              'z' : '6'
            }


function reemplazar_todas(texto, original, reemplazo){
  while (texto.includes(original)) texto = texto.replace(original, reemplazo);
  return texto;
}


function pickRandom(lista){
    return lista[Math.floor(Math.random() * lista.length)];
}



function numero_a_texto(numero){
  var palabra = numero.toString();
  for (var k in mapa['1a']){
    palabra = reemplazar_todas(palabra, k, pickRandom(mapa['1a'][k]));
  }
  return palabra;

}


var invisibles = ['a', 'á', 'e', ,'é', 'i', 'í', 'o', 'ó', 'u', 'ú', 'y', 'h', ' '];
function texto_a_numero(texto){

  texto = texto.toLowerCase();

  // reemplazo letras por números
  for (var letra in mapa['a1']){
    texto = reemplazar_todas(texto, letra, mapa['a1'][letra]);
  }

  // quito vocales y otros caracteres
  for (var i in invisibles){
    texto = reemplazar_todas(texto, invisibles[i], '');
  }

  return texto;

}


console.log(numero_a_texto(6427896));
console.log(texto_a_numero("Hola mamá estoy en el VS"))
