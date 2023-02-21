<template>
  <div class="bg-gray-100 p-4">
    <div class="mb-4">
      <label class="block text-gray-700 font-bold mb-2">Coca-Cola (R$5)</label>
      <div class="flex items-center">
        <button
          class="px-2 py-1 border border-gray-400 rounded-l"
          @click="decreaseCocaCola"
        >
          -
        </button>
        <div class="px-2 py-1 border border-gray-400 flex-1 text-center">
          {{ cocaCola }}
        </div>
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
        <div class="px-2 py-1 border border-gray-400 flex-1 text-center">
          {{ beer }}
        </div>
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
        >Hamburgers (QUANT.)</label
      >
      <div class="flex items-center">
        <button
          class="px-2 py-1 border border-gray-400 rounded-l"
          @click="decreaseHam"
        >
          -
        </button>
        <div class="px-2 py-1 border border-gray-400 flex-1 text-center">
          {{ hamburgers }}
        </div>
        <button
          class="px-2 py-1 border border-gray-400 rounded-r"
          @click="increaseHam"
        >
          +
        </button>
      </div>
    </div>

    <div class="text-lg font-bold mb-2">Valor total: R$ {{ total }}</div>
    <div class="text-lg font-bold mb-2">
      Numero de hamburgers no evento: {{ hamburgers }}
    </div>
    <div class="mb-4">
      <div class="flex items-center">
        <button
          class="px-2 py-1 border border-gray-400 rounded-l"
          @click="decreasePre"
        >
          -
        </button>
        <div class="px-2 py-1 border border-gray-400 flex-1 text-center">
          {{ pre }}
        </div>
        <button
          class="px-2 py-1 border border-gray-400 rounded-r"
          @click="increasePre"
        >
          +
        </button>
      </div>
    </div>
    <label class="block text-gray-900 font-bold mb-2">
      {{ pre }} Hamburgers (VENDIDOS) equivalente a R$: {{ totalv }}
    </label>
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
    hamburgers() {
      return this.hamburgers;
    },
    pre() {
      return this.pre;
    },
    totalv() {
      return this.pre * 30;
    },
  },
  methods: {
    increaseCocaCola() {
      this.cocaCola++;
    },
    decreaseCocaCola() {
      if (this.cocaCola > 0) {
        this.cocaCola--;
      }
    },
    increaseHam() {
      this.hamburgers++;
    },
    decreaseHam() {
      if (this.hamburgers > 0) {
        this.hamburgers--;
      }
    },
    increaseBeer() {
      this.beer++;
    },
    decreaseBeer() {
      if (this.beer > 0) {
        this.beer--;
      }
    },
    increasePre() {
      this.pre++;
    },
    decreasePre() {
      if (this.pre > 0) {
        this.pre--;
      }
    },
  },
};
</script>
