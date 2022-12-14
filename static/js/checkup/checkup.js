
// Get data
async function getDataCheckUp() {
    const url = '/checkup/json'
    return fetch(url)
           .then(response => response.json())
           .catch(_err => console.error(error))
}

// Get Data JSON ID
async function getDataCheckUpID() {
    const url = '/checkup/refresh-json'
    return fetch(url)
         .then(response => response.json())
         .catch(_err => console.error(error))
}

// Refresh Check Up
async function refreshData(){
  document.getElementById("table").innerHTML=""
  const checkup = await getDataCheckUp()
  let htmlString = `<tr>
    <th>Name</th>
    <th>Visit Time</th>
    <th>Doctor</th>
    <th>Status</th>
    <th>Recommendation</th>
    <th>Payment</th>
  </tr>`
  checkup.forEach((item) => {
    htmlString += `\n<tr>
      <th>${item.fields.name}</th>
      <th>${item.fields.date}</th>
      <th>${item.fields.doctor}</th>
      <th>${item.fields.status_checkup_type}</th>
      <th>${item.fields.recommendations}</th>
      <th>${item.fields.paid}</th>
    </tr>` 
  })
  document.getElementById("table").innerHTML = htmlString
}

// Add Data
async function addData() {
  fetch("/checkup/create/", {
    method: "POST",
    body: new FormData(document.getElementById('create_checkup'))
  }).then(refreshData)
  return false
}
// Remove Data
async function removeData(id){
  let url = 'checkup/delete/' + id;
  fetch(url).then(refreshData)
}