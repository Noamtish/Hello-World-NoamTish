console.log("noam");

function createuserList(users){
    console.log(users);
    
    const curr_main = document.querySelector("main");
    
    for (let user of users) {
        const section =document.createElement("section");
        section.innerHTML=
    
        `
        <img src ="${user.avatar}" alt="pic">

        ${user.last_name}
          ${user.first_name}
        
        `;
    
    
    curr_main.appendChild(section);
    
    } 
    
    }


fetch('https://reqres.in/api/users?page=2')
.then(response => response.json())
.then(responseJSON => createuserList(responseJSON.data))
 .catch(err =>console.log(err));



 