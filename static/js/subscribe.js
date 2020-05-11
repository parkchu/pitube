const sub_div = document.querySelector(".sub")
const sub_btn = sub_div.querySelector(".sub-btn")
const user_div = document.querySelector(".like")
const channel_id = parseInt(sub_btn.value)
const sub_a = sub_div.querySelector(".sub-a")
const total_sub = sub_div.querySelector(".total-sub")
const thisUser = parseInt(user_div.id)

function handleSub(event) {
    event.preventDefault()
    const btn = sub_div.querySelector(".btn")
    let total_subscribe = parseInt(total_sub.classList[1])
    console.log(total_subscribe)
    if (btn.value == 'sub') {
        btn.value = 'noSub'
        sub_btn.innerText = '구독'
        total_sub.innerText = `구독자 ${total_subscribe - 1}명`
        total_sub.classList.remove(total_subscribe)
        total_sub.classList.add(total_subscribe - 1)
        fetch(`http://localhost:1204/channel/${channel_id}/`, {
        method: 'PUT',
        body: JSON.stringify({
            user_id: thisUser,
            whether: "cancel",
            channel_id: channel_id
        }),
        headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
    })
    } else {
        btn.value = 'sub'
        sub_btn.innerText = '구독중'
        total_sub.innerText = `구독자 ${total_subscribe + 1}명`
        total_sub.classList.remove(total_subscribe)
        total_sub.classList.add(total_subscribe + 1)
        fetch(`http://localhost:1204/channel/${channel_id}/`, {
        method: 'PUT',
        body: JSON.stringify({
            user_id: user_id,
            whether: "subscribe",
            channel_id: channel_id
        }),
        headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
    })
    }
}

function addSub(channel) {
    const btn = document.createElement('button')
    total_sub.innerText = `구독자 ${channel.subscribe.length}명`
    total_sub.classList.add(channel.subscribe.length)
    btn.hidden = true
    btn.classList.add("btn")
    console.log(channel.subscribe, user_div.id, channel.owner)
    if (user_div.id == channel.owner) {
        sub_btn.hidden = "true"
        console.log("로그인함 주인임")
    } else if (user_div.id != channel.owner && user_div.id != "None" && !channel.subscribe.includes(parseInt(user_div.id))){
        console.log("로그인함 주인아님 구독안함")
        sub_btn.innerText = "구독"
        btn.value = "noSub"
    } else if (channel.subscribe.includes(parseInt(user_div.id)) && user_div.id != "None" && user_div.id != channel.owner) {
        console.log("로그인함 주인아님 구독함")
        sub_btn.innerText = "구독중"
        btn.value = 'sub'
    } else {
        console.log("비로그인")
        sub_btn.innerText = "구독"
        sub_a.href = `/accounts/login/?next=${window.location.pathname}`
    }
    sub_div.appendChild(btn)
}

function init() {
    if (user_div.id != 'None') {
        sub_btn.addEventListener("click", handleSub)
    }
    fetch(`http://localhost:1204/channel/${channel_id}/`).then(function(json){
        return json.json()
    }).then(function(obj){
        addSub(obj)
    })
}

init()