<template>
    <div>
      <h1 class="mt-4 text-center text-2xl font-bold text-black sm:text-3xl font-bold">Estoque:</h1>
      <div class="bg-white shadow-lg rounded-lg p-10 m-5">
        <label class="mb-4 block text-black text-lg font-bold mb-2">Coca-Cola: {{ estoque.coca }}</label>
        <label class="mb-4 block text-black text-lg font-bold mb-2">Cerveja: {{ estoque.cerveja }}</label>
        <label class="mb-4 block text-black text-lg font-bold mb-2">Hamburguer: {{ estoque.hamburguer }}</label>
        <button
        class="mt-4 block w-full rounded-lg bg-red-600 hover:bg-red-700 px-5 py-3 text-sm font-medium text-white"
        @click="zerarEstoque"
        >
      Zerar estoque
    </button>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';
import XLSX from "xlsx";

export default {
  name: 'Estoque',
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
        .get('http://localhost:8000/estoque/1')
        .then((response) => {
          this.estoque = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    zerarEstoque() {
    for (let item in this.estoque) {
      this.estoque[item] = 0;
    }
    axios.patch("http://localhost:8000/patchEstoque/", this.estoque)
      .then(response => {
        console.log("Estoque zerado com sucesso:", response.data);
      })
      .catch(error => {
        console.log("Erro ao zerar estoque:", error);
      });
    alert("Estoque zerado com sucesso!");
    location.reload(); 
  }
  },
};
</script>
  
  