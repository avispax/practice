new Vue({
  el: '#app',
  data: {
    a: 1
  },
  created: function () {
    // `this` は vm インスタンスを指します
    console.log('a is: ' + this.a)
  }
})
// => "a is: 1"
//F12でConsole見れ。
