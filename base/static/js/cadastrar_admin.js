//funções para o template cadastrar administrador
function validatePassword() {
    let senha = document.getElementById("id_senha").value;
    let confirmarSenha = document.getElementById("id_confirmar_senha").value;
    let passwordHelp = document.getElementById("passwordHelp");
    let submitBtn = document.getElementById("submitBtn");

    if (confirmarSenha === "") {
        // Nenhuma senha digitada ainda
        document.getElementById("id_confirmar_senha").classList.remove("is-valid", "is-invalid");
        passwordHelp.innerText = "";
        submitBtn.disabled = true;
    } else if (senha === confirmarSenha) {
        // Senhas coincidem
        document.getElementById("id_confirmar_senha").classList.remove("is-invalid");
        document.getElementById("id_confirmar_senha").classList.add("is-valid");
        passwordHelp.innerText = "As senhas coincidem!";
        passwordHelp.style.color = "green";
        submitBtn.disabled = false; // Habilita o botão
    } else {
        // Senhas diferentes
        document.getElementById("id_confirmar_senha").classList.remove("is-valid");
        document.getElementById("id_confirmar_senha").classList.add("is-invalid");
        passwordHelp.innerText = "As senhas não coincidem!";
        passwordHelp.style.color = "red";
        submitBtn.disabled = true; // Desabilita o botão
    }
}

function togglePassword(inputId) {
    let input = document.getElementById(inputId);
    let button = input.nextElementSibling.querySelector("i");

    if (input.type === "password") {
        input.type = "text";
        button.classList.remove("bi-eye");
        button.classList.add("bi-eye-slash");
    } else {
        input.type = "password";
        button.classList.remove("bi-eye-slash");
        button.classList.add("bi-eye");
    }
}

// Impede envio do formulário caso as senhas sejam diferentes
document.querySelector("form").addEventListener("submit", function(event) {
    let senha = document.getElementById("id_senha").value;
    let confirmarSenha = document.getElementById("id_confirmar_senha").value;

    if (senha !== confirmarSenha) {
        event.preventDefault(); // Bloqueia o envio
        alert("As senhas não coincidem. Corrija antes de continuar.");
    }
});