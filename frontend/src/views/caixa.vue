<script>
// import axios from "axios";
import calculator from "../components/calculator.vue";
import caixa from "../components/eletronicmoney.vue";
export default {
  components: { calculator, caixa },
  data() {
    return {};
  },
};
</script>

<template>
  <div class="justify-center flex flex-col md:flex-row" style="margin: 20px">
    <div class="p-1 bg-gray-100 md:w-1/2 border rounded-md shadow-md">
      <caixa />
    </div>
    <div class="m-2"></div>
    <div
      class="bg-gray-100 md:w-1/2 w-full p-1 border rounded-md shadow-md order-2 md:order-1"
    >
      <calculator />
    </div>
  </div>
</template>
