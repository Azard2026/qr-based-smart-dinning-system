var names = document.querySelector("#name");
var price = document.querySelector("#price");
var bill = document.querySelector("#total");
var remove = document.querySelector("#remove");
var qty = document.querySelector("#quantity");
var quantity = 1;


function shoppingCart(){


    var orders= JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    

    names.innerHTML = '<h5>Name</h5>';
    price.innerHTML= '<h5>Price</h5>';
    remove.innerHTML = '<h5><br></h5>';
    //
    qty.innerHTML ='<h5>Quantity</h5>';
    ///quantity
  
    
    
    for (let i=0; i< cartSize; i++){
        
        remove.innerHTML += '<h6 class="mt-3"><button class=btn-danger onclick="removeItem('+i+')">X</button></h6>';
        names.innerHTML += '<h6 class="mt-3">'+orders[i][0]+'</h6>';
        ////qty
        qty.innerHTML +='<h6>'+'<button class="btn btn-danger" onclick="decrement('+i+')">-</button>'+orders[i][1]+'<button class="btn btn-success"  onclick="increment('+i+')">+ </button>'+'</h6>'
        
        // qty.innerHTML += '<h4>'+'<button class=btn-secondary onclick="decrement()">-</button>&nbsp;'+qtys +'&nbsp;<button class=btn-secondary onclick="increment()">+</button></h5>'+'</h4>';
      

        price.innerHTML += '<h6 class="mt-4">'+'₹'+orders[i][2]+'</h6>';
            
    }
    bill.innerHTML = 'Total:₹'+total;
   

    
}

shoppingCart();
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
    shoppingCart();

 }
 //decrement quentity 
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

    shoppingCart();

 }







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
    shoppingCart();

}

/// ajax method to get the data
 
var notes = document.querySelector('#message');
function order()
{

   var msg = notes.value;
   var orders = localStorage.getItem('orders');
   var total = localStorage.getItem('total');

   var ur = '/food/order';
   var orderData = {};
   orderData['orders'] = orders;
   orderData ['notes'] = msg;
   orderData['total']= total;

   $.ajax(
       {
           url: ur,
           type: "POST",
           data: orderData,
           headers: {
               "X-Requested-With": "XMLHttpRequest",
               
             },
           success: function(data){
            //it redirect the page when the user click submit

            window.location.replace('/food/success')
            localStorage.setItem('orders', JSON.stringify([]));
            localStorage.setItem('total', 0);

        }
       }
   );
   }
