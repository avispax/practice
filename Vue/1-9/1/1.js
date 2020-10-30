Vue.component("my-comp", {
  template: '<p class="static">この場合、static（背景青） + 文字色赤</p>',
});

var v = new Vue({
  el: "#el",
  data: {
    counter: 0,
    name: "my Sample",
  },
  methods: {
    greet: function (event) {
      // メソッド内の this は Vue インスタンス（ここで言う5行目の v ）を参照します。
      alert("Hello " + this.name + "!");
      // 'event' はネイティブ DOM イベントです。
      if (event) {
        alert(event.target.tagName);
      }
    },
    say: function (message) {
      alert(message);
    },
    warn: function (msg, event) {
      // eventはネイティブイベントを参照
      if (event) {
        // この場合はたぶんクリックとかをデフォルトイベントとかするから、クリック系の後続イベントを殺してるんじゃないかしら。
        event.preventDefault();
        alert("prevent");
      }
      // 公式例を信じるならpreventでFormとしてSubmitイベントは死んだはず。
      alert(msg);
    },
    one(msg, event) {
      console.log("111");
      alert(msg);
      console.log("111222");
    },
    two(event) {
      console.log("222");
      alert("two");
      console.log("222222");
    },
  },
});
