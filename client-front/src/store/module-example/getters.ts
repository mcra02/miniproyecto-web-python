/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-unsafe-call */
import { GetterTree } from 'vuex'
import { StateInterface } from '../index'
import { ExampleStateInterface } from './state'

const getters: GetterTree<ExampleStateInterface, StateInterface> = {
  someAction (/* context */) {
    // your code
  }
}

export default getters
