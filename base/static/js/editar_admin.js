//funções para editar administrador
document.addEventListener("DOMContentLoaded", function () {
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm_password");
    const passwordHelp = document.getElementById("passwordHelp");
    const submitButton = document.getElementById("submitButton");

    // Alternar exibição da senha
    document.getElementById("togglePassword").addEventListener("click", function () {
        togglePasswordVisibility(password, this);
    });

    document.getElementById("toggleConfirmPassword").addEventListener("click", function () {
        togglePasswordVisibility(confirmPassword, this);
    });

    function togglePasswordVisibility(input, button) {
        if (input.type === "password") {
            input.type = "text";
            button.innerHTML = '<i class="bi bi-eye-slash"></i>';
        } else {
            input.type = "password";
            button.innerHTML = '<i class="bi bi-eye"></i>';
        }
    }

    // Verificar se as senhas coincidem
    function checkPasswordMatch() {
        if (password.value || confirmPassword.value) {  // Só valida se algum dos campos estiver preenchido
            if (password.value === confirmPassword.value) {
                confirmPassword.classList.remove("is-invalid");
                confirmPassword.classList.add("is-valid");
                passwordHelp.classList.add("d-none");
                submitButton.disabled = false;
            } else {
                confirmPassword.classList.remove("is-valid");
                confirmPassword.classList.add("is-invalid");
                passwordHelp.classList.remove("d-none");
                submitButton.disabled = true;
            }
        } else {
            confirmPassword.classList.remove("is-valid", "is-invalid");
            passwordHelp.classList.add("d-none");
            submitButton.disabled = false;
        }
    }

    password.addEventListener("input", checkPasswordMatch);
    confirmPassword.addEventListener("input", checkPasswordMatch);
});