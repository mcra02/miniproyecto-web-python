
<template>
  <div class="q-pa-md">
    <q-card
      flat
      bordered
      class="my-card"
    >
      <q-card-section>
        <div class="text-h6">Endpoints</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        <q-list
          v-for="x in data.urls"
          :key="x.endpoint"
          bordered
          separator
          v-bind="x"
        >
          <q-item>
            <q-item-section>
              <q-item-label class="text-subtitle1">{{ x.endpoint }}</q-item-label>
              <div
                v-for="y in x.method"
                :key="y"
              >
                <q-badge
                  outline
                  :color="y === 'GET'? 'secondary': y==='POST'? 'orange': y=== 'PUT'? 'primary' : 'red'"
                  :label="y"
                />
              </div>
              <div
                v-for="z in x.input"
                :key="z.id"
                v-bind="z"
              >
                <q-item>
                  <q-item-section>
                    <q-item-label>{{ z.name }}</q-item-label>
                    <q-item-label overline>{{ z.type }}</q-item-label>
                  </q-item-section>
                </q-item>
              </div>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>

      <br>

      <q-card-section class="q-pt-none">
        <q-list
          v-for="xx in data.urlb"
          :key="xx.id"
          bordered
          separator
          v-bind="xx"
        >
          <q-item>
            <q-item-section>
              <q-item-label overline>{{ xx.endpoint }}</q-item-label>
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
</template>

<script lang="ts">
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-floating-promises */
/* eslint-disable @typescript-eslint/no-unsafe-call */
import { defineComponent, ref, onMounted } from '@vue/composition-api'
import axios from 'axios'

export default defineComponent({
  setup () {
    const urlc = ref('http://127.0.0.1:8000/api/v1.0/stats')
    const data = ref({
      urls: [
        {
          endpoint: '/api/v1.0/stats',
          method: ['GET'],
          input: []
        },
        {
          endpoint: '/api/v1.0/remove_friend',
          method: ['POST'],
          input: [
            {
              id: 0,
              name: 'id',
              type: 'String'
            }
          ]
        },
        {
          endpoint: '/api/v1.0/add_friend',
          method: ['POST'],
          input: [
            {
              id: 1,
              name: 'startingAccountId',
              type: 'String'
            },
            {
              id: 2,
              name: 'endingAccountId',
              type: 'String'
            }
          ]
        },
        {
          endpoint: '/api/v1.0/account/{account}/mutualfriends/{friend}',
          method: ['GET'],
          input: []
        },
        {
          endpoint: '/api/v1.0/account/{account}/friends',
          method: ['GET'],
          input: []
        },
        {
          endpoint: '/api/v1.0/friends',
          method: ['GET', 'POST'],
          input: [
            {
              id: 3,
              name: 'startingAccountId',
              type: 'String'
            },
            {
              id: 4,
              name: 'endingAccountId',
              type: 'String'
            }
          ]
        },
        {
          endpoint: '/api/v1.0/friends/{id}',
          method: ['GET', 'DELETE'],
          input: []
        },
        {
          endpoint: '/api/v1.0/accounts',
          method: ['GET', 'POST'],
          input: [
            {
              id: 5,
              name: 'user',
              type: 'String'
            },
            {
              id: 6,
              name: 'name',
              type: 'String'
            }
          ]
        },
        {
          endpoint: '/api/v1.0/accounts/{id}',
          method: ['GET', 'DELETE', 'PUT'],
          input: [
            {
              id: 7,
              name: 'user',
              type: 'String'
            },
            {
              id: 8,
              name: 'name',
              type: 'String'
            }
          ]
        },
        {
          endpoint: '/api/v1.0/auth/me',
          method: ['GET'],
          input: []
        },
        {
          endpoint: '/api/v1.0/auth/signup',
          method: ['POST'],
          input: [
            {
              id: 9,
              name: 'username',
              type: 'String'
            },
            {
              id: 10,
              name: 'password',
              type: 'String'
            },
            {
              id: 11,
              name: 'passwordConfirmation',
              type: 'String'
            }
          ]
        },
        {
          endpoint: '/api/v1.0/auth/signin',
          method: ['POST'],
          input: [
            {
              id: 12,
              name: 'username',
              type: 'String'
            },
            {
              id: 13,
              name: 'password',
              type: 'String'
            }
          ]
        }
      ],
      urlb: [
        {
          id: '0',
          endpoint: ''
        }
      ],
      page: 1,
      count: 10,
      next: ''
    })
    async function nextUrl () {
      await mappingUrl(data.value.next)
    }
    async function prevUrl () {
      await mappingUrl(urlc.value + '?limit=10&page=' + (data.value.page - 1).toString())
    }
    async function mappingUrl (url:string) {
      const token = window.localStorage.getItem('apikey')
      // eslint-disable-next-line @typescript-eslint/restrict-template-expressions
      const res = await axios.get(url, { headers: { Authorization: `Bearer ${token}` } })
      const ep = res.data.data
      data.value.urlb = ep
      data.value.page = res.data.pagination.page
      data.value.count = res.data.pagination.count
      data.value.next = res.data.pagination.next
      // console.log(ep)
    }
    onMounted(() => {
      mappingUrl(urlc.value)
    })
    return {
      data,
      nextUrl,
      prevUrl
    }
  }
})
</script>

<style scoped>

</style>
