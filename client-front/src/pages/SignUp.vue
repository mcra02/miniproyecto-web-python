<template>
  <div>
    <register-form />
  </div>
</template>

<script lang="ts">
import { defineComponent } from '@vue/composition-api'
import RegisterForm from '@/components/RegisterForm.vue'
export default defineComponent({
  components: {
    RegisterForm
  },
  setup () {
    return {}
  }
})
</script>

<style scoped>

</style>
