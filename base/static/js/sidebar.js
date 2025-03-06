// Obter os elementos
const menuBtn = document.getElementById('menu-btn');
const sidebar = document.getElementById('sidebar');
const closeBtn = document.getElementById('close-btn');

// Mostrar o sidebar
menuBtn.addEventListener('click', () => {
    sidebar.style.left = '0';  // Exibir o sidebar
});

// Fechar o sidebar
closeBtn.addEventListener('click', () => {
    sidebar.style.left = '-250px';  // Esconder o sidebar
});

// Função para garantir que o sidebar está visível corretamente ao redimensionar
function adjustSidebarVisibility() {
    if (window.innerWidth > 768) {
        sidebar.style.left = '0';  // Exibe o sidebar em telas grandes
    } else {
        sidebar.style.left = '-250px';  // Esconde o sidebar em telas pequenas
    }
}

// Adiciona evento para verificar o redimensionamento da janela
window.addEventListener('resize', adjustSidebarVisibility);

// Chama a função para garantir a visibilidade correta assim que a página for carregada
adjustSidebarVisibility();
