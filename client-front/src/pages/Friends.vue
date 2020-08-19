<template>
  <div>
    <friends />
  </div>
</template>

<script lang="ts">
import { defineComponent } from '@vue/composition-api'
import Friends from '@/components/Friends.vue'
export default defineComponent({
  components: {
    Friends
  },
  setup () {
    return {}
  }
})
</script>

<style scoped>

</style>
