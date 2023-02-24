<template>
  <div>
    <h2>Estoque:</h2>
    <p>Coca: {{ estoque.coca }}</p>
    <p>Cerveja: {{ estoque.cerveja }}</p>
    <p>Hamburguer: {{ estoque.hamburguer }}</p>
    <h2>Fazer Pedido:</h2>
    <div>
      <label>Coca:</label>
      <input type="number" v-model="pedido.coca" />
    </div>
    <div>
      <label>Cerveja:</label>
      <input type="number" v-model="pedido.cerveja" />
    </div>
    <div>
      <label>Hamburguer:</label>
      <input type="number" v-model="pedido.hamburguer" />
    </div>
    <button @click="fazerPedido">Fazer pedido</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      estoque: {},
      pedido: {
        coca: 0,
        cerveja: 0,
        hamburguer: 0,
      },
    };
  },
  mounted() {
    axios
      .get("http://localhost:8000/estoque/")
      .then((response) => {
        this.estoque = response.data[0];
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    fazerPedido() {
      axios
        .patch("http://localhost:8000/pedido/", this.pedido)
        .then((response) => {
          this.estoque.coca -= this.pedido.coca;
          this.estoque.cerveja -= this.pedido.cerveja;
          this.estoque.hamburguer -= this.pedido.hamburguer;
          this.pedido = {
            coca: 0,
            cerveja: 0,
            hamburguer: 0,
          };
          this.$emit("pedidoRealizado", response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
