function sendMessage() {
    let input = document.getElementById("input").value;
    document.getElementById("output").innerText = "Бабка думает...";
    
    fetch("/get_response?msg=" + input)
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText = data.response;
    });
}
