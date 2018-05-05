function queryDates() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var dates = JSON.parse(this.responseText)
            displayDates(dates)
        }
    };
    var date_param = document.getElementById('timestamp_param').value
    if (date_param == '') {
        date_param = ' '
    }
    xhttp.open("GET", "/"+date_param+"/", true);
    xhttp.send();
}

function displayDates(dates) {
    var unix = dates['unix'] == null ? "Not a date" : dates['unix']
    var natural = dates['natural'] == null ? "Not a date" : dates['natural']
    document.getElementById('unix').innerHTML="Timestamp: " + unix
    document.getElementById('natural').innerHTML="Date: " + natural
}
