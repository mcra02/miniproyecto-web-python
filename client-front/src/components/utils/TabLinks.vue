<template>
  <q-route-tab
    :to="{ name: link }"
    :label="title"
  />
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    },

    link: {
      type: String,
      default: '#'
    },

    icon: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss" scoped></style>
