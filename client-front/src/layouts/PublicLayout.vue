<template>
  <q-layout
    view="lHh Lpr lFf"
  >

    <q-page-container>
      <q-page class="bg_page row justify-center flex-center">
        <div class="">
          <router-view />
        </div>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { ref, defineComponent } from '@vue/composition-api'
import TabLinks from '@/components/utils/TabLinks.vue'
export default defineComponent({
  components: {
    TabLinks
  },
  setup () {
    const leftDrawerOpen = ref<boolean>(false)
    const tab = ref('home')
    const links = ref([
      {
        title: 'Home',
        icon: '',
        link: 'home'
      },
      {
        title: 'Books',
        icon: '',
        link: 'books'
      },
      {
        title: 'Catalogs',
        icon: '',
        link: 'catalogs'
      },
      {
        title: 'Magazines',
        icon: '',
        link: 'magazines'
      }
    ])
    return { leftDrawerOpen, tab, links }
  }
})
</script>
