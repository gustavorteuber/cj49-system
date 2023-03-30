<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">{{ titulo }}</h1>
    <form @submit.prevent="salvar">
      <div class="mb-4">
        <label class="block font-medium mb-2">Nome</label>
        <input
          class="border border-gray-400 rounded-lg p-2 w-full"
          v-model="produto.nome"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block font-medium mb-2">Preço</label>
        <input
          class="border border-gray-400 rounded-lg p-2 w-full"
          v-model="produto.preco"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block font-medium mb-2">Etiqueta</label>
        <select
          class="border border-gray-400 rounded-lg p-2 w-full"
          v-model="produto.etiqueta"
        >
          <option value="" disabled selected>Selecione uma etiqueta</option>
          <option
            v-for="etiqueta in etiquetas"
            :key="etiqueta.id"
            :value="etiqueta.id"
          >
            {{ etiqueta.nome }}
          </option>
        </select>
      </div>
      <div class="mb-4">
        <button
          class="text-green-700 hover:text-white border border-green-700 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2"
          type="submit"
        >
          {{ botao }}
        </button>
        <router-link
          class="text-gray-700 hover:text-white border border-gray-700 hover:bg-gray-800 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2"
          to="/produto"
          >Cancelar</router-link
        >
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      produto: {
        nome: "",
        preco: "",
        descricao: "",
        etiqueta: null,
      },
      etiquetas: [],
      id: null,
      titulo: "",
      botao: "",
    };
  },
  created() {
    this.id = this.$route.params.id;
    if (this.id) {
      this.titulo = "Editar produto";
      this.botao = "Salvar";
      this.carregarProduto();
    } else {
      this.titulo = "Novo produto";
      this.botao = "Adicionar";
    }
    this.carregarEtiquetas();
  },
  methods: {
    carregarProduto() {
      axios
        .get(`http://localhost:8000/produto/${this.id}/`)
        .then((response) => {
          this.produto = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async carregarEtiquetas() {
      try {
        const response = await axios.get("http://localhost:8000/etiqueta/");
        this.etiquetas = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async salvar() {
      if (this.id) {
        try {
          await axios.put(
            `http://localhost:8000/produto/${this.id}/`,
            this.produto
          );
          this.$router.push("/produto");
          location.reload();
        } catch (error) {
          console.log(error);
        }
      } else {
        try {
          await axios.post("http://localhost:8000/produto/", this.produto);
          this.$router.push("/produto");
          location.reload();
        } catch (error) {
          console.log(error);
        }
      }
    },
  },
};
</script>
