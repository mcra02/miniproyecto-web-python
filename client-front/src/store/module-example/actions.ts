/* eslint-disable @typescript-eslint/no-unsafe-member-access */
/* eslint-disable @typescript-eslint/no-unsafe-call */
import { ActionTree } from 'vuex'
import { StateInterface } from '../index'
import { ExampleStateInterface } from './state'

const actions: ActionTree<ExampleStateInterface, StateInterface> = {
  someAction (/* context */) {
    // your code
  }
}

export default actions
