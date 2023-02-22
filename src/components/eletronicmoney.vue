<template>
  <div class="bg-gray-100 p-4 rounded">
    <h1 class="text-xl block text-gray-700 font-bold mb-4">
      Controle de items do caixa:
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
          v-model="cocaCola"
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
          v-model="beer"
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
        >Hamburgers (QUANT.)</label
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
          v-model="hamburgers"
          @input="updateHam"
        />
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
        <input
          type="number"
          class="px-2 py-1 border border-gray-400 text-center flex-1"
          v-model="pre"
          @input="updatepre"
        />
        <button
          class="px-2 py-1 border border-gray-400 rounded-r"
          @click="increasePre"
        >
          +
        </button>
      </div>
    </div>
    <label class="block text-gray-900 font-bold mb-2">
      {{ pre }} Hamburgers (VENDIDOS) equivalente a R$: {{ totalVendido }}
    </label>
    <button
      class="bg-green-500 text-white px-4 py-2 rounded-md"
      @click="exportToExcel"
    >
      Exportar para Excel
    </button>
  </div>
</template>

<script>
import * as XLSX from "xlsx";

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
    // clearLocalStorage() {
    //   window.localStorage.clear();
    //   this.pre = 0;
    //   this.beer = 0;
    //   this.hamburgers = 0;
    //   this.cocaCola = 0;
    // },
    increaseCocaCola() {
      this.cocaCola++;
      window.localStorage.setItem("cocaCola", this.cocaCola);
    },
    decreaseCocaCola() {
      if (this.cocaCola > 0) {
        this.cocaCola--;
        window.localStorage.setItem("cocaCola", this.cocaCola);
      }
    },
    increaseHam() {
      this.hamburgers++;
      window.localStorage.setItem("hamburgers", this.hamburgers);
    },
    decreaseHam() {
      if (this.hamburgers > 0) {
        this.hamburgers--;
        window.localStorage.setItem("hamburgers", this.hamburgers);
      }
    },
    increaseBeer() {
      this.beer++;
      window.localStorage.setItem("beer", this.beer);
    },
    decreaseBeer() {
      if (this.beer > 0) {
        this.beer--;
        window.localStorage.setItem("beer", this.beer);
      }
    },
    increasePre() {
      this.pre++;
      window.localStorage.setItem("pre", this.pre);
    },
    decreasePre() {
      if (this.pre > 0) {
        this.pre--;
        window.localStorage.setItem("pre", this.pre);
      }
    },
    updatepre() {
      if (this.pre > 0) {
        this.pre--;
        window.localStorage.setItem("pre", this.pre);
      }
    },
    updateBeer() {
      if (this.beer > 0) {
        this.beer--;
        window.localStorage.setItem("beer", this.beer);
      }
    },
    updateHam() {
      if (this.hamburgers > 0) {
        this.hamburgers--;
        window.localStorage.setItem("hamburgers", this.hamburgers);
      }
    },
    updateCoca() {
      if (this.cocaCola > 0) {
        this.cocaCola--;
        window.localStorage.setItem("cocaCola", this.cocaCola);
      }
    },
    exportToExcel() {
      const worksheet = XLSX.utils.json_to_sheet([
        {
          Hamburgers: this.totalHamburgers,
          "Coca-Cola": this.cocaCola,
          Cerveja: this.beer,
          Total: this.total,
          Prevenda: this.totalVendido,
          Hamburgerspegos: this.pre,
        },
      ]);

      const workbook = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(workbook, worksheet, "Produtos");

      XLSX.writeFile(workbook, "produtos.xlsx");
    },
  },
  mounted() {
    this.cocaCola = parseInt(window.localStorage.getItem("cocaCola")) || 0;
    this.beer = parseInt(window.localStorage.getItem("beer")) || 0;
    this.hamburgers = parseInt(window.localStorage.getItem("hamburgers")) || 0;
    this.pre = parseInt(window.localStorage.getItem("pre")) || 0;
  },
};
</script>
