const Http = new XMLHttpRequest();
const url='https://stroke-service.herokuapp.com/stroke_proba';

function getPrediction(){
  console.log("Getting prediction")
  
  console.log(prepareQueryString())
  Http.open("GET", url + '?' + prepareQueryString(), true);
  Http.send();
  
  Http.onreadystatechange = (e) => {
    if (Http.readyState == 4) {
      if(Http.status == 200)
        parseResponse(Http.responseText)
      else
        dump("Błąd podczas ładowania strony\n");
   }
  }  
}


function prepareQueryString(){
  return $('form').serialize()
}

function parseResponse(responseText){
  var res = JSON.parse(responseText);
  $('#predictionOut').text("The chance of getting stroke is about : " + Math.round(res.Proba * 100) + "%")
}