function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getToken('csrftoken');

var user = localStorage.getItem("user");
// console.log("user is: ",user);

var cartButtons = document.getElementsByClassName("cartbtn");
for(var i=0; i<cartButtons.length; i++){
cartButtons[i].addEventListener("click",function(){
  var item_id = this.dataset.item_id;
  var action = this.dataset.action;
  // console.log("id:",item_id, "act: ",action);
  if(user === 'AnonymousUser'){
    console.log("aditya");
  }
  else{
  updateUserOrder(item_id,action);
  }
});
}
function updateUserOrder(item_id,action){
var url = "/update_item/";

fetch(url,{
  method: 'POST',
  headers:{
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken,
  },
  body:JSON.stringify({"item_id": item_id, "action":action})
})
.then((response)=>{
  return response.json();
})
.then((data)=>{
  console.log("data:",data);
    if(data["action"] === "buy"){
      location = "/cart/cart";
    }
    else{
      location.reload();
    }
  });
}
