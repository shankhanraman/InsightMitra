const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Waitlist API Route
app.post('/api/waitlist', (req, res) => {
    const { email } = req.body;
    if (!email) {
        return res.status(400).json({ message: 'Email is required' });
    }
    // Save email to database or send to an email list (implement your logic here)
    console.log(`New waitlist signup: ${email}`);
    res.status(200).json({ message: 'Successfully signed up!' });
});

// Chat API Route
app.post('/api/chat', (req, res) => {
    const { message } = req.body;
    if (!message) {
        return res.status(400).json({ message: 'Message is required' });
    }
    // Implement chat logic here
    console.log(`User message: ${message}`);
    const botResponse = `Echo: ${message}`; // Example response
    res.status(200).json({ response: botResponse });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
