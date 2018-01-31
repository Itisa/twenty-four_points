// pages/test.js
var types = ['default','primay','warn'],anss,q1,q2,q3
var pageObject = {
  data: {
    plain: false,
    loading: false
  },
  setDisabled: function () {
    this.setData({
      disabled: !this.data.disabled
    })
  },
  setPlain: function () {
    this.setData({
      plain: !this.data.plain
    })
  },
  setLoading: function () {
    this.setData({
      loading: !this.data.loading
    })
  },
  // 第二个
  Count: function (e) {
    console.log(q1,q2,q3);
    if(!q1 || !q2 || !q3){
      this.setData({ ans: "没有给全参数"})
      console.log(1)
    }else{
      this.setData({ ans: q1-q2-q3 });
      console.log(2)
    }
  },
  Count1: function (e) {
    q1 = parseInt(e.detail.value);
  },
  Count2: function (e) {
    q2 = parseInt(e.detail.value);
  },
  Count3: function (e) {
    q3 = parseInt(e.detail.value);
  }
  //第三个
  
} 


Page(pageObject)

function Count () {
  
} 



// Page({
//   /**
//    * 页面的初始数据
//    */
//   data: {

//   },

//   /**
//    * 生命周期函数--监听页面加载
//    */
//   onLoad: function (options) {
  
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

