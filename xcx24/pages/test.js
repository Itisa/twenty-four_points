// pages/test.js

var n1,n2,n3,n4,n=1,ans,nums=[]
var input
Page({

  onLoad: function (e) {
  //   this.setData({ hid1: "true" });
  //   this.setData({ hid2: "true" });
  //   this.setData({ hid3: "true" });
  //   this.setData({ hid4: "true" });
    this.setData({ hid_ans: "true"});
  },

    
  find_input: function (e) {
    input = e.detail.value;
    
    if(input.length==2){
      this.setData({ num: nums[n-1]})
      switch (n) {
        case 1:
          nums = [input]
          this.setData({ buton: nums });
          n = 2;
          ans = 0
          break;
        case 2:
          nums.push(input);
          this.setData({ buton: nums });
          n = 3;
          ans = 0
          break;
        case 3:
          nums.push(input);
          this.setData({ buton: nums });
          n = 4;
          ans = 0
          break;
        case 4:
          nums.push(input);
          this.setData({ buton: nums });
          n = 1;
          ans = 1;
          break;
      }
      console.log(ans,n);
      if(ans == 1 & n == 1){
        this.setData({ hid_ans: false });
        
      }else{
        this.setData({ hid_ans: true });
      }

      return "";
    }
    
  },

  get_ans: function (e) {
    console.log(1)
    this.setData({ ans: 123 })
  },
  X: function (e) {
    console.log(nums)
    nums.pop();
    this.setData({ buton: nums });

    this.setData({ hid_ans: true });
    console.log(n,nums);
    if(n==1){
      n = 4;
      ans = 0;   
    }else{
      n -= 1;
      ans = 0; 
    }
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
// 