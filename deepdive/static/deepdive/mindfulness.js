document.addEventListener('DOMContentLoaded' ,() =>{
    fetch("https://api.themotivate365.com/stoic-quote")
    .then(res => res.json())
    .then(res => {
        console.log(res);
        document.getElementById('stoicQuote').innerHTML = `<h2>${res.quote}</h2>-${res.author}`
    })

    fetch("https://api.adviceslip.com/advice")
    .then(res => res.json())
    .then(res => {
        console.log(res);
        document.getElementById('adviceQuote').innerHTML = `<h2>${res.slip.advice}</h2>`
    })
})


document.querySelector('#imageCreatorForm').addEventListener(
    'submit', e =>{
        e.preventDefault()
        query = document.getElementById('query').value;
        console.log(query)

        imgDiv = document.getElementById('imageCreator');
        loading = document.createElement('div');
        loading.id = 'loading';
        loading.innerText = "loading..."
        imgDiv.appendChild(loading)

        fetch('/create_image', {
            method: 'POST',
            body: JSON.stringify({
                query : query
            })
        })
            .then(response => response.json())
            .then(res => {
                document.getElementById('loading').remove();
                for (const key in res) {
                    const element = document.createElement('img');
                    element.src = res[key];
                    imgDiv.appendChild(element);
                  }
            })
}
    
)
