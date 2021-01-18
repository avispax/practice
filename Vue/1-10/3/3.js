const myData = {
  data() {
    return {
      searchText: '',
    }
  }
}

// Create a Vue application
const app = Vue.createApp(myData)

app.component('my-custom', {
  props: ['modelValue'],
  template: `
  <input
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
  >
  `
})

app.mount('#el')
