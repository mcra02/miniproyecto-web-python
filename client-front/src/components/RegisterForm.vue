<template>
  <div>
    <q-card
      flat
      bordered
      class="my-card"
    >
      <q-card-section>
        <div class="text-h6">Registro</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        <q-form
          class="q-gutter-md"
          @submit="onSubmit"
        >
          <q-input
            v-model="form.username"
            outlined
            label="Username *"
            hint="Username"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please type username']"
          />

          <q-input
            v-model="form.password"
            outlined
            label="Password *"
            hint="Password"
            lazy-rules
            :rules="[
              val => val !== null && val !== '' || 'Please type your password',
            ]"
          />

          <q-input
            v-model="form.passwordConfirmation"
            outlined
            label="Confirmar Password *"
            hint="Confirmar Password"
            lazy-rules
            :rules="[
              val => val !== null && val !== '' || 'Please type your password',
            ]"
          />

          <div>
            <q-btn
              label="Submit"
              type="submit"
              color="primary"
              class="full-width"
            />
          </div>
        </q-form>
      </q-card-section>
    </q-card>
  </div>
</template>

<script lang="ts">
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-floating-promises */
/* eslint-disable @typescript-eslint/no-unsafe-call */
import { defineComponent, ref } from '@vue/composition-api'
import axios from 'axios'

export default defineComponent({
  setup (_, { root }) {
    const form = ref({
      username: '',
      password: '',
      passwordConfirmation: ''
    })

    const urlc = ref('http://127.0.0.1:8000/api/v1.0/auth/signup')

    async function onSubmit () {
      try {
        const res = await axios.post(urlc.value, form.value)
        // eslint-disable-next-line @typescript-eslint/restrict-template-expressions
        const apikey = res.data.data.apikey
        window.localStorage.setItem('apikey', apikey)
        root.$q.notify({
          type: 'positive',
          message: 'Realizado correctameente'
        })
        root.$router.push({ name: 'home' })
      } catch (error) {
        root.$q.notify({
          type: 'negative',
          message: 'Ocurrio un error al realizar la operacion'
        })
      }
    }

    return { form, onSubmit }
  }
})
</script>

<style scoped>

</style>
