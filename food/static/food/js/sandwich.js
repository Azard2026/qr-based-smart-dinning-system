var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');


///update the cart lengh
var cart = document.querySelector('#cart');
var orders = JSON.parse(localStorage.getItem('orders'));
cart.innerHTML = orders.length;


// ADD drink in shoping 
function addSandwich(wid){
    alert('item added successfully');
    //get chaat name
    sandwichId = '#sandwich'+wid;
    var name = document.querySelector(sandwichId).innerHTML;
    // get the chaat price
  
    var radio = '#wprice'+wid
    
    var price = document.querySelector(radio).innerHTML;
    var quentity=1
    var duplicateprice=Number(price)
   

    var orders= JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem("total");
    var cartSize = orders.length;
    // saving  item and total in localstorage
    orders[cartSize] = [name, quentity,duplicateprice,price];
    localStorage.setItem('orders', JSON.stringify(orders));
    

    total = Number(total)+(Number(price)*Number(quentity));
    localStorage.setItem('total',total);

    //updating  number of the cartsize
    var cart = document.querySelector('#cart');
    cart.innerHTML = orders.length;

    removebtn = '<button class=btn-danger onclick="removeItem('+cartSize+')">X</button>';

    pcart.innerHTML += '<li>'+name+' --->₹ '+''+quentity+price+removebtn+'</li>';
    ptotal.innerHTML = 'Total:'+total;
}
