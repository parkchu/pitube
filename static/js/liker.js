const like_div = document.querySelector(".like")
const like_btn = like_div.querySelector(".like-btn")
const user_id = parseInt(like_div.id)
const video_id = parseInt(like_btn.id)
const like_a = like_div.querySelector(".like-a")
const like_span = like_div.querySelector(".total-good")
let video = null

function handleLike(event){
    event.preventDefault()
    if (like_btn.innerText == "좋아요") {
        like_span.innerText = parseInt(like_span.innerText) + 1
        like_btn.innerText = "좋아요 취소"
        fetch(`http://localhost:1204/video/${video_id}/`, {
        method: 'PUT',
        body: JSON.stringify({
            user_id: user_id,
            whether: "like",
            video_id: video_id
        }),
        headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
    })
    } else {
        like_span.innerText = parseInt(like_span.innerText) - 1
        like_btn.innerText = '좋아요'
        fetch(`http://localhost:1204/video/${video_id}/`, {
        method: 'PUT',
        body: JSON.stringify({
            user_id: user_id,
            whether: "dislike",
            video_id: video_id
        }),
        headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
    })
    }
}

function addText(video){
    like_span.innerText = `${video.good.length}`
    if (video.good.includes(user_id)) {
        like_btn.innerText = '좋아요 취소'
    } else if (!video.good.includes(user_id) && like_div.id != 'None') {
        like_btn.innerText = '좋아요'
    } else {
        like_a.href = `/accounts/login/?next=${window.location.pathname}`
        like_btn.innerText = 'test'
    }
}

function init(){
    if (like_div.id != 'None') {
        like_btn.addEventListener("click", handleLike)
    }
    fetch(`http://localhost:1204/video/${video_id}/`).then(function(json){
        return json.json()
        }).then(function(obj){
        video = obj
        addText(video)
    })
}

init()
