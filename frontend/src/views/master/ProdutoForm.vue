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
        <label class="block font-medium mb-2">Descrição</label>
        <textarea
          class="border border-gray-400 rounded-lg p-2 w-full"
          v-model="produto.descricao"
        ></textarea>
      </div>
      <div class="mb-4">
        <button
          class="bg-emerald-500 text-white px-4 py-2 rounded-lg"
          type="submit"
        >
          {{ botao }}
        </button>
        <router-link
          class="bg-gray-300 text-gray-700 px-4 py-2 rounded-lg ml-2"
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
      },
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
