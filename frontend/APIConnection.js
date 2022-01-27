const Http = new XMLHttpRequest();
const url='https://stroke-service.herokuapp.com/stroke_proba';

function getPrediction(){
  
  queryString = prepareQueryString()
  if(isInvalid(queryString)){
    return
  }
  Http.open("GET", url + '?' + queryString, true);
  Http.send();
  
  Http.onreadystatechange = (e) => {
    if (Http.readyState == 4) {
      if(Http.status == 200)
        parseResponse(Http.responseText)
      else
        alert('Error with connection to the server');
   }
  }  
}

function isInvalid(queryString){
  var urlParams = new URLSearchParams(queryString);
  var missingKeys = [];
  var radioKeys = ['gender', 'Residence_type', 'ever_married', 'work_type', 'smoking_status'];
  urlParams.forEach((value, key) => {
      if(value == ""){
        missingKeys.push(key);
      }
  })
  radioKeys.forEach(rKey => {
    if(!urlParams.has(rKey)) missingKeys.push(rKey);
  })
  if(missingKeys.length > 0){
    alert("These fields can't be empty:\n" + missingKeys.join(separator = '\n'));
    return true;
  }
  return false;
}

function prepareQueryString(){
  return $('form').serialize()
}

function parseResponse(responseText){
  var res = JSON.parse(responseText);
  $('#predictionOut').text("The chance of getting stroke is about : " + Math.round(res.Proba * 100) + "%")
}