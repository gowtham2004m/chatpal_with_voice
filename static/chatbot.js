$(document).ready(function () {
    $('#send-button').click(function () {
        sendMessage();
    });

    $('#user-input').keypress(function (e) {
        if (e.which === 13) {
            sendMessage();
        }
    });

    function sendMessage() {
        var userMessage = $('#user-input').val();
        if (userMessage.trim() === "") return;

        appendMessage('You', userMessage);

        $.post('/chatbot', { message: userMessage }, function (response) {
            appendMessage('Bot', response.response);
            $('#user-input').val('');
        });
    }

    function appendMessage(sender, message) {
        var chatbox = $('#chat');
        var messageClass = sender === 'You' ? 'user-message' : 'bot-message';
        var messageElement = $('<div class="chat-message ' + messageClass + '"><strong>' + sender + ':</strong> ' + message + '</div>');
        chatbox.append(messageElement);
        chatbox.scrollTop(chatbox[0].scrollHeight);
    }
});
