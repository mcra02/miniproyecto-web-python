/* eslint-disable @typescript-eslint/no-unsafe-call */
import VueCompositionApi from '@vue/composition-api'
import { boot } from 'quasar/wrappers'

export default boot(({ Vue }) => {
  // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
  Vue.use(VueCompositionApi)
})
