document.addEventListener("DOMContentLoaded", function () {
  var passwordInput = document.getElementById("password");
  var confirmPasswordInput = document.getElementById("confirm_password");
  var showPasswordCheckbox = document.getElementById("togglePassword");

  if (showPasswordCheckbox && passwordInput && confirmPasswordInput) {
    showPasswordCheckbox.addEventListener("change", function () {
      var type = this.checked ? "text" : "password";
      passwordInput.type = type;
      confirmPasswordInput.type = type;
    });
  }
});
