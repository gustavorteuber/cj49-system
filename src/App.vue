<template>
  <div
    class="p-1 justify-center flex flex-col md:flex-row"
    style="margin: 20px"
  >
    <div class="bg-gray-100 md:w-1/2 p-4 border rounded-md shadow-md">
      <MeuCaixaEletronico />
    </div>
    <div class="m-2"></div>
    <div
      class="bg-gray-100 md:w-1/2 w-full p-4 border rounded-md shadow-md order-2 md:order-1"
    >
      <calculator />
    </div>
  </div>
</template>

<script>
import MeuCaixaEletronico from "./components/eletronicmoney.vue";
import calculator from "./components/calculator.vue";
export default {
  components: {
    MeuCaixaEletronico,
    calculator,
  },
};
</script>
