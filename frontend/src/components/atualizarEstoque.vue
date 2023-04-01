<template>
  <div class="p-4">
    <form @submit.prevent="adicionarEstoque" class="mb-4">
      <label for="produto" class="block mb-2 font-bold">Produto</label>
      <select
        v-model="produtoSelecionado"
        id="produto"
        class="w-full py-2 px-3 rounded border"
      >
        <option
          v-for="produto in produtos"
          :key="produto.id"
          :value="produto.id"
        >
          {{ produto.nome }}
        </option>
      </select>
      <label for="quantidade" class="block mt-4 mb-2 font-bold"
        >Quantidade</label
      >
      <input
        type="number"
        v-model.number="quantidade"
        id="quantidade"
        class="w-full py-2 px-3 rounded border"
      />
      <div class="m-3"></div>
      <button
        type="submit"
        class="text-green-700 hover:text-white border border-green-700 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2"
      >
        Adicionar Estoque
      </button>
    </form>

    <div>
      <h2 class="font-bold text-lg mb-2">Estoque</h2>
      <table class="table-auto">
        <thead>
          <tr>
            <th class="px-4 py-2">Produto</th>
            <th class="px-4 py-2">Quantidade</th>
            <th class="px-4 py-2">Editar</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="estoque in estoques" :key="estoque.id" class="border">
            <td class="px-4 py-2">{{ estoque.produto.nome }}</td>
            <td class="px-4 py-2">{{ estoque.quantidade }}</td>
            <td class="px-4 py-2">
              <button
                @click="editarEstoque(estoque)"
                class="text-amber-700 hover:text-white border border-amber-700 hover:bg-amber-800 focus:ring-4 focus:outline-none focus:ring-amber-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2"
              >
                Editar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="editando" class="mt-4">
      <h3 class="font-bold text-lg mb-2">Editar Estoque</h3>
      <form @submit.prevent="salvarEdicao">
        <label for="produto-editar" class="block mb-2 font-bold">Produto</label>
        <select
          v-model="produtoSelecionado"
          id="produto-editar"
          class="w-full py-2 px-3 rounded border"
        >
          <option
            v-for="produto in produtos"
            :key="produto.id"
            :value="produto.id"
          >
            {{ produto.nome }}
          </option>
        </select>
        <label for="quantidade-editar" class="block mt-4 mb-2"
          >Quantidade</label
        >
        <input
          type="number"
          v-model.number="quantidade"
          id="quantidade-editar"
          class="w-full py-2 px-3 rounded border"
        />
        <div class="flex justify-end mt-4">
          <button
            type="button"
            @click="cancelarEdicao"
            class="mr-2 bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded"
          >
            Cancelar
          </button>
          <button
            type="submit"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Salvar
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      produtos: [],
      estoques: [],
      produtoSelecionado: null,
      quantidade: null,
      estoqueSelecionado: null,
      editando: false,
    };
  },
  mounted() {
    this.carregarProdutos();
    this.carregarEstoques();
  },
  methods: {
    carregarProdutos() {
      axios
        .get("http://localhost:8000/produto/")
        .then((response) => {
          this.produtos = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    carregarEstoques() {
      axios
        .get("http://localhost:8000/estoque/")
        .then((response) => {
          this.estoques = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    adicionarEstoque() {
      const novoEstoque = {
        produto: this.produtoSelecionado,
        quantidade: this.quantidade,
      };
      axios
        .post("http://localhost:8000/estoque/", novoEstoque)
        .then((response) => {
          this.estoques.push(response.data);
          this.produtoSelecionado = null;
          this.quantidade = null;
          window.location.reload();
        })
        .catch((error) => {
          console.error(error.response.data);
        });
    },
    editarEstoque(estoque) {
      this.estoqueSelecionado = estoque;
      this.produtoSelecionado = estoque.produto.id;
      this.quantidade = estoque.quantidade;
      this.editando = true;
    },
    cancelarEdicao() {
      this.estoqueSelecionado = null;
      this.produtoSelecionado = null;
      this.quantidade = null;
      this.editando = false;
    },
    salvarEdicao() {
      const estoqueEditado = {
        id: this.estoqueSelecionado.id,
        produto: this.produtoSelecionado,
        quantidade: this.quantidade,
      };
      axios
        .put(
          `http://localhost:8000/estoque/${estoqueEditado.id}/`,
          estoqueEditado
        )
        .then((response) => {
          const index = this.estoques.findIndex(
            (estoque) => estoque.id === response.data.id
          );
          this.estoques.splice(index, 1, response.data);
          this.cancelarEdicao();
          window.location.reload();
        })
        .catch((error) => {
          console.error(error.response.data);
        });
    },
  },
};
</script>
