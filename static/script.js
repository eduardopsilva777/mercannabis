async function adicionarProduto() {
    let titulo = document.getElementById("titulo").value;
    let descricao = document.getElementById("descricao").value;
    let valor = document.getElementById("valor").value;
    let cartegoria = document.getElementById("cartegoria");

    if (!titulo || descricao <= 0 || valor <= 0 || cartegoria <= 0) {
        alert("Preencha os campos corretamente!");
        return;
    }

    await fetch('/api/adicionar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ titulo, descricao, valor, cartegoria })
    });
}
