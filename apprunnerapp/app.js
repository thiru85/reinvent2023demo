const express = require('express');
const app = express();

// Middleware to serve static files like CSS
app.use(express.static('public'));

// Route for the root path
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/views/dummy.html');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
