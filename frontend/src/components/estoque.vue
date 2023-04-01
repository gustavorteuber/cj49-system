<template>
  <div class="flex flex-wrap">
    <div
      v-for="produto in produtos"
      :key="produto.id"
      class="w-full md:w-1/2 p-3"
    >
      <div class="bg-white rounded-lg shadow-lg p-5">
        <h2 class="text-lg font-bold mb-2">{{ produto.nome }}</h2>
        <p class="text-gray-700 mb-4">{{ produto.descricao }}</p>
        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              type="number"
              v-model="produto.quantidade"
              class="form-input w-20"
            />
            <span class="ml-2 text-gray-700">x R$ {{ produto.preco }}</span>
          </div>
          <button
            @click="fazerPedido(produto)"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Pedir
          </button>
        </div>
      </div>
    </div>
    <div class="w-full p-3">
      <button
        @click="fazerTodosPedidos"
        class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
      >
        Fazer todos os pedidos
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      produtos: [],
    };
  },
  methods: {
    fazerPedido(produto) {
      const pedido = {
        produto: produto.id,
        quantidade: produto.quantidade,
      };

      axios
        .post("http://localhost:8000/pedido/", pedido)
        .then((response) => {
          console.log(response);
          alert("Pedido realizado com sucesso!");
          window.location.reload();
        })
        .catch((error) => {
          console.log(error);
          alert("Erro ao fazer o pedido.");
        });
    },
    fazerTodosPedidos() {
      this.produtos.forEach((produto) => {
        this.fazerPedido(produto);
      });
    },
  },
  mounted() {
    axios
      .get("http://localhost:8000/produto/")
      .then((response) => {
        this.produtos = response.data.map((produto) => {
          return {
            id: produto.id,
            nome: produto.nome,
            descricao: produto.descricao,
            preco: produto.preco,
            quantidade: 0,
          };
        });
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
