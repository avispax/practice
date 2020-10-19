Vue.component("my-component", {
  template: "<div>{{ msg }} , {{ index }}</div>",
  props: ["msg", "index"],
});

var v1 = new Vue({
  el: "#el",
  data: {
    items: [
      { id: 0, msg: "Foo" },
      { id: 1, msg: "Bar" },
    ],
  },
});
