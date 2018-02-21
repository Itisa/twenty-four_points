// pages/test.js

var nu1,nu2,nu3,nu4,n=1,ans,nums=[],ans_li=[];
var input;
Page({

  data: {
    e: "+",
    f: "-",
    g: "*",
    h: "/",
    i: "(",
    k: ")",
    hid_f: "true",
    hid_ans: "true",
  },


  find_input: function (e) {
    input = e.detail.value;

    if(input.length==2){
      switch (n) {
        case 1:
          nums = [input]
          this.setData({ buton: nums });
          n = 2;
          ans = 0;
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
      if(ans == 1 & n == 1){
        this.get_anli(nums[0],nums[1],nums[2],nums[3]);
      }else{
        this.setData({ hid_f: true });
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
        ans_li = res.data;
        console.log(ans_li);
        var a = getCurrentPages();
        a[0].setData({ ans_list: ans_li });
        if(ans_li=="nothing"){
          a[0].setData({ hid_ans: true });
          a[0].setData({ hid_f: false });
        }else{
          a[0].setData({ ans_list: ans_li });
          a[0].setData({ hid_ans: false });  
        }
      }
    })
  },
  X: function (e) {
    nums.splice(e.target.dataset.num,1);
    this.setData({ buton: nums });

    this.setData({ hid_f: true });
    this.setData({ hid_ans: true });
    if(n==1){
      n = 4;
      ans = 0;   
    }else{
      n -= 1;
      ans = 0; 
    }
  },
  
})

