Vue.component("my-comp", {
  template: '<p class="static">この場合、static（背景青） + 文字色赤</p>',
});

var v = new Vue({
  el: "#el",
  data: {
    radio: "",
    checked: true,
    selected: "",
    check2: true,
    radio2: "",
    b: "b1b1b1b1b1b1",
    c: "c1c1c1c1c1c1",
    select2: "",
    msg1: "",
    msgx: "",
    msg2: "",
    msg3: "",

  },
});
