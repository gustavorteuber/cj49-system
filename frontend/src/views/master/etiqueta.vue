<template>
  <div>
    <ul class="font-">
      <li v-for="etiqueta in etiquetas" :key="etiqueta.id">
        <div class="flex items-center space-x-2">
          <div
            :style="{ backgroundColor: etiqueta.cor }"
            class="w-4 h-4 rounded-full"
          ></div>
          <div>{{ etiqueta.nome }}</div>
          <button @click="excluirEtiqueta(etiqueta.id)">
            <i class="fas fa-trash"></i>
          </button>
        </div>
      </li>
    </ul>
  </div>
  <div class="font-bold text-xl text-gray-800 leading-none"></div>
  <div class="mt-5">
    <div>
      <form @submit.prevent="criarEtiqueta">
        <label for="nome">Nome:</label>
        <input
          type="text"
          id="nome"
          v-model="nome"
          class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-300 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white font-extralight"
          placeholder="Digite o nome da etiqueta que deseja criar"
        />

        <div class="flex items-center">
          <label class="font-semibold" for="cor">Cor:</label>
          <input
            type="color"
            id="cor"
            v-model="cor"
            class="hidden font-medium"
          />

          <label
            for="cor"
            class="bg-white rounded-full cursor-pointer inline-block w-8 h-8 border-gray-300 border-2 ml-2"
            style="background-color: {{ cor }};"
          ></label>
        </div>
      </form>
    </div>
    <div class="m-7"></div>
    <button
      @click="criarEtiqueta"
      type="submit"
      class="text-green-700 hover:text-white border border-green-700 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2"
    >
      Criar etiqueta
    </button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      etiquetas: [],
      nome: "",
      cor: "#000000",
    };
  },
  methods: {
    criarEtiqueta() {
      axios
        .post("http://localhost:8000/etiqueta/", {
          nome: this.nome,
          cor: this.cor,
        })
        .then((response) => {
          console.log(response.data);
          location.reload();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    listarEtiquetas() {
      axios
        .get("http://localhost:8000/etiqueta")
        .then((response) => {
          this.etiquetas = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    excluirEtiqueta(id) {
      axios
        .delete(`http://localhost:8000/etiqueta/${id}`)
        .then((response) => {
          console.log(response.data);
          location.reload();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    this.listarEtiquetas();
  },
};
</script>

<style>
input[type="color"]::-webkit-color-swatch-wrapper {
  padding: 0;
}
input[type="color"]::-webkit-color-swatch {
  border: none;
  border-radius: 50%;
}
label[for="cor"]:hover {
  box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.5);
}
</style>
