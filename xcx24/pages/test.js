// pages/test.js

var n1,n2,n3,n4,n=1,ans
var input
Page({

  // onLoad: function (e) {
  //   this.setData({ hid1: "true" });
  //   this.setData({ hid2: "true" });
  //   this.setData({ hid3: "true" });
  //   this.setData({ hid4: "true" });
  //   this.setData({ hid_ans: "true"});
  // },

    
  find_input: function (e) {
    input = e.detail.value
    console.log(e.detail.value);
    
    if(input.length==2){
      this.setData({ hid1: false });
      switch (n) {
        case 1:
          this.setData({ hid1: false });
          this.setData({ num1: input });
          n = 2;
          ans = 0
          break;
        case 2:
          this.setData({ hid2: false });
          this.setData({ num2: input });
          n = 3;
          break;
        case 3:
          this.setData({ hid3: false });
          this.setData({ num3: input });
          n = 4;
          break;
        case 4:
          this.setData({ hid4: false });
          this.setData({ num4: input });
          n = 1;
          ans = 1;
          break;
      }

      if(ans == 1){
        this.setData({ hid_ans: false})
      }

      return "";
    }
    
  },

  get_ans: function (e) {
    console.log(1)
    this.setData({ ans: 123 })
  }

  
})

//   /**
//    * 页面的初始数据
//    */
//   data: {
  
//   },

//   /**
//    * 生命周期函数--监听页面加载
//    */
// onLoad: function (options) {
  
//   },

//   /**
//    * 生命周期函数--监听页面初次渲染完成
//    */
//   onReady: function () {
  
//   },

//   /**
//    * 生命周期函数--监听页面显示
//    */
//   onShow: function () {
  
//   },

//   /**
//    * 生命周期函数--监听页面隐藏
//    */
//   onHide: function () {
  
//   },

//   /**
//    * 生命周期函数--监听页面卸载
//    */
//   onUnload: function () {
  
//   },

//   /**
//    * 页面相关事件处理函数--监听用户下拉动作
//    */
//   onPullDownRefresh: function () {
  
//   },

//   /**
//    * 页面上拉触底事件的处理函数
//    */
//   onReachBottom: function () {
  
//   },

//   /**
//    * 用户点击右上角分享
//    */
//   onShareAppMessage: function () {
  
//   }
// })