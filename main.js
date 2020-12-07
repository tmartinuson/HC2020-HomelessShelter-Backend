
const shelterList = [
    {
        name: "Shelter 1",
        addressline1: "123 Cordova St",
        addressline2: "Vancouver, BC",
        postcode: "V5N 5K2",
        phone: "604-563-9298",
        email: "shelter1@email.com"
    },
    {
        name: "Shelter 2",
        addressline1: "123 Broadway Ave",
        addressline2: "Vancouver, BC",
        postcode: "V2N 5K4",
        phone: "604-563-9298",
        email: "shelter2@email.com"

    },

    {
        name: "Shelter 3",
        addressline1: "123 Broadway Ave",
        addressline2: "Vancouver, BC",
        postcode: "V5N 5K2",
        phone: "604-563-9298",
        email: "shelter3@email.com"

    }
    
];
const searchBtn = document.getElementById("search-btn");
const shelterInput = document.getElementById("location-search");
const resultText = document.getElementById("no-result");





function showShelter() {
    const searchName = shelterInput.value;

    for (let i =0; i<shelterList.length; i++) {
       
        if (searchName === shelterList[i].name) {
            const shelterUl = document.getElementById("shelter-list");
           
            // should create a list of the shelter infomation
            const shelterNm = document.createElement("li");
            const shelterAddr1 = document.createElement("li");
            const shelterAddr2 = document.createElement("li");
            const shelterPos = document.createElement("li");
            const shelterPh = document.createElement("li");
            const shelterEm = document.createElement("li");


            shelterNm.innerText = shelterList[i].name; 
            shelterAddr1.innerText = shelterList[i].addressline1;
            shelterAddr2.innerText = shelterList[i].addressline2;
            shelterPos.innerText = shelterList[i].postcode;
            shelterPh.innerText = shelterList[i].phone;
            shelterEm.innerText = shelterList[i].email;

            shelterUl.appendChild(shelterNm);
            shelterUl.appendChild(shelterAddr1);
            shelterUl.appendChild(shelterAddr2);
            shelterUl.appendChild(shelterPos);
            shelterUl.appendChild(shelterPh);
            shelterUl.appendChild(shelterEm);

            shelterInput.innerText = "";
             
            console.log(shelterList[i]);

        } else {

            resultText.innerText = "There is no shelter nearby";
            shelterInput.innerText = "";
            
        }
    }





}

searchBtn.addEventListener("click", showShelter)