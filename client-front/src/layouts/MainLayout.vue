<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          <q-btn
            color="secondary"
            label="Cerrar sesion"
            @click="close"
          />
        </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        />
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-floating-promises */
/* eslint-disable @typescript-eslint/no-unsafe-call */
import EssentialLink from 'components/EssentialLink.vue'
import axios from 'axios'
const linksData = [
  {
    title: 'Home',
    icon: 'code',
    to: 'home'
  },
  {
    title: 'Personas',
    icon: 'school',
    to: 'friends'
  },
  {
    title: 'Endpoints',
    icon: 'code',
    to: 'endpoints'
  }

]

import { defineComponent, ref, onMounted } from '@vue/composition-api'

export default defineComponent({
  name: 'MainLayout',
  components: { EssentialLink },
  setup (_, { root }) {
    const leftDrawerOpen = ref(false)
    const essentialLinks = ref(linksData)

    const urlc = ref('http://127.0.0.1:8000/api/v1.0/auth/me')

    async function isAuth () {
      const token = window.localStorage.getItem('apikey')
      if (token) {
        // eslint-disable-next-line @typescript-eslint/restrict-template-expressions
        await axios.get(urlc.value, { headers: { Authorization: `Bearer ${token}` } })
      } else {
        root.$router.push({ name: 'login' })
      }
    }

    function close () {
      window.localStorage.removeItem('apikey')
      root.$router.push({ name: 'login' })
    }
    onMounted(() => {
      isAuth()
    })

    return { leftDrawerOpen, essentialLinks, close }
  }
})
</script>
