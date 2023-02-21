<template>
  <div class="flex">
    <input
      type="text"
      placeholder="Pesquisar lugares"
      class="border rounded py-2 px-3 mr-2 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
      v-model="searchText"
      @keyup.enter="search"
    />
    <button
      type="button"
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      @click="search"
    >
      Pesquisar
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchText: "",
    };
  },
  methods: {
    search() {
      this.$emit("search", this.searchText);
    },
  },
};
</script>
