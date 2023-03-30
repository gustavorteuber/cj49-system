<template>
  <div>
    <!-- <h1 class="text-2xl font-bold mb-4">Produtos</h1> -->
    <div v-if="produtos.length === 0" class="text-lg font-medium text-gray-600">
      Nenhum produto encontrado
    </div>
    <div v-else>
      <div
        v-for="produto in produtos"
        :key="produto.id"
        class="bg-white rounded-lg mb-4 p-4"
      >
        <div class="font-bold">{{ produto.nome }}</div>
        <div class="text-gray-600">{{ produto.descricao }}</div>
        <div class="text-gray-600">R$ {{ produto.preco }}</div>
        <span
          class="flex items-center border rounded-full w-24 pr-2 justify-center"
          ><div
            :style="{
              backgroundColor: produto.etiqueta.cor
                ? produto.etiqueta.cor
                : '#000000',
            }"
            class="rounded-full w-2.5 h-2.5 block mr-2"
          ></div>
          {{ produto.etiqueta.nome }}</span
        >
        <div class="m-3"></div>
        <button
          class="text-green-700 hover:text-white border border-green-700 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2"
          @click="editar(produto.id)"
        >
          Editar
        </button>
        <button
          class="text-red-700 hover:text-white border border-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2"
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
