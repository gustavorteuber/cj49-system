<template>
    <div>
      <h1 class="mt-4 text-center text-2xl font-bold text-black sm:text-3xl text-gray-700 font-bold">Estoque:</h1>
      <div class="bg-white shadow-lg rounded-lg p-10 m-5">
        <label class="mb-4 block text-gray-700 font-bold mb-2">Coca-Cola: {{ estoque.coca }}</label>
        <label class="mb-4 block text-gray-700 font-bold mb-2">Cerveja: {{ estoque.cerveja }}</label>
        <label class="mb-4 block text-gray-700 font-bold mb-2">Hamburguer: {{ estoque.hamburguer }}</label>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
  name: 'Estoque',
  data() {
    return {
      estoque: {
        coca: 0,
        cerveja: 0,
        hamburguer: 0,
      },
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
  },
};
</script>
  
  