<script>
import axios from "axios";
import feed from "../master/feed.vue";
export default {
  components: { feed },
  data() {
    return {
      tarefas: [],
      isOpen: false,
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
    toggleOpen() {
      this.isOpen = !this.isOpen;
    },
  },
};
</script>

<template>
  <div class="relative">
    <button
      @click="toggleOpen"
      class="relative z-10 block p-2 text-gray-700 border border-transparent rounded-md text-neutral-800 focus:border-gray-500 focus:ring-opacity-40 focus:ring-gray-300 dark:focus:ring-gray-400 focus:ring bg-gray-100 focus:outline-none"
    >
      <svg
        class="w-5 h-5 text-gray-800"
        viewBox="0 0 24 24"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M12 22C10.8954 22 10 21.1046 10 20H14C14 21.1046 13.1046 22 12 22ZM20 19H4V17L6 16V10.5C6 7.038 7.421 4.793 10 4.18V2H13C12.3479 2.86394 11.9967 3.91762 12 5C12 5.25138 12.0187 5.50241 12.056 5.751H12C10.7799 5.67197 9.60301 6.21765 8.875 7.2C8.25255 8.18456 7.94714 9.33638 8 10.5V17H16V10.5C16 10.289 15.993 10.086 15.979 9.9C16.6405 10.0366 17.3226 10.039 17.985 9.907C17.996 10.118 18 10.319 18 10.507V16L20 17V19ZM17 8C16.3958 8.00073 15.8055 7.81839 15.307 7.477C14.1288 6.67158 13.6811 5.14761 14.2365 3.8329C14.7919 2.5182 16.1966 1.77678 17.5954 2.06004C18.9942 2.34329 19.9998 3.5728 20 5C20 6.65685 18.6569 8 17 8Z"
          fill="currentColor"
        ></path>
      </svg>
    </button>

    <div
      v-if="isOpen"
      class="absolute right-0 z-20 w-64 mt-2 overflow-hidden origin-top-right bg-white shadow-2xl rounded-md sm:w-80"
    >
      <div class="py-2" style="overflow: auto; height: 300px">
        <feed
          v-for="tarefa in tarefas.slice(-4).reverse()"
          :key="tarefa.id"
          :tarefa="tarefa"
        />
      </div>
      <a
        href="#"
        class="block py-2 font-bold text-center text-gray-800 bg-gradient-to-r from-rose-200 to-gray-200 hover:underline"
        >Ver todas</a
      >
    </div>
  </div>
</template>
