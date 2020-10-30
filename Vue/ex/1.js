Vue.component("my-comp", {
  template: '<p class="static">この場合、static（背景青） + 文字色赤</p>',
});

var v = new Vue({
  el: "#el",
  data: {
  },
  methods: {
    myClick: function (msg) {
      console.log("myClick : " + msg);
    },

  },
});
