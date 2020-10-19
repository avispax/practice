Vue.component("my-comp", {
  template: '<p class="static">この場合、static（背景青） + 文字色赤</p>',
});

var v1 = new Vue({
  el: "#el",
  data: {
    numbers: [1, 2, 3, 4, 5],
    sets: [
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
    ],
    items: [{ msg: "Foo" }, { msg: "Bar" }],
    datas: [],
  },
  computed: {
    evenNumbers: function () {
      return this.numbers.filter(function (number) {
        return number % 2 === 0;
      });
    },
  },
  methods: {
    even: function (numbers) {
      return numbers.filter(function (number) {
        return number % 2 === 0;
      });
    },
  },
});
