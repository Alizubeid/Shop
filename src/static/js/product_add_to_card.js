function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}
function setCookie(cname, cvalue) {
    document.cookie = cname + "=" + cvalue + ";";
}

function addToCard(Product_ID){
    let cart = getCookie("cart");
    if (cart == ""){
        setCookie("cart",`{ "${Product_ID}" : 1 }`);
    }
    else{
        let data = JSON.parse(cart);
        let get_product = data[`${Product_ID}`];
        if (get_product){
            data[`${Product_ID}`]++;
            console.log(data);
            setCookie("cart",JSON.stringify(data));
        }
        else{
            data[`${Product_ID}`] = 1;
            setCookie("cart",JSON.stringify(data));
        }
    }
}
