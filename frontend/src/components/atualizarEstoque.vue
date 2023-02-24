<template>
    <div>
      <h1 class="mt-4 text-center text-2xl font-bold text-black sm:text-3xl text-gray-700 font-bold">
      Atualizar estoque:
    </h1>
    <div class="bg-white shadow-lg rounded-lg p-10 m-5">
      <label class="block text-gray-700 font-bold mb-2">Coca-Cola (R$5)</label>
      <div class="flex items-center">
        <button
          class="px-2 py-1 border border-gray-400 rounded-l"
          @click="decreaseCocaCola"
        >
          -
        </button>
        <input
          type="number"
          class="px-2 py-1 border border-gray-400 text-center flex-1"
          v-model="estoque.coca"
          @input="updateCoca"
        />
        <button
          class="px-2 py-1 border border-gray-400 rounded-r"
          @click="increaseCocaCola"
        >
          +
        </button>
      </div>
      <label class="mt-4 block text-gray-700 font-bold mb-2">Cerveja (R$12)</label>
      <div class="flex items-center">
        <button
          class="px-2 py-1 border border-gray-400 rounded-l"
          @click="decreaseBeer"
        >
          -
        </button>
  
        <input
          type="number"
          class="px-2 py-1 border border-gray-400 text-center flex-1"
          v-model="estoque.cerveja"
          @input="updateBeer"
        />
        <button
          class="px-2 py-1 border border-gray-400 rounded-r"
          @click="increaseBeer"
        >
          +
        </button>
      </div>
      <label class="mt-4 block text-gray-700 font-bold mb-2"
        >Hamburger (R$15)</label
      >
      <div class="flex items-center">
        <button
          class="px-2 py-1 border border-gray-400 rounded-l"
          @click="decreaseHam"
        >
          -
        </button>
        <input
          type="number"
          class="px-2 py-1 border border-gray-400 text-center flex-1"
          v-model="estoque.hamburguer"
          @input="updateHam"
        />
        <button
          class="px-2 py-1 border border-gray-400 rounded-r"
          @click="increaseHam"
        >
          +
        </button>
      </div>
      <button
      class="mt-4 block w-full rounded-lg bg-blue-600 hover:bg-blue-700 px-5 py-3 text-sm font-medium text-white"
      @click="atualizarEstoque"
      >
      Atualizar estoque
    </button>
    </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        estoque: {
          coca: 0,
          cerveja: 0,
          hamburguer: 0,
        },
      };
    },
    methods: {
      atualizarEstoque() {
        axios.patch("http://localhost:8000/patchEstoque/", this.estoque)
        .then(response => {
        console.log("Estoque atualizado com sucesso:", response.data);
        })
        .catch(error => {
            console.log("Erro ao atualizar estoque:", error);
        });
        location.reload();  
        alert("Estoque atualizado com sucesso!");
    },
      updateCoca() {
        this.estoque.coca = this.estoque.coca < 0 ? 0 : this.estoque.coca;
        window.localStorage.setItem("coca", this.estoque.coca);
      },
      updateBeer() {
        this.estoque.cerveja = this.estoque.cerveja < 0 ? 0 : this.estoque.cerveja;
        window.localStorage.setItem("cerveja", this.estoque.cerveja);
      },
      updateHam() {
        this.estoque.hamburguer = this.estoque.hamburguer < 0 ? 0 : this.estoque.hamburguer;
        window.localStorage.setItem("hamburguer", this.estoque.hamburguer);
      },
      increaseCocaCola() {
        this.estoque.coca++;
        windows.localStorage.setItem("coca", this.estoque.coca);
      },
      decreaseCocaCola() {
        this.estoque.coca--;
        this.updateCoca();
        windows.localStorage.setItem("coca", this.estoque.coca);
      },
      increaseBeer() {
        this.estoque.cerveja++;
        windows.localStorage.setItem("cerveja", this.estoque.cerveja);
      },
      decreaseBeer() {
        this.estoque.cerveja--;
        this.updateBeer();
        windows.localStorage.setItem("cerveja", this.estoque.cerveja);
      },
      increaseHam() {
        this.estoque.hamburguer++;
        windows.localStorage.setItem("hamburguer", this.estoque.hamburguer);
      },
      decreaseHam() {
        this.estoque.hamburguer--;
        this.updateHam();
        windows.localStorage.setItem("hamburguer", this.estoque.hamburguer);
      },
    },
  };
  </script>