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
    var correctEmail = testEmail(email.value);
    var correctUsername = username.value !== '';
    var correctPasswordsLengths = password1.value.length > 7;
    var correctPasswordsMatching = password1.value === password2.value;

    var registrationSuccessful = correctEmail && correctUsername && correctPasswordsLengths && correctPasswordsMatching;
    if (registrationSuccessful) return true;
    else {
        if (!correctUsername) {
            handleUsername.style.display = 'block';
            handleUsername.innerText = 'Username must exist';
        } else {
            handleUsername.style.display = 'none';
            handleUsername.innerText = 'Username already exists';
        }
        handleEmail.style.display = !correctEmail ? 'block' : 'none';
        handleShortPassword.style.display = !correctPasswordsLengths ? 'block' : 'none';
        handlePassNoMatch.style.display = !correctPasswordsMatching ? 'block' : 'none';
        return false;
    }
}