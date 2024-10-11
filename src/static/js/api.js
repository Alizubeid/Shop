const HttpRespose = new XMLHttpRequest();

HttpRespose.onload = function(){
    console.log(this.responseText);
}  
HttpRespose.open("GET","api/products/",true);
HttpRespose.send();
