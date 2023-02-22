<template>
  <div class="flex justify-center items-center h-screen">
    <test />
    <div class="justify-center items-center">
      <calculator />
    </div>
  </div>
</template>

<script>
import MeuCaixaEletronico from "./components/eletronicmoney.vue";
import calculator from "./components/calculator.vue";
import test from "./components/test.vue";
export default {
  components: {
    MeuCaixaEletronico,
    calculator,
    test,
  },
};
</script>
