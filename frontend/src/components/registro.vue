<script>
import { mapState } from "pinia";
import { useAuthStore } from "../stores/auth";
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
  <div
    class="transform transition cursor-pointer hover:-translate-y-2 ml-10 relative flex items-center px-6 py-4 bg-gray-600 text-white rounded mb-10 flex-col md:flex-row space-y-4 md:space-y-0"
  >
    <div
      class="w-5 h-5 bg-gray-600 absolute -left-10 transform -translate-x-2/4 rounded-full z-10 mt-2 md:mt-0"
    ></div>

    <div class="w-10 h-1 bg-gray-500 absolute -left-10 z-0"></div>

    <div class="flex-auto">
      <h1 class="text-lg">
        {{ formatDate(tarefa.data) }} - {{ formatRelativeTime(tarefa.data) }}
      </h1>
      <h1 class="text-xl font-bold">DETALHES DO PEDIDO {{ tarefa.id }}</h1>
      <h3>
        Foram pedidos: {{ tarefa.coca }} unidades de Refrigerante <br />
        {{ tarefa.cerveja }} unidades de Cerveja
      </h3>
    </div>
  </div>
</template>
