function sendMessage(){
    const input = document.getElementById("user-input");
    const message = input.value;
    if(!message) return;
    addMessage(message, "user");
    input.value = "";
    
    fetch("/ask", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({message: message})
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.response, "susu");
    });
}

function addMessage(msg, sender){
    const box = document.getElementById("chat-box");
    const div = document.createElement("div");
    div.className = sender === "user" ? "user-msg" : "susu-msg";
    div.innerText = msg;
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
      }
