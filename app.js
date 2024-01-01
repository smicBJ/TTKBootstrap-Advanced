
console.log("Script Connected")

const apiUrl = 'http://10.6.21.76:8000/tasks'

var tasks = []

fetch(apiUrl)
  .then((response) => {
    // Check if the response status is OK (200)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    
    // Parse the JSON response
    tasks = response.json()
    return response.json();
  })
  .then((data) => {
    // Data is now a JavaScript object containing the response JSON
    console.log(data);
    
    // You can access specific properties from the response JSON here
    const title = data.title;
    const body = data.body;
    
    // Do something with the data
    console.log(`Title: ${title}`);
    console.log(`Body: ${body}`);
  })
  .catch((error) => {
    console.error('Fetch error:', error);
  });

console.log(tasks);
