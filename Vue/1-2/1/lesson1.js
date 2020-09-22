var obj = {
    foo: 'bar'
  }
  
  // この行がコメントアウトかどうかでボタンの挙動が変わります。
  //Object.freeze(obj)
  
  new Vue({
    el: '#app',
    data: obj
  })