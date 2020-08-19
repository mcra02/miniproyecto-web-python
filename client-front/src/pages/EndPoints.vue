<template>
  <div>
    <endpoints />
  </div>
</template>

<script lang="ts">
import { defineComponent } from '@vue/composition-api'
import Endpoints from '@/components/Endpoints.vue'
export default defineComponent({
  components: {
    Endpoints
  },
  setup () {
    return {}
  }
})
</script>

<style scoped>

</style>
