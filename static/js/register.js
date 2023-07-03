var email = document.getElementById('email');
var username = document.getElementById('username');
var passwordOne = document.getElementById('password1');
var passwordTwo = document.getElementById('password2');
var handleEmail = document.getElementById('email-error');
var handleUsername = document.getElementById('username-error');
var handleShortPassword = document.getElementById('password-error');
var handlePassNoMatch = document.getElementById('password-matching-error');
var allUsernames = [];

allUsernames = all_users.map((user) => user.username);
const testEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

function validateRegistration(e) {
    const correctEmail = testEmail(email.value);
    const correctUsername = username.value !== '';
    const correctPasswordsLengths = password1.value.length > 7;
    const correctPasswordsMatching = password1.value === password2.value;

    const registrationSuccessful = correctEmail && correctUsername && correctPasswordsLengths && correctPasswordsMatching;
    if (registrationSuccessful) 
        return true;
    else {
        handleUsername.style.display = !correctUsername ? 'block' : 'none';
        handleUsername.innerText = !correctUsername ? 'Username must not be empty' : 'Username already exists'; 
        handleEmail.style.display = !correctEmail ? 'block' : 'none';
        handleShortPassword.style.display = !correctPasswordsLengths ? 'block' : 'none';
        handlePassNoMatch.style.display = !correctPasswordsMatching ? 'block' : 'none';
        return false;
    }
}
