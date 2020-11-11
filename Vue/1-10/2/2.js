const myData = {
  data() {
    return {
      posts: [
        { id: 1, title: 'my Title1', date: '2020/01/01', color: 'blue', size: 'big' },
        { id: 2, title: 'bbb', date: '2020/12/12', color: 'red', size: 'medium' },
        { id: 3, title: 'ccccccccccccccc', date: '1999/11/11', color: 'green', size: 'small' },
      ],
      postFontSize: 1
    }
  }
}

// Create a Vue application
const app = Vue.createApp(myData)

app.component('bp2', {
  props: ['post'],
  emits: ['enlarge-text'],
  template: `
  <div class="bp2">
    <h3>{{ post.title }}</h3>
    <div v-html="post.date"></div>
    <button @click="$emit('enlarge-text')"> Enlarge text </button>
  </div>`
})

app.mount('#el')
