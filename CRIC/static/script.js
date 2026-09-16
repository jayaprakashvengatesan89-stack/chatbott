const form=document.getElementById("form");
const input=document.getElementById("input");
const messages=document.getElementById("messages");
const welcome=document.getElementById("welcome");
const sidebar=document.getElementById("sidebar");

function addMessage(text,type){
  const row=document.createElement("div");
  row.className="message "+type;
  const bubble=document.createElement("div");
  bubble.className="bubble";
  bubble.textContent=text;
  row.appendChild(bubble);
  messages.appendChild(row);
  messages.scrollTop=messages.scrollHeight;
  return bubble;
}

function showTyping(){
  const row=document.createElement("div");
  row.className="message bot";
  row.id="typing";
  const bubble=document.createElement("div");
  bubble.className="bubble";
  bubble.innerHTML='<span class="typing"><i></i><i></i><i></i></span>';
  row.appendChild(bubble);
  messages.appendChild(row);
  messages.scrollTop=messages.scrollHeight;
  return row;
}

async function sendMessage(text){
  if(welcome) welcome.style.display="none";
  addMessage(text,"user");
  const typing=showTyping();
  try{
    const response=await fetch("/chat",{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({message:text})
    });
    const data=await response.json();
    typing.remove();
    addMessage(data.reply || "I couldn't generate a response.","bot");
  }catch(error){
    typing.remove();
    addMessage("Unable to connect to the CRIC server. Please make sure Flask is running.","bot");
  }
}

form.addEventListener("submit",event=>{
  event.preventDefault();
  const text=input.value.trim();
  if(!text) return;
  input.value="";
  sendMessage(text);
});

function quickAsk(question){
  input.value=question;
  input.focus();
  form.dispatchEvent(new Event("submit"));
  if(window.innerWidth<=800) sidebar.classList.remove("open");
}

function newChat(){
  document.querySelectorAll(".message").forEach(el=>el.remove());
  if(welcome) welcome.style.display="";
  input.value="";
  input.focus();
}

function toggleTheme(){
  document.body.classList.toggle("dark");
  localStorage.setItem("cric-theme",document.body.classList.contains("dark")?"dark":"light");
}

function toggleSidebar(){
  sidebar.classList.toggle("open");
}

if(localStorage.getItem("cric-theme")==="dark") document.body.classList.add("dark");
