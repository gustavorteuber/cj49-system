<template>
  <div>
    <meu-caixa-eletronico></meu-caixa-eletronico>
    <calculator />
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
