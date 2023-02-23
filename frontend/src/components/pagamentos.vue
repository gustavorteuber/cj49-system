<template>
  <div class="container mx-auto">
    <h1 class="text-2xl font-bold mb-4">Controle de Pagamentos</h1>

    <!-- Adicione a lista de usuários abaixo -->
    <div>
      <h2>Usuários:</h2>
      <ul>
        <li
          v-for="usuario in usuarios"
          :key="usuario.id"
          @click="usuarioSelecionado = usuario.nome"
        >
          {{ usuario.nome }}
        </li>
      </ul>
    </div>

    <div class="grid grid-cols-4 gap-4">
      <div
        v-for="(status, index) in pagamentos"
        :key="index"
        class="bg-gray-200 p-4 rounded-md"
      >
        <h2 class="text-lg font-bold mb-2">{{ meses[index] }}</h2>
        <p class="mb-2">Status: {{ status }}</p>
        <input type="checkbox" :value="index" v-model="selecionados" />
        <button
          class="bg-green-500 text-white px-4 py-2 rounded-md mr-2"
          @click="pagar(index)"
        >
          Pagar
        </button>
        <button
          class="bg-red-500 text-white px-4 py-2 rounded-md"
          @click="abrir(index)"
        >
          Abrir
        </button>
      </div>
    </div>
    <div class="mt-4">
      <button
        class="bg-blue-500 text-white px-4 py-2 rounded-md mr-2"
        @click="pagarTodos"
      >
        Pagar Todos
      </button>
      <button
        class="bg-yellow-500 text-white px-4 py-2 rounded-md mr-2"
        @click="abrirTodos"
      >
        Abrir Todos
      </button>
      <button
        class="bg-green-500 text-white px-4 py-2 rounded-md"
        @click="pagarSelecionados"
      >
        Pagar Selecionados
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      meses: [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
      ],
      pagamentos: Array(12).fill("Em aberto"),
      selecionados: [],
      usuarios: [],
      usuarioSelecionado: null,
    };
  },
  methods: {
    pagar(index) {
      this.pagamentos[index] = "Pago";
    },
    abrir(index) {
      this.pagamentos[index] = "Em aberto";
    },
    pagarTodos() {
      this.pagamentos = Array(12).fill("Pago");
    },
    abrirTodos() {
      this.pagamentos = Array(12).fill("Em aberto");
    },
    pagarSelecionados() {
      for (let index of this.selecionados) {
        this.pagamentos[index] = "Pago";
      }
      this.selecionados = [];
    },
    buscarUsuarios() {
      axios
        .get("http://localhost:8000/usuario/")
        .then((response) => {
          this.usuarios = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    buscarPagamentos() {
      axios
        .get(
          `http://localhost:8000/boletos/?titular=${this.usuarioSelecionado}`
        )
        .then((response) => {
          const pagamentos = Array(12).fill("Em aberto");
          response.data.forEach((pagamento) => {
            const mes = new Date(pagamento.vencimento).getMonth();
            pagamentos[mes] = pagamento.status;
          });
          this.pagamentos = pagamentos;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  watch: {
    usuarioSelecionado() {
      if (this.usuarioSelecionado) {
        this.buscarPagamentos();
      } else {
        this.pagamentos = Array(12).fill("Em aberto");
      }
    },
  },
  mounted() {
    this.buscarUsuarios();
  },
};
</script>
