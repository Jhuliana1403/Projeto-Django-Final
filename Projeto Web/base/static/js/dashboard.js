document.addEventListener("DOMContentLoaded", function () {
    // Gráfico Financeiro Comparativo
    var ctxFinanceiro = document.getElementById("graficoFinanceiro").getContext("2d");
    new Chart(ctxFinanceiro, {
        type: "bar",
        data: {
            labels: ["Salários", "Pagamentos", "Vendas"],
            datasets: [{
                data: [
                    parseFloat(document.getElementById("graficoFinanceiro").dataset.salarios),
                    parseFloat(document.getElementById("graficoFinanceiro").dataset.pagamentos),
                    parseFloat(document.getElementById("graficoFinanceiro").dataset.vendas)
                ],
                backgroundColor: ["#3498db", "#e74c3c", "#f1c40f"]
            }]
        },
        options: { 
            responsive: true,
            plugins: { legend: { display: false } }
        }
    });

    // Gráfico de Pagamentos Mensais
    var ctxMensal = document.getElementById("graficoMensal").getContext("2d");
    new Chart(ctxMensal, {
        type: "line",
        data: {
            labels: document.getElementById("graficoMensal").dataset.meses.split(","),
            datasets: [{
                label: "Pagamentos Mensais",
                data: document.getElementById("graficoMensal").dataset.valores.split(",").map(parseFloat),
                backgroundColor: "#f1c40f",
                borderColor: "#f39c12",
                fill: false
            }]
        },
        options: { 
            responsive: true,
            plugins: { legend: { display: false } }
        }
    });

    // Gráfico de Vendas Mensais (Novo gráfico de linhas para vendas)
    var ctxVendas = document.getElementById("graficoVendas").getContext("2d");
    new Chart(ctxVendas, {
        type: "line",
        data: {
            labels: document.getElementById("graficoVendas").dataset.meses.split(","),
            datasets: [{
                label: "Vendas Mensais",
                data: document.getElementById("graficoVendas").dataset.valores.split(",").map(parseFloat),
                backgroundColor: "#2ecc71", // Cor do fundo da linha
                borderColor: "#27ae60",     // Cor da linha
                fill: false
            }]
        },
        options: { 
            responsive: true,
            plugins: { legend: { display: false } }
        }
    });

    // Gráfico de Salários por Funcionário
    var ctxSalarios = document.getElementById("graficoSalarios").getContext("2d");
    new Chart(ctxSalarios, {
        type: "bar",
        data: {
            labels: document.getElementById("graficoSalarios").dataset.funcionarios.split(","),
            datasets: [{
                data: document.getElementById("graficoSalarios").dataset.salarios.split(",").map(parseFloat),
                backgroundColor: "#2ecc71"
            }]
        },
        options: { 
            responsive: true,
            plugins: { legend: { display: false } }
        }
    });
});
