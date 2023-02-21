<template>
  <div>
    <l-map :zoom="zoom" :center="center">
      <l-tile-layer :url="url" :attribution="attribution" />
      <l-marker :lat-lng="marker"></l-marker>
    </l-map>
  </div>
</template>

<script>
import L from "leaflet";
import { LMap, LTileLayer, LMarker } from "vue3-leaflet";
import { ref } from "vue";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  props: {
    latitude: Number,
    longitude: Number,
  },
  setup(props) {
    const zoom = ref(13);
    const center = ref([props.latitude, props.longitude]);
    const marker = ref([props.latitude, props.longitude]);

    const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    const attribution =
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors';

    return {
      zoom,
      center,
      marker,
      url,
      attribution,
    };
  },
};
</script>
