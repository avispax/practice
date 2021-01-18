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

// btn-counter と呼ばれる新しいコンポーネントを定義します
// Define a new global component called button-counter
app.component('button-counter', {
  data() {
    return {
      count: 0
    }
  },
  template: `
    <button @click="count++">
      You clicked me {{ count }} times.
    </button>`
})

app.component('blog-post', {
  props: ['title'],
  template: '<h4>{{ title }}</h4>'
})

app.component('bp2', {
  props: ['post'],
  template: `
  <div class="bp2">
    <h3>{{ post.title }}</h3>
    <div v-html="post.date"></div>
    <button @click="$emit('enlarge-text')"> Enlarge text </button>
  </div>`
})

app.mount('#el')