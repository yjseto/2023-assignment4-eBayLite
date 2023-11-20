document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('#new_comment').onsubmit = update_comments();
    setInterval(update_comments, 2000);
});

function update_comments() {
    fetch(`comment/status/${auction_id}`)
    .then(response=response.json)
    .then(data => {
        // document.querySelector('#all_comments').data[comments] = data[all_comments]
        console.log("Hello");
    })
}

