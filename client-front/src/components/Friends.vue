
<template>
  <div class="q-pa-md">
    <q-card
      flat
      bordered
      class="my-card"
    >
      <q-card-section>
        <div class="text-h6">Personas</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        <div class="row">
          <div class="col-12  q-pa-md">
            <q-card
              flat
              bordered
              class="my-card"
            >
              <q-card-section>
                <div class="text-h6">Cuentas</div>
              </q-card-section>

              <q-card-section class="q-pt-none">
                <q-form
                  class="q-gutter-md"
                >
                  <q-input
                    v-model="data.account.user"
                    outlined
                    label="Cuenta"
                    hint="Cuenta"
                    lazy-rules
                  />

                  <q-input
                    v-model="data.account.name"
                    outlined
                    label="Nombre *"
                    hint="Nombre"
                    lazy-rules
                    :rules="[
                      val => val !== null && val !== '' || 'Please type your password',
                    ]"
                  />

                  <div>
                    <q-btn
                      label="Agregar"
                      color="primary"
                      class="full-width"
                      @click="addAcc"
                    />
                  </div>
                </q-form>
              </q-card-section>
            </q-card>
          </div>
          <div class="col-12  q-pa-md">
            <q-card
              flat
              bordered
              class="my-card"
            >
              <q-card-section>
                <div class="text-h6">Amigos</div>
              </q-card-section>

              <q-card-section class="q-pt-none">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
                tempor incididunt ut labore et dolore magna aliqua.
              </q-card-section>
            </q-card>
          </div>
          <div class="col-12  q-pa-md">
            <q-card
              flat
              bordered
              class="my-card"
            >
              <q-card-section>
                <div class="text-h6">Personas</div>
              </q-card-section>

              <q-card-section class="q-pt-none">
                <q-list
                  v-for="x in data.persons"
                  :key="x.id"
                  bordered
                  separator
                  v-bind="x"
                >
                  <q-item>
                    <q-item-section>
                      <q-item-label overline>{{ x.name }}</q-item-label>
                      <q-item-label>{{ x.user }}</q-item-label>
                      <q-item-label>{{ x.friendCollectionUrl }}</q-item-label>
                    </q-item-section>
                    <q-item-section avatar>
                      <q-btn
                        color="negative"
                        label="Eliminar cuenta"
                        @click="accountdel(x.id)"
                      />
                    </q-item-section>
                    <q-item-section avatar>
                      <q-btn
                        color="primary"
                        label="Ver amigos"
                        @click="$router.replace('friends/' + x.id)"
                      />
                    </q-item-section>
                    <q-item-section avatar>
                      <q-btn
                        round
                        color="secondary"
                        icon="person_add"
                        @click="addFriend(x.id)"
                      />
                    </q-item-section>
                  </q-item>
                </q-list>
                <br>
                <div
                  class="row"
                  style="text-align:center"
                >
                  <div class="col">
                    <q-btn
                      round
                      color="primary"
                      icon="navigate_before"
                      @click="prevUrl"
                    />
                  </div>
                  <div class="col">
                    <q-btn
                      disable
                      round
                      color="black"
                      :label="data.page"
                    />
                  </div>
                  <div class="col">
                    <q-btn
                      round
                      color="primary"
                      icon="navigate_next"
                      @click="nextUrl"
                    />
                  </div>
                </div>
              </q-card-section>
            </q-card>
          </div>
        </div>
      </q-card-section>
    </q-card>
    <q-dialog
      v-model="ondialog"
      persistent
    >
      <q-card>
        <q-card-section class="row items-center">
          <span class="q-ml-sm">Desea eliminar el registro ?</span>
        </q-card-section>

        <q-card-actions align="right">
          <q-btn
            v-close-popup
            flat
            label="Cancelar"
            color="primary"
          />
          <q-btn
            v-close-popup
            flat
            label="si"
            color="primary"
            @click="ondelete"
          />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script lang="ts">
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-unsafe-call */
/* eslint-disable */
import { defineComponent, onMounted, ref } from '@vue/composition-api'
import axios from 'axios'

let root = null

export default defineComponent({
  setup (_, { root }) {
    const data = ref({
      page: 1,
      count: 10,
      next: '',
      persons: [
        {
          id: '0',
          name: '',
          user: '',
          friendCollectionUrl: ''
        }
      ],
      account: {
        name: '',
        user: ''
      },
      accountSel: ''
    })

    const urlc = ref('https://yarems.com/api/v1.0/accounts')

    async function nextUrl () {
      await getPersons(data.value.next)
    }

    async function prevUrl () {
      await getPersons(urlc.value + '?limit=10&page=' + (data.value.page - 1).toString())
    }

    async function getPersons (url:string) {
      const token = window.localStorage.getItem('apikey')
      try {
        // const res = await axios.get('https://yarems.com/api/v1.0/accounts')
        // eslint-disable-next-line @typescript-eslint/restrict-template-expressions
        const res = await axios.get(url, { headers: { Authorization: `Bearer ${token}` } })
        data.value.persons = res.data.data
        data.value.page = res.data.pagination.page
        data.value.count = res.data.pagination.count
        data.value.next = res.data.pagination.next
      } catch (error) {
        console.log(error)
      }
    }
    function addFriend (id:string) {
      console.log(id)
    }
    async function addAcc () {
      const token = window.localStorage.getItem('apikey')
      try {
        let req = {
        }
        if (data.value.account.user === '') {
          req = {
            name: data.value.account.name
          }
        } else {
          req = data.value.account
        }
        // eslint-disable-next-line @typescript-eslint/restrict-template-expressions
        await axios.post(urlc.value, req, { headers: { Authorization: `Bearer ${token}` } })
        // @ts-ignore
        root.$q.notify({
          type: 'positive',
          message: 'Realizado correctameente'
        })
      } catch (error) {
        // @ts-ignore
        root.$q.notify({
          type: 'negative',
          message: 'Ocurrio un error al realizar la operacion'
        })
      }
    }

    const ondialog = ref(false)

    function accountdel (id:string) {
      data.value.accountSel = id
      ondialog.value = true
    }
    async function ondelete () {
      const token = window.localStorage.getItem('apikey')
      try {
        const nurl = urlc.value + '/' + data.value.accountSel
        await axios.delete(nurl, { headers: { Authorization: `Bearer ${token}` } })
        const index = data.value.persons.findIndex(d => d.id === data.value.accountSel)
        data.value.persons.splice(index, 1)
        // @ts-ignore
        root.$q.notify({
          type: 'positive',
          message: 'Realizado correctameente'
        })
      } catch (error) {
        console.log(error)
        // @ts-ignore
        root.$q.notify({
          type: 'negative',
          message: 'Ocurrio un error al realizar la operacion'
        })
      }
    }
    onMounted(() => {
      // eslint-disable-next-line @typescript-eslint/no-floating-promises
      getPersons(urlc.value)
    })
    return {
      data,
      nextUrl,
      prevUrl,
      addFriend,
      addAcc,
      ondialog,
      ondelete,
      accountdel
    }
  }
})
</script>

<style scoped>

</style>
