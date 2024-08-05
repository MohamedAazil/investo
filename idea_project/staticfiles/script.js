function loadPage(page) {
    fetch(page)
        .then(response => response.text())
        .then(html => {
            document.getElementById('content').innerHTML = html;
        })
        .catch(error => {
            console.error('Error loading page:', error);
        });
}

function sendMessage() {
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');
    const message = chatInput.value;
    chatInput.value = '';
    const div = document.createElement('div');
    div.textContent = 'You: ' + message;
    chatMessages.appendChild(div);
}

function redirectToMessage(email) {
    window.location.href = `/chat/${encodeURIComponent(email)}/`;
}

function saveProfile(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const bio = document.getElementById('bio').value;

    console.log("Name:", name);
    console.log("Email:", email);
    console.log("Bio:", bio);

    // Your code to handle form submission, e.g., sending data to a server
}
