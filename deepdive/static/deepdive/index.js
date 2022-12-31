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
    content.focus()
    content.id = `content${postId}`;
    form.appendChild(content);

    br = document.createElement('br');
    form.appendChild(br);

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
            console.log(result.message);

        document.getElementById(`addbtn${postId}`).style.display = 'block';
        document.getElementById(`itemForm${postId}`).remove();

        itemDiv = document.getElementById(`notCompletedItem${postId}`);
        if (itemDiv === null){
            itemDiv = document.createElement('div')
            itemDiv.id = `#notCompletedItem${postId}`;
            document.getElementById(`items${postId}`).appendChild(itemDiv);
        }
        item = document.createElement('div')
        item.id = `item${result.id}`
        item.innerHTML = `${content}<button id="doneBtn${result.id}" class="button" onclick="completed(${result.id},${postId})">Done</button>`;
        itemDiv.appendChild(item);
        })

}


function completed(itemId,postId){
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


    itemDiv = document.querySelector(`#doneBtn${itemId}`).style.display = 'none';

}


//save new post
document.querySelector('#newPostForm').addEventListener('submit', function(event) {
    event.preventDefault();
    console.log('form submitted');
    title = document.querySelector("#newPostTitle").value;
    if (title.trim() === "") {
        alert("The input field is required!");
        return
    }
    desc = document.querySelector("#newPostDesc").value;
    image = document.querySelector("#newPostImage").value;
    page = document.querySelector("#newPostcategory").value.trim();
    console.log(page)
    
    let csrftoken = document.cookie;
    const actualToken=csrftoken.split('=')[1]
    fetch('/create_post', {
        method: 'POST',
        headers: {
            "X-CSRFToken": actualToken
        },
        body: JSON.stringify({
            title: title,
            desc: desc,
            image:image,
            page:page
        })
    })
        .then(response => response.json())
        .then(result => {
            console.log(result.message);
        })
    div = document.createElement('div');
    div.innerHTML =`<h5>Refresh to view new post.</h5>`;
    document.querySelector('#newPost').appendChild(div);
    //clears the fields
    document.querySelector("#newPostTitle").value = '';
    document.querySelector("#newPostDesc").value = '';
    document.querySelector("#newPostImage").value = '';
  });
  