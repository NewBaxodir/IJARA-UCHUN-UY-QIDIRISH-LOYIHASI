  anime({
  targets: '.row svg',
  translateY: 10,
  autoplay: true,
  loop: true,
  easing: 'easeInOutSine',
  direction: 'alternate'
});

anime({
  targets: '#zero',
  translateX: 10,
  autoplay: true,
  loop: true,
  easing: 'easeInOutSine',
  direction: 'alternate',
  scale: [{value: 1}, {value: 1.4}, {value: 1, delay: 250}],
    rotateY: {value: '+=180', delay: 200},
});







  
    // const dataa = '{{street}}'

    // const data = '{{qs_json}}'
    // console.log(data)

    // const rdata = JSON.parse(data.replace(/&quot;/g, '"'))
    // console.log(rdata)



    // const input = document.getElementById('search_here')
    // console.log(input)

    // let filteredArr = []

    // input.addEventListener('keyup', (e)=>{
    //     box.innerHTML = ""
    //     filteredArr = rdata.filter(info=> info['address'].includes(e.target.value))
    //     console.log(filteredArr)
    //         if (filteredArr.length > 0){
    //         filteredArr.map(info=>{
    //             box.innerHTML += `

// <div class="card card bg-body ms-3" style="border-top-left-radius: 5px; border-top-right-radius: 5px; border-bottom-left-radius: 5px; border-bottom-right-radius: 5px; box-shadow: 0 7px 14px 0 rgb(59 65 94 / 10%), 0 3px 6px 0 rgb(0 0 0 / 7%);">
//   <div class="card-header bg-white" style="border-top-left-radius: 10px; border-top-right-radius: 10px;">
//   <h6 class="card-header-title text-capitalize pt-2" style="font-family: 'Baloo Chettan 2', cursive; font-size: 17px;">
//    ${info['address']}
//   </h6>
//   </div>
//   <div class="card-body">
//   <div class="container">
//     <div class="row">
    
//     <div class="col-12 col-sm-12 col-md-12 col-lg-3">
//     <img src="/media/${info['house_image']}" class="card-img-top" alt="...">
//     </div>

//   <div class="col-12 col-sm-12 col-md-12 col-lg-7">
//   <div class="row">
//   <div class="col-12 col-sm-12">

// <div class="row">
// <div class="col-sm">

// <table class="table-sm table-nowrap card-table">
// <tr><td class="goal-project rounded" style="color: #00864e; background-color: #ccf6e4; font-family: 'Baloo Chettan 2', cursive;">Iste'mol ehtiyojlari</td></tr>
// <tr><td class="goal-project"><span class="text-danger">●</span> ${info['sovuq_suv']}</td></tr>
// <tr><td class="goal-project"><span class="text-danger">●</span> ${info['issiq_suv']}</td></tr>
// <tr><td class="goal-project"><span class="text-danger">●</span> ${info['svet']}</td></tr>
// <tr><td class="goal-project"><span class="text-danger">●</span> ${info['gaz']}</td></tr>

// <tr><td class="goal-project rounded" style="color: #00864e; background-color: #ccf6e4; font-family: 'Baloo Chettan 2', cursive;">Elektron vositalari</td></tr>
// <tr><td class="goal-project"><span class="text-danger">●</span> ${info['wifi']}</td></tr>
// <tr><td class="goal-project"><span class="text-danger">●</span> ${info['sovutgich']}</td></tr>
// <tr><td class="goal-project"><span class="text-danger">●</span> ${info['kondisioner']}</td></tr>
// </table>
// </div>
// <div class="col-sm">
// <table>
  
// <tr><td class="goal-project rounded p-1" style="color: #00864e; background-color: #ccf6e4; font-family: 'Baloo Chettan 2', cursive;">Gigiyena sharaoidlar</td></tr>
// <tr><td class="goal-project"><span class="text-danger">●</span> ${info['hojat']}</td></tr>
// <tr><td class="goal-project"><span class="text-danger">●</span> ${info['hammom']}</td></tr>

// <tr><td class="goal-project rounded p-1" style="color: #00864e; font-family: 'Baloo Chettan 2', cursive;
//     background-color: #ccf6e4;">Xavfsizlik tizimi</td></tr>
// <tr><td class="goal-project"><span class="text-danger">●</span> ${info['xafsiz']}</td></tr>

// <tr><td class="goal-project rounded p-1" style="color: #00864e; font-family: 'Baloo Chettan 2', cursive;
//     background-color: #ccf6e4;">Kimlar uchun</td></tr>
// <tr><td class="goal-project"><span class="text-danger">●</span> ${info['kimlar']}</td></tr>

// <tr><td class="goal-project rounded p-1" style="color: #00864e; font-family: 'Baloo Chettan 2', cursive;
//     background-color: #ccf6e4;">Odamlar soni</td></tr>
//     <tr><td class="goal-project"><span class="text-danger">●</span> ${info['kishilar']}</td></tr>

// <tr><td class="goal-project rounded p-1" style="color: #00864e; font-family: 'Baloo Chettan 2', cursive;
//     background-color: #ccf6e4;">Uy holati</td></tr>
//     <tr><td class="goal-project"><span class="text-danger">●</span> ${info['topshirilgan']}</td></tr>

// </table>
// </div>
// </div>
// </div>
// </div>
// </div>

//  <div class="col-12 col-sm-12 col-md-12 col-lg-2">
 
//   <div class="p-2 mb-2 fw-bold rounded mt-3" style="font-family: 'Baloo Chettan 2', cursive; font-size: 16px; background-color: rgb(29,163,29); color: white;">${info['phone_numer']}</div>
//   <div class="p-2 bg-warning fw-bold rounded" style="font-family: 'Baloo Chettan 2', cursive; font-size: 16px; color: white;"> ${info['mode']}</div>

//   <div class="p-2 mb-2 bg-primary fw-bold rounded mt-3" style="font-family: 'Baloo Chettan 2', cursive; font-size: 16px; color: white;"> ${info['money']} ${info['moneyc']}<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span></div>
  
//    <button type="button" class="btn btn-primary btn-lg" data-bs-toggle="collapse" href="#infor${info['id']}" role="button" aria-expanded="false" aria-controls="collapseExample"  style="font-family: 'Baloo Chettan 2', cursive; font-size: 16px;">Qo'shimcha malumot</button>

// </div>


// <div class="collapse" id="infor${info['id']}">
//  <div class="card border-0">
    
// <div class="rounded p-1" style="color: red; font-family: 'Baloo Chettan 2', cursive;">
//   Ijaraga beriladigan uyning tartib qoidalari
// </div>

// <div style="font-family: 'Baloo Chettan 2', cursive; font-size: 13px;">
//   <span class="text-danger">●</span> ${info['tartiblar']}
// </div>


// <div class="rounded p-1" style="color: red; font-family: 'Baloo Chettan 2', cursive;">
//   Ijaraga beriladigan uyda ish bilan taminlanish holati 
// </div>

// <div style="font-family: 'Baloo Chettan 2', cursive; font-size: 13px;">
//   <span class="text-danger">●</span>${info['ish']}
// </div>

// </div>
// </div>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
//     </div>
//   </div>
//   </div>
//   </div>

// <div class="container-fluid" style="height:50px; background-color: #edf2f9;">
// </div>

    //             `            })
    //     } else {
    //         box.innerHTML = "<b>No results found...</b>"
    //     }
    
    // })

