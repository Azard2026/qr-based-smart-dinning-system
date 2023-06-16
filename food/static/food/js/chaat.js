var pcart = document.querySelector('#pcart');
var ptotal = document.querySelector('#ptotal');


///update the cart lengh
var cart = document.querySelector('#cart');
var orders = JSON.parse(localStorage.getItem('orders'));
cart.innerHTML = orders.length;

function clears(){

    localStorage.setItem('orders', JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'));
    localStorage.setItem('total', 0);
    orders = JSON.parse(localStorage.getItem('total'));
}
// ADD chaat
function addChaat(cid){
    alert('item added successfully');
    //get chaat name
    chaatId = '#chaat'+cid;
    var name = document.querySelector(chaatId).innerHTML;
    // get the chaat price
  
    var radio = '#price'+cid
    
    var price = document.querySelector(radio).innerHTML;
    var quentity=1
    var duplicateprice=price

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

    
    removebtn = '<button class= btn btn-danger onclick="removeItem('+cartSize+')">X</button>';
    pcart.innerHTML += '<li>'+name+''+' ---> ₹'+quentity+' '+price+''+removebtn+'</li>';
    ptotal.innerHTML = 'Total:'+total;
    
}

function cshoppingCart(){


    var orders= JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    pcart.innerHTML='';
    
    
    for (let i=0; i< cartSize; i++){
        
        removebtn = '<button class=btn-danger onclick="removeItem('+i+')">X</button>';
        pluss='<button class="btn-success" onclick="increment('+i+')"> +</button>'
        minuss='<button class="btn-danger" onclick="decrement('+i+')">-</button>'

        pcart.innerHTML += '<li>'+orders[i][0]+' --->  '+''+minuss+''+orders[i][1]+''+pluss+'&nbsp;&nbsp;'+'₹'+orders[i][2]+removebtn+'</li>';

    }
    ptotal.innerHTML = 'Total:₹'+total;
}

cshoppingCart();
//increment quantity function
function increment(n){

    var orders = JSON.parse(localStorage.getItem('orders'));
    //USE IT FOR OVER ALL CALCULATION
    var total = localStorage.getItem('total');
//increase the quentity number
    orders[n][1]+=Number(1);
    // console.log(orders[n][2]);
//adding the price as per the quentity
    orders[n][2]=Number(orders[n][2])+Number(orders[n][3]);
    // console.log(orders[n][3]);
//ADD THE TOTAL
    total = Number(total) + Number(orders[n][3]);
    

    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total',total);
    cshoppingCart();

 }
 function decrement(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');//TOTAL COUNT

    
    //decrease the quentity
    orders[n][1]-=Number(1);
    if (orders[n][1]==0){
        orders[n][1]=1;
        
        total = Number(total)

    }
    else
    {
        total = Number(total) - Number(orders[n][3]);
    }
    // console.log(orders[n][4]);
    //decrease the  price as per the rate
    if(orders[n][2]==Number(orders[n][3]) ||  orders[n][2]<=Number(orders[n][3]) ){
        orders[n][2]=Number(orders[n][3]);
    }
    else{

        orders[n][2]=Number(orders[n][2])-Number(orders[n][3]);

    }
    // if (orders[n][2]!=1){
    
    //     total = Number(total) - Number(orders[n][4]);
    //     log(total)     

    // }
    // while(orders[n][2]<Number(1)){

    //     total = Number(total) - Number(orders[n][4]);
    // }
    // //DECREMENT TOTAL
    
    console.log(n);
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total',total);

    cshoppingCart();

 }



///remove the chaat item in the cart page

function removeItem(n)
{
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total)- Number(orders[n][2]);
    orders.splice(n,1);
    //updating  number of the cartsize
    var cart = document.querySelector('#cart');
    cart.innerHTML = orders.length;
    

    localStorage.setItem('orders',JSON.stringify(orders));
    localStorage.setItem('total',total);
    cshoppingCart();

}
