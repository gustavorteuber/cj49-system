<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">Produtos</h1>
    <div v-if="produtos.length === 0" class="text-lg font-medium text-gray-600">
      Nenhum produto encontrado
    </div>
    <div v-else>
      <div
        v-for="produto in produtos"
        :key="produto.id"
        class="bg-white rounded-lg shadow-md mb-4 p-4"
      >
        <div class="font-bold">{{ produto.nome }}</div>
        <div class="text-gray-600">{{ produto.descricao }}</div>
        <div class="text-gray-600">{{ produto.preco }}</div>
        <button
          class="bg-blue-500 text-white px-4 py-2 rounded-lg mt-2"
          @click="editar(produto.id)"
        >
          Editar
        </button>
        <button
          class="bg-red-500 text-white px-4 py-2 rounded-lg mt-2 ml-2"
          @click="excluir(produto.id)"
        >
          Excluir
        </button>
      </div>
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
  mounted() {
    this.listarProdutos();
  },
  methods: {
    listarProdutos() {
      axios
        .get("http://localhost:8000/produto/")
        .then((response) => {
          this.produtos = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    editar(id) {
      this.$router.push(`http://localhost:8000/produto/${id}/editar`);
    },
    excluir(id) {
      axios
        .delete(`http://localhost:8000/produto/${id}/`)
        .then((response) => {
          this.listarProdutos();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
