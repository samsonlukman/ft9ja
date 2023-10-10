
    // Fetch updated data and update the chart
    function fetchUpdatedData() {
        fetch('{% url "simulate_profit_or_loss" %}')  // Replace with the actual URL
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Update the chart with the new profit or loss data
                // You can add logic here to update the chart with the received data
    
                // Example: Update an HTML element with the new profit/loss value
                document.getElementById('profit-loss-value').textContent = data.new_profit_or_loss;
            })
            .catch(error => {
                console.error('Fetch error:', error);
            });
    }

    // function updateGraph() {
    // Generate a unique query parameter to prevent caching
    // const timestamp = new Date().getTime();
    // const graphUrl = '{% url "index" %}?timestamp=' + timestamp;

    // Update the graph image source
   // document.getElementById('profit-loss-graph').src = graphUrl;
//} //
    
    // Fetch updated data initially and then every minute (adjust the interval as needed)
    fetchUpdatedData();
    setInterval(fetchUpdatedData, 60000);  // 60,000 milliseconds = 1 minute
    // Update the graph every minute
    // setInterval(updateGraph, 60000);  // 60,000 milliseconds = 1 minute
    