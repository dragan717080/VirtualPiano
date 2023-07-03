const inboxMessageContent = document.getElementById('inbox-message__content');
const inboxMessagesOverviews = document.getElementsByClassName('inbox-message__msg');
const messageTitle = document.getElementsByClassName('inbox-message__msg_content');
const inboxReceivedMessage = document.getElementById('received');
const inboxMessageElement = document.getElementsByClassName('inbox-message');
const inboxReceivedMessageSenderAvatar = document.getElementById('received__sender_avatar_img');
const inboxReceivedMessageSenderEmail = document.getElementById('received__sender_email');
const inboxReceivedMessageReceiverAvatar = document.getElementById('received__receiver_avatar_img');
const inboxReceivedMessageReceiverEmail = document.getElementById('received__receiver_email');
const messageContentSender = document.getElementById('received__content-header__sender');
const messageContentDatetime = document.getElementById('received__content-header__datetime');
const messageContent = document.getElementById('received__content_content');
const replyMessageLink = document.getElementById('reply-link');
const senderEmail = document.getElementById('received__sender_email');
const receiverEmail = document.getElementById('received__receiver-email');

for (let i = 0; i < inboxMessagesOverviews.length; i++) {
    inboxMessagesOverviews[i].addEventListener("click", event => {
        console.log(inboxMessages[i]);
        inboxMessageContent.style.display = "none";
        inboxReceivedMessage.style.display = "block";
        inboxMessageElement[i].style.backgroundColor = "#657ee4";
        //inboxReceivedMessageReceiverAvatar.setAttribute("src", `../static/uploads/images/${avatar}`);
        //if (inboxMessagesOverviews[i].avatar != false) inboxReceivedMessageSenderAvatar.setAttribute("src", `../static/uploads/images/${inboxMessagesOverviews[i].avatar}`);
        //else inboxReceivedMessageSenderAvatar.setAttribute("src", "../static/uploads/images/login-icon.jpg");
        //messageContentSender.innerText = "From:  " + inboxMessagesOverviews[i].author;
        messageContentSender.style.fontWeight = "bold";
        messageContentSender.style.paddingLeft = "14px";
        messageContentDatetime.innerText = inboxMessages[i].created_at;
        messageContent.innerText = inboxMessages[i].content;
        replyMessageLink.href = `/compose_message?recipient=${inboxMessages[i].author}`;
        senderEmail.innerText = inboxMessages[i].author;
        receiverEmail.innerText = username;
    });
}
