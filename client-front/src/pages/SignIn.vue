<template>
  <div>
    <login-form />
  </div>
</template>

<script lang="ts">
import { defineComponent } from '@vue/composition-api'
import LoginForm from '@/components/LoginForm.vue'
export default defineComponent({
  components: {
    LoginForm
  },
  setup () {
    return {}
  }
})
</script>

<style scoped>

</style>
