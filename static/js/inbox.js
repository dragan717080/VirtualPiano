var inboxMessagesContent = document.getElementsByClassName('inbox_message_content')[0];
var inboxMessages = document.getElementsByClassName('inbox_message_msg');
var messageTitle = document.getElementsByClassName('inbox_message_msg_content');
var inboxReceivedMessage = document.getElementsByClassName('inbox_received_message')[0];
var inboxMessagesElement = document.getElementsByClassName('inbox_message');
var inboxReceivedMessageSenderAvatar = document.getElementsByClassName('inbox_received_message_sender_avatar_img')[0];
var inboxReceivedMessageSenderEmail = document.getElementsByClassName('inbox_received_message_sender_email')[0];
var inboxReceivedMessageReceiverAvatar = document.getElementsByClassName('inbox_received_message_receiver_avatar_img')[0];
var inboxReceivedMessageReceiverEmail = document.getElementsByClassName('inbox_received_message_receiver_email')[0];
var messageContentSender = document.getElementsByClassName('inbox_received_message_content_header_sender')[0];
var messageContentDatetime = document.getElementsByClassName('inbox_received_message_content_header_datetime')[0];
var messageContent = document.getElementsByClassName('inbox_received_message_content_content')[0];
var replyMessageLink = document.getElementsByClassName('reply_message_link')[0];
var senderEmail = document.getElementsByClassName('inbox_received_message_sender_email')[0];
var receiverEmail = document.getElementsByClassName('inbox_received_message_receiver_email')[0];

for (let i = 0; i < inboxMessages.length; i++) {
    inboxMessages[i].addEventListener('click', event => {
        inboxMessagesContent.style.display = 'none';
        inboxReceivedMessage.style.display = 'block';
        inboxMessagesElement[i].style.backgroundColor = '#657ee4';
        inboxReceivedMessageReceiverAvatar.setAttribute('src', `../static/uploads/images/${avatar}`);
        if (inboxMessagess[i].avatar != false) inboxReceivedMessageSenderAvatar.setAttribute('src', `../static/uploads/images/${inboxMessagess[i].avatar}`);
        else inboxReceivedMessageSenderAvatar.setAttribute('src', '../static/uploads/images/login-icon.jpg');
        messageContentSender.innerText = 'From:  ' + inboxMessagess[i].author;
        messageContentSender.style.fontWeight = 'bold';
        messageContentSender.style.paddingLeft = '14px';
        messageContentDatetime.innerText = inboxMessagess[i].datetime;
        messageContent.innerText = inboxMessagess[i].content;
        replyMessageLink.href = `/compose_message?recipient=${inboxMessagess[i].author}`;
        senderEmail.innerText = allEmails[inboxMessagess[i].author];
        receiverEmail.innerText = allEmails[inboxMessagess[i].recipient];

        for (let j = 0; j < inboxMessages.length; j++) {
            if (i != j) inboxMessagesElement[j].style.backgroundColor = '#fff';
        }

    })

}


