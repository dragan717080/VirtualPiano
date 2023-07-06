const email = document.getElementById('email');
const username = document.getElementById('username');
const passwordOne = document.getElementById('password1');
const passwordTwo = document.getElementById('password2');
const handleEmail = document.getElementById('email-error');
const handleUsername = document.getElementById('username-error');
const handleShortPassword = document.getElementById('password-error');
const handlePassNoMatch = document.getElementById('password-matching-error');
const handleNonUniqueUsername = document.getElementById('unique-username-error');
const handleNonUniqueEmail = document.getElementById('unique-email-error');

const { allUsernames, allEmails } = allUsers.reduce((acc, { username, email }) => {
    acc.allUsernames.push(username);
    acc.allEmails.push(email);
    return acc;
  }, { allUsernames: [], allEmails: [] });
const testEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

function validateRegistration(e) {
    const correctEmail = testEmail(email.value);
    const usernameNotEmpty = username.value !== '';
    const correctPasswordsLengths = password1.value.length > 7;
    const passwordsMatching = password1.value === password2.value;
    const usernameIsUnique = !allUsernames.includes(username.value);
    const emailIsUnique = !allEmails.includes(email.value);

    const registrationSuccessful = correctEmail && usernameNotEmpty && correctPasswordsLengths && passwordsMatching;
    if (registrationSuccessful) 
        return true;
    else {
        handleUsername.style.display = !usernameNotEmpty ? 'block' : 'none';
        handleEmail.style.display = !correctEmail ? 'block' : 'none';
        handleShortPassword.style.display = !correctPasswordsLengths ? 'block' : 'none';
        handlePassNoMatch.style.display = !passwordsMatching ? 'block' : 'none';
        handleNonUniqueUsername.style.display = !usernameIsUnique ? 'block' : 'none';
        handleNonUniqueEmail.style.display = !emailIsUnique ? 'block' : 'none';
        return false;
    }
}
