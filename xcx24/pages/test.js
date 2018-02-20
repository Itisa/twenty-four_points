// pages/test.js

var nu1,nu2,nu3,nu4,n=1,ans,nums=[];
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
          nu1 = input
          nums = [input]
          this.setData({ buton: nums });
          this.setData({ a: nu1 });
          n = 2;
          ans = 0;
          break;
        case 2:
          nu2 = input
          nums.push(input);
          this.setData({ buton: nums });
          this.setData({ b: nu2 });
          n = 3;
          ans = 0
          break;
        case 3:
          nu3 = input
          nums.push(input);
          this.setData({ buton: nums });
          this.setData({ c: nu3 });
          n = 4;
          ans = 0
          break;
        case 4:
          nu4 = input
          nums.push(input);
          this.setData({ buton: nums });
          this.setData({ d: nu4 });
          n = 1;
          ans = 1;
          break;
      }
      if(ans == 1 & n == 1){
        this.setData({ hid_ans: false });
        this.get_anli(nu1,nu2,nu3,nu4);
      }else{
        this.setData({ hid_ans: true });
      }

      return "";
    }
    
  },

  get_anli: function (n1,n2,n3,n4) {
    wx.request({
      url: 'https://point.101weiqi.com/get24',
      data: {
        n1: n1,
        n2: n2,
        n3: n3,
        n4: n4
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      success: function (res) {
        console.log(res.data);
        this.setData({ ans_list: res.data});
      }
    })
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