<script>
import notificationbar from "../components/registro.vue";
import headerinfo from "../components/header.vue";
import axios from "axios";
export default {
  components: { notificationbar, headerinfo },
  data() {
    return {
      tarefas: [],
    };
  },
  async created() {
    await this.getAllTasks();
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
  },
};
</script>

<template>
  <headerinfo />
  <h1
    class="mt-4 text-center text-2xl font-bold text-black sm:text-3xl text-black font-bold"
  >
    Feed de pedidos:
  </h1>
  <section class="overflow-y-auto w-100 overflow-hidden h-5/6 p-4">
    <notificationbar
      v-for="tarefa in tarefas"
      :key="tarefa.id"
      :tarefa="tarefa"
    />
  </section>
</template>
