Vue.component("my-comp", {
  template: '<p class="static">この場合、static（背景青） + 文字色赤</p>',
});

var v = new Vue({
  el: "#el",
  data: {
    msg: "",
    msg2: "",
    checked: true,
    checkMulti: [],
    radio: "",
    selected: "",
    selected2: "",
    selected3: 'A',
    options: [
      { text: "One", value: 'A' },
      { text: "Two", value: 'B' },
      { text: "Tree", value: 'C' },
    ],
  },
});
