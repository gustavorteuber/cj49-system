<template>
  <div>
    <h2 class="text-center text-xl block text-gray-700 font-bold mb-4">
      Calculadora de Bebidas:
    </h2>
    <!-- Inputs para as bebidas -->
    <div class="mb-4">
      <label class="block text-gray-700 font-bold mb-2">Coca-Cola</label>
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
      <label class="block text-gray-700 font-bold mb-2">Cerveja</label>
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
    <!-- Exibir total e inputs para dinheiro recebido e troco -->
    <div class="flex items-center mb-4">
      <label for="total" class="mr-2">Total:</label>

      <span id="total" class="font-medium">R$: {{ calcularTotal() }},00</span>
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
      <span id="troco" class="font-medium">R$: {{ calcularTroco() }},00</span>
    </div>
    <!-- Botão para limpar os inputs -->
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
  </div>
</template>

<script>
import * as XLSX from "xlsx";
export default {
  data() {
    return {
      cocaCola: 0,
      beer: 0,
      total: 0,
      dinheiroRecebido: 0,
      troco: 0,
      tableData: [],
    };
  },
  computed: {
    troco() {
      return this.dinheiroRecebido - this.total;
    },
  },
  methods: {
    calcularTotal() {
      return this.cocaCola * 5 + this.beer * 12;
    },
    calcularTroco() {
      return this.dinheiroRecebido - this.calcularTotal();
    },
    limpar() {
      this.beer = 0;
      this.cocaCola = 0;
      this.total = 0;
      this.dinheiroRecebido = 0;
      this.troco = 0;
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
    clearConfirmation() {
      if (window.confirm("Tem certeza que deseja apagar todos os dados?")) {
        this.limpar();
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
    exportToExcel() {
      const newData = {
        "Coca-Cola": this.cocaCola,
        Cerveja: this.beer,
        Total: this.calcularTotal(),
        "Dinheiro Recebido": this.dinheiroRecebido,
        Troco: this.calcularTroco(),
      };
      this.tableData.push(newData);
      const worksheet = XLSX.utils.json_to_sheet(this.tableData);
      worksheet["C2"].z = "R$0.00";
      worksheet["D2"].z = "R$0.00";
      worksheet["E2"].z = "R$0.00";
      const workbook = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(workbook, worksheet, "Produtos");
      XLSX.writeFile(workbook, "produtos.xlsx");
    },
    updatepre() {
      if (this.pre > 0) {
        this.pre--;
        window.localStorage.setItem("pre", this.pre);
      }
    },
    addTableData() {
      this.exportToExcel();
      this.limpar();
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
