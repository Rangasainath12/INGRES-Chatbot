document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const chatForm = document.getElementById('chatForm');
    const userInput = document.getElementById('userInput');
    const chatLog = document.getElementById('chatLog');
    const actionButtons = document.querySelectorAll('.action-btn');
    
    // Backend API URL - update this to match your backend
    const API_URL = 'http://localhost:5000';
    
    // Event listener for form submission
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const message = userInput.value.trim();
        
        if (message) {
            // Add user message to chat
            addMessageToChat('user', message);
            
            // Clear input field
            userInput.value = '';
            
            // Send message to backend
            sendMessageToBackend(message);
        }
    });
    
    // Event listeners for quick action buttons
    actionButtons.forEach(button => {
        button.addEventListener('click', function() {
            const action = this.getAttribute('data-action');
            
            // Add user action to chat
            addMessageToChat('user', `I want to ${action.replace('_', ' ')}`);
            
            // Send action to backend
            sendActionToBackend(action);
        });
    });
    
    // Function to add message to chat log
    function addMessageToChat(sender, message) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        const paragraph = document.createElement('p');
        paragraph.textContent = message;
        
        contentDiv.appendChild(paragraph);
        messageDiv.appendChild(contentDiv);
        chatLog.appendChild(messageDiv);
        
        // Scroll to bottom of chat
        chatLog.scrollTop = chatLog.scrollHeight;
    }
    
    // Function to send message to backend
    async function sendMessageToBackend(message) {
        try {
            // Show typing indicator
            showTypingIndicator();
            
            const response = await fetch(`${API_URL}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            
            // Remove typing indicator
            removeTypingIndicator();
            
            // Add assistant response to chat
            addMessageToChat('assistant', data.response);
            
        } catch (error) {
            console.error('Error:', error);
            
            // Remove typing indicator
            removeTypingIndicator();
            
            // Add error message to chat
            addMessageToChat('assistant', 'Sorry, I encountered an error. Please try again later.');
        }
    }
    
    // Function to send action to backend
    async function sendActionToBackend(action) {
        try {
            // Show typing indicator
            showTypingIndicator();
            
            const response = await fetch(`${API_URL}/action`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ action: action })
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            
            // Remove typing indicator
            removeTypingIndicator();
            
            // Add assistant response to chat
            addMessageToChat('assistant', data.response);
            
        } catch (error) {
            console.error('Error:', error);
            
            // Remove typing indicator
            removeTypingIndicator();
            
            // Add error message to chat
            addMessageToChat('assistant', 'Sorry, I encountered an error. Please try again later.');
        }
    }
    
    // Function to show typing indicator
    function showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message assistant-message typing-indicator';
        typingDiv.id = 'typingIndicator';
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        const paragraph = document.createElement('p');
        paragraph.textContent = 'Typing...';
        
        contentDiv.appendChild(paragraph);
        typingDiv.appendChild(contentDiv);
        chatLog.appendChild(typingDiv);
        
        // Scroll to bottom of chat
        chatLog.scrollTop = chatLog.scrollHeight;
    }
    
    // Function to remove typing indicator
    function removeTypingIndicator() {
        const typingIndicator = document.getElementById('typingIndicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
});