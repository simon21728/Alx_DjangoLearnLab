// Basic form validation example
document.querySelector('form').addEventListener('submit', function(event) {
    var username = document.querySelector('input[name="username"]');
    if (!username.value) {
        alert("Username is required.");
        event.preventDefault(); // Prevent form submission
    }
});
