<template>
  <h1 class="text-center text-xl block text-gray-700 font-bold mb-4">
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
    class="bg-emerald-500 border-solid border-2 border-emerald-500 text-white px-4 py-2 rounded-md hover:bg-emerald-600"
    @click="exportConfirmation"
  >
    Exportar para Excel
  </button>
  <div class="p-1"></div>
  <button
    class="bg-rose-800 border-solid border-2 border-rose-900 text-white px-4 py-2 rounded-md hover:bg-rose-900"
    @click="clearConfirmation"
  >
    Limpar dados
  </button>
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
      custoham: 0,
      custococa: 0,
      custocerva: 0,
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
    final() {
      return (
        this.total +
        this.totalVendido -
        this.custoham -
        this.custococa -
        this.custocerva
      );
    },
  },
  methods: {
    clearLocalStorage() {
      window.localStorage.clear();
      this.pre = 0;
      this.beer = 0;
      this.hamburgers = 0;
      this.cocaCola = 0;
    },
    clearConfirmation() {
      if (window.confirm("Tem certeza que deseja apagar todos os dados?")) {
        this.clearLocalStorage();
      }
    },
    exportConfirmation() {
      if (
        window.confirm(
          "Tem certeza que deseja exportar a planilha de levantamento?"
        )
      ) {
        this.exportToExcel();
      }
    },
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
      window.localStorage.setItem("pre", this.pre);
    },
    updateBeer() {
      window.localStorage.setItem("beer", this.beer);
    },
    updateHam() {
      window.localStorage.setItem("hamburgers", this.hamburgers);
    },
    updateCoca() {
      window.localStorage.setItem("cocaCola", this.cocaCola);
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
          Final: this.final,
        },
      ]);
      worksheet["D2"].z = "R$0.00";
      worksheet["E2"].z = "R$0.00";
      worksheet["F2"].z = "R$0.00";
      worksheet["G2"].z = "R$0.00";
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
    this.final = parseInt(window.localStorage.getItem("final")) || 0;
  },
};
</script>
