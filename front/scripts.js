const URL ="https://v6.exchangerate-api.com/v6/31e6837d9bf5717e3d305eaf/latest/USD"
let apiJSON;
fetch(URL)
    .then(res => res.json())
    .then(data => {
        apiJSON = data;
        console.log(apiJSON); 
        console.log(apiJSON["conversion_rates"]);
    })
    .then(data => console.log(data))
    .catch(error => console.log("oopsie"))

function result(){
    let output = document.getElementById("news-input").value;
    document.getElementById("demo").innerHTML = output * apiJSON["conversion_rates"]["PHP"];
}