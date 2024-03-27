$(document).ready(function() {
    // Array to store message history
    var messageHistory = [];

    // Voice input button click event handler
    $('#voice-input-btn').click(function() {
        startVoiceInput();
    });

    // Function to start voice input
    function startVoiceInput() {
        var recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;

        recognition.onresult = function(event) {
            var transcript = event.results[0][0].transcript;
            $('#user-input').val(transcript); // Set transcript as user input
            sendUserInput(); // Send user input to the chatbot
        };

        recognition.onerror = function(event) {
            console.error('Speech recognition error:', event.error);
        };

        recognition.start();
    }

    // Chat form submission event handler
    $('#chat-form').submit(function(event) {
        event.preventDefault();
        sendUserInput();
    });

    // Function to send user input to the server
    function sendUserInput() {
        var user_input = $('#user-input').val();
        $('#user-input').val('');

        // Display user's message
        displayMessage('user', user_input);

        // Send user's message to the server
        $.ajax({
            url: '/get_response',
            type: 'POST',
            data: {user_input: user_input},
            success: function(response) {
                // Display bot's response
                displayMessage('bot', response.response);
            }
        });
    }
    

    // Function to display messages
    // Function to display messages
function displayMessage(sender, message) {
    // Update message history array
    messageHistory.push({ sender: sender, message: message });

    // Display messages in the message history
    var messageDiv;
    if (sender === 'user') {
        messageDiv = '<div class="message ' + sender + '-message user-message">' + message +"   "+
                         '<img src="/static/images/user_image.png" alt="User Image" class="user-image">'+
                     '</div>';
    } else {
        messageDiv = '<div class="message ' + sender + '-message bot-message">' +
                         '<img src="/static/images/bot_image.png" alt="Bot Image" class="bot-image">' +"   "+
                         message +
                     '</div>';
    }
    $('#message-history').append(messageDiv);

    // Scroll to bottom
    $('#message-history').scrollTop($('#message-history')[0].scrollHeight);
}

    var audio = document.getElementById('meditation-audio');

    $('#play-btn').click(function() {
        audio.play();
        $(this).hide();
        $('#stop-btn').show();
    });

    $('#stop-btn').click(function() {
        audio.pause();
        audio.currentTime = 0;
        $(this).hide();
        $('#play-btn').show();
    });
});
