<template>
  <div>
    <label class="mb-4 block text-gray-800 text-lg font-bold mb-2"
      >Coca-Cola: {{ estoque.coca }}</label
    >
    <label class="mb-4 block text-gray-800 text-lg font-bold mb-2"
      >Cerveja: {{ estoque.cerveja }}</label
    >
    <label class="mb-4 block text-gray-800 text-lg font-bold mb-2"
      >Hamburguer: {{ estoque.hamburguer }}</label
    >
    <button
      class="rounded-xl inline-flex items-center justify-center py-2 px-3 border border-emerald-400rounded-xl text-gray-800 hover:text-green-500 text-sm font-semibold transition"
      @click="gerarPlanilha"
    >
      Gerar planilha
    </button>
    <button
      class="inline-flex items-center justify-center py-2 px-3 rounded-xl text-gray-800 hover:text-red-500 text-sm font-semibold transition"
      @click="zerarEstoque"
    >
      Zerar estoque
    </button>
  </div>
</template>

<script>
import axios from "axios";
import ExcelJS from "exceljs";

export default {
  name: "Estoque",
  data() {
    return {
      estoque: {
        coca: 0,
        cerveja: 0,
        hamburguer: 0,
      },
      pedidos: [],
    };
  },
  mounted() {
    this.carregarEstoque();
  },
  methods: {
    carregarEstoque() {
      axios
        .get("http://localhost:8000/estoque/1")
        .then((response) => {
          this.estoque = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    zerarEstoque() {
      const estoqueZerado = {
        coca: 0,
        cerveja: 0,
        hamburguer: 0,
      };

      axios
        .patch("http://localhost:8000/patchEstoque/", estoqueZerado)
        .then((response) => {
          console.log("Estoque zerado com sucesso:", response.data);
          alert("Estoque zerado com sucesso!");
          location.reload();
        })
        .catch((error) => {
          console.log("Erro ao zerar estoque:", error);
          alert("Erro ao zerar estoque.");
        });
    },

    gerarPlanilha() {
      axios
        .get("http://localhost:8000/pedido")
        .then((response) => {
          const pedidos = response.data;
          let totalPedidos = 0;

          // Criar nova planilha
          const workbook = new ExcelJS.Workbook();
          const sheet = workbook.addWorksheet("Pedidos");

          // Definir cabeçalhos das colunas
          sheet.columns = [
            { header: "Produto", key: "produto", width: 15 },
            { header: "Quantidade", key: "quantidade", width: 15 },
            { header: "Valor Unitário", key: "valorUnitario", width: 15 },
            { header: "Valor Total", key: "valorTotal", width: 15 },
          ];

          // Preencher planilha com dados dos pedidos
          pedidos.forEach((pedido) => {
            const linhaPedido = {
              produto: "",
              quantidade: "",
              valorUnitario: "",
              valorTotal: "",
            };

            if (pedido.coca >= 0) {
              linhaPedido.produto = "Coca";
              linhaPedido.quantidade = pedido.coca;
              linhaPedido.valorUnitario = "R$5.00";
              linhaPedido.valorTotal = `R$${(pedido.coca * 5).toFixed(2)}`;
              sheet.addRow(linhaPedido);
              totalPedidos += pedido.coca * 5;
            }

            if (pedido.cerveja >= 0) {
              linhaPedido.produto = "Cerveja";
              linhaPedido.quantidade = pedido.cerveja;
              linhaPedido.valorUnitario = "R$12.00";
              linhaPedido.valorTotal = `R$${(pedido.cerveja * 12).toFixed(2)}`;
              sheet.addRow(linhaPedido);
              totalPedidos += pedido.cerveja * 12;
            }

            if (pedido.hamburguer >= 0) {
              linhaPedido.produto = "Hamburguer";
              linhaPedido.quantidade = pedido.hamburguer;
              linhaPedido.valorUnitario = "R$15.00";
              linhaPedido.valorTotal = `R$${(pedido.hamburguer * 15).toFixed(
                2
              )}`;
              sheet.addRow(linhaPedido);
              totalPedidos += pedido.hamburguer * 15;
            }

            if (linhaPedido.produto !== "") {
              sheet.addRow({});
            } else {
              // Tratar valores zerados no banco de dados
              linhaPedido.produto = "Produto não informado";
              linhaPedido.quantidade = 0;
              linhaPedido.valorUnitario = "";
              linhaPedido.valorTotal = "";
              sheet.addRow(linhaPedido);
            }
          });

          // Adicionar linha com o valor total de todos os pedidos somados
          sheet.addRow({});
          sheet.addRow({
            produto: "Total",
            quantidade: "",
            valorUnitario: "",
            valorTotal: `R$${totalPedidos.toFixed(2)}`,
          });

          // Salvar planilha em buffer
          workbook.xlsx.writeBuffer().then((buffer) => {
            // Criar blob com buffer da planilha
            const blob = new Blob([buffer], {
              type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            });

            // Criar objeto URL para download da planilha
            const url = window.URL.createObjectURL(blob);

            // Criar link para download e clicar nele para iniciar o download
            const link = document.createElement("a");
            link.href = url;
            link.download = "pedidos.xlsx";
            document.body.appendChild(link);
            link.click();

            // Limpar objeto URL da memória
            window.URL.revokeObjectURL(url);
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
