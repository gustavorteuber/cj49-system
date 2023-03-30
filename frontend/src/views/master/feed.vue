<script>
import { mapState } from "pinia";
import { useAuthStore } from "./stores/auth";
import dayjs from "dayjs";
import relativeTime from "dayjs/plugin/relativeTime";
import ptBr from "dayjs/locale/pt-br";
import axios from "axios";
dayjs.locale("pt-br", ptBr);
dayjs.extend(relativeTime);
export default {
  props: ["tarefa"],
  user: {},
  data() {
    return {
      tarefas: [],
    };
  },
  methods: {
    async getAllTasks() {
      axios
        .get(`http://localhost:8000/pedido/`)
        .then((res) => {
          this.tarefas = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    formatDate(date) {
      return dayjs(date).format("DD/MM/YYYY HH:mm");
    },
    formatRelativeTime(date) {
      return dayjs(date).fromNow();
    },
  },
  computed: {
    ...mapState(useAuthStore, ["id", "username", "foto"]),
  },
  mounted() {
    dayjs.extend(relativeTime);
  },
};
</script>

<template>
  <a
    href="#"
    class="flex items-center px-4 py-3 -mx-2 transition-colors duration-300 transform border-b border-gray-700 hover:bg-gray-50"
  >
    <p class="mx-2 text-sm text-neutral-800">
      <span class="font-bold text-red-500" href="#"
        >DETALHES DO PEDIDO {{ tarefa.id }}</span
      >
      Foram pedidos: {{ tarefa.coca }} unidades de Refrigerante <br />
      {{ tarefa.cerveja }} unidades de Cerveja {{ formatDate(tarefa.data) }} -
      {{ formatRelativeTime(tarefa.data) }}
    </p>
  </a>
</template>
