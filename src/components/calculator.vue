<template>
  <div class="bg-gray-100 p-4">
    <h2 class="text-xl block text-gray-700 font-bold mb-4">
      Calculadora de Bebidas:
    </h2>
    <div class="flex items-center mb-2">
      <label for="cervejas" class="mr-2">Cervejas:</label>
      <input
        id="cervejas"
        type="number"
        v-model="beer"
        @change="total"
        class="p-2 border border-gray-300 rounded-md w-16"
      />
    </div>
    <div class="flex items-center mb-2">
      <label for="cocacolas" class="mr-2">Coca-Colas:</label>
      <input
        id="cocacolas"
        type="number"
        v-model="cocaCola"
        @change="total"
        class="p-2 border border-gray-300 rounded-md w-16"
      />
    </div>
    <div class="flex items-center mb-4">
      <label for="total" class="mr-2">Total:</label>
      <span id="total" class="font-medium">R$: {{ total }},00</span>
    </div>
    <button
      @click="limpar"
      class="bg-red-500 hover:bg-red-600 text-white py-2 px-4 rounded-md"
    >
      Limpar
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cocaCola: 0,
      beer: 0,
      hamburgers: 0,
      pre: 0,
    };
  },
  computed: {
    total() {
      return this.cocaCola * 5 + this.beer * 12;
    },
    totalHamburgers() {
      return this.hamburgers;
    },
    totalPre() {
      return this.pre;
    },
    totalVendido() {
      return this.pre * 30;
    },
  },
  methods: {
    calcularTotal() {
      this.total = parseInt(this.cervejas) + parseInt(this.cocacolas);
    },
    limpar() {
      this.beer = 0;
      this.cocaCola = 0;
      this.total = 0;
    },
  },
};
</script>
