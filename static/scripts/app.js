document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault(); // prevent normal form submit

    const form = e.target;
    const formData = new FormData(form);

    // Send it to your Flask endpoint
    const response = await fetch('/send-email', {
        method: 'POST',
        body: formData
    });

    // Get the response text (could be JSON if you like)
    const result = await response.text();

    // Show a success message in the page
    document.getElementById('result').innerHTML = 
        "<p>Thank you for reaching out! We'll get back to you soon.</p>";

    // Optionally reset the form
    form.reset();
});

