<template>
  <div class="p-4 bg-white rounded-md shadow-md">
    <form @submit.prevent="addPassword" class="flex flex-col items-center">
      <label class="text-xl font-medium mb-2">Digite o número da senha:</label>
      <input
        type="text"
        v-model="password"
        class="p-2 border border-gray-300 rounded-md mb-2 w-40 text-center text-xl font-medium"
      />
      <button
        type="submit"
        class="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
      >
        Adicionar senha
      </button>
    </form>
    <div class="flex flex-col items-center mt-4">
      <h2 class="text-xl font-medium mb-2">Senhas</h2>
      <ul class="flex flex-col items-center">
        <li
          v-if="passwordList.length > 0"
          class="text-lg text-gray-600 mb-1"
          :class="{ 'text-4xl font-bold': index === 0 }"
          v-for="(password, index) in passwordList.slice().reverse()"
          :key="index"
        >
          <span v-if="index === 0">SENHA ATUAL: {{ password }}</span>
          <span v-else>Últimas senhas: {{ password }}</span>
        </li>
        <li v-else>Nenhuma senha adicionada ainda</li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: ["passwordList"],
  data() {
    return {
      password: "",
      passwordList: [],
    };
  },
  methods: {
    addPassword() {
      if (this.password) {
        this.passwordList.push(this.password);
        this.password = "";
        if (this.passwordList.length > 7) {
          this.passwordList.shift();
        }
      }
    },
  },
};
</script>
