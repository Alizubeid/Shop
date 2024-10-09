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
    console.log(document.cookie);
    let cart = getCookie("cart");
    if (cart == ""){
        setCookie("cart",`{ "${Product_ID}" : 1 }`);
        let price = document.getElementById(`product_${Product_ID}_amount`).innerHTML;
        let total = data[`${Product_ID}`] * price;
        document.getElementById(`product_${Product_ID}_total`).innerHTML = total;
        document.getElementById("total_match").innerHTML = Number(document.getElementById("total_match").innerHTML) + Number(price);
    }
    else{
        let data = JSON.parse(cart);
        let get_product = data[`${Product_ID}`];
        if (get_product){
            data[`${Product_ID}`]++;
            setCookie("cart",JSON.stringify(data));
            let price = document.getElementById(`product_${Product_ID}_amount`).innerHTML;
            let total = data[`${Product_ID}`] * price;
            document.getElementById(`product_${Product_ID}_total`).innerHTML = total;
            document.getElementById("total_match").innerHTML = Number(document.getElementById("total_match").innerHTML) + Number(price);
        }
        else{
            data[`${Product_ID}`] = 1;
            setCookie("cart",JSON.stringify(data));
            let price = document.getElementById(`product_${Product_ID}_amount`).innerHTML;
            let total = data[`${Product_ID}`] * price;
            document.getElementById(`product_${Product_ID}_total`).innerHTML = total;
            document.getElementById("total_match").innerHTML = Number(document.getElementById("total_match").innerHTML) + Number(price);
        }
    }
}

function oddToCard(Product_ID){
    console.log(document.cookie);
    let cart = getCookie("cart");
    if (cart != ""){
        let data = JSON.parse(cart);
        if (data[`${Product_ID}`] > 0){
            data[`${Product_ID}`]--;
            if (data[`${Product_ID}`] == 0){
                delete data[`${Product_ID}`];
            }
            setCookie("cart",JSON.stringify(data));
            let price = document.getElementById(`product_${Product_ID}_amount`).innerHTML;
            let total = data[`${Product_ID}`] * price;
            document.getElementById(`product_${Product_ID}_total`).innerHTML = total;
            document.getElementById("total_match").innerHTML = Number(document.getElementById("total_match").innerHTML) - price;
        }
    }
}

let cart = getCookie("cart");
let data = JSON.parse(cart);
if (cart != "" ){
    for (var product in data){
        try{
            document.getElementById(`product_${product}`).value = data[product];
            let price = document.getElementById(`product_${product}_amount`).innerHTML;
            let total = document.getElementById(`product_${product}`).value * price;
            document.getElementById(`product_${product}_total`).innerHTML = total;
            document.getElementById("total_match").innerHTML = Number(document.getElementById("total_match").innerHTML) + total;
        }
        catch(err){
            
        }
        
    }
}

