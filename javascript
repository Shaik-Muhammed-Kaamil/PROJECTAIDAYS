//login
<!DOCTYPE html>
<html>
<head>
  <title>Login</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

  <div class="container mt-5">
    <h2 class="text-center">Login</h2>
    <form id="loginForm" class="mx-auto" style="max-width: 400px;">
      <div class="mb-3">
        <input type="email" id="email" class="form-control" placeholder="Email">
        <div id="emailError" class="text-danger"></div>
      </div>
      <div class="mb-3">
        <input type="password" id="password" class="form-control" placeholder="Password">
        <div id="passwordError" class="text-danger"></div>
      </div>
      <button type="submit" class="btn btn-primary w-100">Login</button>
    </form>
  </div>

  <!-- Link to external JS file -->
  <script src="script.js"></script>

</body>
</html>
//Js
document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault(); // Stop form from submitting

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();

  const emailError = document.getElementById("emailError");
  const passwordError = document.getElementById("passwordError");

  emailError.textContent = "";
  passwordError.textContent = "";

  let valid = true;

  if (email === "") {
    emailError.textContent = "Email is required.";
    valid = false;
  } else if (!email.includes("@")) {
    emailError.textContent = "Invalid email format.";
    valid = false;
  }

  if (password === "") {
    passwordError.textContent = "Password is required.";
    valid = false;
  }

  if (valid) {
    alert("Login successful (client-side)");
    // Optionally submit form or redirect
  }
});
