// pages/test.js

var n1,n2,n3,n4,n=1,ans,nums=[];
var input;
Page({

  data: {
    e: "+",
    f: "-",
    g: "*",
    h: "/",
    i: "(",
    k: ")",


    // Things: [
    //   { value:"+",  isnum: false, issign: true },
    //   { value:"-",  isnum: false, issign: true },
    //   { value:"*",  isnum: false, issign: true },
    //   { value:"/",  isnum: false, issign: true },
    //   { value:"(",  isnum: false, issign: true },
    //   { value:")",  isnum: false, issign: true },
    // ],
    Things: {
      "+": { isnum: false, issign: true },
      "-": { isnum: false, issign: true },
      "*": { isnum: false, issign: true },
      "/": { isnum: false, issign: true },
      "(": { isnum: false, issign: true },
      ")": { isnum: false, issign: true },

    },

    hid_ans: "true",
    ans_list: ['(1+2+3)*4', '1*2*3*4', '1*2*4*3']
  },


  find_input: function (e) {
    input = e.detail.value;

    if(input.length==2){

      switch (n) {
        case 1:
          nums = [input]
          this.setData({ buton: nums });
          this.setData({ a: 1 });
          n = 2;
          ans = 0;
          break;
        case 2:
          nums.push(input);
          this.setData({ buton: nums });
          this.setData({ b: 2 });
          n = 3;
          ans = 0
          break;
        case 3:
          nums.push(input);
          this.setData({ buton: nums });
          this.setData({ c: 3 });
          n = 4;
          ans = 0
          break;
        case 4:
          nums.push(input);
          this.setData({ buton: nums });
          this.setData({ d: 4 });
          n = 1;
          ans = 1;
          break;
      }
      if(ans == 1 & n == 1){
        this.setData({ hid_ans: false });
      }else{
        this.setData({ hid_ans: true });
      }

      return "";
    }
    
  },

  get_ans: function (e) {
    this.setData({ ans: 123 })
  },
  X: function (e) {
    console.log("");
    nums.splice(e.target.dataset.num,1);
    this.setData({ buton: nums });

    this.setData({ hid_ans: true });
    if(n==1){
      n = 4;
      ans = 0;   
    }else{
      n -= 1;
      ans = 0; 
    }
  },
  Numcolor: function (e) {
    console.log(1);
    return false;
    
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