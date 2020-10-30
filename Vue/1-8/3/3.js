Vue.component("my-comp", {
  template: '<p class="static">この場合、static（背景青） + 文字色赤</p>',
});

var v = new Vue({
  el: "#el",
  data: {
    x: 0,
    y: 0,
  },
  methods: {
    doThis: function (msg) {
      alert("doThis" + " : " + msg + "です。");
    },

    mousePos: function (event) {
      this.x = event.clientX;
      this.y = event.clientY;
    },
  },
});
