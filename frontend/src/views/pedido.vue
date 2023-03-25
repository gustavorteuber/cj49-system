<template>
  <div>
    <h1
      class="mt-4 text-center text-2xl font-bold text-black sm:text-3xl text-black font-bold"
    >
      Fazer pedido:
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
      <button
        class="mt-4 block w-full rounded-lg bg-blue-600 hover:bg-blue-700 px-5 py-3 text-sm font-medium text-white"
        @click="fazerPedido"
      >
        Fazer Pedido
      </button>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      pedido: {
        coca: 0,
        cerveja: 0,
        hamburguer: 0,
      },
      estoque: {
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
      if (this.total === 0) {
        alert("Pedido vazio. Adicione pelo menos um item!");
        return;
      }
      axios
        .post("http://localhost:8000/pedido/", this.pedido)
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
      alert("Pedido realizado com sucesso!");
      this.$router.push("/registro");
      // location.reload();
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
      this.pedido.hamburguer =
        this.pedido.hamburguer < 0 ? 0 : this.pedido.hamburguer;
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
