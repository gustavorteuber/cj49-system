<template>
  <div>
    <h2 class="text-xl block text-gray-700 font-bold mb-4">
      Calculadora de Bebidas:
    </h2>
    <!-- Inputs para as bebidas -->
    <div class="flex items-center mb-2">
      <label for="cervejas" class="mr-2">Cervejas:</label>
      <input
        id="cervejas"
        type="number"
        v-model="beer"
        @change="calcularTotal"
        class="p-2 border border-gray-300 rounded-md w-16"
      />
    </div>
    <div class="flex items-center mb-2">
      <label for="cocacolas" class="mr-2">Coca-Colas:</label>
      <input
        id="cocacolas"
        type="number"
        v-model="cocaCola"
        @change="calcularTotal"
        class="p-2 border border-gray-300 rounded-md w-16"
      />
    </div>
    <!-- Exibir total e inputs para dinheiro recebido e troco -->
    <div class="flex items-center mb-4">
      <label for="total" class="mr-2">Total:</label>

      <span id="total" class="font-medium">R$: {{ total }},00</span>
    </div>
    <div class="items-center mb-2">
      <label class="block text-gray-700 font-bold mb-2">Troco: </label>
      <label for="dinheiro-recebido" class="mr-2">Dinheiro Recebido:</label>
      <input
        id="dinheiro-recebido"
        type="number"
        v-model="dinheiroRecebido"
        @change="calcularTroco"
        class="p-2 border border-gray-300 rounded-md w-16"
      />
    </div>
    <div class="flex items-center mb-4">
      <label for="troco" class="mr-2">Troco:</label>
      <span id="troco" class="font-medium">R$: {{ troco }},00</span>
    </div>
    <!-- Botão para limpar os inputs -->
    <button
      @click="limpar"
      class="border-solid border-2 border-rose-900 bg-gray-100 text-rose-900 px-4 py-2 rounded-md"
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
      total: 0,
      dinheiroRecebido: 0,
    };
  },
  computed: {
    troco() {
      return this.dinheiroRecebido - this.total;
    },
  },
  methods: {
    calcularTotal() {
      this.total = this.cocaCola * 5 + this.beer * 12;
    },
    calcularTroco() {
      this.troco = this.dinheiroRecebido - this.total;
    },
    limpar() {
      this.beer = 0;
      this.cocaCola = 0;
      this.total = 0;
      this.dinheiroRecebido = 0;
      this.troco = 0;
    },
  },
};
</script>
