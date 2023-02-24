<template>
  <div>
    <h1 class="text-center text-xl block text-gray-700 font-bold mb-4">
    Fazer pedido:
  </h1>
  <div class="mb-4">
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
        v-model="pedido.coca"
        @input="updateCoca"
      />
      <button
        class="px-2 py-1 border border-gray-400 rounded-r"
        @click="increaseCocaCola"
      >
        +
      </button>
    </div>
  </div>

  <div class="mb-4">
    <label class="block text-gray-700 font-bold mb-2">Cerveja (R$12)</label>
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
        v-model="pedido.cerveja"
        @input="updateBeer"
      />
      <button
        class="px-2 py-1 border border-gray-400 rounded-r"
        @click="increaseBeer"
      >
        +
      </button>
    </div>
  </div>
  <div class="mb-4">
    <label class="block text-gray-700 font-bold mb-2"
      >Hamburgers (R$15)</label
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
        v-model="pedido.hamburguer"
        @input="updateHam"
      />
      <button
        class="px-2 py-1 border border-gray-400 rounded-r"
        @click="increaseHam"
      >
        +
      </button>
    </div>
    <div class="mt-4 text-lg font-bold mb-2">Valor total: R$ {{ total }}</div>
  </div>
    <button
    class="bg-emerald-500 border-solid border-2 border-emerald-500 text-white px-4 py-2 rounded-md hover:bg-emerald-600"
    @click="fazerPedido"
  >
    Fazer Pedido
  </button>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      pedido: {
        usuario: 1,
        coca: 0,
        cerveja: 0,
        hamburguer: 0,
      },
    };
  },
  computed: {
    total() {
      return (
        this.pedido.coca * 5 +
        this.pedido.cerveja * 12 +
        this.pedido.hamburguer * 15
      );
    },
  },
  methods: {
    fazerPedido() {
      axios
        .post("http://localhost:8000/pedido/", this.pedido)
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
        alert("Pedido realizado com sucesso!");
    },
    updateCoca() {
      this.pedido.coca = this.pedido.coca < 0 ? 0 : this.pedido.coca;
      window.localStorage.setItem("coca", this.pedido.coca);
    },
    updateBeer() {
      this.pedido.cerveja = this.pedido.cerveja < 0 ? 0 : this.pedido.cerveja;
      window.localStorage.setItem("cerveja", this.pedido.cerveja);
    },
    updateHam() {
      this.pedido.hamburguer = this.pedido.hamburguer < 0 ? 0 : this.pedido.hamburguer;
      window.localStorage.setItem("hamburguer", this.pedido.hamburguer);
    },
    increaseCocaCola() {
      this.pedido.coca++;
      windows.localStorage.setItem("coca", this.pedido.coca);
    },
    decreaseCocaCola() {
      this.pedido.coca--;
      this.updateCoca();
      windows.localStorage.setItem("coca", this.pedido.coca);
    },
    increaseBeer() {
      this.pedido.cerveja++;
      windows.localStorage.setItem("cerveja", this.pedido.cerveja);
    },
    decreaseBeer() {
      this.pedido.cerveja--;
      this.updateBeer();
      windows.localStorage.setItem("cerveja", this.pedido.cerveja);
    },
    increaseHam() {
      this.pedido.hamburguer++;
      windows.localStorage.setItem("hamburguer", this.pedido.hamburguer);
    },
    decreaseHam() {
      this.pedido.hamburguer--;
      this.updateHam();
      windows.localStorage.setItem("hamburguer", this.pedido.hamburguer);
    },
  },
};
</script>