function addItemForm(postId){
    console.log('AddItemForm button clicked');
    var itemDiv = document.querySelector(`#items${postId}`);
    document.querySelector(`#addbtn${postId}`).style.display = 'none'

    var form = document.createElement('form')
    form.id = `itemForm${postId}`;

    var content = document.createElement("input");
    content.type = "text";
    content.class = "textinput"
    content.required = true
    content.id = `content${postId}`;
    form.appendChild(content);

    var btn = document.createElement('button');
    btn.type = "submit";
    btn.textContent = "Save";
    btn.className = "button";
    form.appendChild(btn);
    btn.addEventListener('click', (e) => {
        e.preventDefault ()
       console.log('Add item button clicked');
       saveItem(postId)
   });

   itemDiv.appendChild(form);
}


function saveItem(postId){
    var content = document.querySelector(`#content${postId}`).value;

    if (content.trim() === "") {
        alert("The input field is required!");
        return
    }

    let csrftoken = document.cookie;
    const actualToken=csrftoken.split('=')[1]
    fetch('/add_item', {
        method: 'POST',
        headers: {
            "X-CSRFToken": actualToken
        },
        body: JSON.stringify({
            content: content,
            post: postId
        })
    })
        .then(response => response.json())
        .then(result => {
            console.log(result.message);})


    document.querySelector(`#addbtn${postId}`).style.display = 'block';
    document.querySelector(`#itemForm${postId}`).style.display = 'none';
    
    var itemDiv = document.querySelector(`#notCompletedItem${postId}`);
    var item = document.createElement('div')
    item.innerText = `${content}`;
    itemDiv.appendChild(item);


}


function completed(itemId){
    console.log(`completed${itemId}`)
    let csrftoken = document.cookie;
    const actualToken=csrftoken.split('=')[1]
    fetch('/completed', {
        method: 'PUT',
        headers: {
            "X-CSRFToken": actualToken
        },
        body: JSON.stringify({
            postItemId: itemId
        })
    })
        .then(response => response.json())
        .then(result => {
            console.log(result.message);})


    document.querySelector(`#item${itemId}`).style.display = 'none';
    
    var itemDiv = document.querySelector(`#notCompletedItem${itemId}`);
    var item = document.createElement('div')
    item.innerHTML = `${content}<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9 16.2L4.8 12L9 7.8L6.6 5.4L5.4 6.6L9 10.2L15.6 3.6L16.8 4.8L9 16.2Z" fill="#00C853"/></svg>`;
    itemDiv.appendChild(item);
}