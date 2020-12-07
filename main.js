
var shelterList = [
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
const mapPlaceSrc = "https://www.google.com/maps/embed/v1/place?key=AIzaSyAndD7qZMcCCGLyxGzzHsT1udRD6Y-sYHA";

window.onload = function () {
    const searchBtn = document.getElementById("search-btn");
    searchBtn.addEventListener("click", showShelter);

    requestShelters();
};

function requestShelters() {

  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://127.0.0.1:5000/shelter', true);

  xhr.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        shelterList = JSON.parse(this.responseText).map(shelter => {
          return {
            ...shelter,
            addressline1: shelter.address_line_1,
            addressline2: shelter.address_line_2,
            postcode: shelter.post_code,
            phone: shelter.phone,
            email: shelter.email
          }
        });
        showAllShelters();
      } else {
        console.log('Error connecting to server!');
      }
    }
  };

  xhr.send();
}

function showAllShelters() {
  const bannerHandle = document.getElementById("banner");
  bannerHandle.classList.add("banner-disappear")

  // update google map
  if (shelterList.length > 0) {
    const map = document.getElementById("embedded-map");
    const addressQuery1 = shelterList[0].addressline1.split(' ').join('+');
    const addressQuery2 = shelterList[0].addressline2.split(' ').join('+');
    map.setAttribute("src", mapPlaceSrc + "&q=" + addressQuery1 + '+' + addressQuery2);
  }

  const shelterUl = document.getElementById("shelter-list");
  shelterUl.innerHTML = "";
  for (let i = 0; i < shelterList.length; i++) {
    // create a list of shelter infos - each of which is a list containing the name, address, etc
    const shelterInfo = document.createElement("li");
    const shelterInfoList = document.createElement("ul");

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

    shelterInfoList.appendChild(shelterNm);
    shelterInfoList.appendChild(shelterAddr1);
    shelterInfoList.appendChild(shelterAddr2);
    shelterInfoList.appendChild(shelterPos);
    shelterInfoList.appendChild(shelterPh);
    shelterInfoList.appendChild(shelterEm);

    shelterInfo.appendChild(shelterInfoList);
    shelterUl.appendChild(shelterInfo);
  }
}

function showShelter() {
  const shelterInput = document.getElementById("location-search");
  const resultText = document.getElementById("no-result");

  const searchName = shelterInput.value;
  // const bannerHandle = document.getElementById("banner");
  // bannerHandle.classList.add("banner-disappear")

  for (let i = 0; i < shelterList.length; i++) {

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
